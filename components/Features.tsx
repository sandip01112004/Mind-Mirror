// components/Features.tsx
export default function Features() {
  const features = [
    {
      title: "Concept-Centered Assessments",
      description: "Go beyond memorization with AI-generated questions that test real understanding.",
    },
    {
      title: "Personalized Feedback",
      description: "Get instant reports showing strengths, weaknesses, and next steps.",
    },
    {
      title: "Gamified Experience",
      description: "Interactive, fun, and engaging assessments that don’t feel like tests.",
    },
  ];

  return (
    <section className="py-16 bg-gray-50">
      <div className="max-w-6xl mx-auto px-6 text-center">
        <h2 className="text-3xl font-bold mb-8">Why Choose MindMirror?</h2>
        <div className="grid md:grid-cols-3 gap-8">
          {features.map((f, i) => (
            <div key={i} className="bg-white shadow-md rounded-2xl p-6 hover:shadow-lg transition">
              <h3 className="text-xl font-semibold mb-2">{f.title}</h3>
              <p className="text-gray-600">{f.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
