<div align="center">

```
╔═══════════════════════════════════════════════════════╗
║  ONLINE SHOPPERS                                      ║
║  PURCHASE INTENTION                                   ║
║  ── MLOps Pipeline ──────────────────────────────     ║
╚═══════════════════════════════════════════════════════╝
```

**End-to-end machine learning system** — from raw CSV to live cloud API.  
ETL · Training · Tracking · Deployment · Monitoring. 

[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-→_online--shoppers--mlops.onrender.com-000000?style=flat-square)](https://online-shoppers-mlops.onrender.com)
[![API Docs](https://img.shields.io/badge/API_DOCS-→_Swagger-1a1a1a?style=flat-square)](https://online-shoppers-mlops.onrender.com/docs)

</div>

---

## What this is

An e-commerce company wants to know — before a session ends — whether a visitor will buy.
This system predicts that in real time using behavioral signals from the session itself.

Target high-intent users. Improve retargeting. Increase conversions.
Built as a production ML system instead of a notebook-only workflow.

---

## Architecture


## System Architecture

<div align="center">

<img src="assets/System Architecture.drawio.png" alt="architecture" width="950"/>

</div>


Every stage is automated. Push to `main` → tests run → Docker builds → deploys to Render.

---

## Stack

| Layer | Tools |
|---|---|
| **Language** | Python 3.11 |
| **API** | FastAPI + Uvicorn |
| **ML** | Scikit-learn · XGBoost · LightGBM |
| **Databases** | MySQL (source) · PostgreSQL (warehouse) |
| **Experiment Tracking** | MLflow |
| **Drift Monitoring** | Evidently AI |
| **CI/CD** | GitHub Actions |
| **Containerization** | Docker + Docker Hub |
| **Deployment** | Render |
| **Testing** | Pytest |

---

## Dataset

18 features. 1 binary target: `Revenue` (did the session convert?).

```
Administrative        Informational         ProductRelated
Admin_Duration        Info_Duration         Product_Duration
BounceRates           ExitRates             PageValues
SpecialDay            Month                 OperatingSystems
Browser               Region                TrafficType
VisitorType           Weekend               → Revenue ✓/✗
```

Class imbalance handled via **SMOTE**.

---

## Models evaluated

```
Logistic Regression   Decision Tree   Random Forest
XGBoost               LightGBM
```

All tracked in MLflow. Best model selected by F1 + ROC-AUC.  
Metrics logged: Accuracy · Precision · Recall · F1 · ROC-AUC · Confusion Matrix.

---

## API

```
GET  /         →  Frontend UI
GET  /health   →  System status
POST /predict  →  Purchase prediction
```

Full Swagger docs: [online-shoppers-mlops.onrender.com/docs](https://online-shoppers-mlops.onrender.com/docs)

---

## Run locally

```bash
git clone <repo-url>
cd online-shoppers-mlops

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
uvicorn api.main:app --reload

# → http://127.0.0.1:8000/docs
```

---

## Docker

```bash
docker build -t shoppers-ml .
docker run -p 8001:8000 --env-file .env shoppers-ml
```

---

## CI/CD pipeline

On every push to `main`:

```
1. Run Pytest suite
2. Initialize databases
3. Execute ETL pipeline
4. Train + evaluate model
5. Build Docker image
6. Push to Docker Hub
7. Redeploy on Render
```

Config: `.github/workflows/cicd.yml`

---

## Project structure

```
online-shoppers-mlops/
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── api/
│   ├── static/
│   │   ├── script.js
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   └── main.py
│
├── data/
│   ├── online_shoppers_intention.csv
│   └── reload_data.py
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── ml/
│   ├── evaluate.py
│   ├── mlflow_tracker.py
│   ├── model.pkl
│   ├── predict.py
│   ├── preprocess.py
│   ├── scaler.pkl
│   ├── selected_features.pkl
│   ├── selector.pkl
│   └── train.py
│
├── monitoring/
│   └── drift_report.py
│
├── scheduler/
│   └── retrain_job.py
│
├── tests/
│   └── test_api.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── render.yaml
├── requirements.txt
└── README.md
```

---

## Contact

Priyaa Sharma

LinkedIn:
www.linkedin.com/in/priyasharmada


---
