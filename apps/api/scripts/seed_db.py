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
    No debe usarse en producción sin una estrategia previa de backup.
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
        name="Luca Parolin Massara",
        headline=(
            "Full Stack Developer SSR | Automatización de Procesos | "
            "SQL Server | C# | Java | Angular | React"
        ),
        location="Buenos Aires, Argentina",
        summary=(
            "Full Stack Developer con experiencia en desarrollo de soluciones web, "
            "automatización de procesos batch e integración de datos para entornos "
            "bancarios. Trabajo principalmente con C#, .NET, ASP.NET, Angular, "
            "SQL Server, scripting con CMD y PowerShell, y actualmente estoy "
            "fortaleciendo mi perfil con React, Docker, PostgreSQL y fundamentos "
            "de despliegue cloud con AWS ECS y S3."
        ),
        # Recomendación: usar email público profesional.
        # Si preferís no mostrar email en el sitio, dejá None.
        email="lucaparolin02@gmail.com",
        socials=[
            SocialLink(
                name="GitHub",
                url="https://github.com/LucaParolin02",
                sort_order=1,
            ),
            SocialLink(
                name="LinkedIn",
                url="https://linkedin.com/in/luca-parolin",
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
            summary=(
                "Portfolio personal desarrollado como aplicación fullstack real, "
                "con frontend, API, base de datos, contenedores y despliegue propio."
            ),
            description=(
                "Proyecto personal diseñado para presentar experiencia profesional, "
                "proyectos, habilidades técnicas y evolución como desarrollador. "
                "La solución está pensada como una aplicación fullstack real, no "
                "solo como una landing estática: cuenta con frontend en React, API "
                "en Python, persistencia con PostgreSQL, migraciones, seed de datos, "
                "Docker, NGINX y despliegue planificado en DigitalOcean."
            ),
            role="Full Stack Developer / Backend / DevOps Learning",
            repository_url=None,  # TODO: reemplazar cuando subas el repo público.
            demo_url=None,  # TODO: reemplazar cuando esté deployado.
            featured=True,
            technologies=[
                ProjectTechnology(name="React", sort_order=1),
                ProjectTechnology(name="Vite", sort_order=2),
                ProjectTechnology(name="TypeScript", sort_order=3),
                ProjectTechnology(name="Tailwind CSS", sort_order=4),
                ProjectTechnology(name="Python", sort_order=5),
                ProjectTechnology(name="FastAPI", sort_order=6),
                ProjectTechnology(name="PostgreSQL", sort_order=7),
                ProjectTechnology(name="SQLAlchemy", sort_order=8),
                ProjectTechnology(name="Alembic", sort_order=9),
                ProjectTechnology(name="Docker", sort_order=10),
                ProjectTechnology(name="Docker Compose", sort_order=11),
                ProjectTechnology(name="NGINX", sort_order=12),
                ProjectTechnology(name="DigitalOcean", sort_order=13),
            ],
            highlights=[
                ProjectHighlight(
                    text="Arquitectura separada entre frontend, API, base de datos e infraestructura.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="API versionada con FastAPI, schemas Pydantic, services y repositories.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Persistencia con PostgreSQL, SQLAlchemy y migraciones con Alembic.",
                    sort_order=3,
                ),
                ProjectHighlight(
                    text="Proyecto preparado para deploy en VPS con Docker, NGINX y dominio personalizado.",
                    sort_order=4,
                ),
            ],
        ),
        Project(
            title="E-commerce con Angular y Java",
            slug="ecommerce-angular-java",
            summary=(
                "Aplicación e-commerce desarrollada con frontend en Angular y backend en Java."
            ),
            description=(
                "Proyecto orientado a construir una plataforma de comercio electrónico "
                "con separación entre frontend y backend. El frontend se desarrolla con "
                "Angular y TypeScript, mientras que el backend utiliza Java, con foco en "
                "modelado de entidades, exposición de APIs, gestión de productos y "
                "estructura escalable para funcionalidades comerciales."
            ),
            role="Full Stack Developer",
            repository_url=None,  # TODO: agregar URL si el repo es público.
            demo_url=None,
            featured=True,
            technologies=[
                ProjectTechnology(name="Angular", sort_order=1),
                ProjectTechnology(name="TypeScript", sort_order=2),
                ProjectTechnology(name="Java", sort_order=3),
                ProjectTechnology(name="Spring", sort_order=4),
                ProjectTechnology(name="REST APIs", sort_order=5),
                ProjectTechnology(name="SQL", sort_order=6),
                ProjectTechnology(name="Git", sort_order=7),
            ],
            highlights=[
                ProjectHighlight(
                    text="Separación entre frontend Angular y backend Java.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Diseño orientado a funcionalidades típicas de e-commerce.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Uso de APIs REST para comunicación entre capas.",
                    sort_order=3,
                ),
                ProjectHighlight(
                    text="Proyecto útil para demostrar manejo fullstack fuera del stack laboral principal.",
                    sort_order=4,
                ),
            ],
        ),
        Project(
            title="Landing Page para Trabajador Independiente",
            slug="landing-page-trabajador-csharp-react",
            summary=(
                "Landing page profesional desarrollada con React y backend en C# para presentación de servicios."
            ),
            description=(
                "Sitio web orientado a presentar los servicios de un trabajador independiente, "
                "con foco en claridad comercial, presencia digital y estructura mantenible. "
                "El frontend se trabaja con React y el backend con C#, permitiendo separar "
                "la capa visual de posibles funcionalidades futuras como formulario de contacto, "
                "gestión de consultas o integración con servicios externos."
            ),
            role="Full Stack Developer",
            repository_url=None,
            demo_url=None,
            featured=False,
            technologies=[
                ProjectTechnology(name="React", sort_order=1),
                ProjectTechnology(name="TypeScript", sort_order=2),
                ProjectTechnology(name="C#", sort_order=3),
                ProjectTechnology(name=".NET", sort_order=4),
                ProjectTechnology(name="REST APIs", sort_order=5),
                ProjectTechnology(name="HTML", sort_order=6),
                ProjectTechnology(name="CSS", sort_order=7),
            ],
            highlights=[
                ProjectHighlight(
                    text="Diseño orientado a presentación profesional de servicios.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Separación entre frontend React y backend C#.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Base preparada para agregar formulario de contacto e integraciones.",
                    sort_order=3,
                ),
            ],
        ),
        Project(
            title="Sitio de Reporte de Saldos",
            slug="sitio-reporte-saldos",
            summary=(
                "Aplicación interna para consulta y visualización de saldos mediante integración con API laboral."
            ),
            description=(
                "Proyecto orientado a construir un sitio de reportes para visualizar saldos "
                "y consultar información proveniente de una API interna del entorno laboral. "
                "La solución contempla un frontend en Angular, consumo de servicios internos "
                "y presentación de datos de forma clara para usuarios técnicos o funcionales."
            ),
            role="Full Stack / Frontend Developer",
            repository_url=None,
            demo_url=None,
            featured=True,
            technologies=[
                ProjectTechnology(name="Angular", sort_order=1),
                ProjectTechnology(name="TypeScript", sort_order=2),
                ProjectTechnology(name="C#", sort_order=3),
                ProjectTechnology(name=".NET", sort_order=4),
                ProjectTechnology(name="REST APIs", sort_order=5),
                ProjectTechnology(name="SQL Server", sort_order=6),
                ProjectTechnology(name="Git", sort_order=7),
            ],
            highlights=[
                ProjectHighlight(
                    text="Consumo de API interna para obtener información de saldos.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Frontend desarrollado en Angular para visualización de datos.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Enfoque en reportes claros para facilitar análisis operativo.",
                    sort_order=3,
                ),
                ProjectHighlight(
                    text="Proyecto alineado con experiencia real en sistemas internos y datos bancarios.",
                    sort_order=4,
                ),
            ],
        ),
        Project(
            title="Automatización de Procesos Batch y CSV",
            slug="automatizacion-procesos-batch-csv",
            summary=(
                "Automatización de procesos operativos mediante scripts, SQL Server y generación de archivos CSV."
            ),
            description=(
                "Conjunto de tareas y procesos orientados a automatizar operaciones batch, "
                "consolidar información, generar archivos CSV y reducir tareas manuales "
                "en contextos de datos bancarios. Incluye scripting con CMD y PowerShell, "
                "consultas SQL, mantenimiento de datos y soporte a procesos internos."
            ),
            role="Full Stack Developer / Automation Developer",
            repository_url=None,
            demo_url=None,
            featured=False,
            technologies=[
                ProjectTechnology(name="PowerShell", sort_order=1),
                ProjectTechnology(name="CMD scripting", sort_order=2),
                ProjectTechnology(name="SQL Server", sort_order=3),
                ProjectTechnology(name="Stored Procedures", sort_order=4),
                ProjectTechnology(name="CSV", sort_order=5),
                ProjectTechnology(name="C#", sort_order=6),
                ProjectTechnology(name=".NET", sort_order=7),
            ],
            highlights=[
                ProjectHighlight(
                    text="Automatización de tareas batch y procesos repetitivos.",
                    sort_order=1,
                ),
                ProjectHighlight(
                    text="Generación y consolidación de archivos CSV con información bancaria.",
                    sort_order=2,
                ),
                ProjectHighlight(
                    text="Uso de SQL Server para consultas, joins, stored procedures y mantenimiento.",
                    sort_order=3,
                ),
                ProjectHighlight(
                    text="Foco en estabilidad, trazabilidad y reducción de intervención manual.",
                    sort_order=4,
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
                Skill(name="Angular", sort_order=1),
                Skill(name="React", sort_order=2),
                Skill(name="TypeScript", sort_order=3),
                Skill(name="JavaScript", sort_order=4),
                Skill(name="Vite", sort_order=5),
                Skill(name="Tailwind CSS", sort_order=6),
                Skill(name="HTML", sort_order=7),
                Skill(name="CSS", sort_order=8),
            ],
        ),
        SkillCategory(
            category="Backend",
            sort_order=2,
            skills=[
                Skill(name="C#", sort_order=1),
                Skill(name=".NET", sort_order=2),
                Skill(name="ASP.NET", sort_order=3),
                Skill(name="Java", sort_order=4),
                Skill(name="Spring", sort_order=5),
                Skill(name="Python", sort_order=6),
                Skill(name="FastAPI", sort_order=7),
                Skill(name="REST APIs", sort_order=8),
            ],
        ),
        SkillCategory(
            category="Bases de Datos",
            sort_order=3,
            skills=[
                Skill(name="SQL Server", sort_order=1),
                Skill(name="PostgreSQL", sort_order=2),
                Skill(name="SQL", sort_order=3),
                Skill(name="Stored Procedures", sort_order=4),
                Skill(name="Joins", sort_order=5),
                Skill(name="Mantenimiento de datos", sort_order=6),
                Skill(name="SQLAlchemy", sort_order=7),
                Skill(name="Alembic", sort_order=8),
            ],
        ),
        SkillCategory(
            category="Automatización y Procesos",
            sort_order=4,
            skills=[
                Skill(name="PowerShell", sort_order=1),
                Skill(name="CMD scripting", sort_order=2),
                Skill(name="Procesos batch", sort_order=3),
                Skill(name="Generación de CSV", sort_order=4),
                Skill(name="Consolidación de datos", sort_order=5),
                Skill(name="Integración de servicios internos", sort_order=6),
            ],
        ),
        SkillCategory(
            category="Infraestructura y DevOps",
            sort_order=5,
            skills=[
                Skill(name="Docker", sort_order=1),
                Skill(name="Docker Compose", sort_order=2),
                Skill(name="NGINX", sort_order=3),
                Skill(name="Linux", sort_order=4),
                Skill(name="DigitalOcean", sort_order=5),
                Skill(name="Git", sort_order=6),
                Skill(name="GitHub", sort_order=7),
                Skill(name="GitHub Actions", sort_order=8),
            ],
        ),
        SkillCategory(
            category="Cloud en Aprendizaje",
            sort_order=6,
            skills=[
                Skill(name="AWS ECS", sort_order=1),
                Skill(name="AWS S3", sort_order=2),
                Skill(name="Contenedores en cloud", sort_order=3),
                Skill(name="Despliegue de aplicaciones", sort_order=4),
            ],
        ),
        SkillCategory(
            category="Herramientas",
            sort_order=7,
            skills=[
                Skill(name="Jira", sort_order=1),
                Skill(name="Visual Studio", sort_order=2),
                Skill(name="Visual Studio Code", sort_order=3),
                Skill(name="Adminer", sort_order=4),
                Skill(name="Docker Desktop", sort_order=5),
            ],
        ),
    ]

    db.add_all(skill_categories)
    db.commit()


def seed_experience(db: Session) -> None:
    experiences = [
        Experience(
            company="ASJ, Grupo Petersen",
            role="Full Stack Developer",
            period="2023 - Actualidad",
            summary=(
                "Desarrollo y mantenimiento de aplicaciones web, automatización de "
                "procesos batch y trabajo con datos bancarios. Participación en "
                "integraciones mediante APIs REST, procesos internos, generación de "
                "archivos CSV, consultas SQL y colaboración con equipos técnicos y "
                "funcionales bajo gestión de tareas en Jira."
            ),
            sort_order=1,
            achievements=[
                ExperienceAchievement(
                    text="Desarrollo y mantenimiento de aplicaciones web con C#, .NET, ASP.NET y Angular.",
                    sort_order=1,
                ),
                ExperienceAchievement(
                    text="Diseño y consumo de APIs REST para integrar servicios internos.",
                    sort_order=2,
                ),
                ExperienceAchievement(
                    text="Automatización de procesos batch mediante scripts en CMD y PowerShell.",
                    sort_order=3,
                ),
                ExperienceAchievement(
                    text="Trabajo con SQL Server mediante consultas, joins, stored procedures y tareas de mantenimiento.",
                    sort_order=4,
                ),
                ExperienceAchievement(
                    text="Generación y consolidación de archivos CSV con información de bancos del grupo.",
                    sort_order=5,
                ),
                ExperienceAchievement(
                    text="Trabajo colaborativo con equipos técnicos y de negocio usando Jira.",
                    sort_order=6,
                ),
            ],
            technologies=[
                ExperienceTechnology(name="C#", sort_order=1),
                ExperienceTechnology(name=".NET", sort_order=2),
                ExperienceTechnology(name="ASP.NET", sort_order=3),
                ExperienceTechnology(name="Angular", sort_order=4),
                ExperienceTechnology(name="SQL Server", sort_order=5),
                ExperienceTechnology(name="REST APIs", sort_order=6),
                ExperienceTechnology(name="PowerShell", sort_order=7),
                ExperienceTechnology(name="CMD scripting", sort_order=8),
                ExperienceTechnology(name="CSV", sort_order=9),
                ExperienceTechnology(name="Jira", sort_order=10),
                ExperienceTechnology(name="Git", sort_order=11),
            ],
        ),
        Experience(
            company="Formación y proyectos personales",
            role="Full Stack Developer en formación continua",
            period="Actualidad",
            summary=(
                "Profundización práctica en tecnologías modernas para desarrollo "
                "fullstack, contenedores, despliegue de aplicaciones e infraestructura. "
                "Construcción de proyectos propios con React, FastAPI, PostgreSQL, Docker "
                "y exploración de servicios cloud como AWS ECS y S3."
            ),
            sort_order=2,
            achievements=[
                ExperienceAchievement(
                    text="Construcción de portfolio personal fullstack con React, FastAPI, PostgreSQL y Docker.",
                    sort_order=1,
                ),
                ExperienceAchievement(
                    text="Práctica de arquitectura por capas: routers, schemas, services, repositories y models.",
                    sort_order=2,
                ),
                ExperienceAchievement(
                    text="Uso de Docker Compose para levantar servicios locales como PostgreSQL y Adminer.",
                    sort_order=3,
                ),
                ExperienceAchievement(
                    text="Aprendizaje progresivo de despliegues cloud con AWS ECS y almacenamiento en S3.",
                    sort_order=4,
                ),
            ],
            technologies=[
                ExperienceTechnology(name="React", sort_order=1),
                ExperienceTechnology(name="Vite", sort_order=2),
                ExperienceTechnology(name="TypeScript", sort_order=3),
                ExperienceTechnology(name="Tailwind CSS", sort_order=4),
                ExperienceTechnology(name="Python", sort_order=5),
                ExperienceTechnology(name="FastAPI", sort_order=6),
                ExperienceTechnology(name="PostgreSQL", sort_order=7),
                ExperienceTechnology(name="Docker", sort_order=8),
                ExperienceTechnology(name="Docker Compose", sort_order=9),
                ExperienceTechnology(name="AWS ECS", sort_order=10),
                ExperienceTechnology(name="AWS S3", sort_order=11),
            ],
        ),
    ]

    db.add_all(experiences)
    db.commit()


def main() -> None:
    db = SessionLocal()

    try:
        reset_database(db)
        seed_profile(db)
        seed_projects(db)
        seed_skills(db)
        seed_experience(db)

        print("Database seeded successfully with real portfolio data.")
    finally:
        db.close()


if __name__ == "__main__":
    main()