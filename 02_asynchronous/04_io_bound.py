"""
IO Bound

Amaç:
    - fastapi ile io bound işlemleri simülasyonu
    - io bound: dosya okuma, dış api bekleme, veritabanı yazma veya ağ üzerinden veri gönderme
    - pdf dosyası işleyip vektör veritabanına kaydediyormuşuz gibi yapacağız

Plan/program:
    1. fastapi ile async endpointi
    2. pdf işleme ve vektör veritabanı yazma simülasyonu
    3. aynı anda birden fazla isteğin gelebileceği bir yapıyı örnekle 

"""
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# pdf verisini temsil eden model
class PDFData(BaseModel):
    content: str

# 1. fastapi ile async endpointi
# pdf işleme sürecini temsil eden asenkron fonksiyon
async def pdf_isleme(dosya_adi: str):
   print(f"{dosya_adi} için PDF okuma işi başladı")
   
   # pdf okuma ve parçalama simulasyonu
   await asyncio.sleep(2)
   
   print(f"{dosya_adi} için embedding hazırlama işi başladı")
   
   #embeddding hazırlama süreci
   await asyncio.sleep(2)
   
   print(f"{dosya_adi} için vektör veritabanı kayıt işi başladı")
   
   #vektör veritabanı kayıt süreci
   await asyncio.sleep(2)
   
   print(f"{dosya_adi} başarıyla işlendi")
   
# 2. pdf işleme ve vektör veritabanı yazma süreci endpointi
@app.post("/pdf-isle")
async def pdf_isle(veri: PDFData):
    dosya_adi = veri.content
    await pdf_isleme(dosya_adi)
    return {
        "durum": "başarılı",
        "mesaj": f"{dosya_adi} başarıyla işlendi ve vektör veritabanına kaydedildi"
    }


# 3. aynı anda birden fazla isteğin gelebileceği bir yapıyı örnekle
@app.post("/iki-pdf-isle")
async def iki_pdf_isle():
   await asyncio.gather(
       pdf_isleme("rapor_1.pdf"),
       pdf_isleme("rapor_2.pdf")
   )
   return {
        "durum": "başarılı",
        "mesaj": "2 pdf aynı anda başarıyla işlendi ve vektör veritabanına kaydedildi"
    }

