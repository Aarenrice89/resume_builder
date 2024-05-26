from dataclasses import dataclass

from builder.sections import BaseTexDataClass
from builder.utils.const import L1
from builder.utils.formatting import handle_bulled_list


@dataclass(kw_only=True)
class ExperienceDetail(BaseTexDataClass):
    name: str
    title: str
    location: str
    start_date: str
    end_date: str
    highlights: list[str]

    @classmethod
    def from_config(cls, **kwargs) -> "ExperienceDetail":
        return cls(**kwargs)

    def to_tex(self) -> str:
        tex = ""
        tex += f"{L1}\\datedexperience{{{self.name}}}{{{self.start_date} - {self.end_date}}}\n"
        tex += f"{L1}\\explanation{{{self.title}}}{{{self.location}}}\n"
        tex += handle_bulled_list(self.highlights)
        tex += f"{L1}%\n"
        return tex


@dataclass(kw_only=True)
class Experience(BaseTexDataClass):
    experience_details: list[ExperienceDetail]

    @classmethod
    def from_config(cls, **kwargs) -> "Experience":
        experience_details = []
        for _, detail in kwargs.items():
            experience_details.append(ExperienceDetail.from_config(**detail))
        return cls(experience_details=experience_details)

    def to_tex(self) -> str:
        tex = ""
        tex += "\\section{Experience}\n"
        tex += f"{L1}%\n"
        for group in self.experience_details:
            tex += group.to_tex()
        tex += "%\n"
        return tex
