import os
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Topik Produk Digital Anda
TOPIK = "Panduan Efektif Mengatasi Keraguan Pembeli (Objection Handling)"

# Prompt yang dioptimalkan menggunakan rumus AIDA/PAS dari riset Anda
PROMPT = f"""
Bertindaklah sebagai ahli Copywriting profesional. Buatlah sebuah panduan produk digital tentang: {TOPIK}.
Gunakan prinsip-prinsip dalam dokumen 'Panduan Copywriting Pemula':
1. Gunakan rumus PAS (Problem-Agitation-Solution) untuk pendahuluan.
2. Identifikasi Pain Points audiens terlebih dahulu.
3. Fokus pada manfaat (bukan fitur).
4. Gunakan bahasa yang personal dan percakapan (scannable).
5. Sertakan CTA yang kuat di akhir.

Format output dalam Markdown yang sangat rapi.
"""

def generate_konten_pro():
    try:
        model = genai.GenerativeModel('gemini-1.5-flash') # Gunakan model stabil
        response = model.generate_content(PROMPT)
        
        file_name = f"produk_{datetime.now().strftime('%Y-%m-%d')}.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"# Produk Digital: {TOPIK}\n\n")
            f.write(response.text)
        print(f"Produk sukses dibuat dengan teknik Copywriting Anda: {file_name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_konten_pro()
