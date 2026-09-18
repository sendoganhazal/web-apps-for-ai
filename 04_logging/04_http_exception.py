"""
    Amaç:
        - HTTPException
        - fastapi içinde hata döndürme
        - status code mantığını görme

    Plan/program:
        1. gerekli kütüphaneleri içeri aktar ve fastapi app oluştur
        2. get endpoint içinde hata kontrolü
        3. post endpoint içinde hata kontrolü

    Kurulum:
    pip install fastapi uvicorn
"""


# 1. gerekli kütüphaneleri içeri aktar ve fastapi app oluştur
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#fastapi nesnesi olştur
app = FastAPI()

# örnek veri listesi
products = [
    {"id": 1, "name": "laptop", "price": 2500},
    {"id": 2, "name": "mouse", "price": 500}
]

#post için veri modeli oluştur
class ProductModel(BaseModel):
    id: int
    name: str
    price: float

# 2. get endpoint içinde hata kontrolü

#belirli bir ürünü getiren get endpointi
@app.get("/products/{product_id}")
async def get_product(product_id:int):
    
    for product in products:
        if product["id"] == product_id: #ürün varsa
            return product
        
    #ürün yoksa hata return edelim
    raise HTTPException(status_code=404, detail="urun bulunamadi")

# 3. post endpoint içinde hata kontrolü

#yeni ürün ekleme
@app.post("/products")
async def create_product(product: ProductModel):
    
    #aynı id var mı?
    for item in products:
        if item["id"] == product.id:
            raise HTTPException(status_code=400, detail="bu id zaten kayitli")
        
    #fiyat kontrolü
    if product.price < 0:
        raise HTTPException(status_code=400, detail="fiyat sifirdan buyuk olmali")
    
    # yeni ürün ekleme
    new_product = {
        "id": product.id,
        "name": product.name,
        "price": product.price
    }
    
    return {
        "mesaj": "urun basariyla eklendi",
        "product":new_product
    }