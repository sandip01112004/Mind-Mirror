"use client";
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow-sm fixed top-0 left-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="text-2xl font-bold text-indigo-600">
          MindMirror
        </Link>

        {/* Links */}
        <div className="hidden md:flex gap-6">
          <Link href="#features" className="text-gray-700 hover:text-indigo-600">
            Features
          </Link>
          <Link href="#benefits" className="text-gray-700 hover:text-indigo-600">
            Why MindMirror
          </Link>
          <Link href="#about" className="text-gray-700 hover:text-indigo-600">
            About
          </Link>
        </div>

        {/* Buttons */}
        <div className="flex gap-3">
          <Link
            href="/login"
            className="px-4 py-2 rounded-lg text-sm font-medium border border-gray-300 text-gray-700 hover:bg-gray-100"
          >
            Log in
          </Link>
          <Link
            href="/signup"
            className="px-4 py-2 rounded-lg text-sm font-medium bg-indigo-600 text-white hover:bg-indigo-700"
          >
            Sign up
          </Link>
        </div>
      </div>
    </nav>
  );
}
