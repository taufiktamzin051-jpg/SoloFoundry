import os
import requests
import time
from google import genai
from google.genai import errors
import tweepy

# Setup
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Tambahkan Jeda (Sleep) agar tidak kena limit
def execute():
    try:
        print("Pabrik mulai beroperasi (Mode Sabar)...")
        time.sleep(30) # Tunggu 30 detik agar server stabil
        
        # Generate dengan model yang paling ringan
        judul_res = client.models.generate_content(model="gemini-2.0-flash-lite", contents="Create a catchy title for an AI productivity e-book.")
        time.sleep(10) # Jeda antar request
        isi_res = client.models.generate_content(model="gemini-2.0-flash-lite", contents="Write a short, professional e-book about AI productivity tips.")
        
        judul = judul_res.text.strip()
        
        # Upload ke Gumroad
        # (Pastikan GUMROAD_ACCESS_TOKEN sudah benar di Secrets)
        upload_ke_gumroad(judul, isi_res.text)
        
        print(f"Produk '{judul}' berhasil dibuat!")
        
    except Exception as e:
        print(f"Gagal karena: {e}")

# ... (fungsi upload_ke_gumroad dan posting_twitter tetap sama)
