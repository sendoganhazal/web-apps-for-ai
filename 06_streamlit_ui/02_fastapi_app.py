"""
streamlit
"""
import streamlit as st
import requests
from PIL import Image

# sayfa ayarları
st.set_page_config(
    page_title = "Hastalık tespit arayüzü",
    page_icon = "./stethoscope.png",
    layout = "centered"
)

# başlık ve açıklamalar
st.title("Görüntüden Hastalık Tespiti")
st.write("Görüntü yükle ve hastalık teşhisi sonucunu gör")
st.markdown("---")

# dosya yükleme
uploaded_file = st.file_uploader(
    "Bir görüntü yükleyin",
    type = ["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption = "yüklenen görüntü", use_container_width = True)

    # tahmin butonu
    if st.button("Tahmin Yap"):
        try:
            uploaded_file.seek(0) #dosya pointerini başa al

            api_url = "http://127.0.0.1:8000/predict"

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }

            response = requests.post(api_url, files=files)

            if response.status_code == 200:
                
                result = response.json()

                st.success("Tahmin işlemi başarılı")
                st.subheader("Tahmin sonucu:")
                st.write(f"Tahmin: {result["prediction"]}")
                st.write(f"Olasılık: {result["probability"]}")

                if result["prediction"] == "Hastalık Var":
                    st.error("Hastalık var")
                else:
                    st.success("Hastalık yok")
            else:
                st.error("API tarafında bir hata oluştu")
        except Exception as e:
            st.error(e)
else:
    st.info("Lütfen önce bir görüntü yükleyin")