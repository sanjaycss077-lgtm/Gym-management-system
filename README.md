# 🏋️ CollegeGym — Event Management System
### Final Year College Project | Flask + HTML/CSS/JS

---

## 📌 Features
- **Home Page** — Hero section, upcoming events, stats counter
- **Events Page** — Browse all events, filter by category, search by keyword
- **Event Detail Page** — Full event info + student registration form
- **Admin Panel** — Add new events, delete events, view all registrations

---

## 🚀 How to Run

### 1. Install Python (3.9 or above)
Download from https://www.python.org/downloads/

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

### 4. Open in browser
Visit: **http://127.0.0.1:5000**

---

## 📂 Project Structure
```
gym_system/
├── app.py                  ← Flask backend (routes & logic)
├── requirements.txt        ← Python dependencies
├── templates/
│   ├── base.html           ← Shared layout (navbar, footer)
│   ├── index.html          ← Home page
│   ├── events.html         ← Events listing with filters
│   ├── event_detail.html   ← Single event + registration form
│   └── admin.html          ← Admin panel
└── static/
    ├── css/style.css       ← All styles
    └── js/main.js          ← Frontend interactions
```

---

## 📖 Pages

| Route | Page |
|-------|------|
| `/` | Home — Hero + Upcoming Events |
| `/events` | All events with filter & search |
| `/events/<id>` | Event detail + Register |
| `/admin` | Admin — Add/Delete events, view registrations |

---

## 🛠 Tech Stack
- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, Vanilla JS
- **Fonts:** Bebas Neue, DM Sans, Space Mono (Google Fonts)
- **Data Storage:** In-memory (no database needed for demo)

---

## 📝 Notes
- Data resets on server restart (no database). For persistence, extend with SQLite/SQLAlchemy.
- To expand: Add login system, email confirmation, QR code for registrations.
- Tested on Python 3.10+

---

**Built as a Final Year College Project — Sports & Fitness Department**
