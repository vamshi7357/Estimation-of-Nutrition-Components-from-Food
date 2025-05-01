# Food Nutrition Analysis App

A full-stack web application that allows users to upload food images and receive detailed nutritional breakdowns using the Google Gemini AI API. This application helps users understand the nutritional content of their food easily and efficiently.

## Live Demo
- Frontend: Coming Soon
- Backend: Coming Soon

## Features

- Image Analysis
  - Upload food images for analysis
  - AI-powered food recognition using Google Gemini 1.5 Flash API
  - Detailed nutritional breakdown (calories, protein, fats, carbohydrates, vitamins)
  - Immediate analysis results

- User Interface
  - Responsive design for all devices
  - Modern UI with Tailwind CSS
  - Intuitive image upload system
  - Clear presentation of nutritional data

## Tech Stack

### Frontend
- React.js (Vite)
- Tailwind CSS for styling
- Fetch API for backend communication
- Component-based architecture

### Backend
- Flask (Python)
- Google Gemini 1.5 Flash API for image analysis
- MongoDB for storing results
- Flask-CORS for handling cross-origin requests

## Project Structure

```
food-nutrition-app/
│── frontend/               # React.js (Vite) frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── assets/         # Images and static files
│   │   ├── App.js          # Main app component
│   │   ├── index.js        # Entry point
│   ├── public/             # Static assets
│   ├── package.json        # Dependencies
│── backend/                # Flask backend
│   ├── app.py              # Main Flask API
│   ├── env/                # API Keys (Ignored in Git)
│   ├── uploads/            # Uploaded images (Git ignored)
│   ├── requirements.txt    # Python dependencies
│── .gitignore              # Ignore unnecessary files
│── README.md               # Project documentation
```

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/prabhaspaddana/food-nutrition-app.git
cd food-nutrition-app
```

2. Set up backend:
```bash
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
# OR
venv\Scripts\activate  # Activate (Windows)

pip install -r requirements.txt  # Install dependencies
```

3. Create a `.env` file in the backend directory:
```env
GEMINI_API_KEY=your_google_gemini_api_key
```

4. Set up frontend:
```bash
cd ../frontend
npm install
```

5. Start the development servers:

Backend:
```bash
cd backend
python app.py
```

Frontend:
```bash
cd frontend
npm run dev
```

## API Documentation

### Image Analysis Endpoints
- `POST /api/analyze` - Upload and analyze food image
- `GET /api/results/:id` - Get specific analysis result
- `GET /api/results` - Get user's analysis history

## Deployment

Deployment information will be updated when the application is live.

## Future Enhancements
- User authentication system
- Analysis history tracking
- Meal planning features
- Dietary restriction filtering
- Recipe suggestions based on analyzed foods
- Mobile application version

## Contributing
Want to improve the project? Feel free to contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to your fork: `git push origin feature-name`
5. Open a Pull Request

## License
This project is MIT Licensed – Free to use & modify!

## Contact
For any queries regarding the application, please contact:
- Email: vamshikrishnavadlakonda24@gmail.com
- GitHub: https://github.com/vamshi7357
