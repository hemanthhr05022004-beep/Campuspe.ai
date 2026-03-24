import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("sk-1234567890abcdef"))

user_input = input("Enter your question: ")

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)