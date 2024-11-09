from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.keylogger_detection

def save_user_details(name, mobile, email, address, education):
    user_details = {
        "name": name,
        "mobile": mobile,
        "email": email,
        "address": address,
        "education": education
    }
    db.user_details.insert_one(user_details)

def toggle_keylogger_status(activate):
    keylogger_status = {
        "status": activate,
        "timestamp": datetime.now()
    }
    db.keylogger_status.insert_one(keylogger_status)
