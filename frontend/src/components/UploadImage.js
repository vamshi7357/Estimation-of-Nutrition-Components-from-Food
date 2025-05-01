import React, { useState } from "react";
import "./styles.css"; // CSS file for styling

function UploadImage({ setNutritionData }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [uploadedImageUrl, setUploadedImageUrl] = useState(null);

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      setSelectedFile(file);
      setPreview(URL.createObjectURL(file)); // Create preview URL
    }
  };

  // Handle file upload
  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select an image.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("Response from backend:", data); // Debugging

      if (data.image_url) {
        setUploadedImageUrl(data.image_url); // Save uploaded image URL
      }

      setNutritionData(data);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div className="upload-container">
      {/* Custom File Upload Button */}
      <label className="custom-file-upload">
        <input type="file" onChange={handleFileChange} />
        <i className="fas fa-upload"></i> Choose File
      </label>

      {/* Show preview before uploading */}
      {preview && <img src={preview} alt="Preview" className="preview-image" />}

      {/* Upload & Analyze Button */}
      <button className="analyze-btn" onClick={handleUpload}>
        <i className="fas fa-search"></i> Upload & Analyze
      </button>

      {/* Show uploaded image returned from backend */}
      {uploadedImageUrl && (
        <div>
          <h3>Uploaded Image:</h3>
          <img src={uploadedImageUrl} alt="Uploaded" className="uploaded-image" />
        </div>
      )}
    </div>
  );
}

export default UploadImage;
