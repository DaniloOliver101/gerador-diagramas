import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")  # Corrigido de "OPENIA_API_KEY"

if not api_key:
    raise ValueError("A variável de ambiente 'OPENAI_API_KEY' não está definida.")

def send_request_to_openai(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    print(content)
    return content  