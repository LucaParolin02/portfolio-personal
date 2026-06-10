import type {
    Experience,
    Profile,
    Project,
    SkillCategory,
  } from '../types/portfolio'
  
  const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1'
  
  async function request<T>(path: string): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${path}`)
  
    if (!response.ok) {
      throw new Error(
        `API request failed: ${response.status} ${response.statusText}`,
      )
    }
  
    return response.json() as Promise<T>
  }
  
  export const portfolioApi = {
    getProfile: (): Promise<Profile> => request<Profile>('/profile'),
  
    getProjects: (): Promise<Project[]> => request<Project[]>('/projects'),
  
    getSkills: (): Promise<SkillCategory[]> => request<SkillCategory[]>('/skills'),
  
    getExperience: (): Promise<Experience[]> =>
      request<Experience[]>('/experience'),
  }