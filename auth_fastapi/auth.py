from fastapi import FastAPI
from jose import jwt,JWTError
from datetime import datetime,timedelta



ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret app Key"

def create_access_token(subject: str , expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


app = FastAPI()

@app.get("/new_route")
def get_access_token(user_name: str):
    access_token_expires = timedelta(minutes=1)

    print("access_token_expires",access_token_expires)
    access_token = create_access_token(subject=user_name, expires_delta=access_token_expires)


    return {"access_token": access_token}



def decode_access_token(token:str):
    decode_access_token = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    return decode_access_token

    





