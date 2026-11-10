"""Validate shipped reader files and local Markdown links without network access."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
import hashlib
import json
import re
import sys

def main():
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    manifest=json.loads((root/'distribution-manifest.json').read_text(encoding='utf-8'))
    errors=[]
    for name,digest in manifest['files'].items():
        p=root/name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
            errors.append(f'File hash mismatch: {name}')
    for p in root.rglob('*.json'):
        if '.git' not in p.relative_to(root).parts:json.loads(p.read_text(encoding='utf-8'))
    count=0
    for p in root.rglob('*.md'):
        if '.git' in p.relative_to(root).parts:continue
        text=p.read_text(encoding='utf-8')
        # Fenced examples may intentionally show nonexistent sample paths.
        prose=re.sub(r'^```[^\n]*\n.*?^```\s*$', '',text,flags=re.M|re.S)
        for destination in re.findall(r'\]\(([^)]+)\)',prose):
            url=urlsplit(destination)
            if url.scheme or url.netloc:continue
            target=(p.parent/unquote(url.path)).resolve() if url.path else p
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'Broken local link in {p.relative_to(root)}: {destination}');continue
            if url.fragment and target.suffix=='.md':
                content=target.read_text(encoding='utf-8')
                fragment=unquote(url.fragment)
                if f'id="{fragment}"' not in content:
                    # Most appendix anchors are explicit HTML ids. Support
                    # ordinary GitHub heading slugs as well.
                    slugs=[]
                    for heading in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
                        slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
                        slugs.append(slug)
                    if fragment not in slugs:errors.append(f'Missing anchor in {p.relative_to(root)}: {destination}')
            count+=1
    prohibited=[p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and
                (p.suffix in {'.docx','.pdf','.rar'} or p.name=='.env' or '__pycache__' in p.parts)]
    if prohibited:errors.append(f'Unexpected publishing files: {prohibited}')
    with ZipFile(root / 'indir' / f"kitap-materyalleri-{manifest['version']}.zip") as z:
        if z.testzip():errors.append('Corrupted ZIP')
        expected=set(manifest['files'])|{'distribution-manifest.json'}
        if set(z.namelist())!=expected:errors.append('ZIP manifest mismatch')
        for name,digest in manifest['files'].items():
            if hashlib.sha256(z.read(name)).hexdigest()!=digest:errors.append(f'ZIP content mismatch: {name}')
    result={'files_verified':len(manifest['files']),'local_links_checked':count,'appendices':len(list((root/'ekler').glob('kitap-*/ek-*.md'))),'errors':errors}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
