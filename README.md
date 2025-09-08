#  Django Ticket System with Gemini AI

This is a simple **ticket management system** built with **Django**, where users can submit tickets and admins can manage them.  
It integrates with **Google Gemini API** to auto-generate helpful responses for support tickets.

---

## 🚀 Features
- User authentication (login, logout, register)
- Users can:
  - Submit tickets
  - View their own tickets
- Admins can:
  - View all tickets
  - Update ticket status
  - Edit / approve AI-generated responses
- AI Integration:
  - Auto-draft ticket responses using Gemini API
  - Minimal, polite replies (no greetings/signatures)

---

## 🛠️ Setup & Installation

### 1. Clone the repository
git clone https://github.com/rooo1/ai_support_sys.git
cd django-ticket-system

### 2. Create a virtual environment

python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Environment variables

Create a .env file in the project root:
GEMINI_API_KEY=your_api_key_here

### 5. Database setup

python manage.py migrate
python manage.py createsuperuser

### 6. Run the server
python manage.py runserver
