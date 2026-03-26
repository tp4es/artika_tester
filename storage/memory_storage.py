class MemoryStorage:
    def __init__(self):
        self.executions = {}

    async def save_execution(self, execution_id: str, execution: dict):
        self.executions[execution_id] = execution

    async def get_execution(self, execution_id: str):
        return self.executions.get(execution_id)

    # Función vacía para futuro: integración con Jenkins
    def trigger_jenkins_job(self, job_name: str):
        # TODO: Trigger Jenkins job
        pass