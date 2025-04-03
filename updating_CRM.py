import requests

def update_google_sheet(name, email, lead_score, interest):
    """
    Sends lead details to the Google Apps Script Web App.
    """
    url = "https://script.google.com/macros/s/AKfycbx4xj-p3EKxmNkNn7zAZrqTKENCH2-wkHFyoYq8waPcYGGjt9DSmzDMTxiJUiArfhH3sg/exec"  # Replace with the Web App URL from Step 1

    # Data to send
    data = {
        "name": name,
        "email": email,
        "leadScore": lead_score,
        "interest": interest
    }

    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            print("[Sales Agent] Google Sheet updated successfully!")
        else:
            print(f"[Sales Agent] Failed to update Google Sheet: {response.text}")
    except Exception as e:
        print(f"[Sales Agent] Error: {e}")


