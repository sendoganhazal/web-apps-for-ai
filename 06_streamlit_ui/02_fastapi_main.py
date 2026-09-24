"""
    Fastapi ve streamlit ile görüntü üzerinden hastalık tespiti sistemi

    Amaç:
        - görüntüyü streamlit ile yükleriz, fastapi servisine gider, sanki bir ai avarmış gibi hastalık teşhisi yapılır

    Sistem Senaryosu:
        1. kullanıcı streamlit ekranından bir görüntü yükler
        2. streamlit bu görüntüyü fastapi endpointine gönderir
        3. fastapi gelen dosyayı alır
        4. servis tarafında ml/ai sahte bir teşhis yapar
        5. sistem hastalık var yada yok sonucunu bir olasılık ile geri döner
        6. streamlit üzerinden cevap ekrana yazdırılır

    Plan/program:
        1. import libraries
        2. fastapi app başlatma
        3. test amaçlı endpoint tanımla
        4. görüntü yüklemeyi kabul eden tahmin endpointi
        5. görüntü olup olmadığını kontrol et
        6. sahte ml tahmin mantığı kur
        7. hastalık durumu ve olasılık değeri json olarak döndür
        8. uvicorn ile servisi çalıştır

    Kurulumlar:
        pip install fastapi uvicorn python-multipart
"""

# 1. import libraries
from fastapi import FastAPI, UploadFile, File, HTTPException
import random

# 2. fastapi app başlatma
app = FastAPI(
    title = "Sahte Hastalık Teşhisi API",
    description= "Yüklenen Görüntü Üzerinden Hastalık Teşhisi ",
    version="0.0.1"
)

# 3. test amaçlı endpoint tanımla
@app.get("/")
def home():
    #api çalışıyor mu çalışmıyor mu
    
    return {
        "message": "FastAPI çalışıyor",
        "status": "OK"
    }
    
# 4. görüntü yüklemeyi kabul eden tahmin endpointi
@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
     #  bu endpoint ile hastalık teşhisi yapılır

    # 5. görüntü olup olmadığını kontrol et
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code = 400,
            detail = "lütfen geçerli bir görüntü dosyası yükleyiniz"
        )
    
    image_bytes = await file.read()

    if not image_bytes:
        raise HTTPException(
            status_code = 400,
            detail = "yüklenen dosya boş görünüyor"
        )

    # 6. sahte ml tahmin mantığı kur
    probability = round(random.uniform(0.4, 0.99), 2)

    # eğer olasılık 0.6 üzerinde ise hastalık var
    if probability >= 0.6:
        prediction = "Hastalık Var"
    else:
        prediction = "Hastalık Yok"

    # 7. hastalık durumu ve olasılık değeri json olarak döndür 
    return {
        "filename": file.filename,
        "prediction": prediction,
        "probability": probability
    }