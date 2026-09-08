"""
Amaç:
    - asenkron programlama kullanırken sık yapılan hatalar
    - sadece async yazmak yeterli değil, 
    yanlış yerde async kullanmak, 
    blocking kod yazmak veya await yapısını hatalı kullanmak beklenen faydayı azaltır

Plan/Program:
    1. önce async içerisinde blocking kod kullanımı 
    2. sonra doğru bekleme (await) ile hatalıyı karşılaştır
    3. await kullanımının neden gerekli olduğunu görmüş olalım
"""

import time
import asyncio 
from fastapi import FastAPI

app = FastAPI() # fastapi uygulamasını başlat

@app.get("/")
def home():
    return {
        "mesaj": "asenkron programlama hataları dersine hoşgeldiniz"
    }

def random_function():
    return "herhangi bir fonksiyon"
    
# 1. async içerisinde blocking kod kullanımı
"""
async endpoint içinde blocking kod kullanımı hatalıdır, 
çünkü async endpointler event loop üzerinde çalışır ve blocking kodlar event loop'u bloke eder. 
Bu nedenle, async endpointler içinde blocking kodlar kullanmaktan kaçınılmalıdır.
"""
@app.get("/blocking")
async def blocking():
    #hatalı kullanım
    # bu yapılar senkron çalışır ve işlemi durdurur.
    time.sleep(5) # senkron çalışır
    random_function() # senkron çalışır
    return {
        "durum":"hatalı",
        "mesaj": "bu endpoint async yazıldı ancak içinde blocking kod kullanıldı."
    }


# 2. doğru bekleme (await) ile hatalıyı karşılaştır
# burada bekleme işlemi await asyncio.sleep() ile yapılır.
async def random_func():
    return "asenkron fonksiyon"

@app.get("/non_blocking")
async def non_blocking():
    #doğru kullanım
    await asyncio.sleep(5) # asenkron çalışır
    await random_func() # asenkron çalışır
    return {
        "durum":"başarılı",
        "mesaj": "bekleme işlemi async mantığına uygun şekilde yapıldı"
    }
    
# 3. await kullanımının neden gerekli olduğunu görmüş olalım
async def data_preparation():
    # bi milyon tane işlem yapılıyor
    await asyncio.sleep(5)
    return "veri hazır"

@app.get("/await")
async def await_example():
    sonuc = await data_preparation() 
    return {
        "durum":"başarılı",
        "mesaj": sonuc
    }