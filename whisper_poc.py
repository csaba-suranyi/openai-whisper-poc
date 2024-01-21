#
import openai

from dotenv import load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file_path = open(r".\audio\eazy.mp3", 'rb')

transcript = openai.Audio.transcribe("whisper-1", 
                                     audio_file_path)

print(transcript)