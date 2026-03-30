import json
import asyncio
import uuid
from models.schemas import InputConfig
from services.execution_service import ExecutionService

# Funciones para futuras fases (comentadas)
# def call_ozap_docker(url, user, encrypted_password):
#     # TODO: Implementar llamada a docker OZAP
#     # Usar subprocess o docker SDK para ejecutar el contenedor
#     # Pasar url, user, encrypted_password
#     # Retornar el informe del scan
#     pass

# def call_n8n_docker(scan_report):
#     # TODO: Implementar llamada a docker N8N
#     # Pasar el scan_report para automatizaciones
#     # Retornar resultado de automatizaciones
#     pass

def main():
    print("Program start")

    # Leer el JSON de entrada
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)
        config = InputConfig(**data)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    # Verificar información
    has_credentials = bool(config.user and config.password)
    print(f"Checked json, with/without login info. Credentials: {'present' if has_credentials else 'absent'}")

    # Si hay credenciales, encriptar
    if has_credentials:
        execution_service = ExecutionService()
        encrypted_password = execution_service.security.encrypt_password(config.password)
        print("Credentials encrypted")
    else:
        encrypted_password = ""

    # Simular llamada al scanner (OZAP docker - comentado para fase 1)
    print("Scan started")
    # scan_result = call_ozap_docker(config.url, config.user if has_credentials else "", encrypted_password if has_credentials else "")
    scan_result = "Simulated scan report"  # Placeholder
    print("Scan finished (success)")

    # Simular llamada a automatizaciones (N8N docker - comentado para fase 1)
    print("Start automations")
    # automation_result = call_n8n_docker(scan_result)
    automation_result = "Simulated automation completed"  # Placeholder
    print("Finished automa")

    print("Finish program")

if __name__ == "__main__":
    main()