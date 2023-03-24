from dotenv import load_dotenv
import openai
import os

load_dotenv()

API_KEY = os.environ.get('OPENAI_API_KEY')
openai.api_key = f"{API_KEY}"

print(f"{openai.api_key}")

messages = []
messages.append({"role": "system", "content": "you are a educator bot for school"})

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