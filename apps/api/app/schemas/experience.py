from pydantic import BaseModel


class ExperienceResponse(BaseModel):
    company: str
    role: str
    period: str
    summary: str
    achievements: list[str]
    technologies: list[str]