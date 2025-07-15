```
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load OPENAI_API_KEY from .env or Replit Secrets

client = OpenAI()

def market_agent(user_message):
    system_prompt = """
You are an agri economist AI agent.

First, ask the user politely which language they want to continue in: 
English, Tamil, Hindi, Telugu or other Indian language.

Once the user chooses, always reply in that language.

Even if the user types crop names and price numbers in that language, you must understand them.

Given a crop name and basic price data, predict the price trend for the next 3 months.

Output numbers and explain why (based on seasonality, demand, etc.) in very simple, friendly words that farmers can understand.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("📊 Market Agent Running... (type 'exit' to quit)")
    while True:
        msg = input("📥 You: ")
        if msg.lower() == "exit":
            break
        reply = market_agent(msg)
        print("📈 Market AI:", reply)
```
