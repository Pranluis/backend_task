from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import base64
import mimetypes

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        try:
            # Extract data from the JSON payload
            data = request.json.get('data', [])
            file_b64 = request.json.get('file_b64', None)

            # Log the incoming request data
            app.logger.info(f"Data received: {data}")
            app.logger.info(f"File received: {file_b64}")

            # Process the data
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            highest_lowercase = sorted([x for x in data if x.islower()], reverse=True)[:1]

            # Check for file validity (you can expand this with actual file processing if needed)
            file_valid = False
            mime_type = ""
            file_size_kb = 0
            if file_b64:
                try:
                    file_data = base64.b64decode(file_b64)
                    file_size_kb = len(file_data) / 1024
                    mime_type = mimetypes.guess_type(file_data)[0]
                    file_valid = True
                except Exception as e:
                    file_valid = False

            # Prepare the response
            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase,
                "file_valid": file_valid,
                "file_mime_type": mime_type,
                "file_size_kb": file_size_kb
            }

            return jsonify(response), 200

        except Exception as e:
            app.logger.error(f"Error processing request: {e}")
            return jsonify({"is_success": False, "error": "Server error"}), 500

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
