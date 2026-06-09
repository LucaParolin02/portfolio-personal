from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.experience import (
    Experience,
    ExperienceAchievement,
    ExperienceTechnology,
)
from app.models.profile import Profile, SocialLink
from app.models.project import Project, ProjectHighlight, ProjectTechnology
from app.models.skill import Skill, SkillCategory


def reset_database(db: Session) -> None:
    """
    Limpia las tablas del portfolio para volver a cargar datos iniciales.

    Este script está pensado para desarrollo local.
    No debe usarse en producción sin una estrategia de backup/migración.
    """

    db.execute(delete(ExperienceTechnology))
    db.execute(delete(ExperienceAchievement))
    db.execute(delete(Experience))

    db.execute(delete(Skill))
    db.execute(delete(SkillCategory))

    db.execute(delete(ProjectTechnology))
    db.execute(delete(ProjectHighlight))
    db.execute(delete(Project))

    db.execute(delete(SocialLink))
    db.execute(delete(Profile))

    db.commit()


def seed_profile(db: Session) -> None:
    profile = Profile(
        name="Luca",
        headline="Software Engineer, Data Engineer & Builder",
        location="Argentina",
        summary=(
            "Desarrollo soluciones fullstack, automatizaciones, procesos de datos "
            "e infraestructura para productos digitales. Este portfolio está "
            "construido como una aplicación real: React, FastAPI, PostgreSQL, "
            "Docker, NGINX y despliegue propio en DigitalOcean."
        ),
        email=None,
        socials=[
            SocialLink(
                name="GitHub",
                url="https://github.com/tu-usuario",
                sort_order=1,
            ),
            SocialLink(
                name="LinkedIn",
                url="https://www.linkedin.com/in/tu-perfil",
                sort_order=2,
            ),
        ],
    )

    db.add(profile)
    db.commit()


def seed_projects(db: Session) -> None:
    projects = [
        Project(
            title="Portfolio Personal Fullstack",
            slug="portfolio-personal-fullstack",
            summary="Portfolio personal construido como aplicación fullstack propia.",
            description=(
                "Proyecto personal diseñado para mostrar habilidades de frontend, "
                "backend, infraestructura, despliegue, Docker, NGINX y arquitectura "
                "de servicios. No es solo una landing: está pensado como una "
                "plataforma evolutiva con API, base de datos y futuras integraciones."
            ),
            role="Fullstack Developer / DevOps",
            repository_url=None,
            demo_url=None,
            featured=True,
            technologies=[
                ProjectTechnology(name="React", sort_order=1),
                ProjectTechnology(name="Vite", sort_order=2),
                ProjectTechnology(name="TypeScript", sort_order=3),
                ProjectTechnology(name="Tailwind CSS", sort_order=4),
                ProjectTechnology(name="FastAPI", sort_order=5),
                ProjectTechnology(name="PostgreSQL", sort_order=6),
                ProjectTechnology(name="Docker", sort_order=7),
                ProjectTechnology(name="NGINX", sort_order=8),
                ProjectTechnology(name="DigitalOcean", sort_order=9),
            ],
            highlights=[
                ProjectHighlight(
                    text="Arquitectura frontend/backend separada.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="API versionada con FastAPI.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Persistencia real con PostgreSQL.",
                    sort_order=3,
                ),
                ProjectHighlight(
                    text="Despliegue pensado para VPS propio.",
                    sort_order=4,
                ),
            ],
        ),
        Project(
            title="API Gateway para Webhooks",
            slug="api-gateway-webhooks",
            summary="Base conceptual para recibir, validar y redirigir webhooks.",
            description=(
                "Servicio backend orientado a recibir webhooks, validar payloads, "
                "registrar eventos y derivar información hacia servicios internos "
                "o APIs externas según reglas de negocio."
            ),
            role="Backend Developer",
            repository_url=None,
            demo_url=None,
            featured=False,
            technologies=[
                ProjectTechnology(name="Python", sort_order=1),
                ProjectTechnology(name="FastAPI", sort_order=2),
                ProjectTechnology(name="Docker", sort_order=3),
                ProjectTechnology(name="RabbitMQ", sort_order=4),
                ProjectTechnology(name="PostgreSQL", sort_order=5),
            ],
            highlights=[
                ProjectHighlight(
                    text="Validación de payloads.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Separación de responsabilidades.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Diseño preparado para mensajería asincrónica.",
                    sort_order=3,
                ),
            ],
        ),
        Project(
            title="Procesos ETL y Automatización",
            slug="etl-automation",
            summary="Automatización de procesos de datos con Python y SQL.",
            description=(
                "Procesos orientados a extracción, transformación y carga de datos, "
                "integración con bases SQL, generación de reportes y reducción de "
                "tareas manuales operativas."
            ),
            role="Data Engineer",
            repository_url=None,
            demo_url=None,
            featured=False,
            technologies=[
                ProjectTechnology(name="Python", sort_order=1),
                ProjectTechnology(name="SQL Server", sort_order=2),
                ProjectTechnology(name="Pandas", sort_order=3),
                ProjectTechnology(name="SQLAlchemy", sort_order=4),
                ProjectTechnology(name="Docker", sort_order=5),
            ],
            highlights=[
                ProjectHighlight(
                    text="Automatización de tareas repetitivas.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Integración con bases de datos.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Optimización de tiempos de procesamiento.",
                    sort_order=3,
                ),
            ],
        ),
    ]

    db.add_all(projects)
    db.commit()


def seed_skills(db: Session) -> None:
    skill_categories = [
        SkillCategory(
            category="Frontend",
            sort_order=1,
            skills=[
                Skill(name="React", sort_order=1),
                Skill(name="Vite", sort_order=2),
                Skill(name="TypeScript", sort_order=3),
                Skill(name="Tailwind CSS", sort_order=4),
                Skill(name="HTML", sort_order=5),
                Skill(name="CSS", sort_order=6),
            ],
        ),
        SkillCategory(
            category="Backend",
            sort_order=2,
            skills=[
                Skill(name="Python", sort_order=1),
                Skill(name="FastAPI", sort_order=2),
                Skill(name="Flask", sort_order=3),
                Skill(name="Node.js", sort_order=4),
                Skill(name="REST APIs", sort_order=5),
            ],
        ),
        SkillCategory(
            category="Data",
            sort_order=3,
            skills=[
                Skill(name="SQL", sort_order=1),
                Skill(name="SQL Server", sort_order=2),
                Skill(name="PostgreSQL", sort_order=3),
                Skill(name="Pandas", sort_order=4),
                Skill(name="ETL", sort_order=5),
                Skill(name="Data Modeling", sort_order=6),
            ],
        ),
        SkillCategory(
            category="Infrastructure",
            sort_order=4,
            skills=[
                Skill(name="Docker", sort_order=1),
                Skill(name="Docker Compose", sort_order=2),
                Skill(name="NGINX", sort_order=3),
                Skill(name="Linux", sort_order=4),
                Skill(name="DigitalOcean", sort_order=5),
                Skill(name="GitHub Actions", sort_order=6),
            ],
        ),
    ]

    db.add_all(skill_categories)
    db.commit()


def seed_experience(db: Session) -> None:
    experience = Experience(
        company="Empresa / Cliente",
        role="Software Engineer / Data Engineer",
        period="2024 - Actualidad",
        summary=(
            "Desarrollo de soluciones internas, automatizaciones, procesos de datos, "
            "APIs, dashboards y herramientas orientadas a mejorar la operación."
        ),
        sort_order=1,
        achievements=[
            ExperienceAchievement(
                text="Diseño e implementación de procesos automatizados.",
                sort_order=1,
            ),
            ExperienceAchievement(
                text="Optimización de consultas y flujos de procesamiento.",
                sort_order=2,
            ),
            ExperienceAchievement(
                text="Construcción de herramientas internas para usuarios de negocio.",
                sort_order=3,
            ),
            ExperienceAchievement(
                text="Integración entre sistemas, APIs y bases de datos.",
                sort_order=4,
            ),
        ],
        technologies=[
            ExperienceTechnology(name="Python", sort_order=1),
            ExperienceTechnology(name="SQL Server", sort_order=2),
            ExperienceTechnology(name="FastAPI", sort_order=3),
            ExperienceTechnology(name="Flask", sort_order=4),
            ExperienceTechnology(name="Docker", sort_order=5),
            ExperienceTechnology(name="Power BI", sort_order=6),
        ],
    )

    db.add(experience)
    db.commit()


def main() -> None:
    db = SessionLocal()

    try:
        reset_database(db)
        seed_profile(db)
        seed_projects(db)
        seed_skills(db)
        seed_experience(db)

        print("Database seeded successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()