# main.py
import os
import json
from flask import Flask, request

# Create a Flask web server application
app = Flask(__name__)

# This decorator creates an endpoint that accepts POST requests at the root URL '/'
@app.route('/', methods=['POST'])
def receive_data():
    """
    A simple cloud receiver endpoint.
    It expects a POST request with a JSON payload.
    """
    # --- 1. Try to parse the incoming JSON data ---
    try:
        data = request.get_json()
        print(f"SUCCESS: Received data: {json.dumps(data)}")

        # You can access specific fields like this:
        # message_content = data.get('content', 'No content found')
        # author = data.get('author', 'No author found')
        # print(f"Message from {author}: '{message_content}'")
        
        # --- 2. This is where your trading logic would go ---

        # --- 3. Send a success response back to the scraper ---
        response_message = {"status": "success", "data_received": data}
        return json.dumps(response_message), 200

    except Exception as e:
        # If the data isn't valid JSON or another error occurs
        print(f"ERROR: Could not process request. Error: {e}")
        return 'Error: Invalid JSON payload or internal server error.', 400

# This section is used to run the server on Cloud Run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))