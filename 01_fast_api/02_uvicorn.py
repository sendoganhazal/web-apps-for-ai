"""
ilk uygulama yazma ve Uvicorn ile çalıştırma

Adımlar:
    1. FastAPI sınıfını içe aktar
    2. Uygulama nesnesi oluştur
    3. ilk endpointi yaz
    4. uvicorn ile uygulamayı çalıştır
    5. tarayıcıdan sunucunun çalışıp çalışmadığını kontrol et

Hedef:
    - ilk fast api uygulamamızı yazmak ve fastapi nin çalışma mantığını öğrenmek
"""

# . fastapi classını içe aktar
from fastapi import FastAPI  

# 2. uygulama nesnesini oluştur
app = FastAPI()

# 3. ilk endpointi tanımla (get: sistemden veri almak)
@app.get("/")

def home():
    # bu bir endpointtir.
    #tarayıcıdan erişildiğinde bir mesaj döndürsün
    
    return { "mesaj": "Merhaba ilk FastAPI uygulamam çalışıyor!" }

