from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

# Configuration
SECRET_KEY = "a_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

# Dummy user database
fake_users_db = {
    "test@example.com": {
        "hashed_password": pwd_context.hash("testpassword"),
        "role": "admin",
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username, "role": user["role"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/artifacts/")
async def read_artifacts(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"message": "Here are the artifacts"}

# Dummy SME whitelist
sme_whitelist = {"admin@example.com"}

@app.post("/artifacts/")
async def create_artifact(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        if username not in sme_whitelist:
            raise HTTPException(status_code=403, detail="User not authorized to create artifacts")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"message": "Artifact created"}

@app.post("/whitelist/add/")
async def add_to_whitelist(user_email: str, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role: str = payload.get("role")
        if role != "admin":
            raise HTTPException(status_code=403, detail="Only admins can modify the whitelist")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    sme_whitelist.add(user_email)
    return {"message": f"User {user_email} added to whitelist"}

@app.post("/whitelist/remove/")
async def remove_from_whitelist(user_email: str, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role: str = payload.get("role")
        if role != "admin":
            raise HTTPException(status_code=403, detail="Only admins can modify the whitelist")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    sme_whitelist.discard(user_email)
    return {"message": f"User {user_email} removed from whitelist"}

@app.post("/premortem-risk-check/")
async def premortem_risk_check(text: str, token: str = Depends(oauth2_scheme)):
    """
    Performs a premortem risk check on a piece of text.
    """
    from generators.chaos_score import calculate_chaos_score

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    chaos_score = calculate_chaos_score(text)
    risk_level = "low"
    if chaos_score > 7:
        risk_level = "high"
    elif chaos_score > 4:
        risk_level = "medium"

    return {"chaos_score": chaos_score, "risk_level": risk_level}

@app.post("/workflow/run/")
async def run_workflow(token: str = Depends(oauth2_scheme)):
    """
    Placeholder for running a workflow.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return {"message": "Workflow run initiated"}

@app.post("/distribute/")
async def distribute_artifact(channel: str, text: str, token: str = Depends(oauth2_scheme)):
    """
    Distributes an artifact to a specified channel.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    if channel == "slack":
        from connectors.slack_connector import send_slack_message
        send_slack_message("general", text)
        return {"message": f"Artifact distributed to Slack channel: general"}
    elif channel == "twitter":
        from connectors.twitter_connector import send_tweet
        send_tweet(text)
        return {"message": f"Artifact distributed to Twitter"}
    else:
        raise HTTPException(status_code=400, detail="Invalid channel")
