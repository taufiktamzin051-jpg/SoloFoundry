import os
from google import genai
import tweepy

# 1. Konfigurasi Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Konfigurasi Twitter (Pastikan secret key ini ada di GitHub Secrets Anda)
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)

def run_factory():
    # A. Buat konten
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Buat tweet pendek (max 280 karakter) tentang tips produktivitas menggunakan AI."
    )
    tweet_text = response.text
    
    # B. Posting ke Twitter
    try:
        api.update_status(tweet_text)
        print("Berhasil posting ke Twitter!")
    except Exception as e:
        print(f"Gagal posting: {e}")

if __name__ == "__main__":
    run_factory()
