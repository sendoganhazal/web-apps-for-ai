"""
Amaç:
    - fastapi içinde async endpoint yazma
    - normal endpoint vs async endpoint

Plan / Program:
    1. önce normql bir endpoint tanımla
    2. async endpoint tanıma
    3. await ile bekleme simülasyonu yapıp farkı gör

pip install fastapi uvicorn
"""

import asyncio
from fastapi import FastAPI

# fastapi uygulama nesnesi oluşturma
app = FastAPI()

# 1. normal bir endpoint tanımlama
@app.get("/")

def home():
    return {
        "mesaj": "Bu Bir Senkron Endpoint Örneğidir",
        "tip": "senkron"
    }

# 2. asenkron bir endpoint tanımlama
@app.get("/asenkron")

async def asenkron() :
    # 3.await ile bekleme simülasyonu yapıp farkı gör
    await asyncio.sleep(5)
    return {
        "mesaj": "Bu Bir Asenkron Endpoint Örneğidir",
        "tip": "asenkron",
        "durum": "Bekleme Tamamlandı"
    }