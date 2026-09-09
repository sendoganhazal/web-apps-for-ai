"""
Amaç:
    - async fonksiyonlarını başka bir py dosyasından (client) test etme
    - request kütüphanesi kullanma
    - swagger yerine python içinden test etmeyi öğrenmiş olacağız

Plan/Program:
    1. get ve post endpointi oluştur
    2. bu entpointleri yani sunucuyu çalıştır
    3. başka bir python dosyasından request ile test et
"""

import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# POST  için input verinin oluşturulması
class MesajModel(BaseModel):
    mesaj: str

# 1. get ve post endpointi oluştur

# get endpointi
@app.get("/durum")
async def durum_kontrol():
    
    await asyncio.sleep(2)
    
    return {
        "durum": "başarılı",
        "mesaj": "get endpointi çalıştı"
    }

# post endpointi
@app.post("/mesaj")
async def mesaj_al(veri:MesajModel):
    
    await asyncio.sleep(2)
    
    return {
        "durum": "başarılı",
        "alinan_mesaj": veri.mesaj,
        "cevap":"post mesaj başarıyla alındı"
    }