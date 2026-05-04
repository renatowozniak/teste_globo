# app-python/app.py
from flask import Flask
from datetime import datetime
import redis

app = Flask(__name__)
# Conexão opcional com Redis
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/texto')
def texto():
    return "Texto Fixo (Python)"

@app.route('/hora')
def hora():
    # O cache aqui é feito pelo NGINX (Camada de Infra)
    return f"Hora do Servidor: {datetime.now().strftime('%H:%M:%S')}"

@app.route('/hora-redis')
def hora_redis():
    # O cache aqui é feito via REDIS (Camada de App)
    cached = r.get("hora_python")
    if cached:
        return f"Hora (via Redis - 10s): {cached}"
    
    now = datetime.now().strftime('%H:%M:%S')
    r.setex("hora_python", 10, now)
    return f"Hora (Novo no Redis): {now}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
