from pydantic import BaseModel


class SocialLink(BaseModel):
    name: str
    url: str


class ProfileResponse(BaseModel):
    name: str
    headline: str
    location: str
    summary: str
    email: str | None = None
    socials: list[SocialLink]