// frontend/app/api/protected/route.ts
import { NextResponse } from "next/server";
import { verifyToken } from "../../../lib/auth";

export async function GET(req: Request) {
  const cookieHeader = req.headers.get("cookie");
  const token = cookieHeader?.split("authToken=")[1];

  if (!token || !verifyToken(token)) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  return NextResponse.json({ message: "You are authenticated 🎉" });
}
