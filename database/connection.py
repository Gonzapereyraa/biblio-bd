import os
import sys
import time
from libsql_client import create_client_sync

TURSO_URL = os.environ.get("TURSO_URL")
TURSO_TOKEN = os.environ.get("TURSO_TOKEN")

if not TURSO_URL or not TURSO_TOKEN:
    print("❌ ERROR: TURSO_URL o TURSO_TOKEN no están configurados en variables de entorno.", file=sys.stderr)

def create_connection(retries: int = 3, delay: int = 2):
    """
    Devuelve un cliente de Turso con reintentos básicos.
    - retries: número de intentos
    - delay: segundos entre intentos
    """
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            client = create_client_sync(url=TURSO_URL, auth_token=TURSO_TOKEN)
            return client
        except Exception as e:
            last_err = e
            print(f"⚠️  Fallo al conectar con Turso (intento {attempt}/{retries}): {e}", file=sys.stderr)
            time.sleep(delay)

    # Si no se pudo conectar, levantar excepción
    raise RuntimeError(f"❌ No se pudo conectar con Turso después de {retries} intentos: {last_err}")
