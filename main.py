from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React frontend (localhost dev)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class TextInput(BaseModel):
    text: str

# Dummy keyword-based emotion mapping with emojis
emotion_keywords = {
    "anxious": ("Anxious", 0.85, "😰"),
    "nervous": ("Nervous", 0.80, "😬"),
    "happy": ("Happy", 0.95, "🥳"),
    "excited": ("Excited", 0.92, "🎉"),
    "sad": ("Sad", 0.75, "😢"),
    "proud": ("Proud", 0.88, "🏆"),
    "loved": ("Loved", 0.93, "❤️"),
    "lonely": ("Lonely", 0.70, "😞"),
    "angry": ("Angry", 0.89, "😡"),
    "stressed": ("Stressed", 0.82, "😓"),
    "calm": ("Calm", 0.90, "😌"),
    "surprised": ("Surprised", 0.91, "😲"),
    "adventurous": ("Adventurous", 0.87, "🌍"),
    "exhausted": ("Exhausted", 0.78, "🥱"),
    "disappointed": ("Disappointed", 0.76, "😔"),
    "fearful": ("Fearful", 0.83, "😨"),
    "hopeful": ("Hopeful", 0.89, "🌟"),
    "joyful": ("Joyful", 0.93, "🎶"),
    "confused": ("Confused", 0.77, "😕"),
    "grateful": ("Grateful", 0.94, "🙏"),
    "relieved": ("Relieved", 0.88, "😌"),
    "frustrated": ("Frustrated", 0.81, "😤"),
    "bored": ("Bored", 0.69, "😐"),
    "jealous": ("Jealous", 0.72, "😒"),
    "guilty": ("Guilty", 0.74, "😟"),
    "motivated": ("Motivated", 0.91, "💪"),
    "inspired": ("Inspired", 0.92, "✨"),
    "curious": ("Curious", 0.87, "🧐"),
    "peaceful": ("Peaceful", 0.90, "🕊️"),
    "embarrassed": ("Embarrassed", 0.73, "😳"),
    "determined": ("Determined", 0.89, "🔥"),
    "confident": ("Confident", 0.93, "😎"),
    "scared": ("Scared", 0.78, "😱"),
    "shy": ("Shy", 0.68, "😳"),
    "regretful": ("Regretful", 0.71, "😞"),
    "disgusted": ("Disgusted", 0.70, "🤢"),
    "hope": ("Hopeful", 0.88, "🌟"),
    "music": ("Joyful", 0.92, "🎶"),
    "success": ("Proud", 0.90, "👏"),
    "failure": ("Disappointed", 0.76, "😔"),
    "relax": ("Calm", 0.90, "😌"),
    "win": ("Proud", 0.88, "🏆"),
    "family": ("Loved", 0.93, "❤️"),
    "alone": ("Lonely", 0.70, "😞"),
    "exam": ("Nervous", 0.80, "😬"),
    "interview": ("Anxious", 0.85, "😰"),
    "travel": ("Adventurous", 0.87, "🌍"),
    "surprise": ("Surprised", 0.91, "😲"),
    "tired": ("Exhausted", 0.78, "🥱"),
}

# POST route to analyze text
@app.post("/analyze")
def analyze(input: TextInput):
    text_lower = input.text.lower()

    for keyword, (emotion, confidence, emoji) in emotion_keywords.items():
        if keyword in text_lower:
            return {
                "emotion": emotion,
                "confidence": confidence,
                "emoji": emoji
            }

    # Default/fallback response
    return {
        "emotion": "Neutral",
        "confidence": 0.60,
        "emoji": "🙂"
    }
