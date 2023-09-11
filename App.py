import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    if not slack_name:
        return jsonify({"error": "The slack_name field is required"}), 400
    
    if not track:
        return jsonify({"error": "The track field is required"}), 400
    # Get current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')
    
    # Get current UTC time with validation of +/-2 minutes
    current_utc_time = datetime.datetime.utcnow()
    
    # Create GitHub URLs
    github_repo_url = "https://github.com/Olajiive/HNGx1"
    github_file_url = f"{github_repo_url}/blob/main/App.py"
    
    # Create response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time.isoformat() + "Z",
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return response_data, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
