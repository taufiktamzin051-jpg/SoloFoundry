import os
import time
import tweepy
import requests
from google import genai

# Inisialisasi
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Fungsi Posting Twitter
def post_to_twitter(text):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(text)
    print("Berhasil posting ke Twitter!")

# 2. Fungsi Upload Gumroad
def upload_ke_gumroad(title, description):
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": title,
        "product[description]": description,
        "product[price]": 0, # Harga 0 (gratis) atau ubah sesuai keinginan
        "product[published]": "true"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Berhasil upload ke Gumroad!")
    else:
        print(f"Gagal upload Gumroad: {response.text}")

# 3. Fungsi Utama
def run_factory():
    print("Pabrik mulai beroperasi...")
    
    # Generate Judul
    judul_res = client.models.generate_content(model="gemini-2.0-flash", contents="Buatkan judul produk digital yang menarik")
    judul = judul_res.text.strip()
    
    time.sleep(5)
    
    # Generate Deskripsi
    isi_res = client.models.generate_content(model="gemini-2.0-flash", contents=f"Buatkan deskripsi singkat untuk produk: {judul}")
    isi = isi_res.text
    
    # Eksekusi
    upload_ke_gumroad(judul, isi)
    post_to_twitter(f"Produk baru rilis: {judul}! Cek sekarang.")
    
    print("Semua proses selesai!")

if __name__ == "__main__":
    try:
        run_factory()
    except Exception as e:
        print(f"Error terjadi: {e}")
    
