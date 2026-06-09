from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class SkillCategory(Base, TimestampMixin):
    __tablename__ = "skill_categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    category: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    skills: Mapped[list[Skill]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan",
    )


class Skill(Base, TimestampMixin):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("skill_categories.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    category: Mapped[SkillCategory] = relationship(back_populates="skills")