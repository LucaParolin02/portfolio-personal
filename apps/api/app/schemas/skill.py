from pydantic import BaseModel


class SkillCategoryResponse(BaseModel):
    category: str
    items: list[str]