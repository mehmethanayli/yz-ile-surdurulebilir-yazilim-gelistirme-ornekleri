"""Inspect the environment; --share omits paths using an explicit output schema."""
import argparse
import json
import os
import platform
import sys
from importlib import metadata
from pathlib import Path


def read_settings(environ):
    app_env = environ.get("APP_ENV", "development").strip().lower()
    if app_env not in {"development", "test", "production"}:
        raise ValueError("APP_ENV must be development, test or production.")
    raw_debug = environ.get("APP_DEBUG", "false").strip().lower()
    if raw_debug not in {"true", "false"}:
        raise ValueError("APP_DEBUG must be true or false.")
    debug = raw_debug == "true"
    if app_env == "production" and debug:
        raise ValueError("APP_DEBUG must be false in production.")
    return {"app_env": app_env, "debug": debug}


def package_version(name):
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return None


def share_report(report):
    """Select known diagnostic fields; do not mutate the complete local report."""
    return {
        "python_version": report["python_version"],
        "in_virtualenv": report["in_virtualenv"],
        "python314": report["python314"],
        "settings": {
            "app_env": report["settings"]["app_env"],
            "debug": report["settings"]["debug"],
        },
        "packages": {
            "Django": report["packages"]["Django"],
            "psycopg": report["packages"]["psycopg"],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-target", action="store_true",
                        help="Require Python 3.14 inside a virtual environment only.")
    parser.add_argument("--share", action="store_true",
                        help="Omit local paths; review remaining diagnostic fields before sharing.")
    args = parser.parse_args()
    try:
        settings = read_settings(os.environ)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    in_venv = sys.prefix != sys.base_prefix
    python314 = sys.version_info[:2] == (3, 14)
    report = {
        "project_root": str(Path(__file__).resolve().parent.parent),
        "working_directory": str(Path.cwd()),
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "in_virtualenv": in_venv,
        "python314": python314,
        "settings": settings,
        "packages": {name: package_version(name) for name in ("Django", "psycopg")},
    }
    output = share_report(report) if args.share else report
    print(json.dumps(output, indent=2))
    if args.require_target and not (python314 and in_venv):
        print("Target requires Python 3.14 and a virtual environment.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
