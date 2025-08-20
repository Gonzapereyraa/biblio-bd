import os
from libsql_client import create_client_sync

TURSO_URL = os.environ.get("TURSO_URL")
TURSO_TOKEN = os.environ.get("TURSO_TOKEN")

def create_connection():
    return create_client_sync(url=TURSO_URL, auth_token=TURSO_TOKEN)
