
import heroImg from "../src/assets/image.png";export default function Hero() {
  return (
    <section className="bg-indigo-50 pt-28 pb-20">
      <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center">
        {/* Left Content */}
        <div className="flex-1 text-center md:text-left">
          <h1 className="text-4xl md:text-6xl font-bold text-gray-900 leading-tight">
            Master Concepts, <span className="text-indigo-600">Not Just Exams</span>
          </h1>
          <p className="mt-6 text-lg text-gray-600">
            MindMirror evaluates your real understanding with AI-powered,
            personalized, gamified assessments.
          </p>
          <div className="mt-6 flex gap-4 justify-center md:justify-start">
            <a
              href="#features"
              className="px-6 py-3 bg-indigo-600 text-white rounded-lg font-medium hover:bg-indigo-700"
            >
              Get Started
            </a>
            <a
              href="#about"
              className="px-6 py-3 border border-gray-300 rounded-lg font-medium text-gray-700 hover:bg-gray-100"
            >
              Learn More
            </a>
          </div>
        </div>

        {/* Right Image */}
        <div className="flex-1 mt-10 md:mt-0">
          <img
            src={heroImg.src}
            alt="Learning"
            className="w-full max-w-lg mx-auto"
          />
        </div>
      </div>
    </section>
  );
}
