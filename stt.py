import speech_recognition as sr
import openai

openai.api_key = "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"

FILENAME="output.wav"

def stt():
	# Initialize recognizer
	r = sr.Recognizer()
	r.pause_threshold = 1
	# Record audio
	with sr.Microphone() as source:
		print("Say something!")
		r.adjust_for_ambient_noise(source, 0.5)
		audio = r.listen(source, phrase_time_limit=5, snowboy_configuration=None)
	# Save audio to file
	with open(FILENAME, "wb") as f:
		f.write(audio.get_wav_data())
  
	audio_file = open(FILENAME, "rb")
	transcript = openai.Audio.transcribe("whisper-1", audio_file)
	return transcript["text"]
	
print(stt())
