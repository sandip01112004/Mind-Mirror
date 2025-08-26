import { NextResponse } from "next/server";

export async function POST(request: Request) {
  const body = await request.json();
  const { email, password } = body;

  // Example check (replace with MongoDB lookup later)
  if (email === "test@example.com" && password === "123456") {
    return NextResponse.json({ success: true, message: "Login successful" });
  }

  return NextResponse.json({ success: false, message: "Invalid credentials" }, { status: 401 });
}
