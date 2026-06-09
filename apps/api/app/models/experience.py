from __future__ import annotations

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Experience(Base, TimestampMixin):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    company: Mapped[str] = mapped_column(String(180), nullable=False)
    role: Mapped[str] = mapped_column(String(180), nullable=False)
    period: Mapped[str] = mapped_column(String(120), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    achievements: Mapped[list[ExperienceAchievement]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan",
    )

    technologies: Mapped[list[ExperienceTechnology]] = relationship(
        back_populates="experience",
        cascade="all, delete-orphan",
    )


class ExperienceAchievement(Base, TimestampMixin):
    __tablename__ = "experience_achievements"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    experience_id: Mapped[int] = mapped_column(
        ForeignKey("experiences.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    text: Mapped[str] = mapped_column(String(500), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    experience: Mapped[Experience] = relationship(back_populates="achievements")


class ExperienceTechnology(Base, TimestampMixin):
    __tablename__ = "experience_technologies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    experience_id: Mapped[int] = mapped_column(
        ForeignKey("experiences.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    experience: Mapped[Experience] = relationship(back_populates="technologies")