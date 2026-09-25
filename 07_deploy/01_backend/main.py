"""FastAPI backend uygulaması ve öğrenme yol haritası uç noktaları."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

ROADMAPS = {
    "yapay_zeka": [
        "Python Temelleri",
        "Veri Analizi",
        "Makine Öğrenmesi",
        "Model Değerlendirme",
        "Mini Projeler"
    ],
    "derin_ogrenme": [
        "Python ve NumPy",
        "Yapay Sinir Ağları",
        "CNN",
        "RNN ve LSTM",
        "Derin Öğrenme Projeleri"
    ],
    "nlp": [
        "Metin Ön İşleme",
        "Word Embedding",
        "RNN ve LSTM ile NLP",
        "Transformer",
        "RAG ve Chatbot Projeleri"
    ]
}

class RoadmapRequest(BaseModel):
    alan: str

@app.get("/")
def home():
    return {"message": "Backend çalışıyor"}

@app.post("/roadmap")
def get_roadmap(data: RoadmapRequest):

    secim = data.alan.lower()

    if secim not in ROADMAPS:
        return {
            "error": "geçersiz seçim"
        }
    return{
        "alan": secim,
        "adimlar": ROADMAPS[secim]
    }