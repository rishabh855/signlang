import requests

url = "http://127.0.0.1:5000/predict"

file_path = r"C:\Users\Rishabh\Desktop\SignLang\datasets\ISL_Dataset\A\A (25).jpg"

with open(file_path, "rb") as f:
    files = {"image": f}
    response = requests.post(url, files=files)
    print(response.json())
