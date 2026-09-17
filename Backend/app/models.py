from pydantic import BaseModel,Field
class SimulationRequest(BaseModel):
    asset_id:str
    severity:int=Field(ge=10,le=100)
    duration_hours:int=Field(ge=1,le=24)
