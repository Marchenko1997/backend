import os
import socket
import time

host = os.getenv("POSTGRES_HOST", "db")
port = int(os.getenv("POSTGRES_PORT", "5432"))

print(f"Waiting for Postgres at {host}:{port}...")

while True:
    try:
        with socket.create_connection((host, port), timeout=2):
            print("Postgres is up!")
            break
    except OSError:
        time.sleep(1)
