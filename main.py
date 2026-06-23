import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Mencetak daftar model yang tersedia untuk API Key Anda
print("Model yang tersedia:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Nama Model: {m.name}")

# Pilih salah satu dari daftar yang muncul di LOG nanti
