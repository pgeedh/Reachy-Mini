# Reachy Mini Sentinel 🛡️🤖

> A unique, high-value application for the Reachy Mini robot that transforms it into an intelligent Desktop Companion.

## 🌟 The Concept
**Reachy Sentinel** is a dual-purpose application designed to add tangible utility to the Reachy Mini platform:

1.  **Focus Guardian (When you are there):**
    *   Reachy monitors your presence and "attention".
    *   If you drift off (looking at phone, leaving desk) during a Focus Session, Reachy gives subtle nudges (sad sounds, head shaking).
    *   Gamifies your productivity.

2.  **Sentry Mode (When you are away):**
    *   Activates when you lock your computer or leave.
    *   Reachy scans the room.
    *   If it detects a person, it tracks them and can send a notification (or just look intimidating/cute).

## 🚀 Architecture
The system consists of two parts running in tandem:

*   **Sentinel Brain (Python Backend):**
    *   Uses `reachy-sdk` to control the robot.
    *   Runs Computer Vision (likely `opencv` or `mediapipe`) for face/pose detection.
    *   Exposes a FastAPI server for the UI to control modes.

*   **Sentinel Command (Web Frontend):**
    *   A beautiful Next.js Dashboard.
    *   View the camera feed.
    *   Start/Stop Focus sessions.
    *   View "Distraction Scores" and stats.

## 📦 Tech Stack
*   **Robot:** Reachy Mini (Pollen Robotics)
*   **Backend:** Python 3.10+, FastAPI, Reachy SDK, MediaPipe
*   **Frontend:** Next.js, Tailwind CSS, Framer Motion
