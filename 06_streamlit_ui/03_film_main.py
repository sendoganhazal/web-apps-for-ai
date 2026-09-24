"""
    PROJE ADI:
        Film Yorumundan Duygu Analizi API

    PROJENİN AMACI:
        Bu projede kullanıcıdan alınan bir film yorumunu analiz eden ve yorumun
        pozitif, negatif veya nötr olduğunu tahmin eden bir FastAPI servisi geliştireceğiz.

    PROJE AÇIKLAMASI:
        Gerçek dünyada duygu analizi projelerinde doğal dil işleme (NLP) ve makine öğrenmesi
        modelleri kullanılır. Bu mini projede ise sistemin genel çalışma mantığını anlamak için
        daha basit bir yaklaşım kullanacağız.

    Kullanıcı bir film yorumu gönderecek.
        Backend tarafında bu yorum içindeki bazı pozitif ve negatif kelimeler kontrol edilecek.
        Ardından sistem:
        - duygu etiketi
        - kısa açıklama
        - pozitif ve negatif skor
        şeklinde bir sonuç döndürecek.

    Bu yapı sayesinde:
        - FastAPI ile backend geliştirmeyi
        - POST endpoint kullanmayı
        - JSON veri alıp JSON veri döndürmeyi
        - basit metin işleme mantığını
        öğrenmiş olacağız.

    SENARYO:
        1. Kullanıcı Streamlit arayüzünden film yorumunu yazar.
        2. Bu yorum FastAPI endpoint'ine gönderilir.
        3. FastAPI yorumu analiz eder.
        4. Sonuç olarak pozitif / negatif / nötr etiketi döner.
        5. Açıklama ve skor bilgileri de eklenir.
        6. Streamlit tarafı bu sonucu kullanıcıya gösterir.

    PLAN / PROGRAM:
        1. Gerekli kütüphaneleri içeriye aktaracağız.
        2. FastAPI uygulamasını oluşturacağız.
        3. Veri modeli için Pydantic sınıfı yazacağız.
        4. Test endpoint'i oluşturacağız.
        5. Yorum analizi endpoint'i yazacağız.
        6. Pozitif ve negatif kelime listeleri tanımlayacağız.
        7. Yorumu analiz edip sonuç üreteceğiz.
        8. Sonucu JSON formatında döndüreceğiz.

    KURULUM:
        pip install fastapi uvicorn pydantic

    ÇALIŞTIRMA:
        uvicorn main:app --reload
"""