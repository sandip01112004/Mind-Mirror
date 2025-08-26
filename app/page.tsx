import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";
import Benefits from "../components/Benefits";
import Footer from "../components/Footer";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen font-sans text-gray-800">
      <Navbar />
      <main className="flex-grow">
        <Hero />
        <Features />
        <Benefits />
      </main>
      <Footer />
    </div>
  );
}
