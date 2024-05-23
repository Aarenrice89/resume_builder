from dataclasses import dataclass

from builder.sections import BaseTexDataClass
from builder.utils.const import L1, NUM_TO_WORD


@dataclass(kw_only=True)
class SkillGroup(BaseTexDataClass):
    key: str
    name: str
    items: list[str]

    @classmethod
    def from_config(cls, **kwargs) -> "SkillGroup":
        prefix, _key = kwargs.pop("key").split("_")
        return cls(key=f"{prefix}{NUM_TO_WORD[_key]}", **kwargs)

    def to_tex(self) -> str:
        joined = " \\cpshalf ".join(self.items)
        tex = f"{L1}\\newcommand{{\\{self.key}}}{{\\createskill{{{self.name}}}{{{joined}}}}}\n"
        return tex


@dataclass(kw_only=True)
class Skills(BaseTexDataClass):
    skill_groups: list[SkillGroup]

    @classmethod
    def from_config(cls, **kwargs) -> "Skills":
        groups = []
        for key, info in kwargs.items():
            groups.append(SkillGroup.from_config(key=key, **info))
        return cls(skill_groups=groups)

    def to_tex(self) -> str:
        joined_skills = ", ".join(f"\\{x.key}" for x in self.skill_groups)

        tex = ""
        tex += "\\section{Skills}\n"
        tex += "%\n"
        tex += f"{L1}%\n"
        tex += f"{L1}\\vspace{{0.25mm}}\n"
        for group in self.skill_groups:
            tex += group.to_tex()
        tex += f"{L1}%\n"
        tex += f"{L1}\\createskills{{{joined_skills}}}\n"
        tex += f"{L1}\n"
        tex += f"{L1}\\vspace{{-2mm}}\n"
        tex += f"{L1}%\n"
        tex += "%\n"
        return tex
