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

# 1. asenkron fonksiyon tanımla
# async def: bu fonk.un asenkron çalışacağını ifade eder
async def gorev_1():
    print("Görev1 başladı")
    
    # burada sanki bir ml modeli varmış gibi 2 sn bekletiyoruz
    await asyncio.sleep(2) # 2. await ile bekleme mantığı
    
    print("Görev1 bitti")
    
async def gorev_2():
    print("Görev2 başladı")
    
    # burada sanki bir ml modeli varmış gibi 1 sn bekletiyoruz
    await asyncio.sleep(1) # 2. await ile bekleme mantığı
    
    print("Görev2 bitti")

# 3. birden fazla asenkron görevi birlikte çalıştır.
async def main():
    # asyncio.gather: birden fazla asenkron görevi birlikte çalıştırır.
    await asyncio.gather(
        gorev_1(),
        gorev_2()
    )

# Programı çalıştır.
asyncio.run(main())