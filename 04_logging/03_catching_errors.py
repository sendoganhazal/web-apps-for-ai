"""
Amaç:
    - try except yapısını öğrenme
    - python ile hata yakalama mantığını öğrenme
    - sık görülen hata türlerini incele

Plan/program:
    1. gerekli örnek fonksiyonları hazırla
    2. try-except yapısını kullanma
    3. value error örneği inceleme
    4. type error
    5. zero division error
"""

# 1. Örnek Fonksiyonlar
def metni_sayiya_cevir(metin): # metni sayıya çeviren fonksiyon
    
    #  2. try-except yapısını kullanma
    try:
        sayi = int(metin) # metni sayıya çevirir
        print(sayi)
    except ValueError:
        print("HATA: Gonderilen deger sayiya cevrilemedi")

    
metni_sayiya_cevir("150") # 150
metni_sayiya_cevir("150s") # HATA: Gonderilen deger sayiya cevrilemedi
    
# 3. zero division error: iki sayıyı bölme örneği
def iki_sayiyi_bol(sayi1, sayi2):
    
    try:
        sonuc = sayi1 / sayi2
        print(sonuc)
    except ZeroDivisionError:
        print("HATA: bir sayi sifira bolunemez")

iki_sayiyi_bol(15,0) # HATA: bir sayi sifira bolunemez

#    4. type error
def topla(deger1, deger2):
    
    try:
        toplam = deger1 + deger2
        print(toplam)
    except TypeError:
        print("HATA: bu iki veri tipi birbiri ile toplanamaz")
    
topla(15,15) # 30
topla(15,"15") # HATA: bu iki veri tipi birbiri ile toplanamaz

#5. index error
def listeden_eleman_getir(liste,index):
  
    try: 
        eleman = liste[index]
        print(eleman)
    except Exception as e:
        print(f"HATA: {e}")
    
listeden_eleman_getir([1,2,3,4,5],0) # 1
listeden_eleman_getir([1,2,3,4,5],10) # HATA: list index out of range

# 6. finally
def dosya_okuma():
  
    try:
        dosya = open("olmayan_dosya_txt", "r",encoding="utf-8")
        icerik = dosya.read()
        print(icerik)
    except Exception as e:
        print(f"HATA:{e}")
    finally:
        print("dosya isleme sona erdi")
    
dosya_okuma()
"""
    HATA:[Errno 2] No such file or directory: 'olmayan_dosya_txt'
    dosya isleme sona erdi
"""
