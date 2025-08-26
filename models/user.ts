// frontend/models/User.ts
import mongoose, { Schema, Document } from "mongoose";

export interface IUser extends Document {
  email: string;
  passwordHash: string;
  role: "student" | "teacher";
  createdAt: Date;
}

const UserSchema = new Schema<IUser>({
  email: { type: String, required: true, unique: true },
  passwordHash: { type: String, required: true },
  role: { type: String, enum: ["student", "teacher"], default: "student" },
  createdAt: { type: Date, default: Date.now },
});

// Prevent recompiling model during hot reload
export default mongoose.models.User || mongoose.model<IUser>("User", UserSchema);
