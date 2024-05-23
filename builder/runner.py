import logging
from dataclasses import dataclass
from functools import partial
from pathlib import Path

import yaml

from builder.sections import (
    BaseTexDataClass,
    Education,
    Experience,
    Header,
    Projects,
    Skills,
)

logger = logging.getLogger(__file__)


@dataclass(kw_only=True)
class Document(BaseTexDataClass):
    theme_color: str = "MidnightBlue"
    header: Header
    skills: Skills
    experience: Experience
    education: Education
    projects: Projects

    def to_tex(self) -> str:
        tex = "\\documentclass{styling}\n\n"
        tex += f"\\setthemecolor{{{self.theme_color}}}\n\n"
        tex += self.header.to_tex()
        tex += "\n\\begin{document}\n"
        tex += "%Create header\n"
        tex += "\\headerview\n"
        tex += "\\bigskip % white space\n"
        tex += "%\n"
        tex += self.skills.to_tex()
        tex += self.experience.to_tex()
        tex += self.education.to_tex()
        tex += self.projects.to_tex()
        tex += "\n\n\\end{document}\n"
        return tex


def main(input: str | Path, output: str | Path) -> str:
    input = input if isinstance(input, Path) else Path(input)
    output = output if isinstance(output, Path) else Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(input, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    document = partial(
        Document,
    )
    for cls, args in data.items():
        try:
            if cls == "Document":
                document.keywords.update(args)
            else:
                document.keywords[cls.lower()] = eval(cls).from_config(**args)
        except NameError:
            logger.error(f"No class for '{cls}' found, skipping creation...")

    with open(output, "w") as f:
        f.write(document().to_tex())


if __name__ == "__main__":
    main(
        r"C:\Users\Aaren\Documents\applications\resume_builder\template\yaml_input\template.yaml",
        r"C:\Users\Aaren\Documents\applications\resume_builder\outputs\testing.tex",
    )
