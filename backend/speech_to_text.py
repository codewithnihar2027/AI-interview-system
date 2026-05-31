import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os


def audio_to_text(audio_file):

    try:

        wav_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        )

        wav_path = wav_file.name
        wav_file.close()

        audio = AudioSegment.from_file(audio_file)
        audio.export(wav_path, format="wav")

        recognizer = sr.Recognizer()

        with sr.AudioFile(wav_path) as source:

            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)

        os.remove(wav_path)

        return text

    except Exception as e:

        return f"Error: {str(e)}"