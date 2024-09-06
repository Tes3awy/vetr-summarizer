# -*- coding: utf-8 -*-
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from vetr_summarizer.config import Config


class VetrSummarizer(object):
    def __init__(self, directory: Path, config: Config):
        self.directory = directory
        self.config = config
        self.accordion_items = []

    def load_json_files(self):
        for json_file in self.directory.glob("*.json"):
            data: dict = json.loads(json_file.read_text())
            if int(data.get("totalCount", 0)):
                key = json_file.stem
                rows = self._process_json_data(data, key)
                if rows:
                    self._add_accordion_item(json_file.stem, rows)

    def _process_json_data(self, data: dict, key: str):
        rows = []
        for item in data.get("imdata", []):
            attributes: dict[str, str] = item.get(key, {}).get("attributes", {})
            valuable_attrs = {
                k: v
                for k, v in attributes.items()
                if v and not v.isspace() and k not in self.config.excluded_keys
            }
            if valuable_attrs:
                rows.append(valuable_attrs)
        return rows

    def _add_accordion_item(self, title: str, rows: list[dict]):
        headers = rows[0].keys()
        table_headers = [{"header": header} for header in headers]
        table_rows = [
            {header: row.get(header, "") for header in headers} for row in rows
        ]
        self.accordion_items.append(
            {
                "title": title,
                "headers": table_headers,
                "rows": table_rows,
            }
        )

    def generate_report(self, output_file: Path = None):
        if not self.accordion_items:
            print("WARNING: No data available to generate HTML report!")
            return

        environment = Environment(
            loader=FileSystemLoader(Path(__file__).parent / "templates")
        )
        html_template = environment.get_template(self.config.template_file)

        output_file = Path.cwd() / self.config.output_html
        output_file.write_text(
            html_template.render(accordion_items=self.accordion_items)
        )
        print(f"HTML report is written to {output_file.resolve()}")

    def summarize(self):
        self.load_json_files()
        self.generate_report()
