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

from fastapi import FastAPI, HTTPException, status # fastapi import edildi
from pydantic import BaseModel #pydantic import edildi

app = FastAPI() # app nesnesi oluşturuldu

# pydantic nesnesi oluştur: kullanıcıdan gelen havadurumu datasının yapısının oluşturulması
class HavaDurumuVerisi(BaseModel) :
    gun1 : float
    gun2 : float
    gun3: float
    
# Anasayfa endpointi: Proje Hakkında Kısa Bilgi Döndürür
@app.get("/")

def home():
    return {
        "mesaj": "Hava Durumu Tahmin Servisine Hoşgeldiniz!",
        "aciklama":"Son 3 günün sıcaklık verilerini göndererek ortalama tahmini yapar"
    }

# Post Endpointi : Son 3 Günün Hava Durumu Verileri Alınır

@app.post("/hava-tahmin",status_code=status.HTTP_201_CREATED)

def hava_tahmin(veri:HavaDurumuVerisi) :
    # Kullanıcıdan gelen son 3 günün sıcaklık verisini alır
    # Ortalamasını hesaplarmakine öğrenmesi algoritması gibi davranan bir algoritma ortalamayı hesaplar
    # Basit bir tahmin döndürür
    
    # gerçekçi bir sıcaklık kontrolü
    for sicaklik in [veri.gun1, veri.gun2, veri.gun3]:
        if sicaklik < -50 or sicaklik > 60 :
            raise HTTPException(
                status_code=400,
                detail="Lütfen Gerçekçi Bir Sıcaklık Verisi Giriniz!"
            )
    # ortalama sıcaklık hesaplama: ( burası makine öğrenmesi algoritması olmalıydı)
    toplam = veri.gun1 + veri.gun2 + veri.gun3
    ortalama = toplam / 3
    
    # ortalama değere göre basit bir yorum üret
    if ortalama < 10 :
       tahmin = "Hava Soğuk Gibi"
    elif ortalama < 25 :
        tahmin = "Hava dengeli"
    else :
        tahmin = "Hava Sıcak"
        
    return {
        "durum": "basarili",
        "girilen_veriler": {
            "gun1": veri.gun1,
            "gun2": veri.gun2,
            "gun3": veri.gun3
        },
        "ortalama_sicaklik": round(ortalama),
        "tahmin": tahmin
    }
    
