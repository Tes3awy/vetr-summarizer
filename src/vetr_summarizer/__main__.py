# -*- coding: utf-8 -*-
import argparse
from pathlib import Path

from vetr_summarizer import __version__
from vetr_summarizer.config import Config
from vetr_summarizer.main import VetrSummarizer


def main():
    parser = argparse.ArgumentParser(
        prog="vetr-summarizer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Process and summarize aci-vetr-data raw JSON files into pretty HTML reports.",
        epilog="Thanks for using %(prog)s! :)",
        add_help=True,
        allow_abbrev=True,
        exit_on_error=True,
        conflict_handler="error",
    )
    parser.add_argument(
        "directory",
        type=Path,
        help="Directory containing JSON files.",
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
        "--excluded-keys-file",
        type=Path,
        required=False,
        default=Path(__file__).parent / "config" / "excluded_keys",
        help="File with keys to exclude from raw JSON files.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s version {__version__}"
    )
    args = parser.parse_args()

    config = Config(
        format=args.format,
        excluded_keys_file=args.excluded_keys_file,
    )

    summarizer = VetrSummarizer(args.directory, config)
    summarizer.summarize()


if __name__ == "__main__":
    main()
