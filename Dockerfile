# Utilise une version légère de Python
FROM python:3.9-slim

# Crée le dossier de travail
WORKDIR /app

# Copie les requirements
COPY requirements.txt .

# --- LA LIGNE MAGIQUE EST ICI (Timeout augmenté) ---
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Copie le code
COPY app.py .

# Expose le port
EXPOSE 5000

# Lance l'application
CMD ["python", "app.py"]