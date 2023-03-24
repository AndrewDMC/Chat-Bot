import openai

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "Sei un robot utilizzato per dare informazioni inerenti alla scuola a ragazzini di 10 anni. Sii simpatico e fai battute."})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")