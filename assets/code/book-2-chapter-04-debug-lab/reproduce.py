"""Reproduce a synthetic settings failure; all values come from CLI arguments."""
import argparse
import json
import logging
import sys
import settings_faulty
import settings_fixed

logger = logging.getLogger("chapter17")


def load_settings(variant, values):
    reader = settings_faulty.read_settings if variant == "faulty" else settings_fixed.read_settings
    return reader(values)


def run_case(args):
    return load_settings(args.variant, {"APP_ENV": args.app_env, "APP_DEBUG": args.debug})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=("faulty", "fixed"), default="fixed")
    parser.add_argument("--app-env", default="production")
    parser.add_argument("--debug", default="false")
    parser.add_argument("--trace", action="store_true", help="Let the synthetic ValueError propagate.")
    parser.add_argument("--log", action="store_true", help="Write a limited diagnostic event to stderr.")
    args = parser.parse_args(argv)
    if args.log:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if args.trace:
        result = run_case(args)
    else:
        try:
            result = run_case(args)
        except ValueError as exc:
            if args.log:
                logger.warning("event=settings_rejected variant=%s error_type=ValueError", args.variant)
            print(str(exc), file=sys.stderr)
            return 2
    if args.log:
        logger.info("event=settings_loaded variant=%s", args.variant)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
