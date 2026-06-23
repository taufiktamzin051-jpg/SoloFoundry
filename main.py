import os
import google.generativeai as genai

# Konfigurasi dengan API Key dari Secret
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Menggunakan daftar model yang didukung secara resmi
# Kita panggil model 1.5 flash dengan format yang benar
model = genai.GenerativeModel('models/gemini-1.5-flash')

def run_factory():
    try:
        response = model.generate_content("Tulis satu kalimat sapaan pendek.")
        print("Berhasil terhubung ke Gemini!")
        print("Jawaban:", response.text)
    except Exception as e:
        print(f"Gagal terhubung: {e}")

if __name__ == "__main__":
    run_factory()
