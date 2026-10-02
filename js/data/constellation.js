/**
 * Knowledge Constellation — positions live in one coordinate space so the web
 * recomposes responsively. Notes are one line each: visual storytelling, not
 * documentation.
 */
export const STAGE = { width: 1000, height: 640 }

export const NODES = [
  { id: 'consciousness',   label: 'Consciousness',        x: 500, y: 300, note: 'The study of what it is like to be something.' },
  { id: 'philosophy', label: 'Philosophy',      x: 322, y: 196, note: 'Questions old enough to have weathered.' },
  { id: 'science',         label: 'Science',              x: 668, y: 192, note: 'Method, practiced as a form of reverence.' },
  { id: 'mythology',       label: 'Mythology',            x: 176, y: 306, note: 'Truth carried as story before it could carry data.' },
  { id: 'meditation',      label: 'Meditation',           x: 316, y: 462, note: 'Attention, turned back upon itself.' },
  { id: 'ai',              label: 'Artificial intelligence', x: 788, y: 330, note: 'A mirror made of mathematics.' },
  { id: 'psychology',      label: 'Psychology',           x: 632, y: 468, note: 'The inner life, instrumented.' },
  { id: 'ancient-wisdom',  label: 'Ancient wisdom',       x: 122, y: 162, note: 'Techniques for attention, discovered independently.' },
  { id: 'mathematics',     label: 'Mathematics',          x: 508, y: 118, note: 'The one language that keeps its meaning between civilizations.' },
  { id: 'cosmology',       label: 'Cosmology',            x: 868, y: 168, note: 'Where the universe has started thinking about itself.' },
  { id: 'art',             label: 'Art',                  x: 396, y: 562, note: 'Knowledge that only exists in the making.' },
  { id: 'human-potential', label: 'Human potential',      x: 706, y: 566, note: 'The ongoing experiment of what a human can be.' },
]

export const LINKS = [
  ['ancient-wisdom', 'mythology'],
  ['mythology', 'philosophy'],
  ['mythology', 'meditation'],
  ['philosophy', 'consciousness'],
  ['philosophy', 'science'],
  ['philosophy', 'art'],
  ['science', 'mathematics'],
  ['science', 'cosmology'],
  ['science', 'ai'],
  ['meditation', 'consciousness'],
  ['meditation', 'human-potential'],
  ['meditation', 'art'],
  ['consciousness', 'ai'],
  ['consciousness', 'psychology'],
  ['consciousness', 'mathematics'],
  ['ai', 'mathematics'],
  ['ai', 'psychology'],
  ['ai', 'cosmology'],
  ['psychology', 'human-potential'],
  ['art', 'human-potential'],
]

/** A deterministic scatter of faint points — the field the constellation sits in. */
export function dustField(count = 46, seed = 14) {
  let s = seed
  const rand = () => (s = (s * 1664525717 + 1) % 2147483648) / 2147483648
  return Array.from({ length: count }, () => ({
    x: rand() * STAGE.width,
    y: rand() * STAGE.height,
    r: 0.4 + rand() * 0.9,
    a: 0.04 + rand() * 0.10,
  }))
}