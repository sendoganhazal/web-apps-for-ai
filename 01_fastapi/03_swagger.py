"""
Swagger Dokümantasyon ile API Testi
    - endpoint listesi görmek
    - istek gönderebilmek
    - dönen cevapları incelemek

Adımlar:
    1. FastAPI sınıfını içe aktar
    2. Uygulama nesnesi oluştur
    3. ilk endpointi yaz
    4. tarayıcı üzerinden /docs swagger arayüzünü aç
    5. swagger ekranından endpointimizi görmek
    6. "try it out" ile endpoint testi
    7. response görüntüle
"""

# 1. FastAPI sınıfını içe aktar
from fastapi import FastAPI

# 2. Uygulama nesnesi oluştur
app = FastAPI()

# 3. ilk endpointi yaz
@app.get("/") # bu bir endpointtir.
def home(): # tarayıcıdan erişildiğinde basit bir mesaj döndürsün

    return {"mesaj": "Merhaba, ilk FastAPI uygulamam çalışıyor!"}

@app.get("/deneme") #deneme endpointi
def home2():
    return {"mesaj": "Deneme endpointi çalışıyor!"}
