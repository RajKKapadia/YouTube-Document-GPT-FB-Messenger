import requests

from config import config

def send_message(sender_id: str, message: str) -> None:
    url = f'https://graph.facebook.com/v13.0/me/messages?access_token={config.FB_AUTH_TOKEN}'
    payload = {
        'messaging_type': 'RESPONSE',
        'recipient': {'id': sender_id},
        'message': {'text': message}
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message.")
