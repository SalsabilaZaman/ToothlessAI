# 🤖 Toothless – A friendly ChatBot

AI Friend is a friendly web-based chatbot that:
- Listens to your rants 😤
- Detects your mood/emotion 🧠
- Gives you funny advice or makes you laugh 😂
- Acts like a true digital buddy 🧡



# 🏗️ Project Structure

├── frontend/ # Frontend (HTML/CSS/JS or React)
├── backend/ # FastAPI backend with emotion detection
├── .gitignore
└── README.md



# 🚀 How to Run

### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

