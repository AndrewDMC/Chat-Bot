import openai

openai.api_key = "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"


def moderation(input):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="translate this text from italian to english: " + input,
    temperature=0,
    max_tokens=60
    )

    translated_text = response["choices"][0]["text"]

    response = openai.Moderation.create(
        translated_text,
    )
    return response["results"][0]["flagged"]


input = input()
print(moderation(input))
