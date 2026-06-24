import os
import time
import datetime
import tweepy
import requests
from google import genai

# Inisialisasi API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Jadwal produksi mingguan
JADWAL_PRODUKSI = {
    0: "E-book",              # Senin
    1: "Notion Template",      # Selasa
    2: "Graphic Asset",        # Rabu
    3: "Course Outline",       # Kamis
    4: "UI/UX Kit",            # Jumat
    5: "Worksheet Bundle",     # Sabtu
    6: "Newsletter Guide"      # Minggu
}

def post_to_twitter(text):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(text)
    print("✅ Twitter: Tweet berhasil diposting!")

def upload_ke_gumroad(title, description):
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": title,
        "product[description]": description,
        "product[price]": 0,
        "product[published]": "true"
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        product_url = response.json()['product']['url']
        print(f"✅ Gumroad: Berhasil! URL: {product_url}")
        return product_url
    else:
        print(f"❌ Gumroad Gagal: {response.text}")
        return None

def run_factory():
    # 1. Deteksi hari ini
    hari_ini = datetime.datetime.now().weekday()
    jenis = JADWAL_PRODUKSI.get(hari_ini, "Premium Digital Asset")
    
    print(f"🚀 Pabrik mode '{jenis}' aktif.")
    
    # 2. Generate Konten
    judul = client.models.generate_content(model="gemini-2.0-flash", contents=f"Generate a viral premium title for a {jenis} in English.").text.strip()
    time.sleep(15) 
    isi = client.models.generate_content(model="gemini-2.0-flash", contents=f"Write a persuasive sales description in English for: '{judul}'. Include a 'Why it's worth it' section.").text
    
    # 3. Upload & Dapatkan URL
    product_link = upload_ke_gumroad(judul, isi)
    
    # 4. Tweet jika upload sukses
    if product_link:
        post_to_twitter(f"🚀 New Premium {jenis} just released: {judul}! Elevate your game today. Get it here: {product_link} #DigitalProduct #PassiveIncome")
        print(f"🎉 Selesai! {jenis} telah terbit.")
    else:
        print("⚠️ Gagal memposting ke Twitter karena upload gagal.")

if __name__ == "__main__":
    try:
        run_factory()
    except Exception as e:
        print(f"⚠️ Terjadi error: {e}")
