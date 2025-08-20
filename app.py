from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Configurações do Supabase
SUPABASE_URL = "https://xmsjjknpnowsswwrbvpc.supabase.co/rest/v1"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhtc2pqa25wbm93c3N3d3JidnBjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI1MDg0NDUsImV4cCI6MjA2ODA4NDQ0NX0.OexXJX7lK_DefGb72VDWGLDcUXamoQIgYOv5Zo_e9L4"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def home():
    return jsonify({"message": "Supabase Dashboard API"})

@app.route('/api/arquetipos')
def get_arquetipos():
    try:
        response = requests.get(f"{SUPABASE_URL}/relatorios_arquetipos", headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/microambiente')
def get_microambiente():
    try:
        response = requests.get(f"{SUPABASE_URL}/relatorios_microambiente", headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/consolidado-arquetipos')
def get_consolidado_arquetipos():
    try:
        response = requests.get(f"{SUPABASE_URL}/consolidado_arquetipos", headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/consolidado-microambiente')
def get_consolidado_microambiente():
    try:
        response = requests.get(f"{SUPABASE_URL}/consolidado_microambiente", headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
