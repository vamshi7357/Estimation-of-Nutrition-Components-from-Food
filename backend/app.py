import os
import re
import requests
import base64
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Get the API key from the .env file

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Food Nutrition API is Running!"})

@app.route('/uploads/<filename>')
def serve_uploaded_image(filename):
    """Serves the uploaded image for frontend display."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/upload", methods=["POST"])
def upload_image():
    """Handles image upload and sends it to Gemini 1.5 Flash API."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "" or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file format"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Get nutrition data from Gemini API
    nutrition_data = get_nutrition_from_image(filepath)

    # Extract and format the nutrition details
    formatted_data = extract_nutrition_info(nutrition_data)

    # Include the image URL in response
    image_url = f"http://localhost:5000/uploads/{filename}"  # Adjust for deployment

    return jsonify({"image_url": image_url, "nutrition_data": formatted_data})

def get_nutrition_from_image(image_path):
    """Uses Gemini 1.5 Flash API to extract nutrition data from a food image."""
    API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    
    # Convert image to base64
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": "Identify this food item and provide its nutritional values (calories, protein, fats, carbs, vitamins, etc.)."},
                    {"inlineData": {"mimeType": "image/jpeg", "data": image_base64}}
                ]
            }
        ]
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, params=params)
        response_data = response.json()
        
        if response.status_code == 200:
            return response_data  # API successfully returned data
        
        return {"error": "API response not recognized", "details": response_data}
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

def extract_nutrition_info(nutrition_data):
    """Extracts relevant nutrition details including the full cleaned food description."""
    if "candidates" in nutrition_data and len(nutrition_data["candidates"]) > 0:
        raw_text = nutrition_data["candidates"][0]["content"]["parts"][0]["text"]

        # Clean the description text
        cleaned_description = clean_description(raw_text)

        # Extract nutrition values
        extracted_values = {
            "food_description": cleaned_description,  # Store cleaned text
            "Calories": extract_value(raw_text, "Calories"),
            "Protein": extract_value(raw_text, "Protein"),
            "Fats": extract_value(raw_text, "Fat"),
            "Carbohydrates": extract_value(raw_text, "Carbohydrates"),
            "Vitamins": extract_vitamins(raw_text)
        }

        return extracted_values

    return {"error": "No nutritional data found."}

def extract_value(text, keyword):
    """Extracts numeric values from the text based on a keyword."""
    pattern = rf"{keyword}.*?(\d+\.?\d*)"
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1) + "g" if match else "N/A"

def extract_vitamins(text):
    """Extracts vitamin details from the text."""
    vitamins = re.findall(r"Vitamin\s([A-Z]+).*?(\d+mg|\d+mcg|\d+%)", text, re.IGNORECASE)
    return ", ".join([f"{v[0]}: {v[1]}" for v in vitamins]) if vitamins else "N/A"

def clean_description(text):
    """Cleans and formats the food description by removing unnecessary characters."""
    text = text.replace("*", "")  # Remove asterisks
    text = text.replace("\n", " ")  # Replace new lines with spaces
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.strip()

if __name__ == "__main__":
    app.run(debug=True)
