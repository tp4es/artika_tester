from pydantic import BaseModel
from typing import Optional, Dict, Any

class RunTestRequest(BaseModel):
    app_url: str
    username: str
    password: str

class StatusResponse(BaseModel):
    status: str
    result: Optional[Dict[str, Any]] = None

class ResultsRequest(BaseModel):
    execution_id: str
    analysis: Dict[str, Any]

class InputConfig(BaseModel):
    url: str
    user: str = ""
    password: str = ""