"""
Response:
    - API nin cevabı, geri döndürdüğü yapı
    - yani bir istek başarılı olduğunda hangi veriyi hangi formatta döneceğimizi burada tanımlarız

Hata Yönetimi:
    - kullanıcı yanlış veri gönderirse yada sistem içerisinde hata oluşursa uygun bir hata mesajı döndürmemiz gerekir.

Status Code
    - API'nin döndürdüğü cevabın durumunu gösteren http kodları
    - Örneğin:
        - 200: işlem başarılı
        - 201: yeni kayıt
        - 400: hatalı istek
        - 404: veri bulunmadı

Adımlar:
    1. başarılı response yapısı
    2. hatalı durumda özel mesaj döndürme
    3. HTTPException kullanmak
    4. status code mantığını uygulamak
    5. swagger üzerinden başarılı ve hatalı durumları test et

"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# fast api nesnesi tanımla
app = FastAPI()

# kullanıcıdan gelen verinin yapısının tanımlanması
class KullaniciBilgisi(BaseModel) :
    ad: str
    yas: int
    sehir: str
    
# ana endpoint
@app.get("/")

def Home() :
    return {
        "mesaj":"Response, Error Handling ve Status Code Dersine Hoşgeldiniz"
    }
    
# başarılı post örneği
@app.post("/kullanici", status_code=status.HTTP_201_CREATED)

def kullanici_ekle(kullanici:KullaniciBilgisi): 
    return {
        "durum": "basarili",
        "mesaj": "kullanıcı bilgisi başarıyla eklendi",
        "veri": {
            "ad": kullanici.ad,
            "yas": kullanici.yas,
            "sehir": kullanici.sehir
        }
    }


# hata yönetimi örneği
@app.get("urun/{urun_id}")

def urun_getir(urun_id : int):
    
    if urun_id != 1 :
        raise HTTPException(
            status_code = 404,
            detail = "not found"
        )
    
    return {
        "durum": "basarili",
        "mesaj":"Urun basariyla getirildi",
        "veri": {
            "urun_id": urun_id,
            "urun_adi":"Urun 1"
        }
    }