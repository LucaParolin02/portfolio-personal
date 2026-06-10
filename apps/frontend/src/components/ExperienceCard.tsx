import type { Experience } from '../types/portfolio'

type ExperienceCardProps = {
  experience: Experience
}

export function ExperienceCard({ experience }: ExperienceCardProps) {
  return (
    <article className="relative rounded-4x1 border border-[#DDCBB6] bg-[#FFF8EF]/85 p-6 shadow-sm md:p-7">
      <div className="absolute -left-2 top-8 hidden h-4 w-4 rounded-full border-4 border-[#F7F0E6] bg-[#A7633D] md:block" />

      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div>
          <h3 className="text-2xl font-bold text-[#2F2520]">
            {experience.role}
          </h3>

          <p className="mt-1 text-sm font-semibold uppercase tracking-[0.18em] text-[#A7633D]">
            {experience.company}
          </p>
        </div>

        <p className="rounded-full border border-[#DDCBB6] bg-[#F7F0E6] px-4 py-2 text-sm font-semibold text-[#6E5E52]">
          {experience.period}
        </p>
      </div>

      <p className="mt-5 leading-8 text-[#6E5E52]">{experience.summary}</p>

      <ul className="mt-5 space-y-2 text-sm leading-7 text-[#55483F]">
        {experience.achievements.map((achievement) => (
          <li key={achievement} className="flex gap-2">
            <span className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-[#7B8066]" />
            <span>{achievement}</span>
          </li>
        ))}
      </ul>

      <div className="mt-6 flex flex-wrap gap-2">
        {experience.technologies.map((technology) => (
          <span
            key={technology}
            className="rounded-full border border-[#DDCBB6] bg-[#EFE2D0] px-3 py-1 text-xs font-semibold text-[#5F5047]"
          >
            {technology}
          </span>
        ))}
      </div>
    </article>
  )
}