import type { SkillCategory } from '../types/portfolio'

type SkillCategoryCardProps = {
  skillCategory: SkillCategory
}

export function SkillCategoryCard({ skillCategory }: SkillCategoryCardProps) {
  return (
    <article className="rounded-[1.75rem] border border-[#DDCBB6] bg-[#FFF8EF]/80 p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">
      <h3 className="text-lg font-bold text-[#2F2520]">
        {skillCategory.category}
      </h3>

      <div className="mt-5 flex flex-wrap gap-2">
        {skillCategory.items.map((skill) => (
          <span
            key={skill}
            className="rounded-full bg-[#EFE2D0] px-3 py-1 text-xs font-semibold text-[#5F5047]"
          >
            {skill}
          </span>
        ))}
      </div>
    </article>
  )
}