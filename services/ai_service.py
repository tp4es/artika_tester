class AIService:
    def analyze_logs(self, logs: list) -> dict:
        # Simulación de análisis IA basado en texto
        summary = "Test execution completed with issues."
        error = "500 Internal Server Error detected."
        cause = "Authentication failed due to invalid credentials."
        recommendation = "Check username and password, verify app_url."

        if "500 error" in str(logs):
            error = "Server error encountered."
            cause = "Application server issue."
            recommendation = "Investigate server logs."

        return {
            "summary": summary,
            "error": error,
            "cause": cause,
            "recommendation": recommendation
        }

    # Función vacía para futuro: integración con n8n
    def send_to_n8n(self, data):
        # TODO: Enviar datos a n8n para procesamiento
        pass