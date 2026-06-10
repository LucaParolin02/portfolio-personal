type SectionHeaderProps = {
    eyebrow: string
    title: string
    description: string
  }
  
  export function SectionHeader({
    eyebrow,
    title,
    description,
  }: SectionHeaderProps) {
    return (
      <header className="max-w-3xl">
        <p className="text-sm font-semibold uppercase tracking-[0.28em] text-[#A7633D]">
          {eyebrow}
        </p>
  
        <h2 className="mt-4 text-3xl font-bold tracking-tight text-[#2F2520] md:text-4xl">
          {title}
        </h2>
  
        <p className="mt-4 text-base leading-8 text-[#6E5E52]">
          {description}
        </p>
      </header>
    )
  }