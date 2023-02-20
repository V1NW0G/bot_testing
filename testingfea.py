import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"].strip()

generated_text = generate_text("What can I do if my parents beat me up?")
print(generated_text)