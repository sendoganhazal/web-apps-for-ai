"""
Amaç:
    - CRUD: Create, Read, Update, Delete işlemleri

Plan/Program:
    1. veritabanı ve tablo yapısı oluştur
    2. CRUD işlemlerini ayrı fonksiyonlar olarak tanımla
    3. fonksiyonları çağır ve test et
"""
import sqlite3

# 1. veritabanı ve tablo yapısı oluştur
# veritabanına bağlanmak için yardımcı fonksiyon
def veritabani_baglantisi_olustur():
    return sqlite3.connect("mesajlar.db")

# tablo oluşturmak için yardımcı fonksiyon
def tablo_olustur():
    baglanti = veritabani_baglantisi_olustur() #veritabanına bağlan
    imlec = baglanti.cursor() #değişiklik için cursor oluştur
    
    imlec.execute(
        """
        CREATE TABLE IF NOT EXISTS mesajlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_mesajlari TEXT NOT NULL,
            bot_cevabi TEXT NOT NULL
        )
    """
    )
    
    baglanti.commit() # değişiklikleri db'ye kaydeder
    baglanti.close()
    
# 2. CRUD işlemlerini ayrı fonksiyonlar olarak tanımla

# CREATE: yeni kayıt ekleme
def mesaj_ekle(kullanici_mesajlari, bot_cevabi):
    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()
    
    imlec.execute(
        """
        INSERT INTO mesajlar (kullanici_mesajlari, bot_cevabi)
        VALUES (?,?)
        """, (
            kullanici_mesajlari,
            bot_cevabi
        )
        
    )
    baglanti.commit()
    baglanti.close()
    
# READ: tablo okuma
def tum_mesajlari_getir():
    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()
    
    imlec.execute("SELECT * FROM mesajlar")
    kayitlar = imlec.fetchall()
    
    baglanti.close()
    return kayitlar

# UPDATE: tablo güncelleme
def mesaj_guncelle(kayit_id, yeni_kullanici_mesaji, yeni_bot_cevabi):
    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()
    
    imlec.execute(
        """
        UPDATE mesajlar
        SET kullanici_mesajlari = ?, bot_cevabi = ?
        WHERE id = ?
        """,(yeni_kullanici_mesaji, yeni_bot_cevabi, kayit_id) 
    )
    
    baglanti.commit()
    baglanti.close()
    
# DELETE: tablodan kayıt silme
def mesaj_sil(kayit_id):
    baglanti = veritabani_baglantisi_olustur()
    imlec = baglanti.cursor()
    
    imlec.execute("DELETE FROM mesajlar WHERE id = ?", (kayit_id,))
    baglanti.commit()
    baglanti.close()

# 3. fonksiyonları çağır ve test et
tablo_olustur()

#create
mesaj_ekle("Merhaba, Ben Hazal", "Merhaba, Ben Chatbot") 

#update
mesaj_guncelle(5, "Merhaba, Ben Alex", "Merhaba, sen Hazal değil miydin?")

#delete
mesaj_sil(3) # idsi 3 olan datayı db'den siler

#read
for kayit in tum_mesajlari_getir(): 
    print(kayit)
    