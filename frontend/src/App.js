import React, { useState } from "react";
import UploadImage from "./components/UploadImage";
import NutritionInfo from "./components/NutritionInfo";
import "./components/styles.css";

function App() {
  const [nutritionData, setNutritionData] = useState(null);

  return (
    <div className="app-container">
      <h1>Food Nutrition Analyzer</h1>
      {!nutritionData ? (
        <UploadImage setNutritionData={setNutritionData} />
      ) : (
        <NutritionInfo data={nutritionData} reset={() => setNutritionData(null)} />
      )}
    </div>
  );
}

export default App;
