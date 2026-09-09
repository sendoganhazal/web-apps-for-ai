"""
Amaç:
    - sanki arka planda bir dil modeli varmış gibi çalışan bir chatbot servisi geliştireceğiz
    - kullanıcıdan gelen mesaj alınır, mesajı işliyormuş gibi bekleme simülasyonu yapılır, uygun bir cevap üretilir, gelen mesaj ile cevap kayıt altına alınır

Plan/program:
    1. fastapi uygulaması ve veri modeli oluşturma
    2. kullanıcı mesajını alan async bir endpoint
    3. cevap üret, kayıt işlemleri ve sonucu döndürme
"""

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

# 1. fastapi uygulaması ve veri modeli oluşturma
app = FastAPI()

class MesajIstek(BaseModel):
    mesaj: str

# sanki bir dil modeli varmış gibi cevap üreten bir asenkron fonksiyon
async def sahte_dil_modeli_cevap_uret(kullanici_mesaji: str) -> str:
    
    # dil modeli düşünür
    await asyncio.sleep(2)
    
    # basit bir cevap modeli: amacı gerçek model kullanmak değil, llm varmış gibi yapmak
    mesaj_kucuk = kullanici_mesaji.lower()
    
    if "merhaba" in mesaj_kucuk:
        return "Merhaba, size nasıl yardımcı olabilirim?"
    elif "hava" in mesaj_kucuk:
        return "Bugün hava durumunu değerlendirmek için elimde gerçek veri yok."
    else:
        return f"Mesajınızı aldım: {kullanici_mesaji}"

# mesaj ve cevabı sanki veritabanına kaydediyormuş gibi simule eden asenkron fonksiyon
async def mesaji_kaydet(kullanici_mesaji:str, model_cevabı: str):
    
    await asyncio.sleep(1)
    
    # normalde burada veritabanına insert işlemi yapılmalı
    print(f"Kullanıcı Mesajı: {kullanici_mesaji}")
    print(f"Model Cevabı: {model_cevabı}")
    print("Kayıt İşlemi Tamamlandı")

# 2. kullanıcı mesajını alan async bir endpoint
@app.post("/chat")
async def chat_yap(istek:MesajIstek):
    
    cevap = await sahte_dil_modeli_cevap_uret(istek.mesaj) # llm cevap üretir
    
    await mesaji_kaydet(istek.mesaj, cevap) # cevap ve mesaj kaydedilir
    
    return {
        "durum": "Başarılı",
        "kullanici_mesaji": istek.mesaj,
        "model_cevabi": cevap
    }
    
    