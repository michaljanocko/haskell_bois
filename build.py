import glob
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from jinja2 import Template
from markdown import markdown
from natsort import natsorted
from pydantic import BaseModel

Day = Tuple[int, List[str], Dict[str, Any], str, str]


class Day(BaseModel):
    number: int
    pictures: List[str]
    data: Dict[str, Any]
    post_cs: str
    post_en: str


def main():
    days: List[Day] = []

    for day in range(1, 21):
        folder = f"content/{day}"
        pictures = glob.glob(f"{folder}/*.jpg")

        data = json.loads(Path(f"{folder}/data.json").read_text())
        post_cs = Path(f"{folder}/post_cs.md").read_text()
        post_en = Path(f"{folder}/post_en.md").read_text()

        days.append(
            Day(
                number=day,
                pictures=natsorted(pictures),
                data=data,
                post_cs=markdown(post_cs.replace("\n\n", "\n<br>\n")),
                post_en=markdown(post_en.replace("\n\n", "\n<br>\n")),
            )
        )

    with open("index.html", "w") as file:
        template = Template(
            Path("template.jinja").read_text(),
            lstrip_blocks=True,
            trim_blocks=True,
        )
        file.write(template.render(days=days))


if __name__ == "__main__":
    main()
