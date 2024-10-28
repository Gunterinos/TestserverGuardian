from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Slack Bot!"

# Example endpoint to handle slash commands
@app.route('/slack/commands', methods=['POST'])
def handle_command():
    command = request.form.get('command')
    user_id = request.form.get('user_id')
    text = request.form.get('text').strip()
    
    if command == '/occupy_server':
        # Logic to handle server occupation
        return jsonify(response=f"You have occupied server '{text}'.")
    
    return jsonify(response="Unknown command.")

if __name__ == '__main__':
    app.run(debug=True, port=5001)