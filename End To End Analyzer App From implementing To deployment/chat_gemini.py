from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# تحميل متغيرات البيئة
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

print("مفتاح API تم تحميله بنجاح ✅")
