"""
Amaç:
    - fastapi ile oluşturulan endpointleri test etme
    - post ve get testleri

Plan/program:
    1. önce api adresini tanımla
    2. post isteği ile kayıt ekle
    3. get ile kayıtları listele

Kurulumlar:
pip install requests
"""
import requests
# 1. önce api adresini tanımla
BASE_URL = "http://127.0.0.1:8000"

gonderilecek_veri = {
    "kullanici_mesaji": "Merhaba, Ben Client.",
    "bot_cevabi": "Merhaba, Client. Ben de Chatbot."
}

# 2. post isteği ile kayıt ekle
post_response = requests.post(f"{BASE_URL}/mesaj-ekle", json = gonderilecek_veri) # "http://127.0.0.1:8000/mesaj-ekle"
print(f"POST cevabı: {post_response.json()}")

# 3. get ile kayıtları listele
get_response = requests.get(f"{BASE_URL}/mesajlar")

print(f"GET cevabı: {get_response.json()}")

"""
POST cevabı: {
    'durum': 'basarili', 
    'mesaj': 'kayıt dbye başarıyla eklendi', 
    'eklenen_veri': {'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}
}
GET cevabı: {
    'durum': 'basarili', 
    'toplam_kayit': 13, 
    'mesajlar': [
        {'id': 1, 'kullanici_mesaji': 'Merhaba nasılsın?', 'bot_cevabi': 'merhaba ben örnek bir chatbot cevabıyım.'}, 
        {'id': 2, 'kullanici_mesaji': 'Merhaba, Ben Hazal', 'bot_cevabi': 'Merhaba, Ben Chatbot'}, 
        {'id': 4, 'kullanici_mesaji': 'Merhaba, Ben Hazal', 'bot_cevabi': 'Merhaba, Ben Chatbot'}, 
        {'id': 5, 'kullanici_mesaji': 'Merhaba, Ben Alex', 'bot_cevabi': 'Merhaba, sen Hazal değil miydin?'}, 
        {'id': 6, 'kullanici_mesaji': 'Merhaba, Ben Hazal', 'bot_cevabi': 'Merhaba, Ben Chatbot'}, 
        {'id': 7, 'kullanici_mesaji': 'sa', 'bot_cevabi': 'as'}, 
        {'id': 8, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}, 
        {'id': 9, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}, 
        {'id': 10, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}, 
        {'id': 11, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}, 
        {'id': 12, 'kullanici_mesaji': 'string', 'bot_cevabi': 'string'}, 
        {'id': 13, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}, 
        {'id': 14, 'kullanici_mesaji': 'Merhaba, Ben Client.', 'bot_cevabi': 'Merhaba, Client. Ben de Chatbot.'}
        ]
    }
"""
