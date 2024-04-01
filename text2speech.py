import tempfile
from deepgram import DeepgramClient, SpeakOptions
from config import Config


def text_to_speech(text):
    try:
        truncated_text = text[:2000]

        deepgram = DeepgramClient(api_key=Config.DG_API_KEY)
        SPEAK_OPTIONS = {"text": truncated_text}
        options = SpeakOptions(model=Config.DG_SPEAK_MODEL, encoding=Config.DG_SPEAK_ENCODING,
                               container=Config.DG_SPEAK_CONTAINER)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix="tts_", mode='wb') as temp_audio:
            deepgram.speak.v("1").save(temp_audio.name, SPEAK_OPTIONS, options)
            return temp_audio.name
    except Exception as e:
        print(f"Text-to-Speech Exception: {e}")
        return None

