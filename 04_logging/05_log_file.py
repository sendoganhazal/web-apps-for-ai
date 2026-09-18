"""
    Amaç:
        - logları dosyaya yazma, logları kalıcı hale getirme ve log takibi yapabilme

    Plan/Program:
        1. farklı log seviyelerinde kayıt oluşturma
        2. logların dosyaya kaydedildiğini görme
"""
import logging

logging.basicConfig(
    filename="app.log", #logların yazılacağı dosya
    level=logging.DEBUG,
    format="%(levelname)s | %(asctime)s | %(message)s",
    encoding="utf-8"
)

def logs():
    logging.debug("MESAJ: debug kaydi")
    logging.info("MESAJ: info kaydi")
    logging.warning("MESAJ: warning kaydi")
    logging.error("MESAJ: error kaydi")
    logging.critical("MESAJ: critical kaydi")

logs() # app.log'a kayıtlar kaydedildi
