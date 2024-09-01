# -*- coding: utf-8 -*-
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def load_excluded_keys(file_path: Path) -> set:
    if not file_path.exists():
        print(f"WARNING: {file_path} does not exist! No keys will be excluded.")
        return set()

    return {
        key.strip()
        for key in Path(file_path).read_text().splitlines()
        if not key.isspace()
    }


def generate_html(directory_path: Path, exclude_file: Path):
    exclude_keys = load_excluded_keys(exclude_file)

    accordion_items = []

    for json_file in directory_path.glob("*.json"):
        try:
            data: dict = json.loads(json_file.read_text())
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {json_file}", e)
            continue

        if int(data.get("totalCount", 0)):
            rows: list[dict] = []

            for item in data.get("imdata", []):
                attributes: dict[str, str] = item.get(json_file.stem, {}).get(
                    "attributes", {}
                )
                valuable_attrs = {
                    k: v
                    for k, v in attributes.items()
                    if v and not v.isspace() and k not in exclude_keys
                }

                if valuable_attrs:
                    rows.append(valuable_attrs)

            if rows:
                headers = rows[0].keys()
                table_headers = "".join(f"<th>{header}</th>" for header in headers)
                table_rows = "".join(
                    f"<tr>{''.join(f'<td>{row.get(header, '')}</td>' for header in headers)}</tr>"
                    for row in rows
                )

                accordion_items.append(
                    {
                        "title": json_file.stem,
                        "headers": table_headers,
                        "rows": table_rows,
                    }
                )

    env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
    template = env.get_template("vetr-data.j2")
    output_html = template.render(accordion_items=accordion_items)

    output_file = Path.cwd() / "vetr-summary.html"
    output_file.write_text(output_html)

    return output_file
