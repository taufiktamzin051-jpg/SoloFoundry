import os
from datetime import datetime
import google.generativeai as genai

# Konfigurasi
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_best_model():
    # Daftar model yang ingin dicoba
    models_to_try = ['gemini-1.5-flash', 'gemini-pro', 'gemini-1.0-pro']
    for m in genai.list_models():
        if m.name in [f"models/{n}" for n in models_to_try]:
            return m.name
    return 'gemini-pro' # fallback

try:
    model_name = get_best_model()
    model = genai.GenerativeModel(model_name)
    
    prompt = "Tuliskan 1 ide produk digital unik untuk pemula. Format: Judul, Masalah, Solusi."
    response = model.generate_content(prompt)
    
    file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Sukses menggunakan {model_name}: {file_name}")

except Exception as e:
    print(f"Gagal total: {e}")
