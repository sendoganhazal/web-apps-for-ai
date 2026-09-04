"""
Proje:
    - sanki elimizde basit bir yapay zeka modeli varmış gibi düşünelim
    - yapay zeka modeli: kullanıcı son 3 güne ait hava durumu değerlerini sisteme gönderir, sistem de ortalama sıcaklı hesaplar ve return eder.

Kullanılacak Yapılar:
    1. fastapi uygulama nesnesi oluştur
    2. get endpointi tanımla
    3. post endpointi tanımla
    4. json body ile veri alma
    5. pydantic model kullanma
    6. response yapısı oluşturma
    7. hata kontrolü yapma
    8. status code kullanma

Senaryo:
    1. kullanıcı son 3 günün sıcaklık değerlerini gönderecek
    2. sistem bu değerlerin ortalamasını alır
    3. ortalama değere göre basit yorum döndürülür

Örnek veri:
    - gelen veri:
        {
            "gun1": 20,
            "gun2": 24,
            "gun3": 22,
        } 
    - dönen cevap:
        {
            "durum": "basarili",
            "ortalama_sicaklik": 22
            "tahmin": "hava dengeli görünüyor"
        }

"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# fastapi uygulama nesnesi oluştur
app = FastAPI()

# pydantic modeli oluştur: kullanıcıdan gelen hava durumu verisinin yapısı
class HavaDurumVerisi(BaseModel):
    gun1: float
    gun2: float
    gun3: float
    
# ana karşılama endpointi
@app.get("/")
def home():
    return {
        "mesaj":"Hava Durumu Tahmin Servisine Hoşgeldiniz",
        "aciklama":"Son 3 günün sıcaklık değerlerini göndererek ortalama sıcaklık tahmini yapar."
    }
    
#post endpointi: kullanıcıdan gelen hava durumu verisini alır ve ortalama sıcaklığı hesaplar
@app.post("/hava-tahmin", status_code=status.HTTP_200_OK)
def hava_tahmin(veri: HavaDurumVerisi):
    for sicaklik in [veri.gun1, veri.gun2, veri.gun3]:
        if sicaklik < -50 or sicaklik > 60:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Lütfen gerçekçi sıcaklık değerleri giriniz (-50 ile 60 derece arasında)."
            )
    #ortalama sıcaklığı hesapla
    toplam = veri.gun1 + veri.gun2 + veri.gun3
    ortalama = toplam / 3
    
    #ortalama sıcaklığa göre basit bir yorum üret
    if ortalama < 10:
        tahmin = "Hava soğuk gibi"
    elif ortalama < 25:
        tahmin = "Hava dengeli gibi"
    else:
        tahmin = "Hava sıcak gibi"

    return {
        "durum": "basarili",
        "girilen_veriler": {
            "gun1": veri.gun1,
            "gun2": veri.gun2,
            "gun3": veri.gun3
        },
        "ortalama_sicaklik": ortalama.round(2),
        "tahmin": tahmin
    }