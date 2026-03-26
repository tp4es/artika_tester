# artika_tester
A fast API created to check for vulnerabilities in applications.

---

## 🚀 Características

* Ejecuta un "test" simulado con `POST /run-test`
* Consulta estado con `GET /status/{execution_id}`
* Actualiza resultado manual con `POST /results`
* Almacenamiento en memoria (`MemoryStorage`)
* Simulación de análisis de logs (`AIService`)
* Encriptación primaria (base64) para credenciales (`SecurityService`)

---

## 📁 Estructura del proyecto

```
.
├── main.py
├── schemas.py
├── execution_service.py
├── security_service.py
├── ai_service.py
├── memory_storage.py
```

---

### main.py

* Definición de la app FastAPI

Endpoints:

* `run_test` → genera ejecución async
* `get_status` → devuelve estado + resultado
* `post_results` → actualiza resultado

---

### schemas.py

```python
RunTestRequest:
    app_url: str
    username: str
    password: str

StatusResponse:
    status: str
    result: dict | None

ResultsRequest:
    execution_id: str
    analysis: dict
```

---

### execution_service.py

```python
ExecutionService

create_execution(...)
    → guarda ejecución en estado PENDING

run_execution(...)
    → RUNNING
    → simula logs
    → ANALYZING
    → análisis IA
    → COMPLETED

get_execution(...)

update_results(...)
```

---

### security_service.py

```python
SecurityService

encrypt_password(...)
decrypt_password(...)
    → base64 (simulado)

get_credentials_from_vault(...)
    → placeholder
```

---

### ai_service.py

```python
AIService

analyze_logs(...)
    → resumen
    → causa
    → recomendación
    → detección de error 500

send_to_n8n(...)
    → placeholder
```

---

### memory_storage.py

```python
MemoryStorage

save_execution(...)
get_execution(...)

trigger_jenkins_job(...)
    → placeholder
```

---

## 🛠️ Uso

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 2. Ejecutar servidor

```bash
uvicorn main:app --reload
```

---

### 3. Llamadas de ejemplo

#### Ejecutar test

```http
POST /run-test
```

```json
{
  "app_url": "http://...",
  "username": "user",
  "password": "pwd"
}
```

---

#### Consultar estado

```http
GET /status/{execution_id}
```

---

#### Enviar resultados manuales

```http
POST /results
```

```json
{
  "execution_id": "...",
  "analysis": {
    "summary": "...",
    "error": "..."
  }
}
```

---

## 🔄 Flujo de ejecución

```
run-test
  ↓
Crea execution_id
  ↓
Estado: PENDING

Async:
  RUNNING
    ↓
  sleep (3–5s)
    ↓
  logs simulados
    ↓
  ANALYZING
    ↓
  análisis IA
    ↓
  COMPLETED

GET /status
  → devuelve estado + resultado

POST /results
  → permite sobreescribir resultado final
```

---

## 🧩 Extensiones previstas

* Persistencia real (base de datos)
* Seguridad con Vault / Secrets Manager
* Integración real con motor de testing
* IA real (OpenAI, etc.)
* Integración con n8n / Jenkins pipelines reales
