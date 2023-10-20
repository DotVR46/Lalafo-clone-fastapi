from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str | None = None
    phone: str
    bio: str | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
