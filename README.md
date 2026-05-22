# 💊 MediNomix | LASA Drugs Error Prevention System

A professional medication safety web application that analyzes drug names for potential confusion risks using advanced algorithms, helping healthcare professionals prevent medication errors and improve patient safety. Built with FastAPI backend and Streamlit frontend with PostgreSQL database.

## Table of Contents
- Features
- 🧑‍⚕️ Use Case
- 🛠 Tech Stack
- 🗃 Database Design
- ⚙️ Installation Guide
- 🔁 App Flow
- 🔐 Security & Environment

## 🚀 Features

### 🎯 Core Analysis
- Drug name search and confusion risk analysis
- Multiple similarity algorithms (Levenshtein, Jaro-Winkler, Fuzzy matching)
- Phonetic matching (Soundex, Metaphone, NYSIIS)
- Therapeutic context analysis
- Real-time risk scoring (0-100%)

### 📊 Analytics Dashboard
- Risk breakdown donut chart (Critical/High/Medium/Low)
- Top 10 high-risk drug pairs bar chart
- Drug confusion risk heatmap matrix
- Interactive Plotly visualizations

### 🔴 Real-Time Monitoring
- Auto-refreshing dashboard every 10 seconds
- Live metrics (total drugs, critical pairs, high risk pairs, avg risk score)
- Recent search activity feed
- System health status monitoring

### 💾 Database Features
- PostgreSQL database with 6 tables
- OpenFDA API integration for drug data
- Automatic drug risk analysis against all existing drugs
- Known risky pairs seeding (ISMP/FDA sources)

### 🎨 Modern UI/UX
- Glass morphism design with purple/pink gradient theme
- Custom animated tabs and buttons
- Responsive layout for all screen sizes
- Medical imagery integration

## 🧑‍⚕️ Use Case

A healthcare professional can:
1. Search any medication name (brand or generic)
2. View all similar drugs with confusion risk scores
3. Filter risks by category (Critical/High/Medium/Low)
4. Analyze risk distribution via interactive charts
5. Monitor real-time system metrics and activity
6. Identify critical drug pairs requiring attention

## 🛠 Tech Stack

**Backend:**
- FastAPI (REST API framework)
- PostgreSQL (Database)
- SQLAlchemy (ORM)
- Uvicorn (ASGI server)

**Frontend:**
- Streamlit (UI framework)
- Plotly (Interactive charts)
- Custom CSS (Glass morphism, animations)

**Data Processing:**
- Pandas (Data manipulation)
- Jellyfish (Phonetic algorithms)
- FuzzyWuzzy (String matching)
- python-Levenshtein (Distance calculations)

**APIs:**
- OpenFDA Drug Label API

## 🗃 Database Design

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

## ⚙️ Installation Guide

**Requirements:**
- Python 3.8 or higher
- PostgreSQL 14 or higher
- Git

**Backend Setup:**

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medinomix.git
cd medinomix

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

**Frontend Setup:**

1. Install frontend dependencies:
```bash
pip install streamlit plotly pandas requests pillow
```

2. Place logo image as `m11.jpg` in project root

3. Start frontend:
```bash
streamlit run app.py
```

**Database Seeding:**
After starting backend, seed with example drugs:
```bash
curl -X POST http://localhost:8000/api/seed-database
```

## 🔁 App Flow

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

## 🔐 Security & Environment

**Current State:**
- Backend runs on localhost:8000
- Frontend runs on localhost:8501
- Database runs on localhost:5432
- CORS enabled for all origins

**Recommended Improvements:**
- Add authentication system
- Move database credentials to environment variables
- Implement rate limiting
- Add HTTPS for production deployment
- Use environment-specific configurations

## 📡 API Endpoints

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

## 🤝 Contribution Guidelines

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Notes

- Backend must be running before starting frontend
- Database tables are created automatically on first run
- First search for a drug may take longer due to OpenFDA fetch
- Heatmap requires at least 5 drugs in database to display
- Real-time tab auto-refreshes every 10 seconds (no WebSocket needed)

## Future Improvements

- User authentication and roles
- Export reports (PDF/CSV)
- Email alerts for critical risks
- Mobile app version
- Integration with hospital EMR systems
- Multi-language support (Urdu, Spanish)
- Historical trend analysis
- Batch drug analysis
```
