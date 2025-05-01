import requests

url = "http://127.0.0.1:5000/upload"
file_path = "C:/Users/praba/Downloads/classiccheeselasagna.jpeg"  # Change this to an actual image path

files = {"file": open(file_path, "rb")}
response = requests.post(url, files=files)

print(response.json())  # Should print the nutrition data
