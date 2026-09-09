"""
Amaç:
    - requests kütüphanesi ile get ve post istekleri gönder

pip install requests
"""

import requests

BASE_URL = "http://127.0.0.1:8000" # fastapi servisinin temel adresi

# get isteği gönderme
get_response = requests.get(f"{BASE_URL}/durum")

print(f"status code: {get_response.status_code}")
print(f"json cevap: {get_response.json()}")


# post isteği gönderme
post_data = {
    "mesaj": "selamın hello"
}

post_response = requests.post(f"{BASE_URL}/mesaj", json=post_data) # json=post_data olmazsa 422 hatası alırız çünkü fastapi pydantic modeline göre json bekliyor

print(f"status code: {post_response.status_code}")
print(f"json cevap: {post_response.json()}")