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
      <p className="text-base font-black uppercase tracking-[0.32em] text-(--color-primary) md:text-lg">
        {eyebrow.toUpperCase()}
      </p>

      <div className="mt-3 h-1 w-20 bg-(--color-primary)" />

      <h2 className="mt-5 text-3xl font-black tracking-tight text-(--color-dark) md:text-5xl">
        {title}
      </h2>

      <p className="mt-5 text-base leading-8 text-(--color-text-muted) md:text-lg">
        {description}
      </p>
    </header>
  )
}