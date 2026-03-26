import asyncio
import random
from storage.memory_storage import MemoryStorage
from services.security_service import SecurityService
from services.ai_service import AIService

class ExecutionService:
    def __init__(self):
        self.storage = MemoryStorage()
        self.security = SecurityService()
        self.ai = AIService()

    async def create_execution(self, execution_id: str, app_url: str, username: str, password: str):
        encrypted_password = self.security.encrypt_password(password)
        execution = {
            "execution_id": execution_id,
            "app_url": app_url,
            "username": username,
            "password_encrypted": encrypted_password,
            "status": "PENDING",
            "logs": [],
            "result": None
        }
        await self.storage.save_execution(execution_id, execution)

    async def run_execution(self, execution_id: str):
        execution = await self.storage.get_execution(execution_id)
        if not execution:
            return

        # Cambiar a RUNNING
        execution["status"] = "RUNNING"
        await self.storage.save_execution(execution_id, execution)

        # Simular ejecución
        await asyncio.sleep(random.uniform(3, 5))

        # Generar logs fake
        logs = [
            "Login attempt",
            "POST /auth",
            "500 error",
            "Test failed"
        ]
        execution["logs"] = logs
        await self.storage.save_execution(execution_id, execution)

        # Cambiar a ANALYZING
        execution["status"] = "ANALYZING"
        await self.storage.save_execution(execution_id, execution)

        # Llamar a IA simulada
        analysis = self.ai.analyze_logs(logs)
        execution["result"] = analysis
        execution["status"] = "COMPLETED"
        await self.storage.save_execution(execution_id, execution)

    async def get_execution(self, execution_id: str):
        return await self.storage.get_execution(execution_id)

    async def update_results(self, execution_id: str, analysis: dict):
        execution = await self.storage.get_execution(execution_id)
        if execution:
            execution["result"] = analysis
            execution["status"] = "COMPLETED"
            await self.storage.save_execution(execution_id, execution)