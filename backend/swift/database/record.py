from pydantic import BaseModel


class User(BaseModel):
    uid: int | str | None = None
    username: str
    hashed_password: str | None

class Dialog(BaseModel):
    dialogid: int | str | None = None
    uid: int | str | None = None

class Message(BaseModel):
    messageid: int | str | None = None
    dialogid: int | str | None = None
    uid: int | str | None = None
    timestamp: str
    role: str
    message_type: str
    message: str