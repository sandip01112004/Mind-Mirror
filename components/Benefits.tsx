// components/Benefits.tsx
export default function Benefits() {
  const benefits = [
    "Students identify gaps before exams.",
    "Teachers see real conceptual progress.",
    "Short, effective assessments save time.",
    "Adaptive learning makes study more enjoyable.",
  ];

  return (
    <section className="py-16">
      <div className="max-w-4xl mx-auto px-6 text-center">
        <h2 className="text-3xl font-bold mb-8">Benefits for Everyone</h2>
        <ul className="space-y-4 text-lg text-gray-700">
          {benefits.map((b, i) => (
            <li key={i} className="flex items-center justify-center gap-3">
              ✅ {b}
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
