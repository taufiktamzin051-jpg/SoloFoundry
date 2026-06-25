import time
import google.generativeai as genai
from google.api_core import exceptions

# Inisialisasi model
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')

def get_ai_response(prompt):
    """Fungsi produksi konten dengan proteksi limit API."""
    max_retries = 5
    wait_time = 15  # Detik awal menunggu
    
    for attempt in range(max_retries):
        try:
            # Panggilan API utama
            response = model.generate_content(prompt)
            return response.text
        
        except exceptions.ResourceExhausted:
            print(f"Peringatan: Limit API penuh. Menunggu {wait_time} detik... (Percobaan {attempt + 1})")
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff: waktu tunggu bertambah
        
        except Exception as e:
            print(f"Error tak terduga: {e}")
            break
            
    return None

# --- Bagian Workflow Utama Anda ---
def run_production_pipeline(prompt_list):
    for i, prompt in enumerate(prompt_list):
        print(f"Memproduksi konten {i+1}/{len(prompt_list)}...")
        
        result = get_ai_response(prompt)
        
        if result:
            # Di sini logika simpan ke file Anda (misal: write to file)
            print("Konten berhasil dibuat.")
        else:
            print("Gagal memproduksi konten setelah beberapa kali percobaan.")
        
        # Jeda antar konten agar tidak kena limit RPM (Requests Per Minute)
        time.sleep(10) 

# Jalankan
# run_production_pipeline(your_prompts)
