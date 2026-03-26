from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import asyncio
from services.execution_service import ExecutionService
from models.schemas import RunTestRequest, StatusResponse, ResultsRequest

app = FastAPI(title="Test Orchestration API", version="1.0.0")

execution_service = ExecutionService()

@app.post("/run-test", response_model=dict)
async def run_test(request: RunTestRequest):
    execution_id = str(uuid.uuid4())
    await execution_service.create_execution(execution_id, request.app_url, request.username, request.password)
    asyncio.create_task(execution_service.run_execution(execution_id))
    return {"execution_id": execution_id}

@app.get("/status/{execution_id}", response_model=StatusResponse)
async def get_status(execution_id: str):
    execution = await execution_service.get_execution(execution_id)
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return StatusResponse(status=execution["status"], result=execution.get("result"))

@app.post("/results")
async def post_results(request: ResultsRequest):
    await execution_service.update_results(request.execution_id, request.analysis)
    return {"message": "Results updated"}