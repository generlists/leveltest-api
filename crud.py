from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

# 사용자 생성
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 모든 사용자 조회
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# 특정 사용자 조회
def get_user(db: Session, nickName: str):
    return db.query(User).filter(User.nickName == nickName).first()

# 사용자 삭제
def delete_user(db: Session, nickName: str):
    db_user = db.query(User).filter(User.nickName == nickName).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# 사용자 점수 저장 (테스트 완료 후 자동 저장)
def save_user_test_result(db: Session, user_data: UserCreate):
    db_user = db.query(User).filter(User.nickName == user_data.nickName).first()

    if db_user:
        db_user.totalScore = user_data.totalScore
        db_user.readScore = user_data.readScore
        db_user.writeScore = user_data.writeScore
        db_user.vocaScore = user_data.vocaScore
    else:
        db_user = User(**user_data.dict(exclude={"testCompleted"}), testCompleted=True)
        db.add(db_user)

    db.commit()
    db.refresh(db_user)
    return db_user

# 사용자 정보 조회
def get_user(db: Session, nickName: str):
    return db.query(User).filter(User.nickName == nickName).first()