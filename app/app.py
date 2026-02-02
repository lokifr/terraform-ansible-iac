from flask import Flask, jsonify
import socket
import platform
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Home page with welcome message"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>IaC Web Application</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }
            h1 {
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                font-size: 1.2em;
                opacity: 0.9;
                margin-bottom: 30px;
            }
            .tech-stack {
                display: flex;
                justify-content: space-around;
                margin: 30px 0;
            }
            .tech-item {
                text-align: center;
                padding: 20px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                flex: 1;
                margin: 0 10px;
            }
            .tech-item h3 {
                margin: 10px 0;
                font-size: 1.3em;
            }
            .links {
                text-align: center;
                margin-top: 30px;
            }
            .links a {
                color: white;
                text-decoration: none;
                margin: 0 15px;
                padding: 10px 20px;
                background: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                display: inline-block;
                transition: all 0.3s;
            }
            .links a:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Infrastructure as Code</h1>
            <p class="subtitle">Automated Deployment with Terraform & Ansible</p>
            
            <div class="tech-stack">
                <div class="tech-item">
                    <h3>☁️ AWS</h3>
                    <p>Cloud Infrastructure</p>
                </div>
                <div class="tech-item">
                    <h3>🏗️ Terraform</h3>
                    <p>Provisioning</p>
                </div>
                <div class="tech-item">
                    <h3>⚙️ Ansible</h3>
                    <p>Configuration</p>
                </div>
            </div>
            
            <div class="links">
                <a href="/health">Health Check</a>
                <a href="/info">System Info</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Flask Web Application'
    })

@app.route('/info')
def info():
    """System information endpoint"""
    return jsonify({
        'hostname': socket.gethostname(),
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor(),
        'python_version': platform.python_version()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
