from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.experience import Experience
from app.models.profile import Profile
from app.models.project import Project
from app.models.skill import SkillCategory


def _profile_to_dict(profile: Profile) -> dict:
    return {
        "name": profile.name,
        "headline": profile.headline,
        "location": profile.location,
        "summary": profile.summary,
        "email": profile.email,
        "socials": [
            {
                "name": social.name,
                "url": social.url,
            }
            for social in sorted(profile.socials, key=lambda item: item.sort_order)
        ],
    }


def _project_to_dict(project: Project) -> dict:
    return {
        "id": project.id,
        "title": project.title,
        "slug": project.slug,
        "summary": project.summary,
        "description": project.description,
        "role": project.role,
        "technologies": [
            technology.name
            for technology in sorted(project.technologies, key=lambda item: item.sort_order)
        ],
        "highlights": [
            highlight.text
            for highlight in sorted(project.highlights, key=lambda item: item.sort_order)
        ],
        "repository_url": project.repository_url,
        "demo_url": project.demo_url,
        "featured": project.featured,
    }


def _skill_category_to_dict(skill_category: SkillCategory) -> dict:
    return {
        "category": skill_category.category,
        "items": [
            skill.name
            for skill in sorted(skill_category.skills, key=lambda item: item.sort_order)
        ],
    }


def _experience_to_dict(experience: Experience) -> dict:
    return {
        "company": experience.company,
        "role": experience.role,
        "period": experience.period,
        "summary": experience.summary,
        "achievements": [
            achievement.text
            for achievement in sorted(
                experience.achievements,
                key=lambda item: item.sort_order,
            )
        ],
        "technologies": [
            technology.name
            for technology in sorted(
                experience.technologies,
                key=lambda item: item.sort_order,
            )
        ],
    }


def get_profile(db: Session) -> dict | None:
    stmt = (
        select(Profile)
        .options(selectinload(Profile.socials))
        .order_by(Profile.id.asc())
    )

    profile = db.scalars(stmt).first()

    if profile is None:
        return None

    return _profile_to_dict(profile)


def get_projects(db: Session) -> list[dict]:
    stmt = (
        select(Project)
        .options(
            selectinload(Project.technologies),
            selectinload(Project.highlights),
        )
        .order_by(Project.featured.desc(), Project.id.asc())
    )

    projects = db.scalars(stmt).all()

    return [_project_to_dict(project) for project in projects]


def get_project_by_slug(db: Session, slug: str) -> dict | None:
    stmt = (
        select(Project)
        .options(
            selectinload(Project.technologies),
            selectinload(Project.highlights),
        )
        .where(Project.slug == slug)
    )

    project = db.scalars(stmt).first()

    if project is None:
        return None

    return _project_to_dict(project)


def get_skills(db: Session) -> list[dict]:
    stmt = (
        select(SkillCategory)
        .options(selectinload(SkillCategory.skills))
        .order_by(SkillCategory.sort_order.asc())
    )

    skill_categories = db.scalars(stmt).all()

    return [_skill_category_to_dict(skill_category) for skill_category in skill_categories]


def get_experience(db: Session) -> list[dict]:
    stmt = (
        select(Experience)
        .options(
            selectinload(Experience.achievements),
            selectinload(Experience.technologies),
        )
        .order_by(Experience.sort_order.asc())
    )

    experiences = db.scalars(stmt).all()

    return [_experience_to_dict(experience) for experience in experiences]