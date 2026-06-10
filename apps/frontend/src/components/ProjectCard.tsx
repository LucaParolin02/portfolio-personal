import type { Project } from '../types/portfolio'

type ProjectCardProps = {
  project: Project
  featured?: boolean
}

export function ProjectCard({ project, featured = false }: ProjectCardProps) {
  return (
    <article
      className={`group rounded-4x1 border p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl md:p-7 ${
        featured
          ? 'border-[#A7633D]/40 bg-[#FFF8EF]'
          : 'border-[#DDCBB6] bg-[#FFF8EF]/80'
      }`}
    >
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.24em] text-[#A7633D]">
            {project.role}
          </p>

          <h3 className="mt-3 text-2xl font-bold leading-tight text-[#2F2520]">
            {project.title}
          </h3>
        </div>

        {featured && (
          <span className="rounded-full border border-[#A7633D]/30 bg-[#F1D8C4] px-3 py-1 text-xs font-bold text-[#7A4329]">
            Destacado
          </span>
        )}
      </div>

      <p className="mt-4 text-sm leading-7 text-[#6E5E52] md:text-base">
        {project.description}
      </p>

      <ul className="mt-5 space-y-2 text-sm leading-6 text-[#55483F]">
        {project.highlights.map((highlight) => (
          <li key={highlight} className="flex gap-2">
            <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-[#A7633D]" />
            <span>{highlight}</span>
          </li>
        ))}
      </ul>

      <div className="mt-6 flex flex-wrap gap-2">
        {project.technologies.map((technology) => (
          <span
            key={technology}
            className="rounded-full border border-[#DDCBB6] bg-[#F7F0E6] px-3 py-1 text-xs font-semibold text-[#5F5047]"
          >
            {technology}
          </span>
        ))}
      </div>

      {(project.repository_url !== null || project.demo_url !== null) && (
        <div className="mt-6 flex flex-wrap gap-3">
          {project.repository_url !== null && (
            <a
              href={project.repository_url}
              target="_blank"
              rel="noreferrer"
              className="text-sm font-bold text-[#A7633D] transition hover:text-[#7A4329]"
            >
              Ver repositorio
            </a>
          )}

          {project.demo_url !== null && (
            <a
              href={project.demo_url}
              target="_blank"
              rel="noreferrer"
              className="text-sm font-bold text-[#A7633D] transition hover:text-[#7A4329]"
            >
              Ver demo
            </a>
          )}
        </div>
      )}
    </article>
  )
}