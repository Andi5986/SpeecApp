import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    DG_API_KEY = os.getenv("DG_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Deepgram Settings
    DG_SPEAK_MODEL = "aura-asteria-en"
    DG_SPEAK_ENCODING = "linear16"
    DG_SPEAK_CONTAINER = "wav"
    DG_LISTEN_MODEL = "nova-2"
    DG_LISTEN_SMART_FORMAT = True

    # Groq Service Settings
    GROQ_MODEL = "llama2-70b-4096"
    GROQ_TEMPERATURE = 0.5
    GROQ_MAX_TOKENS = 1024
    GROQ_TOP_P = 1
    GROQ_STREAM = True
    GROQ_STOP = None
