# 📍 Find Your Space
### *Budget-Friendly Hangout Finder for Students* 🚀

## 📌 Problem Statement
College students often struggle to find affordable hangout places that fit their budget. At the same time, local cafes, restaurants, and entertainment spots lack a simple platform to showcase budget-friendly offers to students.

## 💡 Solution
**Find Your Space** is a simple web-based MVP that helps students discover nearby hangout spots based on their budget and preferred category.

* **Local shopkeepers** can submit their offers through a Google Form, which automatically updates a Google Sheet used as the project database.
* **Students** enter their budget and hangout type, and the system instantly shows matching places.

---

## 👥 Target Users
* **College students**
* **Local businesses:** Cafes, restaurants, movie places, and gaming zones

---

## ⚙️ Features
* **Budget-based filtering** of hangout spots.
* **Category selection** (Cafe, Restaurant, Movie, Playstation).
* **Real-time data updates** using Google Sheets.
* **Separate flow** for data entry (Google Form) and data viewing (Web App).

---

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Data Handling:** Pandas
* **Database:** Google Sheets
* **Google Tools Used:** Google Forms, Google Sheets

---

## 🔄 How It Works
1. **Submit:** Shopkeepers submit hangout details through a Google Form.
2. **Store:** Data is stored automatically in a Google Sheet.
3. **Search:** Students enter their budget and preferred category on the website.
4. **Process:** Flask backend reads the Google Sheet as CSV using Pandas.
5. **Display:** Matching hangout spots are displayed to the user.

---

## 📁 Project Structure
```text
find-your-space/
├── app.py              # Flask backend and filtering logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
└── README.md           # Project documentation
