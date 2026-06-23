import os
import time
from google import genai
import tweepy

# Konfigurasi
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Konfigurasi Twitter
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)

def run_factory():
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"Percobaan produksi ke-{attempt + 1}...")
            
            # Membuat konten
            response = client.models.generate_content(
                model="gemini-2.0-flash", # Coba model 2.0 yang mungkin lebih stabil
                contents="Buat tweet pendek tentang tips produktivitas AI."
            )
            tweet_text = response.text
            
            # Posting ke Twitter
            api.update_status(tweet_text)
            print("Berhasil posting!")
            break # Keluar dari loop jika berhasil
            
        except Exception as e:
            print(f"Gagal: {e}. Menunggu 10 detik sebelum mencoba lagi...")
            time.sleep(10) # Jeda waktu agar server 'tenang'
    else:
        print("Gagal setelah beberapa kali percobaan.")

if __name__ == "__main__":
    run_factory()
