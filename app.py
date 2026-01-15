import logging
import uuid
import time
from flask import Flask, request, jsonify
from prometheus_client import Counter, generate_latest

# --- 1. LOGGING (Logs structurés) ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s] %(message)s')
logger = logging.getLogger("DevOps-App")

app = Flask(__name__)

# --- 2. METRICS (Prometheus) ---
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

# --- 3. TRACING & LOGIC ---
@app.before_request
def start_timer():
    request.start_time = time.time()
    request.trace_id = str(uuid.uuid4()) # ID unique pour le tracing
    logger.info(f"TraceID={request.trace_id} - REQUETE RECUE: {request.method} {request.path}")

@app.after_request
def log_request(response):
    latency = time.time() - request.start_time
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()
    # On ajoute le Trace ID dans la réponse
    response.headers['X-Trace-ID'] = request.trace_id
    logger.info(f"TraceID={request.trace_id} - REPONSE ENVOYEE: Status {response.status_code} en {latency:.4f}s")
    return response

# --- 4. ROUTES (API) ---
@app.route('/')
def home():
    return jsonify({"status": "live", "message": "Projet DevOps - Convertisseur"})

@app.route('/convert')
def convert():
    # Convertit Celsius en Fahrenheit
    celsius = request.args.get('celsius')
    if not celsius:
        return jsonify({"error": "Parametre celsius manquant"}), 400
    try:
        val = float(celsius)
        return jsonify({"celsius": val, "fahrenheit": (val * 9/5) + 32})
    except ValueError:
        return jsonify({"error": "Ce n'est pas un nombre"}), 400

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)