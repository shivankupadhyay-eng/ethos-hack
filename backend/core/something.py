import websocket
import json

def send_message(ws, message):
    ws.send(json.dumps({'message': message}))
    print(f"Sent: {message}")
    
def on_message(ws, message):
    data = json.loads(message)
    print("Received message:", data)

def on_error(ws, error):
    print("Error occurred:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection established")

if __name__ == "__main__":
    websocket_url = "ws://127.0.0.1:8000/ws/chat/41/"  
    # Create a WebSocket client and set the callbacks
    ws = websocket.WebSocketApp(websocket_url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    # Start the WebSocket connection
    ws.run_forever()