from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# ERPNext API URL and credentials
erpnext_url = 'http://198.204.243.58/api/resource/Lead'
erpnext_api_key = '047acb583427526'
erpnext_api_secret = '59c2ac363178b07'

# Headers for authentication
headers = {
    'Authorization': f'token {erpnext_api_key}:{erpnext_api_secret}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    return render_template('lead_form.html')

@app.route('/submit', methods=['POST'])
def submit_lead():
    # Collect lead data from the form
    lead_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email_id": request.form['email_id'],
        "mobile_no": request.form['mobile_no'],
        "status": "Open",
        "type": "Client",
        "source": "Website",
    }

    # Create lead
    response = requests.post(erpnext_url, headers=headers, json=lead_data)

    if response.status_code in [200, 201]:
        return "Lead created successfully!"
    else:
        return f"Failed to create lead: {response.status_code}, {response.text}"

if __name__ == '__main__':
    app.run(debug=True)
