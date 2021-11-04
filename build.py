import glob
import jinja2
import markdown
from pathlib import Path


def main():
    for day in range(1, 2):
        folder = f"content/{day}"
        pictures = glob.glob(f"{folder}/*.jpg")

        data = Path(f"{folder}/data.json").read_text()
        post_cs = Path(f"{folder}/post_cs.md").read_text()
        post_en = Path(f"{folder}/post_en.md").read_text()


if __name__ == "__main__":
    main()
