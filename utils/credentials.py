from dotenv import load_dotenv
import os
from typing import TypedDict

load_dotenv()

class Creds(TypedDict):
    username: str
    password: str

CREDENTIALS = {
    'valid': {
        'username': os.getenv('VALID_USERNAME'),
        'password': os.getenv('VALID_PASSWORD')
    },
    'incorrect_password': {
        'username': os.getenv('VALID_USERNAME'),
        'password': os.getenv('INVALID_PASSWORD')
    },
    'no_password': {
        'username': os.getenv('VALID_USERNAME'),
        'password': ' '
    }
}

def get_credentials(login_type: str) -> Creds:          # <-- export just once
    try:
        return CREDENTIALS[login_type.lower()]
    except KeyError as exc:
        raise ValueError(f"Unknown credential type: '{login_type}'") from exc
