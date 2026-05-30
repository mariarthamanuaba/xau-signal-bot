import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

if not TOKEN or not CHAT_ID:
    print("ENV ERROR: TOKEN atau CHAT_ID kosong")
    exit()

message = "Bot XAU Signal Aktif 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=payload)

print("Response:", response.text)
