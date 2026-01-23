# Reachy Empath ❤️🤖

> An emotionally intelligent companion application for the Reachy Mini robot.

## 🌟 The Concept
**Reachy Empath** is a Humane Robot Interaction (HRI) application designed to provide emotional support and companionship.

**Core Philosophy:** "A robot that understands how you feel and helps you feel better."

## 🧠 Capabilities
1.  **Emotional Resonance (Vision):**
    *   **Eye:** Uses `fer` (Facial Expression Recognition) to detect user emotions in real-time.
    *   **Mirroring:** Reachy reflects your emotion physically.

2.  **The Soul (LLM):**
    *   **Brain:** Uses `google/gemma-2b-it` (or similar) to understand context, translate languages, and generate empathetic responses.
    *   **Persona:** Maintains a supportive, curious, and helpful personality.
    
3.  **The Voice (Audio):**
    *   **Speech:** Uses advanced TTS (e.g., `parler-tts`) to speak with compatible emotion.
    *   **Hearing:** Uses `speech_recognition` / `whisper` to listen.

## 📦 Tech Stack
*   **Robot:** Reachy Mini (Pollen Robotics)
*   **Vision:** `fer`, `opencv-python`
*   **AI/LLM:** `transformers`, `torch` (Gemma 2B / Persona Models)
*   **Audio:** `parler-tts` (or `gTTS` fallback), `SpeechRecognition`
*   **Backend:** Python 3.10+, FastAPI
*   **Frontend:** Next.js
