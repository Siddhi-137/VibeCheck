# 🎵 VibeCheck

## OVERVIEW

VibeCheck is a mood-based music recommendation web application that analyzes a user's text input to detect its underlying emotion using a Hugging Face Transformer model. Based on the detected emotion, the application recommends five matching songs using the Last.fm API and displays them with album artwork, confidence score, and direct links to their Last.fm pages. The project features a Flask backend, a React frontend, and is deployed online using Render and Vercel.

---

## TECH STACK

- **Backend:** Python, Flask, Flask-CORS, Hugging Face Transformers, PyTorch, Last.fm API, pylast
- **Frontend:** React, Vite, CSS
- **Deployment:** Render (Backend), Vercel (Frontend)

---

## SETUP INSTRUCTIONS

### Clone the repository

```bash
git clone https://github.com/Siddhi-137/VibeCheck.git
cd VibeCheck
```

### Backend

```bash
cd backend
pip install -r requirements.txt
```

Create the following environment variables:

```text
LASTFM_API_KEY
LASTFM_API_SECRET
```

Run the Flask server:

```bash
python app.py
```

### Frontend

Open a new terminal and run:

```bash
cd frontend
npm install
npm run dev
```

The application will be available at:

```
http://localhost:5173
```

---

## LIVE DEMO

🌐 https://vibecheckfrontend.vercel.app/
