#hangi temel imajı kullanacağımızı seçelim 
FROM python:3.11-slim

# container içinde çalışma klasörünü belirle
WORKDIR /app

# requierement.txt kurulsun diye
COPY requirements.txt .

#gerekli python kütüphanelerinin kurulumunu yao
RUN pip install --no-cache-dir -r requirements.txt

# projedeki diğer dosyaları container içine kopyalıyoruz
COPY . . 

# Container ayayağa kalkınca hangi komut çalışsın diye onu söylüyoruz
# fastapi uvicorn ile 8000 portunda çalışsın
# hostun "0.0.0.0" olmasının sebebi dışarıdan erişilmesini istemememiz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
