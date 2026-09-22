#  9. request ile client testi yapmak
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_upload_csv(file_path:str):
    
    try:
        with open(file_path, "rb") as csv_file:
            files = {
                "file":(file_path, csv_file, "text/csv")
            }
            response = requests.post(f"{BASE_URL}/upload-csv", files=files)
        
        print(f"upload response: \n {response.json()}")
    
    except Exception as e:
        print(f"Hata: {e}")
        
def test_analysis_history():
    
    try:
        response = requests.get(f"{BASE_URL}/analysis-history")
        print(f"analysis history: \n {response.json()}")
    
    except Exception as e:
        print(f"Hata: {e}")

def test_analysis_detail(analysis_id:int):
    
    try:
        response = requests.get(f"{BASE_URL}/analysis/{analysis_id}")
        print(f"analysis detail: \n {response.json()}")
    
    except Exception as e:
        print(f"Hata: {e}")
        
# 10. tüm sistemi test et

test_upload_csv("sample_data.csv")
print("***")
test_analysis_history()
print("***")
test_analysis_detail(1)