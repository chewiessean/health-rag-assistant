import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

response = client.models.generate_content(model="gemini-3.6-flash", contents="Amatör boks müsabakalarına hazırlanan bir gence 3 cümlelik bir tavsiye ver.")

print(response.text)