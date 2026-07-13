"""
Swagger Dokümantasyon ile API Testi
    - endpoint listesi görmek
    - istek gönderebilmek
    - dönen cevapları incelemek

Adımlar:
    1. mevcut fast api uygulamasını çalıştır
    2. tarayıcı üzerinden /docs swagger arayüzünü aç
    3. swagger ekranından endpointimizi görmek
    4. "try it out" ile endpoint testi
    5. response görüntüle
"""

from fastapi import FastAPI

app = FastAPI()

# 1. get endpointi
@app.get("/")

def home():
    # bu bir endpointtir.
    #tarayıcıdan erişildiğinde bir mesaj döndürsün
    
    return { "mesaj": "Merhaba ilk swagger FastAPI uygulamam çalışıyor!" }


# get metodumuz var, deneme endpointimiz get metodu ile çalışıyor, deneme endpointi çağrılırsa home fonksiyonu çalışır ve bir mesaj return eder.
@app.get("/deneme")
def home():
    """
    deneme
    """

    return {"mesaj": "deneme"}