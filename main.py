import os
import google.generativeai as genai
import requests

# Konfigurasi
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash')
GUMROAD_TOKEN = os.getenv("GUMROAD_TOKEN")

def buat_konten(topic):
    prompt = f"Tulis e-book panduan mendalam tentang {topic}. Berikan format Markdown profesional."
    return model.generate_content(prompt).text

def upload_ke_gumroad(judul, konten):
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": GUMROAD_TOKEN,
        "product[name]": judul,
        "product[description]": "E-book otomatis tentang " + judul,
        "product[price]": 999, # Harga dalam cent
        "product[custom_permalink]": judul.lower().replace(" ", "-")
    }
    # Upload sebagai produk digital
    response = requests.post(url, data=data)
    return response.json()

def run_factory():
    topic = "AI Business Automation 2026"
    print("Memulai produksi...")
    
    konten = buat_konten(topic)
    
    # Upload ke Gumroad
    hasil_upload = upload_ke_gumroad(topic, konten)
    print("Hasil upload ke Gumroad:", hasil_upload)

if __name__ == "__main__":
    run_factory()
