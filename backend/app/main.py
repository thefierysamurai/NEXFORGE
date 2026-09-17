from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models import SimulationRequest
from .network import payload,overview
from .simulation import simulate,warnings,interventions
app=FastAPI(title='NEXFORGE API',version='2.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=['*'],allow_headers=['*'])
@app.get('/api/health')
def health():return {'status':'operational','project':'NEXFORGE'}
@app.get('/api/network')
def network():return payload()
@app.get('/api/overview')
def get_overview():return overview()
@app.get('/api/warnings')
def get_warnings():return warnings()
@app.get('/api/interventions')
def get_interventions():return interventions()
@app.post('/api/simulate')
def run(req:SimulationRequest):
 try:return simulate(req.asset_id,req.severity,req.duration_hours)
 except ValueError as e:raise HTTPException(404,str(e))
