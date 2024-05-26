from dataclasses import dataclass

from builder.sections import BaseTexDataClass
from builder.utils.const import L1, L2
from builder.utils.formatting import handle_bulled_list


@dataclass(kw_only=True)
class ProjectDetail(BaseTexDataClass):
    name: str
    role: str
    location: str
    start_date: str
    end_date: str
    highlights: list[str] = list

    @classmethod
    def from_config(cls, **kwargs) -> "ProjectDetail":
        return cls(**kwargs)

    def to_tex(self) -> str:
        tex = ""
        tex += f"{L1}\\datedexperience{{{self.name}}}{{{self.start_date} - {self.end_date}}}\n"
        tex += f"{L1}\\explanation{{{self.role}}}{{{self.location}}}\n"
        if self.highlights:
            tex += handle_bulled_list(self.highlights)
        tex += f"{L1}%\n"
        return tex


@dataclass(kw_only=True)
class Projects(BaseTexDataClass):
    education_details: list[ProjectDetail]

    @classmethod
    def from_config(cls, **kwargs) -> "Projects":
        education_details = []
        for _, detail in kwargs.items():
            education_details.append(ProjectDetail.from_config(**detail))
        return cls(education_details=education_details)

    def to_tex(self) -> str:
        tex = ""
        tex += "\\section{Notable Projects}\n"
        tex += f"{L1}%\n"
        for group in self.education_details:
            tex += group.to_tex()
        tex += "%\n"
        return tex
