from pydantic import BaseModel


class ProjectResponse(BaseModel):
    id: int
    title: str
    slug: str
    summary: str
    description: str
    role: str
    technologies: list[str]
    highlights: list[str]
    repository_url: str | None = None
    demo_url: str | None = None
    featured: bool = False