import logging
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import yaml

from builder.sections import BaseTexDataClass, Header

logger = logging.getLogger(__file__)


@dataclass(kw_only=True)
class Document(BaseTexDataClass):
    theme_color: str = "MidnightBlue"
    header: Header

    def to_tex(self) -> str:
        tex = "\documentclass{styling}\n\n"
        tex += f"\setthemecolor{{{self.theme_color}}}\n\n"
        tex += self.header.to_tex()
        tex += "\n\n\\begin{document}"
        return tex


def main(input: str | Path, output: str | Path) -> str:
    with open(input, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    document = partial(
        Document,
    )
    for cls, args in data.items():
        try:
            document.keywords[cls.lower()] = eval(cls)(**args)
        except NameError:
            logger.error(f"No class for '{cls}' found, skipping creation...")
    s = document().to_tex()
    print()


if __name__ == "__main__":
    main(
        r"C:\Users\Aaren\Documents\applications\resume_builder\template\yaml_input\template.yaml",
        r"C:\Users\Aaren\Documents\applications\resume_builder\template\yaml_input\template_out.yaml",
    )
