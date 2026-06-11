import type { Experience } from '../types/portfolio'

type ExperienceCardProps = {
  experience: Experience
}

export function ExperienceCard({ experience }: ExperienceCardProps) {
  return (
    <article className="bg-[var(--color-surface)] p-6 shadow-sm md:p-7">
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div>
          <h3 className="text-2xl font-black text-[var(--color-dark)]">
            {experience.role}
          </h3>

          <p className="mt-1 text-sm font-black uppercase tracking-[0.18em] text-[var(--color-primary)]">
            {experience.company}
          </p>
        </div>

        <p className="bg-[rgba(131,143,123,0.16)] px-4 py-2 text-sm font-bold text-[var(--color-dark)]">
          {experience.period}
        </p>
      </div>

      <p className="mt-5 leading-8 text-[var(--color-text-muted)]">
        {experience.summary}
      </p>

      <ul className="mt-5 space-y-2 text-sm leading-7 text-[var(--color-text-muted)]">
        {experience.achievements.map((achievement) => (
          <li key={achievement} className="flex gap-2">
            <span className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--color-accent)]" />
            <span>{achievement}</span>
          </li>
        ))}
      </ul>

      <div className="mt-6 flex flex-wrap gap-2">
        {experience.technologies.map((technology) => (
          <span
            key={technology}
            className="bg-[rgba(131,143,123,0.16)] px-3 py-1 text-xs font-bold text-[var(--color-dark)]"
          >
            {technology}
          </span>
        ))}
      </div>
    </article>
  )
}