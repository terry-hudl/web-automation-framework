from enum import Enum, unique
from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@unique
class CredentialType(str, Enum):
    VALID              = "valid"
    INCORRECT_PASSWORD = "incorrect_password"
    NO_PASSWORD        = "no_password"

@dataclass(frozen=True)
class Credentials:
    username: str
    password: str

def _env(key: str, default: str = "") -> str:
    return os.getenv(key, default)

_CREDENTIALS: dict[CredentialType, Credentials] = {
    CredentialType.VALID: Credentials(
        username=_env("VALID_USERNAME"),
        password=_env("VALID_PASSWORD"),
    ),
    CredentialType.INCORRECT_PASSWORD: Credentials(
        username=_env("VALID_USERNAME"),
        password=_env("INVALID_PASSWORD"),
    ),
    CredentialType.NO_PASSWORD: Credentials(
        username=_env("VALID_USERNAME"),
        password=" ",
    ),
}

def get_credentials(kind: CredentialType = CredentialType.VALID) -> Credentials:
    return _CREDENTIALS[kind]
