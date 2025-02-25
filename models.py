from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# database.py에서 생성한 Base import
from database import Base


# Base를 상속 받아 SQLAlchemy model 생성
class User(Base):
    # 해당 모델이 사용할 table 이름 지정
    __tablename__ = "users"

    # Model의 attribute(column) 생성 -> "="를 사용하여 속성을 정의
    nickName = Column(String, primary_key=True, index=True)
    inputLevel = Column(String,index=True)
    totalScore = Column(Integer)
    readScore = Column(Integer, default=0)
    writeScore = Column(Integer, default=0)
    vocaScore = Column(Integer, default=0)
    testCompleted = Column(Boolean, default=False)

    # 다른 테이블과의 관계 생성
#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
