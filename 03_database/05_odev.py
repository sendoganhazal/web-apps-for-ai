"""
    4.6 Database Katmanı Ödev ve Çözüm

    Bu ödevde küçük bir şirket çalışan kayıt sistemi geliştireceğiz.
    Amaç, SQLite veritabanı ile FastAPI yapısını birlikte kullanarak çalışan ekleme ve çalışan listeleme işlemlerini gerçekleştirmektir.
    Bu dosyada tablo oluşturma, çalışan ekleme ve çalışan listeleme işlemlerini fonksiyonlar halinde yazacağız.
    Daha sonra bu fonksiyonları FastAPI endpointleri ile kullanacağız.
    Test işlemlerini Swagger arayüzü üzerinden yapacağız.

    Talimatlar:
        1. sqlite3 kullanarak sirket.db adında bir veritabanı bağlantısı oluşturun
        2. calisanlar adında bir tablo oluşturun
        3. Bu tabloda id, isim, bolum ve yas alanları bulunsun
        4. veritabani_baglantisi_olustur() adında bir fonksiyon yazın
        5. tablo_olustur() adında bir fonksiyon yazın
        6. calisan_ekle() adında bir fonksiyon yazın
        7. tum_calisanlari_getir() adında bir fonksiyon yazın
        8. CalisanModel adında bir Pydantic model tanımlayın
        9. /calisan-ekle adında bir POST endpoint yazın
        10. /calisanlar adında bir GET endpoint yazın
        11. Uygulamayı çalıştırın ve Swagger üzerinden test edin

    Swagger ile test:
        - Uygulamayı şu komutla çalıştırın: uvicorn main:app --reload
        - Tarayıcıdan şu adrese gidin: http://127.0.0.1:8000/docs
        - Önce /calisan-ekle endpointi ile yeni çalışan ekleyin
        - Sonra /calisanlar endpointi ile tüm çalışanları listeleyin
"""