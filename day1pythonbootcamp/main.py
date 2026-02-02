import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
API_KEY = os.getenv("MY_SECRET_KEY")

table = "codefest_participants"

url = f"{SUPABASE_URL}/rest/v1/{table}"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.json())
