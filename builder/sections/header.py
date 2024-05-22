from dataclasses import dataclass

from builder.sections import BaseTexDataClass


@dataclass(kw_only=True)
class Header(BaseTexDataClass):
    first_name: str
    last_name: str
    city: str
    state: str
    mobile: str
    email: str
    linkedin_url: str
    github_url: str
    years_of_experience: int

    def to_tex(self) -> str:
        tex = ""
        tex += f"\setname{{{self.first_name}}}{{{self.last_name}}}\n"
        tex += f"\setaddress{{{self.city}, {self.state}}}\n"
        tex += f"\setmobile{{{self.mobile}}}\n"
        tex += f"\setmail{{{self.email}}}\n"
        tex += f"\setlinkedinaccount{{{self.linkedin_url}}}\n"
        tex += f"\setgithubaccount{{{self.github_url}}}\n"
        tex += f"\setyearsofexperience{{{self.years_of_experience}}}\n"
        return tex
