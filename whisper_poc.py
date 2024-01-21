//

import openai

openai.api_key = "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"

audio_file_path = open(r"C:\Users\admin\Documents\Hangfelvételek\teszt4.mp3", 'rb')

transcript = openai.Audio.transcribe("whisper-1", 
                                     audio_file_path)

print(transcript)