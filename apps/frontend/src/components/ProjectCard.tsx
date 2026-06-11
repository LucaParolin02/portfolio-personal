import type { Project } from "../types/portfolio";

type ProjectCardProps = {
  project: Project;
  featured?: boolean;
};

export function ProjectCard({ project, featured = false }: ProjectCardProps) {
  return (
    <article
      className={`p-6 shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl md:p-7 ${
        featured ? "bg-[var(--color-surface)]" : "bg-[rgba(251,250,247,0.84)]"
      }`}
    >
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-xs font-black uppercase tracking-[0.24em] text-[var(--color-primary)]">
            {project.role}
          </p>

          <h3 className="mt-3 text-2xl font-black leading-tight text-[var(--color-dark)]">
            {project.title}
          </h3>
        </div>

        {featured && (
          <span className="bg-[rgba(124,106,75,0.16)] px-3 py-1 text-xs font-black text-[var(--color-accent)]">
            Destacado
          </span>
        )}
      </div>

      <p className="mt-4 text-sm leading-7 text-[var(--color-text-muted)] md:text-base">
        {project.description}
      </p>

      <ul className="mt-5 space-y-2 text-sm leading-6 text-[var(--color-text-muted)]">
        {project.highlights.map((highlight) => (
          <li key={highlight} className="flex gap-2">
            <span className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--color-accent)]" />
            <span>{highlight}</span>
          </li>
        ))}
      </ul>

      <div className="mt-6 flex flex-wrap gap-2">
        {project.technologies.map((technology) => (
          <span
            key={technology}
            className="bg-[rgba(131,143,123,0.16)] px-3 py-1 text-xs font-bold text-[var(--color-dark)]"
          >
            {technology}
          </span>
        ))}
      </div>
    </article>
  );
}
