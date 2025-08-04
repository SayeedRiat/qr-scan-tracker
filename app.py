from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

QR_ID = "qr001"
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def handle_qr():
    file_path = os.path.join(DATA_DIR, f"{QR_ID}.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    with open(file_path, "r") as f:
        first_scan_date = f.read()

    return f"""
        <h1>🎉 This QR was first scanned on:</h1>
        <h2>{first_scan_date}</h2>
    """
