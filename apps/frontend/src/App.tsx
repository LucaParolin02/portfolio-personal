function App() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <section className="mx-auto flex min-h-screen max-w-5xl flex-col justify-center px-6 py-16">
        <p className="mb-4 text-sm font-medium uppercase tracking-[0.3em] text-cyan-400">
          Portfolio Personal
        </p>

        <h1 className="max-w-3xl text-4xl font-bold tracking-tight md:text-6xl">
          Luca — Software Engineer, Data Engineer & Builder
        </h1>

        <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
          Portfolio personal construido con React, Vite, TypeScript, Tailwind,
          FastAPI, PostgreSQL, Docker, NGINX y despliegue propio en DigitalOcean.
        </p>

        <div className="mt-10 flex flex-wrap gap-4">
          <a
            href="#projects"
            className="rounded-xl bg-cyan-400 px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-cyan-300"
          >
            Ver proyectos
          </a>

          <a
            href="#contact"
            className="rounded-xl border border-slate-700 px-5 py-3 text-sm font-semibold text-slate-100 transition hover:border-cyan-400 hover:text-cyan-300"
          >
            Contacto
          </a>
        </div>
      </section>
    </main>
  )
}

export default App