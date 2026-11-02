"""Create new, disposable local Git repositories and verify Chapter 15 concepts.

No network remotes, deletion, global config changes or existing repository writes.
Usage: python run_lab.py --output PATH_TO_NEW_DIRECTORY
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.output.resolve()
if root.exists():
    parser.error("Output must be a new directory; existing content is never overwritten.")
root.mkdir(parents=True)
empty_config = root / "empty.gitconfig"
empty_config.write_text("", encoding="utf-8")
hooks = root / "empty-hooks"
hooks.mkdir()
template = root / "empty-template"
template.mkdir()
env = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")}
env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": str(empty_config),
            "GIT_TERMINAL_PROMPT": "0", "GIT_EDITOR": "true",
            "GIT_MERGE_AUTOEDIT": "no", "GIT_ALLOW_PROTOCOL": "file",
            "GIT_TEMPLATE_DIR": str(template)})
checks = []
commands = []


def git(repo, *parts, expected=0):
    command = ["git", "-c", "core.hooksPath=" + str(hooks), "-C", str(repo), *parts]
    result = subprocess.run(command, env=env, text=True, encoding="utf-8",
                            errors="replace", capture_output=True, timeout=30)
    commands.append({"repo": str(Path(repo).relative_to(root)), "args": list(parts),
                     "exit_code": result.returncode})
    if result.returncode != expected:
        raise RuntimeError(f"Git command failed: {parts!r}: {result.stderr}")
    return result.stdout.strip()


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def write(repo, name, value):
    (repo / name).write_text(value, encoding="utf-8", newline="\n")


def configure(repo):
    for key, value in (("user.name", "Book Git Lab"),
                       ("user.email", "git-lab@example.invalid"),
                       ("core.autocrlf", "false"), ("commit.gpgSign", "false"),
                       ("tag.gpgSign", "false")):
        git(repo, "config", "--local", key, value)


def commit(repo, message, *paths):
    git(repo, "add", "--", *paths)
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


try:
    author = root / "author"
    git(root, "init", "--initial-branch=main", str(author))
    configure(author)
    write(author, "README.md", "Environment notes\n")
    write(author, "policy.txt", "startup-note=base\n")
    write(author, ".gitignore", ".env\n.env.*\n!.env.example\n.venv/\n")
    write(author, ".env.example", "APP_DEBUG=false\n")
    initial = commit(author, "Record lab starting point", "README.md", "policy.txt",
                     ".gitignore", ".env.example")
    check("initial_commit_clean", git(author, "status", "--porcelain") == "")
    write(author, ".env", "APP_DEBUG=true\n")
    check("local_env_ignored", git(author, "check-ignore", ".env") == ".env")
    check("example_env_trackable", git(author, "check-ignore", "--no-index",
                                       ".env.example", expected=1) == "")
    write(author, "README.md", "Environment notes\nStage one\n")
    git(author, "add", "--", "README.md")
    write(author, "README.md", "Environment notes\nStage one\nStage two\n")
    check("index_is_snapshot", "Stage two" not in git(author, "show", ":README.md"))
    check("staged_and_unstaged_differ", "Stage one" in git(author, "diff", "--cached")
          and "+Stage two" in git(author, "diff"))
    git(author, "restore", "--staged", "--", "README.md")
    check("unstage_preserves_worktree", git(author, "diff", "--cached") == ""
          and "Stage two" in (author / "README.md").read_text(encoding="utf-8"))
    commit(author, "Explain both lab stages", "README.md")
    git(author, "switch", "-c", "codex/lab-notes")
    write(author, "notes.txt", "A branch isolates recorded history.\n")
    tip = commit(author, "Add branch note", "notes.txt")
    git(author, "switch", "main")
    git(author, "merge", "--ff-only", "codex/lab-notes")
    check("fast_forward_reuses_tip", git(author, "rev-parse", "HEAD") == tip)
    git(author, "switch", "-c", "codex/parallel-note")
    write(author, "parallel.txt", "Feature-side note\n")
    commit(author, "Add feature-side note", "parallel.txt")
    git(author, "switch", "main")
    write(author, "main.txt", "Main-side note\n")
    commit(author, "Add main-side note", "main.txt")
    git(author, "merge", "--no-ff", "--no-edit", "codex/parallel-note")
    check("merge_has_two_parents", len(git(author, "rev-list", "--parents", "-n", "1", "HEAD").split()) == 3)
    remote = root / "remote.git"
    git(root, "init", "--bare", "--initial-branch=main", str(remote))
    git(author, "remote", "add", "origin", str(remote))
    git(author, "push", "-u", "origin", "main")
    check("push_updates_local_remote", git(remote, "rev-parse", "main") == git(author, "rev-parse", "HEAD"))
    peer = root / "peer"
    git(root, "clone", "--no-hardlinks", str(remote), str(peer))
    configure(peer)
    check("clone_has_history", git(peer, "rev-parse", "HEAD") == git(author, "rev-parse", "HEAD"))
    write(peer, "peer.txt", "Peer first change\n")
    peer_tip = commit(peer, "Add peer note", "peer.txt")
    git(peer, "push", "origin", "main")
    before = git(author, "rev-parse", "HEAD")
    git(author, "fetch", "origin")
    check("fetch_leaves_current_branch", git(author, "rev-parse", "HEAD") == before
          and git(author, "rev-parse", "origin/main") == peer_tip)
    git(author, "pull", "--ff-only", "origin", "main")
    check("pull_advances_current_branch", git(author, "rev-parse", "HEAD") == peer_tip)
    write(author, "local.txt", "Local new work\n")
    local_tip = commit(author, "Add local note", "local.txt")
    write(peer, "peer.txt", "Peer second change\n")
    commit(peer, "Revise peer note", "peer.txt")
    git(peer, "push", "origin", "main")
    git(author, "push", "origin", "main", expected=1)
    check("non_fast_forward_push_rejected", git(author, "rev-parse", "HEAD") == local_tip)
    # Exit code for a fatal Git pull failure is 128 in this exercised flow.
    git(author, "pull", "--ff-only", "origin", "main", expected=128)
    check("divergent_ff_pull_preserves_head", git(author, "rev-parse", "HEAD") == local_tip)
    git(author, "merge", "--no-edit", "origin/main")
    git(author, "push", "origin", "main")
    check("reconciled_push_succeeds", git(remote, "rev-parse", "main") == git(author, "rev-parse", "HEAD"))
    git(author, "switch", "-c", "codex/conflict-note")
    write(author, "policy.txt", "startup-note=branch\n")
    commit(author, "Use branch-side wording", "policy.txt")
    git(author, "switch", "main")
    write(author, "policy.txt", "startup-note=main\n")
    conflict_base = commit(author, "Use main-side wording", "policy.txt")
    git(author, "merge", "codex/conflict-note", expected=1)
    check("text_conflict_is_visible", "UU policy.txt" in git(author, "status", "--porcelain"))
    git(author, "merge", "--abort")
    check("abort_restores_clean_start", git(author, "rev-parse", "HEAD") == conflict_base
          and git(author, "status", "--porcelain") == "")
    git(author, "merge", "codex/conflict-note", expected=1)
    write(author, "policy.txt", "startup-note=reviewed\n")
    git(author, "add", "--", "policy.txt")
    git(author, "commit", "-m", "Resolve wording after reviewing both sides")
    check("resolution_records_both_parents", len(git(author, "rev-list", "--parents", "-n", "1", "HEAD").split()) == 3
          and "<<<<<<<" not in (author / "policy.txt").read_text(encoding="utf-8"))
    clean_text = (author / "README.md").read_text(encoding="utf-8")
    write(author, "README.md", clean_text + "Disposable mistake\n")
    git(author, "restore", "--", "README.md")
    check("restore_discards_only_demo_edit", (author / "README.md").read_text(encoding="utf-8") == clean_text)
    write(author, "mistake.txt", "Unwanted demo content\n")
    bad = commit(author, "Add a deliberate demonstration mistake", "mistake.txt")
    git(author, "revert", "--no-edit", bad)
    check("revert_preserves_history", not (author / "mistake.txt").exists()
          and git(author, "rev-parse", "HEAD^") == bad)
    tag_target = git(author, "rev-parse", "HEAD")
    git(author, "tag", "-a", "lab-v0.1.0", "-m", "Verified local learning checkpoint")
    git(author, "push", "origin", "main")
    check("branch_push_does_not_push_tag", git(remote, "show-ref", "--verify", "--quiet", "refs/tags/lab-v0.1.0", expected=1) == "")
    git(author, "push", "origin", "lab-v0.1.0")
    check("annotated_tag_transferred", git(remote, "cat-file", "-t", "refs/tags/lab-v0.1.0") == "tag"
          and git(remote, "rev-parse", "lab-v0.1.0^{commit}") == tag_target)
    # A tracked, non-secret local file shows why ignore rules are not retroactive.
    write(author, "local-note.txt", "No secrets: tracked demonstration\n")
    commit(author, "Track a non-secret local note for demonstration", "local-note.txt")
    with (author / ".gitignore").open("a", encoding="utf-8") as stream:
        stream.write("local-note.txt\n")
    commit(author, "Ignore future untracked local notes", ".gitignore")
    write(author, "local-note.txt", "Changed tracked demonstration\n")
    check("ignore_does_not_untrack", "local-note.txt" in git(author, "diff", "--name-only"))
    git(author, "rm", "--cached", "--", "local-note.txt")
    git(author, "commit", "-m", "Stop tracking the demonstration local note")
    check("untrack_keeps_local_file", (author / "local-note.txt").exists()
          and git(author, "ls-files", "local-note.txt") == "")
    git(author, "switch", "-c", "codex/reset-demo")
    previous = git(author, "rev-parse", "HEAD")
    write(author, "draft.txt", "Private local draft\n")
    draft = commit(author, "Record a disposable private draft", "draft.txt")
    git(author, "reset", "--soft", "HEAD^")
    check("soft_reset_keeps_staged_content", git(author, "rev-parse", "HEAD") == previous
          and "draft.txt" in git(author, "diff", "--cached", "--name-only"))
    check("reflog_records_previous_tip", draft in git(author, "reflog", "--format=%H"))
    git(author, "branch", "codex/recovered-draft", draft)
    check("recovery_branch_reaches_commit", git(author, "rev-parse", "codex/recovered-draft") == draft)
    git(author, "commit", "-m", "Record reviewed draft after local regrouping")
    check("final_worktree_clean", git(author, "status", "--porcelain") == "")
    result = {"git_version": git(root, "--version"), "python_version": sys.version.split()[0],
              "checks_passed": len(checks), "checks": checks, "commands": commands,
              "network_used": False, "github_pr_created": False,
              "scope": "Fresh local repositories only; no application or CI/CD tests"}
    (root / "results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "commands"}, indent=2))
except Exception:
    (root / "commands-before-failure.json").write_text(json.dumps(commands, indent=2), encoding="utf-8")
    raise
