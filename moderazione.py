import openai
from deep_translator import MyMemoryTranslator

openai.api_key = "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"


def moderation(input):
    translated = MyMemoryTranslator(source="it", target="en").translate(text=input)
    print(translated)
    response = openai.Moderation.create(
        translated,
    )
    return response["results"][0]["flagged"]


input = input()
print(moderation(input))
