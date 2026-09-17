# NEXFORGE

Round 1 prototype for M# problem statement **Cascading Failure: When One Failure Becomes Many**.

## Structure
- `frontend/index.html` — markup only
- `frontend/css/styles.css` — all styling
- `frontend/js/app.js` — frontend logic and API integration
- `backend/app/main.py` — API routes
- `backend/app/network.py` — graph/network model
- `backend/app/simulation.py` — cascade, impact and intervention logic
- `backend/app/models.py` — request models
- `backend/data/network.json` — synthetic network data

## Run
Backend:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```
Frontend (port 5501):
```bash
cd frontend
python3 -m http.server 5501
```
Open `http://127.0.0.1:5501`.
