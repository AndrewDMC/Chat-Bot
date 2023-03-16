import openai

openai.api_key = "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"

messages = []
messages.append({"role": "system", "content": "you are a educator bot for school"})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")