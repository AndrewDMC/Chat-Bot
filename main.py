from dotenv import load_dotenv
import openai
import os

load_dotenv()

API_KEY = os.environ.get('OPENAI_API_KEY')

print(f"{API_KEY}")

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


print("Your new assistant is ready!")
while input != "quit()":
    message = input(str("Your message: "))
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")