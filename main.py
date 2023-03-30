from dotenv import load_dotenv
import openai
import os
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9000
VOICE_PORT = 9001

def main():
    load_dotenv()

    API_KEY = os.environ.get("OPENAI_API_KEY")
    openai.api_key = API_KEY

    v = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    v.bind((HOST, VOICE_PORT))
    v.listen()

    print(f"Listening for Voice on {HOST}:{VOICE_PORT}...")

    connv, addrv = v.accept()
    message = connv.recv(1024)

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

    with conn:
        print(f"Connected to {addr[0]}:{addr[1]}")

        while True:
            data = connv.recv(1024)

            messages.append(
                {
                    "role": "user",
                    "content": data.decode("utf-8")
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
            conn.send(openai_response.encode("utf-8"))
            
if __name__ == "__main__":
    main()