from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()

# Token-based authentication using HTTPBearer
security = HTTPBearer()

# Dummy token for example (in real apps, validate JWT or DB token)
VALID_TOKEN = "mysecrettoken123"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token


@app.get("/secure-data")
def get_secure_data(token: str = Depends(verify_token)):
    return {"message": "You have accessed secure data!", "token_used": token}

@app.get("/")
def landing_page():
    return {"message": "you are in landing page!"}
