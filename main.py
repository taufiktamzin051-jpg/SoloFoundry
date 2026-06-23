import os
import requests
import time
from google import genai
import tweepy

# Setup
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Fungsi Upload ke Gumroad
def upload_ke_gumroad(judul, konten):
    with open("produk.txt", "w") as f:
        f.write(konten)
    
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": judul,
        "product[price]": 0,
        "product[description]": "High-quality AI productivity guide for global entrepreneurs."
    }
    files = {"file": open("produk.txt", "rb")}
    return requests.post(url, data=data, files=files).json()

# 2. Fungsi Posting Twitter
def posting_twitter(pesan):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(pesan)

# 3. Fungsi Utama (Pasar Global)
def execute():
    # Generate judul dan isi dalam Bahasa Inggris
    judul_res = client.models.generate_content(model="gemini-2.0-flash-lite", contents="Create a catchy title for an AI productivity e-book.")
    isi_res = client.models.generate_content(model="gemini-2.0-flash-lite", contents="Write a professional, short e-book about AI productivity tips for global entrepreneurs.")
    
    judul = judul_res.text.strip()
    
    # Upload ke Gumroad
    g_res = upload_ke_gumroad(judul, isi_res.text)
    link = g_res['product']['short_url']
    
    # Posting ke Twitter
    tweet_text = f"🚀 Just released: '{judul}'! Boost your productivity with AI. Grab your copy here: {link} #AI #Productivity #GlobalBusiness"
    posting_twitter(tweet_text)
    
    print(f"Pabrik Global Berhasil: {judul} sudah terbit!")

if __name__ == "__main__":
    execute()
