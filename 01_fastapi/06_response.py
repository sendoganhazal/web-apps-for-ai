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

# kullanıcıdan gelecek olan verinin yapısının tanımlanması
class KullaniciBilgisi(BaseModel):
    ad: str
    yas: int
    sehir: str

# ana endpoint
@app.get("/")
def home():
    return {
        "mesaj":"Response, Hata Yönetimi ve Status Code örneği"
    }

# başarılı post örneği
@app.post("/kullanici-ekle", status_code=status.HTTP_201_CREATED)
def kullanici_ekle(kullanici: KullaniciBilgisi):
    # kullanıcı bilgilerini al ve başarılı bir şekilde ekle
    return {
        "durum": "başarılı",
        "mesaj": "Kullanıcı başarıyla eklendi", 
        "veri": {
            "ad": kullanici.ad,
            "yas": kullanici.yas,
            "sehir": kullanici.sehir
        }
    }

# hata yönetimi örneği
# eğer bir ürün bulunamazsa 404 hatası döndür
@app.get("/urun/{urun_id}")
def urun_getir(urun_id: int):
    # örnek olarak ürün id 1 olan bir ürün var, diğerleri yok
    if urun_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ürün bulunamadı"
        )
    return {
        "durum": "başarılı",
        "mesaj": "Ürün bulundu",
        "veri": {
            "urun_id": urun_id,
            "urun_adi": "Örnek ürün 1"
        }
    }