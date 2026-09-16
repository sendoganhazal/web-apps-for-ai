"""
Amaç:
    - sqlite kullanarak veritabanı oluşturma
    - python ile tablo yapısı hazırla ve ilk kaydı ekle
    - veri tabanı bağlantısı, tablo oluşturma ve veri ekleme mantığını görmüş olacağız

Plan/program:
    1. sqlite veritabanı bağlantısı oluştur
    2. tablo oluştur (db tablosu) ve kullanıcı mesajlarını tutar
    3. tabloya kayıt ekleme

"""
import sqlite3

# 1. sqlite veritabanı bağlantısı oluştur
# sqlite veritabanı dosyası bağla
baglanti = sqlite3.connect("mesajlar.db") # eğer db dosyası yoksa yeni dosya oluşturur

# sql komutları için bir cursor nesnesi oluştur
imlec = baglanti.cursor()

# 2. tablo oluştur (db tablosu) ve kullanıcı mesajlarını tutar
imlec.execute(
    """
    CREATE TABLE IF NOT EXISTS mesajlar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kullanici_mesajlari TEXT NOT NULL,
        bot_cevabi TEXT NOT NULL
    )
"""
)

# 3. tabloya kayıt ekleme
imlec.execute(
    """
        INSERT INTO mesajlar (kullanici_mesajlari, bot_cevabi)
        VALUES (?, ?)
    """, (
        "Merhaba nasılsın?",
        "merhaba ben örnek bir chatbot cevabıyım."
    )
)
#yapılan değişiklikleri veritabanına kaydet
baglanti.commit()