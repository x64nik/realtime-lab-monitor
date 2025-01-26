import os
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from dotenv import load_dotenv
load_dotenv()


API_KEY_NAME = os.getenv('API_KEY_NAME')
API_KEY_VALUE = os.getenv('API_KEY_VALUE')
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY_VALUE:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
        )
    return api_key