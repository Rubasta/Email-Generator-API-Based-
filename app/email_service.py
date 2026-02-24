import os
from openai import OpenAI
from dotenv import load_dotenv
from .prompt_builder import build_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(data):

    prompt = build_prompt(
        recipient=data["recipient"],
        sender_role=data["sender_role"],
        purpose=data["purpose"],
        tone=data["tone"],
        key_points=data["key_points"],
        length=data["length"]
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.4,
        messages=[
            {"role": "system", "content": "You write professional structured emails."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content