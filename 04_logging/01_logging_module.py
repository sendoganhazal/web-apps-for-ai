"""
Amaç:
    - python logging modülü tanımak
    - temel log seviyelerini öğrenmek
    - logging kullanımını örnekler ile görmek

Plan/program:
    1. logging kütüphanesini içeriye aktar
    2. temel logging ayarları
    3. log seviyelerini gösterme
    4. print ve logging farkı
    5. örnek senaryolar ile log üretme
"""

# 1. logging kütüphanesini içeriye aktar
import logging

# 2. temel logging ayarları
"""
    DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
"""

logging.basicConfig(
    level=logging.DEBUG, # debug ve üzerindeki tüm seviyelerini görebileceğiz
    format="%(levelname)s | %(asctime)s | %(message)s"
)

# 3. log seviyelerini gösterme
def log_seviyeleri_gorme():
    #debug
    logging.debug("debug message")
    
    #info
    logging.info("info message")
    
    #warning
    logging.warning("warning message")
    
    #error
    logging.error("error message")
    
    #critical
    logging.critical("critical message")
    
log_seviyeleri_gorme()

"""
    DEBUG | 2026-09-17 14:08:02,505 | debug message
    INFO | 2026-09-17 14:08:02,505 | info message
    WARNING | 2026-09-17 14:08:02,505 | warning message
    ERROR | 2026-09-17 14:08:02,505 | error message
    CRITICAL | 2026-09-17 14:08:02,505 | critical message
"""

# 4. print ve logging farkı

print("PRINT: Kullanici sisteme giris yapti") # PRINT: Kullanici sisteme giris yapti
logging.info("Kullanici sisteme giris yapti") # INFO | 2026-09-17 14:10:00,271 | Kullanici sisteme giris yapti

# 5. örnek senaryolar ile log üretme

# işlem başlarken bilgi logu
kullanici_adi="alexcharou"
logging.info(f"kullanici isleme basladi. kullanici adi: {kullanici_adi}") # INFO | 2026-09-17 14:12:39,696 | kullanici isleme basladi. kullanici adi: alexcharou

#geliştirme sırasında değişkenleri görmek için
yas = 15
logging.debug(f"gelen yas datasi: {yas}") # DEBUG | 2026-09-17 14:14:01,952 | gelen yas datasi: 15


kullanici_adi = ""
if not kullanici_adi:
    logging.error("kullanici adi bos") # ERROR | 2026-09-17 14:18:49,982 | kullanici adi bos
    
if yas < 18:
    logging.warning("kullanici 18 yasindan kucuk") # WARNING | 2026-09-17 14:19:47,834 | kullanici 18 yasindan kucuk
    
yas = -5
if yas < 0:
    logging.critical("yas bilgisi negatif geldi") # CRITICAL | 2026-09-17 14:20:38,321 | yas bilgisi negatif geldi