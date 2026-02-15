from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("AIzaSyCQ5MTh71X0Yd5-oflfsJMjd2NKy-Ajro8"))

models = client.models.list()

for m in models:
    print(m.name, "-", getattr(m, "description", ""))
