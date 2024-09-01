# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from pathlib import Path

from vetr_summarizer.html_generator import generate_html

from . import __version__


def main():
    parser = ArgumentParser(
        prog="vetr-summarizer",
        description="Process and summarize aci-vetr-data JSON files into HTML reports.",
        epilog="Thanks for using %(prog)s! :)",
        add_help=True,
        allow_abbrev=True,
        conflict_handler="error",
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="A path to the directory containing the JSON files.",
    )
    parser.add_argument(
        "-f", "--format", choices=["html"], default="html", help="Output format (html)."
    )
    parser.add_argument(
        "-x",
        "--exclude-file",
        type=Path,
        default=Path(__file__).parent / "config/excluded_keys",
        help="File containing keys to exclude from the summary report.",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args()

    output_file = generate_html(args.directory, args.exclude_file)

    print(f"HTML output is written to {output_file}")


if __name__ == "__main__":
    main()
