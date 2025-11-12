from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return jsonify(cpu=cpu, memory=memory, disk=disk)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DevOps Pipeline using Jenkins and Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
