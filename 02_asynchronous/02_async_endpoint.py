"""
Amaç:
    - fastapi içinde async endpoint yazma
    - normal endpoint vs async endpoint

Plan/Program:
    1. önce normal bir endpoint tanımla
    2. async endpoint tanıma
    3. await ile bekleme simülasyonu yapıp farkı gör

pip install fastapi uvicorn
"""

import asyncio
from fastapi import FastAPI

app = FastAPI() # fastapi uygulamasını başlat

# 1. önce normal bir endpoint tanımla
@app.get("/")
def home():
    return {
      "mesaj": "bu normal bir endpoint örneğidir",
       "tip": "senkron"
    }

# 2. async endpoint tanıma
@app.get("/asenkron")
async def asynchronous():
    await asyncio.sleep(5) # 3. await ile bekleme simülasyonu yapıp farkı gör
    return {
      "mesaj": "bu asenkron bir endpoint örneğidir",
       "tip": "asenkron",
       "durum": "bekleme tamamlandı"
    }
