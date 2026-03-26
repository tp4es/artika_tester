import base64

class SecurityService:
    def encrypt_password(self, password: str) -> str:
        # Simulación de encriptación con base64
        return base64.b64encode(password.encode()).decode()

    def decrypt_password(self, encrypted: str) -> str:
        # Simulación de desencriptación
        return base64.b64decode(encrypted.encode()).decode()

    # Función vacía para futuro: integración con Vault
    def get_credentials_from_vault(self):
        # TODO: Integrar con Vault para obtener credenciales
        pass