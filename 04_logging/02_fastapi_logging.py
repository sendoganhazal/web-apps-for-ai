"""
Amaç:
    - fastapi endpoint içerisinde logging kullanmak
    - istem ve işlem bilgilerini loglamak
    - başarılı ve hatalı durumları kayıt altına almak

Plan/program:
    1. gerekli kütüphaneleri içeriye aktar
    2. logging config ayarlarını yap
    3. fastapi app tanımla
    4. get endpointi tanımla
    5. post endpointi tanımla

kurulumlar:
pip install fastapi uvicorn
"""

# 1. gerekli kütüphaneleri içeriye aktar
from fastapi import FastAPI
from pydantic import BaseModel
import logging

# 2. logging config ayarlarını yap
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s %(message)s"
)

# 3. fastapi app tanımla
app = FastAPI()

# post için pydantic veri modeli tanımlama
class UserCreate(BaseModel):
    username: str
    age: int

# 4. get endpointi tanımla
@app.get("/user/{username}")
async def get_user(username:str):
    
    #endpoint çağrıldığında gelen parametreyi logla
    logging.info(f"/user endpointi cagrildi. username: {username}")
    
    #geliştirme sırasında detaylı bilgi görmek için
    logging.debug(f"kullanici bilgisi hazirlaniyor. username: {username}")
    
    # boş veya anlamsız olan bir verinin kontrolü
    if len(username.strip()) < 3:
        logging.error("kullanici adi 3 karakterden kisa olamaz")
        return {
            "error":"kullanici adi 3 karakterden kisa olamaz"
        }
    
    logging.info(f"{username} icin kullanici bilgisi basariyla olusturuldu")
    
    return {
        "username":username,
        "message": "Kullanici Bilgisi Basariyla Geldi"
    }

# 5. post endpointi tanımla
@app.post("/users")
async def create_user(user: UserCreate):
    #endpoint çağrısı ve gelen veri
    logging.info(f"/users cagrildi. username: {user.username}, age: {user.age}")
    
    #hatalı duruma örnek
    if user.age < 0:
        logging.error(f"negatif yas bilgisi girildi. Yas: {user.age}")
        return {
            "error": "yas bilgisi negatif olamaz"
        }
    
    # uyarı seviyesi
    if user.age < 18:
        logging.warning(f"{user.username} kullanicisi icin yas bilgisi {user.age} girildi") 
        
    #başarılı işlem
    logging.info("User Basarili")
    return {
        "message":"kullanici basariyla olusturuldu",
        "user": {
            "username": user.username,
            "age": user.age
        }
    }
    
"""
    INFO 2026-09-17 14:50:11,448 /user endpointi cagrildi. username: hazal
    DEBUG 2026-09-17 14:50:11,448 kullanici bilgisi hazirlaniyor. username: hazal
    INFO 2026-09-17 14:50:11,448 hazal icin kullanici bilgisi basariyla olusturuldu
    INFO:     127.0.0.1:57399 - "GET /user/hazal HTTP/1.1" 200 OK
    INFO 2026-09-17 14:50:39,922 /users cagrildi. username: hazal, age: 34
    INFO 2026-09-17 14:50:39,923 User Basarili
    INFO:     127.0.0.1:57405 - "POST /users HTTP/1.1" 200 OK
    INFO 2026-09-17 14:50:47,687 /user endpointi cagrildi. username: hazal
    DEBUG 2026-09-17 14:50:47,687 kullanici bilgisi hazirlaniyor. username: hazal
    INFO 2026-09-17 14:50:47,687 hazal icin kullanici bilgisi basariyla olusturuldu
    INFO:     127.0.0.1:57408 - "GET /user/hazal HTTP/1.1" 200 OK
    INFO 2026-09-17 14:51:28,619 /users cagrildi. username: hazal, age: 17
    WARNING 2026-09-17 14:51:28,620 hazal kullanicisi icin yas bilgisi 17 girildi
    INFO 2026-09-17 14:51:28,620 User Basarili
    INFO:     127.0.0.1:57414 - "POST /users HTTP/1.1" 200 OK
    INFO 2026-09-17 14:51:57,905 /user endpointi cagrildi. username: ha
    DEBUG 2026-09-17 14:51:57,906 kullanici bilgisi hazirlaniyor. username: ha
    ERROR 2026-09-17 14:51:57,906 kullanici adi 3 karakterden kisa olamaz
    INFO:     127.0.0.1:57425 - "GET /user/ha HTTP/1.1" 200 OK
    INFO 2026-09-17 14:52:17,865 /users cagrildi. username: hazal, age: -34
    ERROR 2026-09-17 14:52:17,865 negatif yas bilgisi girildi. Yas: -34
    INFO:     127.0.0.1:57428 - "POST /users HTTP/1.1" 200 OK
"""
