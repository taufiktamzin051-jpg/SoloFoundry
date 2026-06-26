import os
from datetime import datetime
import google.generativeai as genai

# Konfigurasi API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gunakan model yang paling stabil dan tersedia secara universal
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    # Prompt untuk menghasilkan konten
    prompt = "Tuliskan 1 ide produk digital untuk pemula dengan format: [JUDUL], [MASALAH], [SOLUSI]."
    response = model.generate_content(prompt)
    
    # Simpan file dengan nama berdasarkan tanggal
    file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"File berhasil dibuat: {file_name}")

except Exception as e:
    print(f"Gagal generate konten: {e}")
