from flask import Flask, request

app = Flask(__name__)

# Sample test servers
servers = {
    1: {"name": "Test Server 1", "locked": False},
    2: {"name": "Test Server 2", "locked": False},
    3: {"name": "Test Server 3", "locked": False},
}

@app.route('/test-server', methods=['POST'])
def test_server():
    command = request.form.get('text', '').strip().split()
    action = command[0] if command else None
    server_id = int(command[1]) if len(command) > 1 and command[1].isdigit() else None
    
    if action == 'show':
        return show_servers()
    elif action == 'lock' and server_id in servers:
        return lock_server(server_id)
    elif action == 'unlock' and server_id in servers:
        return unlock_server(server_id)
    else:
        return "Invalid command or server ID.", 400

def show_servers():
    response = "Current Test Servers:\n"
    for id, server in servers.items():
        status = "locked" if server["locked"] else "available"
        response += f"{id}: {server['name']} - {status}\n"
    return response.strip(), 200

def lock_server(server_id):
    servers[server_id]["locked"] = True
    return f"Locked {servers[server_id]['name']}.", 200

def unlock_server(server_id):
    servers[server_id]["locked"] = False
    return f"Unlocked {servers[server_id]['name']}.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
