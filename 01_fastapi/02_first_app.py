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

# 1. FastAPI sınıfını içe aktar
from fastapi import FastAPI

# 2. Uygulama nesnesi oluştur
app = FastAPI()

# 3. ilk endpointi yaz
@app.get("/")
def home():
    """
    bu bir endpointtir.
    tarayıcıdan erişildiğinde basit bir mesaj döndürsün
    """

    return {"mesaj": "Merhaba, ilk FastAPI uygulamam çalışıyor!"}

# 4. uvicorn ile uygulamayı çalıştır
# uvicorn 02_first_app:app --reload

# 5. tarayıcıdan sunucunun çalışıp çalışmadığını kontrol et