from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from config import Config

def speech_to_text(audio_file):
    try:
        deepgram = DeepgramClient(Config.DG_API_KEY)
        with open(audio_file, "rb") as file:
            buffer_data = file.read()
        payload: FileSource = {"buffer": buffer_data}
        options = PrerecordedOptions(model=Config.DG_LISTEN_MODEL, smart_format=Config.DG_LISTEN_SMART_FORMAT)
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript
    except Exception as e:
        print(f"Speech-to-Text Exception: {e}")
        return None
