import speech_recognition as sr
import openai

openai.api_key = "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"

FILENAME="output.wav"

def stt():
	# Initialize recognizer
	r = sr.Recognizer()

	# Record audio
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
	# Save audio to file
	with open(FILENAME, "wb") as f:
		f.write(audio.get_wav_data())
	with sr.AudioFile(FILENAME) as source:
		audio = r.record(source)
  
	audio_file = open(FILENAME, "rb")
	transcript = openai.Audio.transcribe("whisper-1", audio_file)
	return transcript["text"]
	

print(stt())
