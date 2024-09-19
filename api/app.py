import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'bash.html')

@app.route('/<path:filename>')
def serve_file(filename):
    # Verifica se o arquivo existe na pasta static
    file_path = os.path.join(app.static_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, filename)
    else:
        return send_from_directory(app.static_folder, 'bash.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)