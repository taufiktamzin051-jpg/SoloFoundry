import os
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
Buatkan konten produk digital "Cheat Sheet Panduan Strategi" untuk Pemilik Bisnis Digital Pemula.
Format output:
[JUDUL PRODUK]
(Judul menarik & menjual)
[MASALAH UTAMA]
(3 poin masalah)
[SOLUSI/CHEAT SHEET]
(5 langkah praktis)
[HARGA SARAN]
($9 - $27)
[KEYWORD SEO]
(5 tag)
"""

response = model.generate_content(prompt)
file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"

with open(file_name, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Produksi selesai: {file_name}")
