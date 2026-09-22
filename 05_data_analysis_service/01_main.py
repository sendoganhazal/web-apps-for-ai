"""
    Veri Analiz Servisi Projesi

    Proje tanıtımı:
        - bir csv dosyası okuyabilen
        - temel analizler yapabilen
        - sonuçları veritabanına kaydeden
        - geçmiş analiz kayıtlarını listeleyebilen bir veri analiz servisi geliştirme.

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
    filename="analysis_service.log",
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(message)s"
)

# 3. fastapi app oluşturma
app = FastAPI()

# 4. veritabanı altyapısı hazırlama
def init_db():
    connection = sqlite3.connect("analysis_results.db")
    cursor = connection.cursor()
    
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS analysis_history(
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

#analiz yap
def analyse_csv_file(file_bytes: bytes, file_name: str) -> dict:
    try:
        #csv dosyasını pandas ile oku
        dataframe = pd.read_csv(BytesIO(file_bytes))
        
        # temel analiz bilgileri
        row_count = len(dataframe)
        column_count = len(dataframe.columns)
        column_names = dataframe.columns
        numeric_column_count = len(dataframe.select_dtypes(include="number").columns)
        missing_value = len(dataframe.isnull().sum().sum())
        
        return {
            "file_name": file_name,
            "row_count": row_count,
            "column_count":  column_count,
            "column_names": column_names,
            "numeric_column_count":numeric_column_count,
            "missing_value": missing_value,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
       logging.error(f"CSV analiz edilirken bir hata oluştu: {e}")
       raise HTTPException(
           status_code= 400,
           detail="CSV dosyası okunamadı veya geçersiz içerik gönderildi"
       )
     
# analizi dbye kaydet  
def save_analysis_result(analysis_data: dict) -> int:
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
                    missing_value,
                    created_at
                )
                VALUES (?,?,?,?,?,?,?)
            """,(
                analysis_data["file_name"],
                analysis_data["row_count"],
                analysis_data["column_count"],
                json.dumps(analysis_data["column_names"], ensure_ascii=False),
                analysis_data["numeric_column_count"],
                analysis_data["missing_value"],
                analysis_data["created_at"],
            )
        )
        
        connection.commit()
        analysis_id = cursor.lastrowid
        connection.close()
        
        return analysis_id
    
    except Exception as e:
        logging.error(f"Analiz sonucu veritabanına kaydedilirken bir hata oluştu")
        raise HTTPException(
            status_code=500,
            detail="Analiz sonucu veritabanına kaydedilemedi"
        )

# tüm analiz sonuçlarını db den al
def get_all_analysis_history():
    
    try:
        connection = sqlite3.connect("analysis_result.db")
        cursor = connection.cursor()
        
        cursor.execute(
            """
                SELECT id, file_name, row_count, column_count, column_names, numeric_column_count,  missing_value, created_at, 
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
                    "column_names": row[4],
                    "numeric_column_count": row[5],
                    "created_at": row[6],
                }
            )
        
        return history
        
    except Exception as e:
        logging.error(f"Analiz geçmişi okunurken hata oluştu:{e}")
        raise HTTPException(
            status_code=500,
            detail="Analiz geçmişi okunamadı"
        )

# 1 tane analiz sonucunu db den al
def get_analysis_by_id(analysis_id:int):
    
    try:
        connection = sqlite3.connect("analysis_result.db")
        cursor = connection.cursor()
        
        cursor.execute(
            """
                SELECT id, file_name, row_count, column_count, column_names, numeric_column_count,  missing_value, created_at, 
                FROM analysis_history
                WHERE id = ?
            """, (analysis_id,)
        )
        
        row = cursor.fetchone()
        connection.close()
        
        if row is None:
            logging.error(f"analysis_id={analysis_id} için kayıt bulunamadı")
            raise HTTPException(
                status_code=404,
                detail="İstenen analiz kaydı bulunamadı"
            )
        

        
        return {
            "id": row[0],
            "file_name": row[1],
            "row_count": row[2],
            "column_count": row[3],
            "column_names": row[4],
            "numeric_column_count": row[5],
            "created_at": row[6],
        }
        
    except HTTPException:
        raise
    
    except Exception as e:
        logging.error(f"Tekil analiz detayı okunurken hata oluştu:{e}")
        raise HTTPException(
                status_code=500,
                detail="Analiz geçmişi okunamadı"
            )

# 6. csv yükleme endpointinin yazılması

# 7. analiz geçmişi listeleyen endpoint yazılması


# 8. tekil analizi listeleyen endpoint yazılması


# 9. request ile client testi yapmak
# 10. tüm sistem testi
