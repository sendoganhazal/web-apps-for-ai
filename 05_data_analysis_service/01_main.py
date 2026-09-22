"""
Veri Analiz Servisi Projesi

Proje tanıtımı:
    - bir csv dosyası okuyabilen
    - temel analizler yapabilen
    - sonuçları veritabanına kaydeden
    - geçmiş analiz kayıtlarını listeleyebilen
bir veri analiz servisi geliştirme.

Proje senaryosu:
    - kullanıcı csv dosyası yükler
    - sistem csv (veri) dosyası okur, temel analizler yapar ve sonuçları kaydeder
    - sonrasında kullanıcı geçmiş analizleri listeleyebilecek ve isterse tek bir analiz kaydının detayını görebilecek

Plan/Program:
    1. gerekli kütüphanelerin içeriye aktarılması
    2. logging altyapısının kurulması
    3. fastapi app oluşturma
    4. veritabanı altyapısı hazırlama
    5. veri analizi yapan yardımcı fonksiyonların ve db işlemleri yapan fonksiyonların tanımlanması
    6. csv yükleme endpointinin yazılması
    7. analiz geçmişi listeleyen endpoint yazılması
    8. tekil analizi listeleyen endpoint yazılması
    9. request ile client testi yapmak
    10. tüm sistem testi

Kurulumlar:
pip install fastapi uvicorn pandas requests python-multipart

"""

# 1. gerekli kütüphanelerin içeriye aktarılması
from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import sqlite3
import json
import logging
from datetime import datetime
from io import BytesIO

# 2. logging altyapısının kurulması
logging.basicConfig(
    filename = "analysis_service.log",
    level = logging.INFO,
    format = "%(levelname)s | %(asctime)s | %(message)s",
    encoding = "utf-8"
)

# 3. fastapi app oluşturma
app = FastAPI(title = "Veri Analiz Servisi Projesi")

# 4. veritabanı altyapısı hazırlama

def init_db():

    connection = sqlite3.connect("analysis_results.db")
    cursor = connection.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            row_count INTEGER NOT NULL,
            column_count INTEGER NOT NULL,
            column_names TEXT NOT NULL,
            numeric_column_count INTEGER NOT NULL,
            missing_values INTEGER NOT NULL,
            created_at TEXT NOT NULL
            ) 
        """
    )

    connection.commit()
    connection.close()

init_db()

# 5. veri analizi yapan yardımcı fonksiyonların ve db işlemleri yapan fonksiyonların tanımlanması
def analyze_csv_file(file_bytes: bytes, file_name: str) -> dict:

    try:
        # csv dosyasını pandas ile oku
        dataframe = pd.read_csv(BytesIO(file_bytes))

        # temel analiz bilgileri
        row_count = len(dataframe)
        column_count = len(dataframe.columns)
        column_names = list(dataframe.columns)
        numeric_column_count = len(dataframe.select_dtypes(include="number").columns)
        missing_value = int(dataframe.isnull().sum().sum())

        return {
            "file_name": file_name,
            "row_count": row_count,
            "column_count": column_count,
            "column_names": column_names,
            "numeric_column_count": numeric_column_count,
            "missing_values": missing_value,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        logging.error(f"CSV analiz edilirken bir hata oluştu: {e}")
        raise HTTPException(
            status_code = 400,
            detail = "CSV dsoyası okunamadı veya geçersiz içerik gönderildi."
        )

# analizi db ye kaydet
def save_analysis_result(analysis_data:dict) -> int:
    try:
        connection = sqlite3.connect("analysis_results.db")
        cursor = connection.cursor()

        cursor.execute(
            """
                INSERT INTO analysis_history (
                    file_name,
                    row_count,
                    column_count,
                    column_names,
                    numeric_column_count,
                    missing_values,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                analysis_data["file_name"],
                analysis_data["row_count"],
                analysis_data["column_count"],
                json.dumps(analysis_data["column_names"], ensure_ascii=False),
                analysis_data["numeric_column_count"],
                analysis_data["missing_values"],
                analysis_data["created_at"],
            )
        )

        connection.commit()
        analysis_id = cursor.lastrowid
        connection.close()

        return analysis_id
    except Exception as e:
        logging.error(f"Analiz sonucu veritabanına kaydedilirken bir hata oluştu: {e}")
        raise HTTPException(
            status_code = 500,
            detail = "Analiz sonucu veritabanına kaydedilemedi."
        )
    
# tüm analiz sonuçlarını db den al
def get_all_analysis_history():

    try:
        connection = sqlite3.connect("analysis_results.db")
        cursor = connection.cursor()

        cursor.execute(
            """
                SELECT id, file_name, row_count, column_count, created_at
                FROM analysis_history
                ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()
        connection.close()

        history = []
        for row in rows:
            history.append(
                {
                    "id": row[0],
                    "file_name": row[1],
                    "row_count": row[2],
                    "column_count": row[3],
                    "created_at": row[4],
                }
            )
        
        return history
    except Exception as error:
        logging.error(f"Analiz geçmişi okunurken hata oluştu: {error}")
        raise HTTPException(
            status_code = 500,
            detail = "Analiz geçmişi okunamadı."
        )

# 1 tane analiz sonucunu db den al
def get_analysis_by_id(analysis_id: int):
    try:
        connection = sqlite3.connect("analysis_results.db")
        cursor = connection.cursor()

        cursor.execute(
            """
                SELECT id, file_name, row_count, column_count, column_names,
                numeric_column_count, missing_values, created_at
                FROM analysis_history
                WHERE id = ?
            """,(analysis_id, )
        )

        row = cursor.fetchone()
        connection.close()

        if row is None:
            logging.error(f"analysis_id = {analysis_id} içn kayıt bulunamadı.")
            raise HTTPException(
                status_code = 404,
                detail = "istenen analiz kaydı bulunamadı"
            )

        return {
            "id": row[0],
            "file_name": row[1],
            "row_count": row[2],
            "column_count": row[3],
            "column_names": row[4],
            "numeric_column_count": row[5],
            "missing_values": row[6],
            "created_at": row[7]
        }
    except HTTPException:
        raise

    except Exception as e:
        logging.error(f"tekil analiz detay okurken hata oluştu: {e}")
        raise HTTPException(
            status_code = 500,
            detail = "analiz detayı okunamadı."
        )
    
# 6. csv yükleme endpointinin yazılması
# dosyayı alır, kontrol eder, veri analizini çalıştırır, sonucu veritabanına kaydeder
@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    logging.info(f"/upload-csv endpointi çağrıldı. file_name = {file.filename}")

    # dosya uzantısını kontrol etme
    if not file.filename.endswith(".csv"):
        logging.error("CSV olmayan dosya gönderildi.")
        raise HTTPException(
            status_code = 400,
            detail = "Lüften yalnızca .csv uzantılı dosya yükleyiniz."
        )
    
    try:
        # dosyanın içeriğini oku
        file_bytes = await file.read()

        # boş dosya kontrolü
        if not file_bytes:
            logging.error("boş dosya gönderildi.")
            raise HTTPException(
                status_code = 400,
                detail = "Yüklenen dosya boş olamaz."
            )
        
        # veri analizi yapalım
        analysis_result = analyze_csv_file(file_bytes, file.filename)

        # analiz sonucunu veri taabnına kaydet
        analysis_id = save_analysis_result(analysis_result)

        logging.info(f"analiz başarıyla tamamlandı. analysis_id= {analysis_id}")

        return{
            "message": "csv dosyası başarıyla analiz edildi ve db ye kaydedildi.",
            "analysis_id": analysis_id, 
            "analysis_result": analysis_result
        }
    except HTTPException:
        raise
    except Exception as error:
        logging.error(f"upload-csv endpointinde hata oluştu: {error}")
        raise HTTPException(
            status_code = 500,
            detail = "csv yükleme işleme sırasındahata oluştu."
        )

# 7. analiz geçmişi listeleyen endpoint yazılması
@app.get("/analysis-history")
async def list_analysis_history():

    logging.info("/analysis-history endpoint çağrıldı")

    history = get_all_analysis_history()

    logging.info(f"Toplam {len(history)} kayıt listelendi")
    return {
        "analysis_history": history
    }

# 8. tekil analizi listeleyen endpoint yazılması
@app.get("/analysis/{analysis_id}")
async def get_analysis_detail(analysis_id: int):

    logging.info(f"/analysis/{analysis_id} endpointi çağrıldı")

    analysis_detail = get_analysis_by_id(analysis_id)

    logging.info(f"analysis_id = {analysis_id} detayı başarıyla getirildi")
    return analysis_detail