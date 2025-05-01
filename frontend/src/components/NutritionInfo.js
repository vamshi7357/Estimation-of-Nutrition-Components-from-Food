import React from "react";
import "./styles.css";

const NutritionInfo = ({ data, reset }) => {
  if (!data || !data.nutrition_data) {
    return <p>Loading nutrition data...</p>;
  }

  return (
    <div className="nutrition-container">
      <h2 className="nutrition-title">Nutrition Analysis</h2>

      {/* Display uploaded image */}
      {data.image_url && (
        <div className="image-container">
          <img src={data.image_url} alt="Uploaded Food" className="food-image" />
        </div>
      )}

      {/* Display cleaned and formatted description */}
      <p className="food-description">
        {data.nutrition_data.food_description || "No specific description available."}
      </p>

      {/* Display nutrition details in grid format */}
      <div className="nutrition-values">
        <div className="nutrition-item">
          <strong>Calories</strong>
          <p>{data.nutrition_data.Calories}</p>
        </div>
        <div className="nutrition-item">
          <strong>Protein</strong>
          <p>{data.nutrition_data.Protein}</p>
        </div>
        <div className="nutrition-item">
          <strong>Fats</strong>
          <p>{data.nutrition_data.Fats}</p>
        </div>
        <div className="nutrition-item">
          <strong>Carbohydrates</strong>
          <p>{data.nutrition_data.Carbohydrates}</p>
        </div>
        <div className="nutrition-item">
          <strong>Vitamins</strong>
          <p>{data.nutrition_data.Vitamins}</p>
        </div>
      </div>

      {/* Improved Reset Button (Centered) */}
      <div className="button-container">
        <button className="styled-btn" onClick={reset}>
          <i className="fas fa-sync-alt"></i> Analyze Another
        </button>
      </div>
    </div>
  );
};

export default NutritionInfo;
