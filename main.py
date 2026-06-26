import os
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Paksa generate konten
response = model.generate_content("Tuliskan 1 ide produk digital unik untuk pemula.")

# Pastikan nama file sesuai tanggal hari ini
file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"

# Simpan file secara paksa
with open(file_name, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"File {file_name} berhasil dibuat.")
