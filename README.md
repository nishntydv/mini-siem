# 🛡️ Mini SIEM using Python and OpenSearch

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenSearch](https://img.shields.io/badge/OpenSearch-2.19.0-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-red?logo=linux)

## 📖 Overview

Mini SIEM (Security Information and Event Management) is a lightweight cybersecurity project developed using **Python** and **OpenSearch**.

The project demonstrates the basic workflow of a SIEM system by collecting logs, detecting suspicious events, storing alerts, visualizing data through dashboards, and providing search functionality.

This project was developed as a **10-day hands-on learning project** to understand SIEM concepts and OpenSearch.

---

# 🎯 Objective

The objective of this project is to build a basic SIEM system capable of:

- Collecting system logs
- Detecting suspicious events
- Storing alerts in OpenSearch
- Searching stored alerts
- Visualizing security data
- Managing log lifecycle using ISM policies

---

# ✨ Features

- ✅ Log Collection
- ✅ Alert Detection
- ✅ Alert Storage
- ✅ OpenSearch Integration
- ✅ Dashboard Visualization
- ✅ Log Search
- ✅ Search by Severity
- ✅ Search by Host
- ✅ Search by Event
- ✅ Index State Management (ISM)
- ✅ Interactive CLI Search Tool

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| OpenSearch | Log & Alert Storage |
| OpenSearch Dashboards | Data Visualization |
| Docker | Containerization |
| Kali Linux | Development Environment |

---

# 📂 Project Structure

```
mini-siem/
│
├── backend/
│   ├── collector.py
│   ├── alert_engine.py
│   ├── search_logs.py
│   └── sample_logs.txt
│
├── dashboards/
│
├── screenshots/
│
├── docker-compose.yml
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ System Architecture

```
Sample Logs
      │
      ▼
collector.py
      │
      ▼
OpenSearch
      │
      ▼
alert_engine.py
      │
      ▼
mini-siem-alerts Index
      │
      ├──────────────┐
      ▼              ▼
Dashboard      search_logs.py
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/nishntydv/mini-siem
```

Move into the project directory

```bash
cd mini-siem
```

Start Docker containers

```bash
docker compose up -d
```

Verify OpenSearch

```bash
curl http://localhost:9200
```

---

# ▶️ Running the Project

### 1. Run Collector

```bash
python3 collector.py
```

---

### 2. Run Alert Engine

```bash
python3 alert_engine.py
```

---

### 3. Search Alerts

```bash
python3 search_logs.py
```

Search options:

- Search by Severity
- Search by Host
- Search by Event

---

### 4. Open Dashboard

```
http://localhost:5601
```

---

# 📊 Dashboard

The dashboard contains:

- Logs by Severity (Bar Chart)
- Severity Distribution (Donut Chart)

Future dashboards may include:

- Logs Over Time
- Top Hosts
- Event Types
- Recent Alerts
- Failed Login Attempts
- Firewall Events

---

# 🔍 Demo Workflow

1. Start Docker & OpenSearch
2. Verify OpenSearch is running
3. Run `collector.py`
4. Run `alert_engine.py`
5. Verify alerts are stored
6. Run `search_logs.py`
7. Search alerts
8. Open OpenSearch Dashboard
9. View visualizations
10. Verify ISM Policy

---

# 📅 10-Day Development Journey

| Day | Work Completed |
|------|----------------|
| Day 1 | Environment Setup & Project Planning |
| Day 2 | Docker & OpenSearch Setup |
| Day 3 | Log Collector Development |
| Day 4 | Sample Log Generation & Indexing |
| Day 5 | Dashboard Creation & Visualization |
| Day 6 | Alert Engine Development |
| Day 7 | Alert Storage in OpenSearch |
| Day 8 | Index State Management (ISM) |
| Day 9 | Log Search Tool |
| Day 10 | Testing, Documentation & Finalization |

---

# 📸 Screenshots

- Dashboard
- Bar Chart
- Donut Chart
- Alert Engine Output
- Search Tool
- ISM Policy
- OpenSearch Running


---

# 📚 Skills Learned

- Python Programming
- OpenSearch
- Docker
- Log Collection
- Alert Detection
- Log Analysis
- Search Queries
- Dashboard Visualization
- Index Lifecycle Management
- Cybersecurity Fundamentals

---

# 🚀 Future Improvements

Planned for **Mini SIEM v2**

- Real-time Log Monitoring
- Multiple Log Sources
- Rule-based Detection Engine
- Detection Rules (JSON/YAML)
- Email Notifications
- Slack/Discord Alerts
- FastAPI Backend
- REST APIs
- Modern Web Interface
- Threat Intelligence Integration
- MITRE ATT&CK Mapping
- GeoIP Lookup
- PDF/CSV Reports
- Docker Compose Deployment

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

**Nishant Yadav**

Cybersecurity Enthusiast

Mini SIEM Project (Python + OpenSearch)

---

# ⭐ Acknowledgements

This project was built to learn the fundamentals of Security Information and Event Management (SIEM), Python automation, OpenSearch, Docker, and cybersecurity monitoring.

---

## 🎉 Project Status

**✅ Mini SIEM v1 Completed Successfully**

The project demonstrates the complete SIEM workflow:

- Log Collection
- Alert Detection
- Alert Storage
- Dashboard Visualization
- Search & Filtering
- Index Lifecycle Management

This project serves as a strong foundation for developing a more advanced SIEM platform in the future.
