# pip install google-genai
# Set your key first in .env:  EMINI_API_KEY="your_key"  

import asyncio
import os
import time

from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-3.5-flash"  

sem = asyncio.Semaphore(3)   #max 3 Gemini calls at the same time

QUESTIONS = [
    "Explain Python lists in one sentence.",
    "Explain Python dictionaries in one sentence.",
    "Explain Python tuples in one sentence.",
    "Explain Python sets in one sentence.",
    "Explain Python functions in one sentence.",
    "Explain Python classes in one sentence.",
    "Explain Python decorators in one sentence.",
    "Explain Python generators in one sentence.",
]


async def ask(i, question):
    # async with sem:                       #wait here if 3 calls are already running
    print(f"Call {i} started")
    response = await client.aio.models.generate_content(   # async version of the API call
        model=MODEL,
        contents=question,
    )
    print(f"Call {i} done")
    return response.text.strip()


async def main():
    start = time.time()

    #Start all 8 calls together; the semaphore lets only 3 run at a time
    answers = await asyncio.gather(
        *(ask(i, q) for i, q in enumerate(QUESTIONS, start=1))
    )

    print("\n--- Answers ---")
    for q, a in zip(QUESTIONS, answers):
        print(f"\nQ: {q}\nA: {a}")

    print(f"\nTotal time: {time.time() - start:.1f} s")


asyncio.run(main())