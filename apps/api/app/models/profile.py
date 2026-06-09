from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Profile(Base, TimestampMixin):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    headline: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(120), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)

    email: Mapped[str | None] = mapped_column(String(255), nullable=True)

    socials: Mapped[list[SocialLink]] = relationship(
        back_populates="profile",
        cascade="all, delete-orphan",
    )


class SocialLink(Base, TimestampMixin):
    __tablename__ = "social_links"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(80), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    profile: Mapped[Profile] = relationship(back_populates="socials")