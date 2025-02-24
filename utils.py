# utils.py
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply