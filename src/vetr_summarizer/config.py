# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Optional, Set


class Config(object):
    def __init__(
        self,
        format: Optional[str] = "html",
        excluded_keys_file: Optional[Path] = Path("excluded_keys"),
        output_html: Optional[str] = "vetr-summary.html",
        template_file: Optional[str] = "vetr-data.j2",
    ):
        self.format = format
        self.template_file = template_file
        self.output_html = output_html
        self.excluded_keys = self.load_excluded_keys(excluded_keys_file)

    def load_excluded_keys(self, file_path: Path) -> Set[str] | Set:
        if not file_path.exists():
            print(f"WARNING: {file_path} does not exist! No keys will be excluded.")
            return set()

        if file_path.exists() and not file_path.read_text().splitlines():
            print(
                f"WARNING: {file_path} does exists but without keys! No keys will be excluded."
            )
            return set()

        return {
            key.strip()
            for key in Path(file_path).read_text().splitlines()
            if not key.isspace()
        }
