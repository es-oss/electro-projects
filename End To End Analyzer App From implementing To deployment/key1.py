from dotenv import load_dotenv
import os

load_dotenv()  # يحمل .env تلقائيًا من نفس المجلد

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

print("API Key loaded:", api_key)
