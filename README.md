<div align="center">

# 💊 MediNomix | LASA Drugs Error Prevention System
> **Professional Drug Confusion Risk Analysis for Healthcare Safety**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Course](https://img.shields.io/badge/Course-Advance%20Database%20Systems-FF5722?style=flat-square)]()

</div>

---

MediNomix is a professional medication safety web application developed as a **course project for Advance Database Systems**. It analyzes drug names for potential confusion risks using advanced algorithms, helping healthcare professionals prevent medication errors and improve patient safety. Built with **FastAPI** backend and **Streamlit** frontend with **PostgreSQL** database, the system identifies Look-Alike Sound-Alike (LASA) drug pairs that could lead to dangerous medication errors.

---

## Table of Contents
- [About the App](#about-the-app)
- [Course Context](#course-context)
- [Key Features](#key-features)
- [Use Case](#use-case)
- [Technology Stack](#technology-stack)
- [Database Design](#database-design)
- [Installation Guide](#installation-guide)
- [App Flow](#app-flow)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Security & Environment](#security--environment)
- [Future Improvements](#future-improvements)
- [Developed By](#developed-by)

---

## About the App

MediNomix addresses the critical problem of medication errors caused by Look-Alike Sound-Alike (LASA) drug names.

| Aspect | Description |
|:-------|:------------|
| **What it is** | A professional drug confusion risk analysis system that identifies potentially dangerous drug name similarities |
| **Who can use it** | Healthcare professionals, pharmacists, hospital administrators, and medication safety officers |
| **Problem it solves** | LASA drug errors cause thousands of adverse drug events annually. Healthcare workers need rapid risk assessment tools to prevent confusion between similar drug names. |
| **Main features** | Drug name search with confusion risk analysis, multiple similarity algorithms, real-time risk scoring, interactive analytics dashboard, and PostgreSQL database with 6 tables |

---

## Course Context

This project was developed to fulfill the **requirements of the Advance Database Systems course** in the **6th Semester of BS Computer Science**.

| Course Component | Implementation in This Project |
|:----------------|:-------------------------------|
| **Database Design** | PostgreSQL with 6 normalized tables (drugs, confusion_risks, analysis_logs, known_risky_pairs, system_metrics, alembic_version) |
| **Complex Queries** | Risk analysis queries joining multiple tables with similarity scoring |
| **Data Integration** | OpenFDA API integration for drug data ingestion |
| **Database Indexing** | Optimized indexes on drug names, risk scores, and foreign keys |
| **Transaction Management** | ACID compliance for risk analysis and logging operations |
| **Performance Optimization** | Cached analysis results, efficient join strategies |

> This project demonstrates practical application of advanced database concepts including complex schema design, API data integration, query optimization, and real-time analytics.

---

## Key Features

### Core Analysis
- Drug name search and confusion risk analysis
- Multiple similarity algorithms (Levenshtein, Jaro-Winkler, Fuzzy matching)
- Phonetic matching (Soundex, Metaphone, NYSIIS)
- Therapeutic context analysis
- Real-time risk scoring (0-100%)

### Analytics Dashboard
- Risk breakdown donut chart (Critical/High/Medium/Low)
- Top 10 high-risk drug pairs bar chart
- Drug confusion risk heatmap matrix
- Interactive Plotly visualizations

### Real-Time Monitoring
- Auto-refreshing dashboard every 10 seconds
- Live metrics (total drugs, critical pairs, high risk pairs, avg risk score)
- Recent search activity feed
- System health status monitoring

### Database Features
- PostgreSQL database with 6 tables
- OpenFDA API integration for drug data
- Automatic drug risk analysis against all existing drugs
- Known risky pairs seeding (ISMP/FDA sources)

### Modern UI/UX
- Glass morphism design with purple/pink gradient theme
- Custom animated tabs and buttons
- Responsive layout for all screen sizes
- Medical imagery integration

---

## Use Case

A healthcare professional can:

1. Search any medication name (brand or generic)
2. View all similar drugs with confusion risk scores
3. Filter risks by category (Critical/High/Medium/Low)
4. Analyze risk distribution via interactive charts
5. Monitor real-time system metrics and activity
6. Identify critical drug pairs requiring attention

---

## Technology Stack

### Backend

| Technology | Badge |
|:-----------|:------|
| **Language:** Python 3.9+ | [![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) |
| **Framework:** FastAPI | [![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) |
| **Database:** PostgreSQL 14+ | [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/) |
| **ORM:** SQLAlchemy | [![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-FF6F00?style=flat-square)](https://www.sqlalchemy.org/) |
| **ASGI Server:** Uvicorn | [![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-3E7E9E?style=flat-square)](https://www.uvicorn.org/) |

### Frontend

| Technology | Badge |
|:-----------|:------|
| **Framework:** Streamlit | [![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/) |
| **Charts:** Plotly | [![Plotly](https://img.shields.io/badge/Charts-Plotly-00BFFF?style=flat-square)](https://plotly.com/) |
| **Styling:** Custom CSS | [![CSS](https://img.shields.io/badge/Styling-Custom-2962FF?style=flat-square)](https://developer.mozilla.org/en-US/docs/Web/CSS) |

### Data Processing

| Technology | Badge |
|:-----------|:------|
| **Data Manipulation:** Pandas | [![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/) |
| **Phonetic Algorithms:** Jellyfish | [![Jellyfish](https://img.shields.io/badge/Phonetic-Jellyfish-43A047?style=flat-square)](https://github.com/jamesturk/jellyfish) |
| **String Matching:** FuzzyWuzzy | [![FuzzyWuzzy](https://img.shields.io/badge/Matching-FuzzyWuzzy-FF8C00?style=flat-square)](https://github.com/seatgeek/fuzzywuzzy) |
| **Distance Calculation:** python-Levenshtein | [![Levenshtein](https://img.shields.io/badge/Distance-Levenshtein-FF6F00?style=flat-square)](https://github.com/maxbachmann/python-Levenshtein) |

### APIs

| Technology | Badge |
|:-----------|:------|
| **Drug Data:** OpenFDA Drug Label API | [![OpenFDA](https://img.shields.io/badge/API-OpenFDA-005EB8?style=flat-square)](https://open.fda.gov/) |

---

## Database Design

### drugs Table

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Unique identifier |
| openfda_id | VARCHAR | OpenFDA unique ID |
| brand_name | VARCHAR | Brand/trade name |
| generic_name | VARCHAR | Generic name |
| manufacturer | VARCHAR | Manufacturer name |
| substance_name | VARCHAR | Active substance |
| product_type | VARCHAR | Type of product |
| route | VARCHAR | Administration route |
| active_ingredients | TEXT | Active ingredients list |
| purpose | TEXT | Drug purpose |
| warnings | TEXT | Safety warnings |
| indications_and_usage | TEXT | Usage information |
| dosage_form | VARCHAR | Form of medication |
| drug_class | VARCHAR | Therapeutic class |
| therapeutic_category | VARCHAR | Treatment category |
| side_effects | TEXT | Known side effects |
| contraindications | TEXT | Contraindications |
| soundex_code | VARCHAR | Soundex phonetic code |
| metaphone_code | VARCHAR | Metaphone phonetic code |
| created_at | TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | Last update time |

### confusion_risks Table

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Unique identifier |
| source_drug_id | INTEGER FK | Source drug reference |
| target_drug_id | INTEGER FK | Target drug reference |
| spelling_similarity | FLOAT | Spelling match score |
| phonetic_similarity | FLOAT | Phonetic match score |
| therapeutic_context_risk | FLOAT | Therapeutic risk score |
| levenshtein_similarity | FLOAT | Levenshtein distance score |
| soundex_match | BOOLEAN | Soundex match flag |
| metaphone_match | BOOLEAN | Metaphone match flag |
| is_known_risky_pair | BOOLEAN | Known FDA/ISMP pair |
| same_drug_class | BOOLEAN | Same class flag |
| same_therapeutic_category | BOOLEAN | Same category flag |
| combined_risk | FLOAT | Final risk score (0-100) |
| risk_category | VARCHAR | Critical/High/Medium/Low |
| risk_reason | TEXT | Explanation of risk |
| algorithm_version | VARCHAR | Version identifier |
| last_analyzed | TIMESTAMP | Last analysis time |

### analysis_logs Table

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Unique identifier |
| drug_name | VARCHAR | Searched drug name |
| timestamp | TIMESTAMP | Search timestamp |
| similar_drugs_found | INTEGER | Count of similar drugs |
| highest_risk_score | FLOAT | Maximum risk found |
| critical_risks_found | INTEGER | Count of critical risks |
| analysis_duration | FLOAT | Processing time in seconds |
| user_feedback | VARCHAR | Optional user feedback |

### known_risky_pairs Table

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Unique identifier |
| drug1_name | VARCHAR | First drug name |
| drug2_name | VARCHAR | Second drug name |
| risk_level | VARCHAR | Risk category |
| reason | TEXT | Why they are confused |
| source | VARCHAR | Information source |
| reported_incidents | INTEGER | Number of incidents |
| last_reported | TIMESTAMP | Last incident date |
| created_at | TIMESTAMP | Record creation time |
| updated_at | TIMESTAMP | Last update time |

### system_metrics Table

| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL PRIMARY KEY | Unique identifier |
| metric_name | VARCHAR | Metric identifier |
| metric_value | FLOAT | Current value |
| timestamp | TIMESTAMP | Measurement time |

---

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 14 or higher
- Git

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medinomix.git
cd medinomix
```

2. Install backend dependencies:
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pandas numpy requests aiohttp jellyfish fuzzywuzzy python-Levenshtein
```

3. Create PostgreSQL database:
```sql
CREATE DATABASE confusionguard;
```

4. Update database credentials in backend code:
```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/confusionguard"
```

5. Start backend server:
```bash
python backend.py
```

### Frontend Setup

1. Install frontend dependencies:
```bash
pip install streamlit plotly pandas requests pillow
```

2. Place logo image as `m11.jpg` in project root

3. Start frontend:
```bash
streamlit run app.py
```

### Database Seeding

After starting backend, seed with example drugs:
```bash
curl -X POST http://localhost:8000/api/seed-database
```

---

## App Flow

1. **Backend Server** starts on port 8000
2. **Frontend App** connects to backend API
3. **User Interface** displays 4 tabs:
   - **Home**: Hero section, statistics, features, user guide, medical images
   - **Drug Analysis**: Search medications, view risk results, filter by category
   - **Analytics**: Risk breakdown chart, top risks chart, confusion heatmap
   - **Real-Time**: Auto-refreshing metrics, recent activity, system status
4. **Search Process**:
   - User enters drug name
   - Backend checks database cache
   - If not found, fetches from OpenFDA
   - Analyzes against all existing drugs
   - Returns similar drugs with risk scores
5. **Results** display risk percentage, category, and similarity metrics

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/health` | GET | Health check |
| `/api/search/{drug_name}` | GET | Drug analysis |
| `/api/metrics` | GET | Dashboard metrics |
| `/api/top-risks` | GET | Top risk pairs |
| `/api/risk-breakdown` | GET | Risk distribution |
| `/api/heatmap` | GET | Heatmap data |
| `/api/realtime-events` | GET | Recent activity |
| `/api/seed-database` | POST | Seed example drugs |
| `/api/drugs` | GET | List all drugs |

---

## Project Structure

```
MediNomix/
│
├── backend.py                           # FastAPI server with all endpoints
├── app.py                               # Streamlit frontend application
│
├── requirements.txt                     # Python dependencies
├── m11.jpg                              # Logo image for frontend
│
├── database/
│   ├── models.py                        # SQLAlchemy database models
│   ├── database.py                      # Database connection setup
│   └── init_db.py                       # Database initialization script
│
├── algorithms/
│   ├── similarity.py                    # Levenshtein, Jaro-Winkler algorithms
│   ├── phonetic.py                      # Soundex, Metaphone, NYSIIS
│   └── risk_calculator.py               # Combined risk scoring logic
│
├── api/
│   ├── openfda_client.py                # OpenFDA API integration
│   └── drug_processor.py                # Drug data processing
│
├── analytics/
│   ├── metrics.py                       # System metrics calculation
│   └── heatmap_generator.py             # Confusion matrix generation
│
└── migrations/
    └── versions/                        # Alembic database migrations
```

---

## Security & Environment

### Current State
- Backend runs on localhost:8000
- Frontend runs on localhost:8501
- Database runs on localhost:5432
- CORS enabled for all origins

### Recommended Improvements
- Add authentication system
- Move database credentials to environment variables
- Implement rate limiting
- Add HTTPS for production deployment
- Use environment-specific configurations

---

## Future Improvements

- User authentication and roles
- Export reports (PDF/CSV)
- Email alerts for critical risks
- Mobile app version
- Integration with hospital EMR systems
- Multi-language support (Urdu, Spanish)
- Historical trend analysis
- Batch drug analysis

---

## Developed By

| | |
|:---|:---|
| **Developer Name** | Alina Liaquat |
| **GitHub** | [@precious-05](https://github.com/precious-05) |
| **Email** | [alina.insights@gmail.com](mailto:alina.insights@gmail.com) |
| **Class & Semester** | BS Computer Science - 6th Semester |
| **Department** | Department of Computer Science |
| **Course** | Advance Database Systems |
| **LinkedIn** | [www.linkedin.com/in/alina-liaquat-779347325](https://www.linkedin.com/in/alina-liaquat-779347325) |

---

<div align="center">

**MediNomix - LASA Drugs Error Prevention System**  
*Improving medication safety through intelligent database analytics*

*This project was submitted in partial fulfillment of the requirements for the Advance Database Systems course.*

</div>
