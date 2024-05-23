from dataclasses import dataclass

from builder.sections import BaseTexDataClass
from builder.utils.const import L1, L2


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
            tex += f"{L1}\\explanationdetail{'{'}\n"
            tex += f"{L2}\\smallskip\n"
            for highlight in self.highlights:
                tex += f"{L2}\\coloredbullet\\ %\n"
                tex += f"{L2}{highlight}\n"
                tex += f"{L2}\\smallskip\n"
                tex += f"\n"
            tex += f"{L2}\\smallskip\n"
            tex += f"{L1}{'}'}\n"
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
