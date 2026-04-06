import requests
import json

def generate_pdf_from_url(target_url, rapidapi_key):
    # Get your FREE API key here: https://rapidapi.com/titavares33/api/urltopdf-invoices-reports
    api_url = "https://urltopdf-invoices-reports.p.rapidapi.com/api/v1/pdf"
    
    headers = {
        "x-rapidapi-host": "urltopdf-invoices-reports.p.rapidapi.com",
        "x-rapidapi-key": rapidapi_key,
        "Content-Type": "application/json"
    }
    
    payload = {"url": target_url}
    
    print(f"Generating PDF for {target_url}...")
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        with open("output.pdf", "wb") as f:
            f.write(response.content)
        print("Success! PDF saved as output.pdf")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# --- Usage Example ---
API_KEY = "YOUR_RAPIDAPI_KEY" # Replace with your key
TARGET_URL = "https://en.wikipedia.org/wiki/Invoice"

generate_pdf_from_url(TARGET_URL, API_KEY)
