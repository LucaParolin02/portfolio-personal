export type SocialLink = {
    name: string
    url: string
  }
  
  export type Profile = {
    name: string
    headline: string
    location: string
    summary: string
    email: string | null
    socials: SocialLink[]
  }
  
  export type Project = {
    id: number
    title: string
    slug: string
    summary: string
    description: string
    role: string
    technologies: string[]
    highlights: string[]
    repository_url: string | null
    demo_url: string | null
    featured: boolean
  }
  
  export type SkillCategory = {
    category: string
    items: string[]
  }
  
  export type Experience = {
    company: string
    role: string
    period: string
    summary: string
    achievements: string[]
    technologies: string[]
  }