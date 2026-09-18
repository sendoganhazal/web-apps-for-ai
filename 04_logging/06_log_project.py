"""
    TALİMATLAR:
    1. fastapi, HTTPException ve logging kütüphanelerini projeye ekleyiniz.
    2. app.log isimli harici bir log dosyasına yazacak şekilde logging ayarını yapınız.
    3. Bir FastAPI uygulaması oluşturunuz.
    4. /calculate isimli bir GET endpointi tanımlayınız.
    5. Bu endpoint içinde username ve number isminde iki parametre alınız.
    6. Endpoint çağrıldığında gelen username ve number bilgisini log dosyasına kaydediniz.
    7. Eğer username 3 karakterden kısa ise hata logu yazınız ve HTTPException ile 400 hatası döndürünüz.
    8. Eğer number negatif ise hata logu yazınız ve HTTPException ile 400 hatası döndürünüz.
    9. Eğer number değeri 0 ise warning seviyesinde log yazınız.
    10. number değerini 2 ile çarpıp result isminde bir sonuç üretiniz.
    11. İşlem başarılıysa info seviyesinde başarılı işlem logu yazınız.
    12. Sonuç olarak username, number ve result bilgilerini JSON formatında döndürünüz.
    13. Endpointi Swagger üzerinden test ediniz.
    14. app.log dosyasını açarak log kayıtlarının oluştuğunu kontrol ediniz.
"""

# adım 1
from fastapi import FastAPI, HTTPException
import logging

# adım 2
logging.basicConfig(
    filename="project.log",
    level=logging.DEBUG,
    format="%(levelname)s | %(asctime)s | %(message)s",
    encoding="utf-8"
)

# 3. Bir FastAPI uygulaması oluşturunuz.
app = FastAPI() # adım 3


@app.get("/calculate") # 4. /calculate isimli bir GET endpointi tanımlayınız.
async def calculate(username: str, number: int): # 5. Bu endpoint içinde username ve number isminde iki parametre alınız.
    
    # 6. Endpoint çağrıldığında gelen username ve number bilgisini log dosyasına kaydediniz.
    logging.info(f"username:{username}, number: {number}")
    
    # 7. Eğer username 3 karakterden kısa ise hata logu yazınız ve HTTPException ile 400 hatası döndürünüz.
    if len(username.strip()) < 3:
        logging.error(f"Username: {username}. Kullanici adi  3 karakterden kisa olamaz")
        raise HTTPException(
            status_code=400,
            detail=f"Username: {username}. Kullanici adi  3 karakterden kisa olamaz"
        )
    
    # 8. Eğer number negatif ise hata logu yazınız ve HTTPException ile 400 hatası döndürünüz.
    if number < 0: 
        logging.error(f"Number: {number}. Number negatif olamaz")
        raise HTTPException(
            status_code=400,
            detail=f"Number: {number}. Number negatif olamaz"
        )
    # 9. Eğer number değeri 0 ise warning seviyesinde log yazınız.
    if number == 0: 
        logging.warning(f"Number: {number}. Number sifir olamaz")
    # 10. number değerini 2 ile çarpıp result isminde bir sonuç üretiniz.
    result = number * 2
    # 11. İşlem başarılıysa info seviyesinde başarılı işlem logu yazınız.
    logging.info(f"Islem basariyla tamamlandi. Username: {username}, Number: {number}, Result = Number * 2 = {result}")
    # 12. Sonuç olarak username, number ve result bilgilerini JSON formatında döndürünüz.
    return {
        "mesaj":"Islem basariyla tamamlandi.",
        "kullanici_adi": username,
        "sayi": number,
        "carpimin_sonucu": result
    }



# 13. Endpointi Swagger üzerinden test ediniz.
# 14. app.log dosyasını açarak log kayıtlarının oluştuğunu kontrol ediniz.
