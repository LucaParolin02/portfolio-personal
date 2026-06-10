import { useEffect, useState } from 'react'

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
      <main className="flex min-h-screen items-center justify-center bg-[#F7F0E6] px-6 text-[#2F2520]">
        <section className="rounded-4x1 border border-[#DDCBB6] bg-[#FFF8EF]/80 p-8 text-center shadow-sm">
          <p className="text-sm font-semibold uppercase tracking-[0.28em] text-[#A7633D]">
            Cargando
          </p>

          <h1 className="mt-4 text-2xl font-bold">
            Preparando portfolio...
          </h1>

          <p className="mt-3 text-[#6E5E52]">
            Conectando con la API local.
          </p>
        </section>
      </main>
    )
  }

  if (errorMessage !== null) {
    return (
      <main className="flex min-h-screen items-center justify-center bg-[#F7F0E6] px-6 text-[#2F2520]">
        <section className="max-w-xl rounded-4x1 border border-[#B64A36]/30 bg-[#FFF8EF] p-8 shadow-sm">
          <p className="text-sm font-semibold uppercase tracking-[0.28em] text-[#B64A36]">
            Error de conexión
          </p>

          <h1 className="mt-4 text-2xl font-bold">
            No se pudo cargar la información del portfolio.
          </h1>

          <p className="mt-4 text-sm leading-7 text-[#6E5E52]">
            {errorMessage}
          </p>

          <p className="mt-4 text-sm leading-7 text-[#6E5E52]">
            Verificá que la API esté corriendo en{' '}
            <code className="rounded-lg bg-[#EFE2D0] px-2 py-1 font-semibold text-[#2F2520]">
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
    <main className="min-h-screen overflow-hidden text-[#2F2520]">
      <Header />

      <section
        id="top"
        className="relative mx-auto flex min-h-screen max-w-7xl flex-col justify-center px-6 py-24 md:px-10 lg:px-12"
      >
        <div className="absolute right-32 top-24 hidden h-72 w-72 rounded-full bg-[#A7633D]/10 blur-3xl lg:block" />
        <div className="absolute bottom-20 left-32 hidden h-72 w-72 rounded-full bg-[#7B8066]/10 blur-3xl lg:block" />

        <div className="relative grid gap-12 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
          <section>
            <p className="mb-5 text-sm font-bold uppercase tracking-[0.32em] text-[#A7633D]">
              Portfolio personal
            </p>

            <h1 className="max-w-4xl text-5xl font-black tracking-tight text-[#2F2520] md:text-7xl">
              {data.profile.name}
            </h1>

            <h2 className="mt-6 max-w-3xl text-2xl font-semibold leading-snug text-[#6E5E52] md:text-3xl">
              {data.profile.headline}
            </h2>

            <p className="mt-7 max-w-3xl text-lg leading-9 text-[#6E5E52]">
              {data.profile.summary}
            </p>

            <div className="mt-9 flex flex-wrap gap-4">
              <a
                href="#projects"
                className="rounded-full bg-[#A7633D] px-6 py-3 text-sm font-bold text-[#FFF8EF] shadow-lg shadow-[#A7633D]/20 transition hover:-translate-y-0.5 hover:bg-[#7A4329]"
              >
                Ver proyectos
              </a>

              <a
                href="#contact"
                className="rounded-full border border-[#A7633D]/30 bg-[#FFF8EF]/70 px-6 py-3 text-sm font-bold text-[#7A4329] transition hover:-translate-y-0.5 hover:border-[#A7633D] hover:bg-[#FFF8EF]"
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
                  className="rounded-full border border-[#DDCBB6] bg-[#FFF8EF]/70 px-4 py-2 text-sm font-bold text-[#5F5047] transition hover:border-[#A7633D] hover:text-[#A7633D]"
                >
                  {social.name}
                </a>
              ))}
            </div>
          </section>

          <aside className="rounded-[2.5rem] border border-[#DDCBB6] bg-[#FFF8EF]/80 p-7 shadow-xl shadow-[#A7633D]/10 backdrop-blur">
            <p className="text-sm font-bold uppercase tracking-[0.24em] text-[#A7633D]">
              Stack actual
            </p>

            <div className="mt-6 grid gap-3">
              {[
                'React + Vite + TypeScript',
                'FastAPI + PostgreSQL',
                'Docker + Docker Compose',
                'NGINX + DigitalOcean',
                'Aprendiendo AWS ECS y S3',
              ].map((item) => (
                <div
                  key={item}
                  className="rounded-2xl border border-[#DDCBB6] bg-[#F7F0E6] px-4 py-3 text-sm font-semibold text-[#55483F]"
                >
                  {item}
                </div>
              ))}
            </div>

            <div className="mt-7 rounded-3xl bg-[#2F2520] p-5 text-[#FFF8EF]">
              <p className="text-sm font-semibold text-[#E8D8C3]">
                Enfoque
              </p>

              <p className="mt-3 text-2xl font-bold leading-tight">
                Desarrollo fullstack, automatización, datos e infraestructura.
              </p>
            </div>
          </aside>
        </div>
      </section>

      <section id="projects" className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12">
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

      <section id="skills" className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12">
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

      <section id="experience" className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12">
        <SectionHeader
          eyebrow="Experiencia"
          title="Experiencia profesional y evolución técnica"
          description="Trabajo aplicado en desarrollo web, automatización, integración de servicios, SQL Server y construcción de soluciones internas."
        />

        <div className="relative mt-12 space-y-7 md:border-l md:border-[#DDCBB6] md:pl-8">
          {data.experience.map((experience) => (
            <ExperienceCard
              key={`${experience.company}-${experience.role}`}
              experience={experience}
            />
          ))}
        </div>
      </section>

      <section id="contact" className="mx-auto max-w-7xl px-6 py-24 md:px-10 lg:px-12">
        <div className="rounded-[2.5rem] border border-[#DDCBB6] bg-[#2F2520] p-8 text-[#FFF8EF] shadow-xl md:p-10">
          <p className="text-sm font-bold uppercase tracking-[0.28em] text-[#E8D8C3]">
            Contacto
          </p>

          <h2 className="mt-4 max-w-3xl text-3xl font-black tracking-tight md:text-5xl">
            ¿Hablamos sobre desarrollo, datos o automatización?
          </h2>

          <p className="mt-5 max-w-3xl text-base leading-8 text-[#E8D8C3]">
            Estoy construyendo este portfolio como una aplicación real para mostrar
            experiencia fullstack, backend, datos, contenedores y despliegue propio.
          </p>

          <div className="mt-8 flex flex-wrap gap-4">
            {data.profile.email !== null && (
              <a
                href={`mailto:${data.profile.email}`}
                className="rounded-full bg-[#FFF8EF] px-6 py-3 text-sm font-bold text-[#2F2520] transition hover:-translate-y-0.5 hover:bg-[#E8D8C3]"
              >
                Enviar email
              </a>
            )}

            {data.profile.socials.map((social) => (
              <a
                key={social.name}
                href={social.url}
                target="_blank"
                rel="noreferrer"
                className="rounded-full border border-[#FFF8EF]/25 px-6 py-3 text-sm font-bold text-[#FFF8EF] transition hover:-translate-y-0.5 hover:bg-[#FFF8EF]/10"
              >
                {social.name}
              </a>
            ))}
          </div>
        </div>
      </section>

      <Footer />
      <ScrollToTopButton />
    </main>
  )
}

function Header() {
  return (
    <header className="fixed left-0 right-0 top-0 z-40 border-b border-[#DDCBB6]/70 bg-[#F7F0E6]/80 backdrop-blur-xl">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 md:px-10 lg:px-12">
        <a href="#top" className="text-sm font-black tracking-tight text-[#2F2520]">
          Luca Parolin
        </a>

        <div className="hidden items-center gap-6 text-sm font-bold text-[#6E5E52] md:flex">
          <a className="transition hover:text-[#A7633D]" href="#projects">
            Proyectos
          </a>
          <a className="transition hover:text-[#A7633D]" href="#skills">
            Tecnologías
          </a>
          <a className="transition hover:text-[#A7633D]" href="#experience">
            Experiencia
          </a>
          <a className="transition hover:text-[#A7633D]" href="#contact">
            Contacto
          </a>
        </div>
      </nav>
    </header>
  )
}

function Footer() {
  return (
    <footer className="border-t border-[#DDCBB6] px-6 py-8 text-center text-sm text-[#6E5E52]">
      <p>
        Portfolio construido con React, Vite, TypeScript, Tailwind, FastAPI,
        PostgreSQL, Docker y despliegue propio.
      </p>
    </footer>
  )
}

export default App