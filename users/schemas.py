from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None = None
    phone: str
    bio: str | None = None
