from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    nickName: str
    inputLevel: Optional[str] = None
    totalScore: int = 0
    readScore: int = 0
    writeScore: int = 0
    vocaScore: int = 0
    testCompleted: bool = False  # 테스트 완료 여부

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    class Config:
        orm_mode = True