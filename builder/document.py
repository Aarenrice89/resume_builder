from dataclasses import dataclass
from pathlib import Path

from builder.sections import (
    BaseTexDataClass,
    Education,
    Experience,
    Header,
    Projects,
    Skills,
)


@dataclass(kw_only=True)
class Document(BaseTexDataClass):
    job_title: str
    posting_url: str
    local_output_tex_file_path: Path
    theme_color: str = "MidnightBlue"
    header: Header
    skills: Skills
    experience: Experience
    education: Education
    projects: Projects

    def to_tex(self) -> str:
        tex = "\\documentclass{styling}\n\n"
        tex += f"\\setthemecolor{{{self.theme_color}}}\n"
        tex += f"\\setpostingurl{{{self.job_title}}}{{{self.posting_url}}}\n\n"
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
