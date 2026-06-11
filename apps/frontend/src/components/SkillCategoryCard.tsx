import type { SkillCategory } from '../types/portfolio'

type SkillCategoryCardProps = {
  skillCategory: SkillCategory
}

export function SkillCategoryCard({ skillCategory }: SkillCategoryCardProps) {
  return (
    <article className="rounded-[1.75rem] border border-[rgba(124,106,75,0.18)] bg-[var(--color-surface)] p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
      <h3 className="text-center text-lg font-black text-[var(--color-dark)]">
        {skillCategory.category}
      </h3>

      <div className="mt-5 flex flex-wrap justify-center gap-2">
        {skillCategory.items.map((skill) => (
          <span
            key={skill}
            className="rounded-full bg-[rgba(131,143,123,0.16)] px-3 py-1 text-xs font-bold text-[var(--color-dark)]"
          >
            {skill}
          </span>
        ))}
      </div>
    </article>
  )
}