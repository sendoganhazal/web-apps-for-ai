"""
Kullanıcı tarafı simülasyonu

Plan/program:
    1. kullanıcıdan terminal üzerinden mesaj al
    2. bu mesajı fastapi servisine post ile /chat endpointine gönder
    3. en sonunda dönen cevabı ekranda göstericez
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Kullanıcı Mesajı
