from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Project(Base, TimestampMixin):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(180), nullable=False)
    slug: Mapped[str] = mapped_column(String(220), nullable=False, unique=True, index=True)

    summary: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(String(160), nullable=False)

    repository_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    demo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    technologies: Mapped[list[ProjectTechnology]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )

    highlights: Mapped[list[ProjectHighlight]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan",
    )


class ProjectTechnology(Base, TimestampMixin):
    __tablename__ = "project_technologies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    project: Mapped[Project] = relationship(back_populates="technologies")


class ProjectHighlight(Base, TimestampMixin):
    __tablename__ = "project_highlights"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    text: Mapped[str] = mapped_column(String(500), nullable=False)
    sort_order: Mapped[int] = mapped_column(default=0, nullable=False)

    project: Mapped[Project] = relationship(back_populates="highlights")