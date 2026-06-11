import { type FormEvent, useState } from 'react'

import { portfolioApi } from '../services/portfolioApi'

type ContactFormProps = {
  targetEmail: string | null
}

type ContactFormState = {
  name: string
  email: string
  message: string
  companyWebsite: string
}

const initialFormState: ContactFormState = {
  name: '',
  email: '',
  message: '',
  companyWebsite: '',
}

export function ContactForm({ targetEmail }: ContactFormProps) {
  const [formData, setFormData] = useState<ContactFormState>(initialFormState)
  const [formStartedAt] = useState(() => Date.now())
  const [errorMessage, setErrorMessage] = useState<string | null>(null)
  const [successMessage, setSuccessMessage] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)

  function updateField(field: keyof ContactFormState, value: string) {
    setFormData((currentFormData) => ({
      ...currentFormData,
      [field]: value,
    }))
  }

  function isValidEmail(email: string) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
  }

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    setErrorMessage(null)
    setSuccessMessage(null)

    if (targetEmail === null) {
      setErrorMessage('El email de contacto no está configurado.')
      return
    }

    if (formData.companyWebsite.trim() !== '') {
      return
    }

    const elapsedSeconds = (Date.now() - formStartedAt) / 1000

    if (elapsedSeconds < 4) {
      setErrorMessage('Esperá unos segundos antes de enviar el mensaje.')
      return
    }

    if (formData.name.trim().length < 2) {
      setErrorMessage('Ingresá tu nombre.')
      return
    }

    if (!isValidEmail(formData.email.trim())) {
      setErrorMessage('Ingresá un email válido.')
      return
    }

    if (formData.message.trim().length < 10) {
      setErrorMessage('El mensaje debería tener al menos 10 caracteres.')
      return
    }

    try {
      setIsSubmitting(true)

      await portfolioApi.sendContactMessage({
        name: formData.name.trim(),
        email: formData.email.trim(),
        message: formData.message.trim(),
        company_website: formData.companyWebsite.trim(),
        form_started_at: formStartedAt,
      })

      setSuccessMessage('Mensaje enviado correctamente. Gracias por escribir.')
      setFormData(initialFormState)
    } catch (error) {
      const message =
        error instanceof Error
          ? error.message
          : 'No se pudo enviar el mensaje. Intentá nuevamente.'

      setErrorMessage(message)
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-[var(--color-form)] p-6 shadow-xl md:p-7"
    >
      <div className="grid gap-5">
        <div>
          <label
            htmlFor="contact-name"
            className="text-sm font-black text-[var(--color-dark)]"
          >
            Nombre
          </label>

          <input
            id="contact-name"
            type="text"
            value={formData.name}
            onChange={(event) => updateField('name', event.target.value)}
            placeholder="Tu nombre"
            className="mt-2 w-full bg-[var(--color-surface)] px-4 py-3 text-sm font-bold text-[var(--color-dark)] outline-none transition placeholder:text-[var(--color-muted)] focus:ring-4 focus:ring-[rgba(236,234,231,0.45)]"
          />
        </div>

        <div>
          <label
            htmlFor="contact-email"
            className="text-sm font-black text-[var(--color-dark)]"
          >
            Email
          </label>

          <input
            id="contact-email"
            type="email"
            value={formData.email}
            onChange={(event) => updateField('email', event.target.value)}
            placeholder="tu@email.com"
            className="mt-2 w-full bg-[var(--color-surface)] px-4 py-3 text-sm font-bold text-[var(--color-dark)] outline-none transition placeholder:text-[var(--color-muted)] focus:ring-4 focus:ring-[rgba(236,234,231,0.45)]"
          />
        </div>

        <div>
          <label
            htmlFor="contact-message"
            className="text-sm font-black text-[var(--color-dark)]"
          >
            Mensaje
          </label>

          <textarea
            id="contact-message"
            value={formData.message}
            onChange={(event) => updateField('message', event.target.value)}
            placeholder="Contame brevemente en qué te puedo ayudar..."
            rows={5}
            className="mt-2 w-full resize-none bg-[var(--color-surface)] px-4 py-3 text-sm font-bold leading-6 text-[var(--color-dark)] outline-none transition placeholder:text-[var(--color-muted)] focus:ring-4 focus:ring-[rgba(236,234,231,0.45)]"
          />
        </div>

        <div className="hidden" aria-hidden="true">
          <label htmlFor="company-website">Website</label>
          <input
            id="company-website"
            type="text"
            tabIndex={-1}
            autoComplete="off"
            value={formData.companyWebsite}
            onChange={(event) =>
              updateField('companyWebsite', event.target.value)
            }
          />
        </div>

        {errorMessage !== null && (
          <p className="bg-[rgba(47,37,32,0.10)] px-4 py-3 text-sm font-bold text-[#7a3329]">
            {errorMessage}
          </p>
        )}

        {successMessage !== null && (
          <p className="bg-[rgba(47,37,32,0.10)] px-4 py-3 text-sm font-bold text-[var(--color-primary)]">
            {successMessage}
          </p>
        )}

        <button
          type="submit"
          disabled={targetEmail === null || isSubmitting}
          className="bg-[var(--color-panel-dark)] px-6 py-3 text-sm font-black text-[var(--color-bg)] transition hover:-translate-y-0.5 hover:bg-[var(--color-primary)] disabled:cursor-not-allowed disabled:opacity-60"
        >
          {isSubmitting ? 'Enviando...' : 'Enviar mensaje'}
        </button>

        <p className="text-xs leading-5 text-[rgba(47,37,32,0.72)]">
          El envío se realiza desde la API, con validaciones básicas anti-spam.
        </p>
      </div>
    </form>
  )
}