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

"""
GET Endpoint ve parametre mantığı
    - get metodu sunucudan veri almak için kullanılır. Listeleme, görüntüleme, arama ve filtreleme

İki temel parametre yapısı:
    1. path parametresi:
        - path parametresi, url in bir parçası olarak gönderilir
        - örneğin /urun/5 ifadesibbde 5 değeri bir path parametresidir
        - belirli bir kaydı veya tek bir veriyi çağırmak için kullanırız
    2. query parametresi:
        - url in sonunda ? işaretinden sonra gönderilir
        - örneğin /arama?kelime=python ifadesinde kelime bir query parametresidir
        - arama, filtreleme, sıralama ve sayfalama işlemlerinde kullanılabilir.

Bu derste yapacaklarımız:
    1. basit bir get endpoint yaz
    2. path parametresini kullan
    3. query parametresini kullan
    4. tarayıcı ve swagger üzerinden test et
    5. parametrelerin nasıl çalıştığını görmek
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