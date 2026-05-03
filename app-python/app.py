from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/texto')
def texto():
    return "Aplicação Python: Texto Fixo via Flask"

@app.route('/hora')
def hora():
    return f"Hora atual (Python): {datetime.now().strftime('%H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)