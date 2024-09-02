# -*- coding: utf-8 -*-
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from pathlib import Path

from vetr_summarizer.html_generator import generate_html

from . import __version__


def main():
    parser = ArgumentParser(
        prog="vetr-summarizer",
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Process and summarize aci-vetr-data JSON files into pretty HTML reports.",
        epilog="Thanks for using %(prog)s! :)",
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True,
        conflict_handler="error",
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="A path to the directory containing the JSON files.",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=["html"],
        required=False,
        default="html",
        help="Output format",
    )
    parser.add_argument(
        "-x",
        "--exclude-file",
        type=Path,
        required=False,
        default=Path(__file__).parent / "config/excluded_keys",
        help="File containing keys to exclude from the summary report.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s version {__version__}"
    )
    args = parser.parse_args()

    output_file = generate_html(args.directory, args.exclude_file)

    print(f"HTML output is written to {output_file}")


if __name__ == "__main__":
    main()
