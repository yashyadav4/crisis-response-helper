# Crisis Response Helper

A web app that provides AI-powered survival instructions during real-world emergencies.

## Features

- Choose emergency type (flood, earthquake, medical)
- Gets user geolocation
- Uses OpenAI to return survival tips
- Shows local emergency contacts from OpenStreetMap

## Deploy Instructions

### Backend (Render)
1. Push `server/` to GitHub.
2. Create a new web service on render.com.
3. Add your OPENAI_API_KEY to the environment variables.
4. Start command: python app.py

### Frontend (Vercel)
1. Push `client/` to GitHub.
2. Deploy to Vercel. It will auto-detect the static site.

## Local Run

### Backend:
```bash
cd server
pip install -r requirements.txt
python app.py
```

### Frontend:
Open client/index.html in your browser.
