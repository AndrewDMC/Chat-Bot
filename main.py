
import openai
import os
import socket
import speech_recognition as sr

HOST = socket.gethostbyname(socket.gethostname())
print(HOST)
PORT = 9000
VOICE_PORT = 9001
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
def main():
    

    API_KEY = "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"
    openai.api_key = API_KEY
    '''
    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.bind((HOST, VOICE_PORT))
    v.listen()

    print(f"Listening for Voice on {HOST}:{VOICE_PORT}...")

    connv, addrv = v.accept()
    message = connv.recv(1024)
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    
    print(f"Listening for NAO on {HOST}:{PORT}...")

    conn, addr = s.accept()
    message = conn.recv(1024)
    
    print("Received " + message.decode("utf-8"))
    conn.send("Welcome to NAO Chat!".encode("utf-8"))

    messages = []
    messages.append(
        {
            "role": "system",
            "content": "\
                Sei un robot che parla con un bambino in un ospedale. \
                Non menzionare mai qualsiasi termine medico, tecnico o che sia legato ad una malattia. \
                Il bambino ha 10 anni e ha bisogno di un amico con cui parlare. Utilizza termini semplici e non essere troppo prolisso. Non usare emoticon o caratteri speciali all'infuori di virgole e punti nel messaggio.\
            "
        },
    )
    '''
    messages.append(
        {
            "role": "user",
            "content": "\
                Sei un robot che parla con un bambino in un ospedale. \
                Non menzionare mai qualsiasi termine medico, tecnico o che sia legato ad una malattia. \
                Il bambino ha 10 anni e ha bisogno di un amico con cui parlare. Utilizza termini semplici e non essere troppo prolisso. Non usare emoticon o caratteri speciali all'infuori di virgole e punti nel messaggio.\
            "
        },
    )
    '''
    with conn:
        print(f"Connected to {addr[0]}:{addr[1]}")
        i=0
        j=3
        while True:
            print("cosa dire?")
            data = stt()
            print(data)
            i=i+1
            messages.append(
                {
                    "role": "user",
                    "content": data
                }
            )
            
            if not data:
                break
            
                
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )

            openai_response = response["choices"][0]["message"]["content"]
            print(f"\n{openai_response}\n")
            if i==j:
                messages.pop[1]
                i=0
                
            conn.send(openai_response.encode("utf-8"))
            
if __name__ == "__main__":
    main()
