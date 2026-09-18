"""
    Veri Analiz Servisi Projesi

    Proje tanıtımı:
        - bir csv dosyası okuyabilen
        - temel analizler yapabilen
        - sonuçları veritabanına kaydeden
        - geçmiş analiz kayıtlarını listeleyebilen bir veri analiz servisi geliştirme.

    Proje senaryosu:
        - kullanıcı csv dosyası yükler
        - sistem csv (veri) dosyası okur, temel analizler yapar ve sonuçları kaydeder
        - sonrasında kullanıcı geçmiş analizleri listeleyebilecek ve isterse tek bir analiz kaydının detayını görebilecek

    Plan/Program:
        1. gerekli kütüphanelerin içeriye aktarılması
        2. logging altyapısının kurulması
        3. fastapi app oluşturma
        4. veritabanı altyapısı hazırlama
        5. veri analizi yapan yardımcı fonksiyonların ve db işlemleri yapan fonksiyonların tanımlanması
        6. csv yükleme endpointinin yazılması
        7. analiz geçmişi listeleyen endpoint yazılması
        8. tekil analizi listeleyen endpoint yazılması
        9. request ile client testi yapmak
        10. tüm sistem testi

    Kurulumlar:
    pip install fastapi uvicorn pandas requests python-multipart

"""

# 1. gerekli kütüphanelerin içeriye aktarılması
from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import sqlite3
import json
import logging
from datetime import datetime
from io import BytesIO

# 2. logging altyapısının kurulması
logging.basicConfig(
    filename="analysis_service.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s"
)

# 3. fastapi app oluşturma
app = FastAPI()

# 4. veritabanı altyapısı hazırlama


# 5. veri analizi yapan yardımcı fonksiyonların ve db işlemleri yapan fonksiyonların tanımlanması


# 6. csv yükleme endpointinin yazılması


# 7. analiz geçmişi listeleyen endpoint yazılması


# 8. tekil analizi listeleyen endpoint yazılması


# 9. request ile client testi yapmak
# 10. tüm sistem testi
