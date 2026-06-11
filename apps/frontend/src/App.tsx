import { useEffect, useState } from 'react'

import { ContactForm } from './components/ContactForm'
import { ExperienceCard } from './components/ExperienceCard'
import { ProjectCard } from './components/ProjectCard'
import { ScrollToTopButton } from './components/ScrollToTopButton'
import { SectionHeader } from './components/SectionHeader'
import { SkillCategoryCard } from './components/SkillCategoryCard'
import { portfolioApi } from './services/portfolioApi'
import type {
  Experience,
  Profile,
  Project,
  SkillCategory,
} from './types/portfolio'

type PortfolioData = {
  profile: Profile
  projects: Project[]
  skills: SkillCategory[]
  experience: Experience[]
}

function App() {
  const [data, setData] = useState<PortfolioData | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  useEffect(() => {
    async function loadPortfolioData() {
      try {
        setIsLoading(true)
        setErrorMessage(null)

        const [profile, projects, skills, experience] = await Promise.all([
          portfolioApi.getProfile(),
          portfolioApi.getProjects(),
          portfolioApi.getSkills(),
          portfolioApi.getExperience(),
        ])

        setData({
          profile,
          projects,
          skills,
          experience,
        })
      } catch (error) {
        const message =
          error instanceof Error
            ? error.message
            : 'Ocurrió un error inesperado al cargar el portfolio.'

        setErrorMessage(message)
      } finally {
        setIsLoading(false)
      }
    }

    loadPortfolioData()
  }, [])

  if (isLoading) {
    return (
      <main className="flex min-h-screen items-center justify-center bg-[var(--color-bg)] px-6 text-[var(--color-dark)]">
        <section className="bg-[var(--color-surface)] p-8 text-center shadow-sm">
          <p className="text-sm font-black uppercase tracking-[0.28em] text-[var(--color-primary)]">
            Cargando
          </p>

          <h1 className="mt-4 text-2xl font-black">
            Preparando portfolio...
          </h1>

          <p className="mt-3 text-[var(--color-text-muted)]">
            Conectando con la API local.
          </p>
        </section>
      </main>
    )
  }

  if (errorMessage !== null) {
    return (
      <main className="flex min-h-screen items-center justify-center bg-[var(--color-bg)] px-6 text-[var(--color-dark)]">
        <section className="max-w-xl bg-[var(--color-surface)] p-8 shadow-sm">
          <p className="text-sm font-black uppercase tracking-[0.28em] text-[var(--color-primary)]">
            Error de conexión
          </p>

          <h1 className="mt-4 text-2xl font-black">
            No se pudo cargar la información del portfolio.
          </h1>

          <p className="mt-4 text-sm leading-7 text-[var(--color-text-muted)]">
            {errorMessage}
          </p>

          <p className="mt-4 text-sm leading-7 text-[var(--color-text-muted)]">
            Verificá que la API esté corriendo en{' '}
            <code className="bg-[rgba(131,143,123,0.16)] px-2 py-1 font-semibold text-[var(--color-dark)]">
              http://localhost:8000
            </code>
          </p>
        </section>
      </main>
    )
  }

  if (data === null) {
    return null
  }

  const featuredProjects = data.projects.filter((project) => project.featured)
  const secondaryProjects = data.projects.filter((project) => !project.featured)

  return (
    <main className="min-h-screen overflow-hidden text-[var(--color-dark)]">
      <Header />

      <section
        id="top"
        className="relative mx-auto flex min-h-screen max-w-7xl flex-col justify-center px-6 py-24 md:px-10 lg:px-12"
      >
        <div className="absolute right-[-8rem] top-24 hidden h-72 w-72 bg-[rgba(84,112,61,0.10)] blur-3xl lg:block" />
        <div className="absolute bottom-20 left-[-8rem] hidden h-72 w-72 bg-[rgba(124,106,75,0.12)] blur-3xl lg:block" />

        <div className="relative grid gap-12 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
          <section>
            <p className="mb-5 text-sm font-black uppercase tracking-[0.32em] text-[var(--color-primary)]">
              Portfolio personal
            </p>

            <h1 className="max-w-4xl text-5xl font-black tracking-tight text-[var(--color-dark)] md:text-7xl">
              {data.profile.name}
            </h1>

            <h2 className="mt-6 max-w-3xl text-2xl font-semibold leading-snug text-[#6E5E52] md:text-3xl">
              {data.profile.headline}
            </h2>

            <p className="mt-7 max-w-3xl text-lg leading-9 text-[var(--color-text-muted)]">
              {data.profile.summary}
            </p>

            <div className="mt-9 flex flex-wrap gap-4">
              <a
                href="#projects"
                className="bg-[var(--color-panel-dark)] px-6 py-3 text-sm font-black text-[var(--color-bg)] shadow-lg shadow-[rgba(84,112,61,0.22)] transition hover:-translate-y-0.5 hover:bg-[var(--color-primary)]"
              >
                Ver proyectos
              </a>

              <a
                href="#contact"
                className="bg-[var(--color-surface)] px-6 py-3 text-sm font-black text-[var(--color-text-muted)] shadow-sm transition hover:-translate-y-0.5 hover:text-[var(--color-primary)]"
              >
                Contacto
              </a>
            </div>

            <div className="mt-9 flex flex-wrap gap-3">
              {data.profile.socials.map((social) => (
                <a
                  key={social.name}
                  href={social.url}
                  target="_blank"
                  rel="noreferrer"
                  className="bg-[var(--color-surface)] px-4 py-2 text-sm font-bold text-[var(--color-text-muted)] shadow-sm transition hover:-translate-y-0.5 hover:text-[var(--color-primary)]"
                >
                  {social.name}
                </a>
              ))}
            </div>
          </section>

          <aside className="bg-[var(--color-surface)] p-7 text-center shadow-xl shadow-[rgba(51,60,43,0.10)]">
            <div className="inline-block">
              <p className="text-base font-black uppercase tracking-[0.26em] text-[var(--color-primary)]">
                Stack actual
              </p>

              <div className="mx-auto mt-3 h-1 w-20 bg-[var(--color-primary)]" />
            </div>

            <div className="mt-7 grid gap-3">
              {[
                'React + Vite + TypeScript',
                'FastAPI + PostgreSQL',
                'Docker + Docker Compose',
                'NGINX + DigitalOcean',
                'Aprendiendo AWS ECS y S3',
              ].map((item) => (
                <div
                  key={item}
                  className="bg-[rgba(131,143,123,0.14)] px-4 py-3 text-center text-sm font-black text-[var(--color-dark)] shadow-sm"
                >
                  {item}
                </div>
              ))}
            </div>

            <div className="mt-7 bg-[var(--color-panel-dark)] p-5 text-left text-[var(--color-bg)] shadow-sm">
              <p className="text-xs font-black uppercase tracking-[0.24em] text-[var(--color-bg)]">
                Enfoque
              </p>

              <ul className="mt-4 grid gap-3 text-sm font-semibold leading-6 text-[var(--color-bg)]">
                {[
                  'Desarrollo fullstack',
                  'Automatización de procesos',
                  'Datos y SQL',
                  'Infraestructura y despliegue',
                ].map((item) => (
                  <li key={item} className="flex items-center gap-3">
                    <span className="h-2 w-2 shrink-0 rounded-full bg-[var(--color-muted)]" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </aside>
        </div>
      </section>

      <section
        id="projects"
        className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12"
      >
        <SectionHeader
          eyebrow="Proyectos"
          title="Soluciones reales, productos propios y práctica fullstack"
          description="Una selección de proyectos donde se combinan frontend, backend, integración de APIs, datos, automatización e infraestructura."
        />

        <div className="mt-12 grid gap-6 lg:grid-cols-2">
          {featuredProjects.map((project) => (
            <ProjectCard key={project.slug} project={project} featured />
          ))}

          {secondaryProjects.map((project) => (
            <ProjectCard key={project.slug} project={project} />
          ))}
        </div>
      </section>

      <section
        id="skills"
        className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12"
      >
        <SectionHeader
          eyebrow="Tecnologías"
          title="Stack técnico organizado por áreas"
          description="Tecnologías utilizadas en experiencia laboral, proyectos personales y aprendizaje actual."
        />

        <div className="mt-12 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {data.skills.map((skillCategory) => (
            <SkillCategoryCard
              key={skillCategory.category}
              skillCategory={skillCategory}
            />
          ))}
        </div>
      </section>

      <section
        id="experience"
        className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12"
      >
        <SectionHeader
          eyebrow="Experiencia"
          title="Experiencia profesional y evolución técnica"
          description="Trabajo aplicado en desarrollo web, automatización, integración de servicios, SQL Server y construcción de soluciones internas."
        />

        <div className="relative mt-12 space-y-7">
          {data.experience.map((experience) => (
            <ExperienceCard
              key={`${experience.company}-${experience.role}`}
              experience={experience}
            />
          ))}
        </div>
      </section>

      <section
        id="contact"
        className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12"
      >
        <div className="grid gap-8 bg-[var(--color-panel-dark)] p-8 text-[var(--color-bg)] shadow-xl md:p-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
          <section>
            <p className="text-base font-black uppercase tracking-[0.32em] text-[var(--color-bg)]">
              Contacto
            </p>

            <div className="mt-3 h-1 w-20 bg-[var(--color-bg)]" />

            <h2 className="mt-6 max-w-3xl text-3xl font-black tracking-tight md:text-5xl">
              ¿Hablamos sobre desarrollo, datos o automatización?
            </h2>

            <p className="mt-5 max-w-3xl text-base leading-8 text-[rgba(236,234,231,0.78)]">
              Estoy construyendo este portfolio como una aplicación real para
              mostrar experiencia fullstack, backend, datos, contenedores y
              despliegue propio.
            </p>

            <div className="mt-8 flex flex-wrap gap-4">
              {data.profile.socials.map((social) => (
                <a
                  key={social.name}
                  href={social.url}
                  target="_blank"
                  rel="noreferrer"
                  className="bg-[rgba(236,234,231,0.10)] px-6 py-3 text-sm font-bold text-[var(--color-bg)] transition hover:-translate-y-0.5 hover:bg-[rgba(236,234,231,0.16)]"
                >
                  {social.name}
                </a>
              ))}
            </div>
          </section>

          <ContactForm targetEmail={data.profile.email} />
        </div>
      </section>

      <Footer />
      <ScrollToTopButton />
    </main>
  )
}

function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const navItems = [
    {
      label: 'Proyectos',
      href: '#projects',
    },
    {
      label: 'Tecnologías',
      href: '#skills',
    },
    {
      label: 'Experiencia',
      href: '#experience',
    },
    {
      label: 'Contacto',
      href: '#contact',
    },
  ]

  function closeMenu() {
    setIsMenuOpen(false)
  }

  return (
    <header className="fixed left-0 right-0 top-0 z-40 bg-[rgba(236,234,231,0.92)] shadow-sm backdrop-blur-xl">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 md:px-10 lg:px-12">
        <a
          href="#top"
          onClick={closeMenu}
          className="text-sm font-black tracking-tight text-[var(--color-dark)]"
        >
          Luca Parolin
        </a>

        <div className="hidden items-center gap-6 text-sm font-bold text-[var(--color-dark)] md:flex">
          {navItems.map((item) => (
            <a
              key={item.href}
              className="transition hover:text-[var(--color-primary)]"
              href={item.href}
            >
              {item.label}
            </a>
          ))}
        </div>

        <button
          type="button"
          onClick={() => setIsMenuOpen((currentValue) => !currentValue)}
          aria-label={isMenuOpen ? 'Cerrar menú' : 'Abrir menú'}
          aria-expanded={isMenuOpen}
          className="flex h-10 w-10 flex-col items-center justify-center gap-1.5 bg-[var(--color-surface)] shadow-sm md:hidden"
        >
          <span
            className={`h-0.5 w-5 bg-[var(--color-dark)] transition ${
              isMenuOpen ? 'translate-y-2 rotate-45' : ''
            }`}
          />

          <span
            className={`h-0.5 w-5 bg-[var(--color-dark)] transition ${
              isMenuOpen ? 'opacity-0' : ''
            }`}
          />

          <span
            className={`h-0.5 w-5 bg-[var(--color-dark)] transition ${
              isMenuOpen ? '-translate-y-2 -rotate-45' : ''
            }`}
          />
        </button>
      </nav>

      {isMenuOpen && (
        <div className="bg-[rgba(236,234,231,0.96)] px-6 py-4 shadow-sm md:hidden">
          <div className="mx-auto grid max-w-7xl gap-3">
            {navItems.map((item) => (
              <a
                key={item.href}
                href={item.href}
                onClick={closeMenu}
                className="bg-[var(--color-surface)] px-4 py-3 text-sm font-black text-[var(--color-dark)] shadow-sm transition hover:text-[var(--color-primary)]"
              >
                {item.label}
              </a>
            ))}
          </div>
        </div>
      )}
    </header>
  )
}

function Footer() {
  return (
    <footer className="px-6 py-8 text-center text-sm text-[var(--color-text-muted)]">
      <p>
        Portfolio construido con React, Vite, TypeScript, Tailwind, FastAPI,
        PostgreSQL, Docker y despliegue propio.
      </p>
    </footer>
  )
}

export default App