from dataclasses import dataclass

from builder.sections import BaseTexDataClass
from builder.utils.const import L1, L2


@dataclass(kw_only=True)
class EducationDetail(BaseTexDataClass):
    name: str
    location: str
    degree: str
    field: str
    start_date: str
    end_date: str
    highlights: list[str] = list

    @classmethod
    def from_config(cls, **kwargs) -> "EducationDetail":
        return cls(**kwargs)

    def to_tex(self) -> str:
        tex = f"{L1}%\n"
        tex += f"{L1}\\datedexperience{{{self.degree} - {self.field}}}{{{self.start_date} - {self.end_date}}}\n"
        tex += f"{L1}\\explanation{{{self.name}}}{{{self.location}}}\n"
        if self.highlights:
            tex += f"{L1}\\explanationdetail{'{'}\n"
            for highlight in self.highlights:
                tex += f"{L2}\\smallskip\n"
                tex += f"{L2}\\coloredbullet\\ %\n"
                tex += f"{L2}{highlight}\n"
            tex += f"{L2}\\smallskip\n"
            tex += f"{L1}{'}'}\n"
        tex += f"{L1}%\n"
        return tex


@dataclass(kw_only=True)
class Education(BaseTexDataClass):
    education_details: list[EducationDetail]

    @classmethod
    def from_config(cls, **kwargs) -> "Education":
        education_details = []
        for _, detail in kwargs.items():
            education_details.append(EducationDetail.from_config(**detail))
        return cls(education_details=education_details)

    def to_tex(self) -> str:
        tex = ""
        tex += "\\section{Education}\n"
        tex += "%\n"
        for group in self.education_details:
            tex += group.to_tex()
        tex += "%\n"
        return tex
