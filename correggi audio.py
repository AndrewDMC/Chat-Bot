import openai

openai.api_key = "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"



messages = []
messages.append({"role": "system", "content": "converti questo testo in italiano corretto: "})
while True :
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0)


    reply = response["choices"][0]["message"]["content"]
    print("\n" + reply + "\n")
