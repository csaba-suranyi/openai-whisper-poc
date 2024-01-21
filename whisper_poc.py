#
import openai

import dotenv

openai.api_key = "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"

audio_file_path = open(r".\audio\eazy.mp3", 'rb')

transcript = openai.Audio.transcribe("whisper-1", 
                                     audio_file_path)

print(transcript)