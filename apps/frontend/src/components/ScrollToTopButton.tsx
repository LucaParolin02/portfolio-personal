import { useEffect, useState } from 'react'

export function ScrollToTopButton() {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    function handleScroll() {
      setIsVisible(window.scrollY > 420)
    }

    handleScroll()

    window.addEventListener('scroll', handleScroll)

    return () => {
      window.removeEventListener('scroll', handleScroll)
    }
  }, [])

  function scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    })
  }

  if (!isVisible) {
    return null
  }

  return (
    <button
      type="button"
      onClick={scrollToTop}
      aria-label="Volver arriba"
      className="fixed bottom-6 right-6 z-50 flex h-12 w-12 items-center justify-center rounded-full border border-[#A7633D]/30 bg-[#A7633D] text-xl font-bold text-[#FFF8EF] shadow-xl shadow-[#A7633D]/20 transition hover:-translate-y-1 hover:bg-[#7A4329] focus:outline-none focus:ring-4 focus:ring-[#A7633D]/25"
    >
      ↑
    </button>
  )
}