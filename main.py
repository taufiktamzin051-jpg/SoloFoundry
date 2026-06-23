import os
import google.generativeai as genai

# Konfigurasi
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("--- DIAGNOSA SISTEM ---")
try:
    models = genai.list_models()
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            print(f"Model tersedia: {m.name}")
except Exception as e:
    print(f"Error saat list models: {e}")
    
