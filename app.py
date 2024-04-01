import os
from flask import Flask, request, send_file, render_template, jsonify
import tempfile
from werkzeug.utils import secure_filename
from text2speech import text_to_speech
from speech2text import speech_to_text
from groq_service import execute
from config import Config

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-audio", methods=["POST"])
def process_audio_data():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    audio_data = request.files['audio']
    secure_audio_name = secure_filename(audio_data.filename)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix=secure_audio_name) as temp_audio:
            audio_data.save(temp_audio)
            temp_audio_path = temp_audio.name

        text = speech_to_text(temp_audio_path)
        if text is None:
            raise Exception("Speech-to-text conversion failed.")

        generated_answer = execute(f"Please answer the question: {text}")
        if generated_answer is None:
            raise Exception("Failed to generate an answer.")

        generated_speech_path = text_to_speech(generated_answer)
        if generated_speech_path is None:
            raise Exception("Text-to-speech conversion failed.")

        return send_file(generated_speech_path, mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if temp_audio_path:
            os.remove(temp_audio_path)  # Ensure temporary file is deleted.

if __name__ == '__main__':
    app.run(debug=True, port=8080)
