🪞 MindMirror

AI-Powered Personalized Gamified Assessments

MindMirror is an AI-based platform that evaluates a student’s real conceptual understanding through personalized, gamified, and story-based assessments. Unlike traditional tests that only check memory, MindMirror measures deep understanding and provides actionable feedback for both students and teachers.

🚀 Problem Statement

Traditional assessments mainly:

✅ Test facts and memory, not true understanding.

❌ Give the same test to all students (no personalization).

❌ Provide only marks/percentages as feedback, without insights.

This leads to students believing they understood concepts just because they passed, while conceptual gaps remain hidden.

🎯 Objective

MindMirror ensures that when a student learns a concept:

They can self-check their understanding through quick adaptive quizzes.

The system can analyze responses to identify strengths and weaknesses.

Personalized feedback and reports guide both students and teachers.

✨ Key Features

🔮 AI-Generated Questions – Based on syllabus concepts (using Gemini Pro API).

🧩 Multiple Question Types – MCQs, short answers, reasoning, interactive drag-drop.

🎮 Gamified UI – Keeps assessments engaging and fun.

📊 Concept Coverage – Evaluates from prerequisites → mastery level.

👩‍🏫 Teacher Dashboard – Track class performance and conceptual gaps.

🤖 Personalization – Each student has a learning profile (memory of strengths/weaknesses).

🏗️ System Architecture
flowchart TD
    A[Student starts quiz] --> B[Gemini API generates concept-based questions]
    B --> C[React-based UI renders interactive assessment]
    C --> D[Student attempts questions]
    D --> E[Response stored in MongoDB]
    E --> F[Custom NLP Agent analyzes answers]
    F --> G[Conceptual feedback generated]
    G --> H[Report shown to student & teacher dashboard updated]

🛠️ Tech Stack

Frontend: React.js, Tailwind CSS

Backend: Node.js, Express.js

Database: MongoDB / Firebase

AI Integration: Google Gemini Pro API, Hugging Face Transformers

Deployment: Firebase Hosting / Render

Project Management: Agile + Scrum (Notion for sprint tracking)

📅 Agile Development Plan

Sprint 1: Requirement Analysis + SRS Documentation

Sprint 2: System Design (Architecture, UI Mockups)

Sprint 3: Basic Quiz Generation (API + React UI)

Sprint 4: Evaluation & Feedback Module

Sprint 5: Personalization Layer (Student profiles)

Sprint 6: Teacher Dashboard + Final Integration

🎓 Example Use Case (Physics – Gravitation)

Traditional Test Question: Define Newton’s Law of Gravitation.

MindMirror Quiz Question:
“You are an astronaut trying to land on Mars. The spacecraft autopilot asks you to estimate the gravitational force between the spacecraft (2000 kg) and Mars (6.4 × 10²³ kg) when they are 400 km apart. How would you calculate it, and what principle explains your approach?”

🔹 Feedback Example:

✅ You applied the correct formula for gravitational force.

⚠️ You missed unit conversion from km → m.

📖 Suggested review: Units & Dimensional Analysis.

📊 Expected Outcome

Students will get a clear picture of what they understood and where they need to improve.

Teachers will get data-driven insights about class learning levels.

Assessments become engaging, adaptive, and truly educational.

🔮 Future Scope

🎤 Voice-based interactive assessments (AI Tutor).

🖼️ Image/Video-based questions (e.g., label diagrams, science experiments).

🌍 Expansion to multiple subjects & grade levels.

📱 Mobile app version for wider reach.

🤝 Team

👨‍💻 Sandip Kharate – Scrum Master & Backend
👨‍💻 Ritesh Patil – Developer (Frontend)
👨‍💻 Vedant Patil – Product Owner & Research

🧭 How to Run Locally
# Clone repository
git clone https://github.com/username/mindmirror.git
cd mindmirror

# Install dependencies
npm install

# Run development server
npm start

💡 Quote

"MindMirror is not just a test — it’s a reflection of how deeply you truly understand."
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
