"""
Amaç:
    - fastapi ile veritabanına veri yazma ve okuma
    - daha önce fonksiyonlar ile tanımlanan veritabanı işlemlerini API katmanına bağlamak
    - kullanıcıdan gelen verileri kaydetme ve kayıtlı verileri listeleme endpoint üzerinde yapalım

Plan/program:
    1. sqlite ile veritabanı, tablo ve yardımcı fonksiyonların hazırlanması
    2. fastapi ile veri ekleme ve veri silme endpointlerini tanımla
    3. swagger ile test etme

Kurulumlar:
pip install fastapi uvicorn
"""

import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# post ile gönderilecek mesajın veri modelini oluşturma
class MesajModel(BaseModel):
    kullanici_mesaji: str
    bot_cevabi: str

# 1. sqlite ile veritabanı, tablo ve yardımcı fonksiyonların hazırlanması
# veritabanına bağlanmak için yardımcı fonksiyon
def veritabani_baglantisi_olustur():
    return sqlite3.connect("mesajlar.db")

# tablo oluşturmak için yardımcı bir fonksiyon
def tablo_olustur():

    baglanti = veritabani_baglantisi_olustur() # veritabanına bağlan
    imlec = baglanti.cursor() # değişiklik için imlec oluştur

    imlec.execute(
        """
        CREATE TABLE IF NOT EXISTS mesajlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_mesajlari TEXT NOT NULL,
            bot_cevabi TEXT NOT NULL
        )
    """
    )

    baglanti.commit() # değişiklik olması için
    baglanti.close()

# CREATE: yeni kayıt ekleme
def mesaj_ekle(kullanici_mesaji, bot_cevabi):

    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()

    imlec.execute(
        """
            INSERT INTO mesajlar (kullanici_mesajlari, bot_cevabi)
            VALUES (?, ?)
        """, (kullanici_mesaji, bot_cevabi)
    )

    baglanti.commit()
    baglanti.close()

# READ
def tum_mesajlari_getir():

    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()

    imlec.execute("SELECT * FROM mesajlar")
    kayitlar = imlec.fetchall()

    baglanti.close()
    return kayitlar

tablo_olustur()

# 2. fastapi ile veri ekleme ve veri silme endpointlerini tanımla
@app.post("/mesaj-ekle")
def mesaj_ekle_endpoint(veri:MesajModel):
    
    #gelen veriyi dbye kaydet
    mesaj_ekle(veri.kullanici_mesaji, veri.bot_cevabi)
    
    return {
        "durum": "basarili",
        "mesaj": "kayıt dbye başarıyla eklendi",
        "eklenen_veri": {
            "kullanici_mesaji": veri.kullanici_mesajı,
            "bot_cevabi": veri.bot_cevabi
        }
    }
    
@app.get("/mesajlar")
def mesajlari_listele():
    kayitlar = tum_mesajlari_getir()
    sonuc = []
    
    for kayit in kayitlar:
        sonuc.append(
            {
                "id": kayit[0],
                "kullanici_mesaji": kayit[1],
                "bot_cevabi": kayit[2]
            }
        )
    
    return {
        "durum": "basarili",
        "toplam_kayit": len(sonuc),
        "mesajlar": sonuc
    }