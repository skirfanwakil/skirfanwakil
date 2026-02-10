# 📍 Find Your Space - skirfanwakil from Team Sizzlers

### Budget-Friendly Hangout Finder (Hackathon MVP)

## Problem Statement
College students often want to hang out but struggle to find affordable cafes, restaurants, or entertainment options within their budget. At the same time, local businesses lack a simple platform to promote budget-friendly offers to students.

## Solution
Find Your Space is a lightweight web-based MVP that helps students discover nearby hangout places based on their budget and preferred category. Shopkeepers or users can submit offers through Google Forms, which automatically updates a Google Sheet used as the project database.

## Key Features
- Budget-based hangout search
- Category filtering (Cafe, Restaurant, Movie, Playstation)
- Real-time updates using Google Sheets
- Simple and accessible interface for students

## Tech Stack
- Backend: Python (Flask)
- Data Handling: Pandas
- Frontend: HTML, CSS
- Database: Google Sheets
- Data Collection: Google Forms

## How It Works
1. Offers are submitted through a Google Form.
2. Data is stored in a Google Sheet.
3. The Flask backend reads the Sheet as a CSV.
4. Students enter budget and category.
5. Matching hangouts are displayed instantly.

---
## MVP Scope
This project is a Minimum Viable Product built for hackathon submission. It focuses on solving a real student problem with a simple, practical, and scalable approach using Google technologies.

## Future Scope
- Location-based filtering
- Ratings and reviews
- Better UI and mobile support

## Hackathon Compliance
- Real-world problem
- Google Forms + Google Sheets integration
- Working MVP with screenshots and demo video

---

## 🚀 How to Run Locally
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python app.py`

----


## 📄 Project Resources & Links
* **Live Database:** [Google Sheets Backend](https://docs.google.com/spreadsheets/d/1xXJznjhzh0P2Q1CLieVPDBEW3z1Az0Xbmlr5HknBqis/edit?usp=sharing)
* **Data Entry Portal:** [Google Form for Vendors](https://forms.gle/LUzyVDzudVW8QhQN7)
* ## 📄 Project Documentation
View our detailed project methodology, market research, and architecture:
👉 **[Download/View Project PDF](https://github.com/user-attachments/files/24220647/find-your-space.pdf)**


* ## 📺 Project Demo Video
Click the play button below to see the project in action:

https://github.com/user-attachments/assets/7909cadf-2f02-4ed5-a00f-3ef836da6bdc

---

*Developed for Google Developer Group On Campus: TechSprint 2026*

---

## 📁 Project Structure
```text
find-your-space/
├── app.py              # Flask engine & Google Sheet API integration
├── requirements.txt    # Dependencies (Flask, Pandas)
├── templates/
│   └── index.html      # Responsive UI
└── README.md           # Documentation for Google Hackathon
