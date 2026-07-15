"""
Amaç:
    - Bu derste async ve await temel yapısını öğrenme
        - async: asenkron çalışan fonksiyonu tanımlar
        - await: beklenmesi gereken işlemi ifade eder

Plan/Program:
    1. asenkron fonksiyon tanımla
    2. await ile bekleme mantığı
    3. birden fazla asenkron görevi birlikte çalıştır.

Kurulumlar:
pip install asyncio    
"""

import asyncio

# asenkron fonksiyon tanımla
async def gorev1() :
    print("Görev 1 başladı")
    
    # burada bir makine öğrenmesi modeli olsun
    # bu model 2 saniyede çalışıyor olsun
    await asyncio.sleep(2) # 2 saniye bekler
    
    print("Görev 1 tamamlandı")
    
async def gorev2() :
    print("Görev 2 başladı")
    
    # burada bir makine öğrenmesi modeli olsun
    # bu model 1 saniyede çalışıyor olsun
    await asyncio.sleep(1) # 1 saniye bekler
    
    print("Görev 2 tamamlandı")
    
# birden fazla asenkron görevi birlikte çalıştır

async def main() :
    # gather : birden fazla asenkron görevi aynı anda çalıştırır
    await asyncio.gather(gorev1(),gorev2())
    
# main fonksiyonu çalıştırma
asyncio.run(main())