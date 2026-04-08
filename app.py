from flask import Flask, jsonify, render_template_string
import platform
import socket
import datetime
import psutil

app = Flask(__name__)

# Simple HTML UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Dashboard</title>
    <style>
        body { font-family: Arial; background: #0f172a; color: #e2e8f0; text-align: center; }
        .card { background: #1e293b; padding: 20px; margin: 20px auto; width: 300px; border-radius: 10px; }
        h1 { color: #38bdf8; }
    </style>
</head>
<body>
    <h1>🚀 DevOps Dashboard</h1>

    <div class="card">
        <h3>Status</h3>
        <p>✅ Application Running</p>
    </div>

    <div class="card">
        <h3>System Info</h3>
        <p>Hostname: {{hostname}}</p>
        <p>OS: {{os}}</p>
    </div>

    <div class="card">
        <h3>Time</h3>
        <p>{{time}}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_PAGE,
        hostname=socket.gethostname(),
        os=platform.system(),
        time=datetime.datetime.now()
    )

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/api/system')
def system():
    return jsonify({
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "platform": platform.system(),
        "hostname": socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
