import openai
from deep_translator import GoogleTranslator

openai.api_key = "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"

def moderation(input):

    translated = GoogleTranslator(source='italian', target='english').translate(input)
    print(translated)

    response = openai.Moderation.create(
        translated,
    )
    return response["results"][0]["flagged"]


input = input()
print(moderation(input))
