#!/usr/bin/env python3

import argparse
import datetime
import os
import re
import sys


def check(paths: list[str], options: argparse.Namespace) -> int:
    year = datetime.datetime.now().year
    template = options.template
    template = template.replace("[YEAR]", str(year))
    header = re.compile(template)

    exitcode = 0
    for path in paths:
        if os.path.getsize(path) == 0:
            continue

        with open(path, "r") as f:
            lineno = 0
            found = False
            breakpoint()
            try:
                for line in f:
                    if header.search(line):
                        found = True
                        break
                    lineno += 1
                    if lineno > options.max_lines:
                        break
            except UnicodeDecodeError:
                print(f"Cannot read {path} as text, skipping")
                exitcode = 1

            if not found:
                print(f"Missing copyright header in {path}")
                exitcode = 1

    return exitcode


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Checks file headers for the given software license template."
    )
    parser.add_argument(
        "--template",
        help="Template to check files for. Treated as a regex so escape as needed. [YEAR] will be replaced with current year.",
    )
    parser.add_argument(
        "--max_lines", help="Maximum number of lines to scan. Defaults to 1.", default=1
    )
    parser.add_argument("filenames", nargs="*", help="Files to check")

    args = parser.parse_args(argv)

    if args.template is None:
        print("Must pass license template. Exiting.")
        return 1

    return check(args.filenames, args)


if __name__ == "__main__":
    sys.exit(main())
