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

# 1. basit bir get endpoint yaz
@app.get("/")
def home():
    return {"mesaj": "Basit bir get endpointi örneği"}

# 2. path parametresini kullan
@app.get("/urun/{urun_id}")
def urun_getir(urun_id: int):
    return {
        "mesaj": "path parametresi ile ürün getirildi",
        "urun_id": urun_id
    }

# 3. query parametresini kullan
@app.get("/arama")
def arama_yap(kelime: str): # kelime değeri url sonunda ?kelime=... şeklinde gönderilir
    return {
        "mesaj": "query parametresi ile arama yapıldı",
        "aranan_kelime": kelime
    }
