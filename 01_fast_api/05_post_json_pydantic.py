"""
POST endpointi
    - post ile sunucuya veri gönderilir

JSON Body:
    - post isteklerinde çoğu zaman json formatı kullanılıyor

Pydantic Model:
    - api ye gelen veriyi düzenli ve gücenli şekilde tanımlamamızı sağlar
    - hangi alanların geleceğini, bu alanların veri tiplerini ve yapısını önceden ayarlarız

Adımlar:
    1. basit bir post endpointi yaz
    2. json body ile veri alma
    3. pydantic model oluştur
    4. kullanıcıdan gelen veriyi ekrana döndür
    5. swagger ile post testi
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# pydantic ile api input tanımı 

class KullaniciBilgisi(BaseModel):
    ad: str
    yas: int
    sehir: str

# post ile sunucuya veri gönderilir
@app.post("/kullanici")

def kullanici_ekle(kullanici:KullaniciBilgisi) :
    
    return {
        "mesaj": "Kullanıcı bilgisi başarıyla alındı",
        "veri":kullanici
    }