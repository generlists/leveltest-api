from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os
import json
from typing import List, Dict, Any
from dataclasses import dataclass, asdict
from collections import defaultdict

from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from pydantic import BaseModel
from typing import List
from database import get_db 

load_dotenv()

print(f"API Key: {os.environ.get("OPENAI_API_KEY")}")
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # This is the default and can be omitted
    
)


#  테이블 자동 생성
models.Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성
app = FastAPI()

# DB 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORS 설정 (Flutter와 통신 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Flutter 앱이 로컬에서 테스트 가능하도록 모든 origin 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@dataclass
class Answer(BaseModel):
    questionIndex:int
    question: str
    category: str
    type:str # "객관식" 또는 "주관식"
    userAnswer:str
    correctAnswer:str # 객관식만 참고, 주관식은 ChatGPT가 독립 채점

class AnswerRequest(BaseModel):
    nickName: str
    level: str   # 사용자의 초기 레벨 (ex: "몇개의 단어 정도알고 있음", "자기소개,간단한 질문 대답 가능", "일상적 대화,하루일과 설명 가능", "원어민,복잡한 업무 가능")
    answer: List[Answer]

class DetailScore(BaseModel):
    category: str
    score: int
    recommendUrl: str

class QuizResponse(BaseModel):
    user: Dict[str, Any]
    detailScore: List[DetailScore]

    
def convert_to_json(answer_list: List[Answer]) -> str:
    return json.dumps([asdict(answer) for answer in answer_list], ensure_ascii=False, indent=4)
# 객관식 채점 함수
def grade_multiple_choice(answer: Answer) -> int:
    return 5 if answer.userAnswer.strip().lower() == answer.correctAnswer.strip().lower() else 0

# 주관식 채점 함수 (ChatGPT 활용, 초기 레벨 반영)
def grade_open_ended(answer: Answer, user_level: str,totalAnswer:int) -> int:
    system_prompt = f"""
    사용자의 주관식 답변을 채점해주세요.
    
    - 사용자의 초기 영어 레벨: **{user_level}**
    - 문항: {answer.question}
    - 사용자의 답변: {answer.userAnswer}
  
    주관식 채점 기준:
    - 초급({user_level == "몇개의 단어 정도알고 있음"}): 기본적인 문법이 맞으면 점수 부여.
    - 중급({user_level == "자기소개,간단한 질문 대답 가능"}): 문법, 어휘, 문장 완성도를 고려하여 점수 부여.
    - 고급({user_level == "일상적 대화,하루일과 설명 가능"}): 문장의 자연스러움, 고급 단어 활용을 중점적으로 평가.
    - 원어민({user_level == "원어민,복잡한 업무 가능"}): 문장의 자연스러움, 고급 단어 활용,원어민 수준의 답변을 중점적으로 평가

    **채점 규칙 (절대 100점 초과 금지!)**
    - 객관식과 주관식을 포함한 최종 점수는 **100점을 넘지 않아야 합니다**.
    - 문항당 최대 10점,문제 단어가 포함되면 1점 부여, 최저 0점 부여.
    - 점수만 반환하세요. 예제 응답:
    ```
    7
    ```
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": system_prompt}],
        temperature=0.7,
        max_tokens=5
    )
    
    try:
        score = int(response.choices[0].message.content.strip())
        return min(max(score, 0), 10)  # 0~10점 범위 유지
    except ValueError:
        return 0

@app.post("/user-answer", response_model=QuizResponse)
async def user_answer(request: AnswerRequest,db: Session = Depends(get_db)):
    total_score = 0
    category_scores = defaultdict(lambda: {"score": 0, "recommendUrl": ""})
    total_questions = len(request.answer)
    # 객관식과 주관식 문제 처리
    for answer in request.answer:
        if answer.type == "객관식":
            score = grade_multiple_choice(answer)
        else:  # "주관식"
            score = grade_open_ended(answer, request.level,total_questions)

        total_score += score
        # 카테고리별 점수 합산 및 추천 URL 저장
        category_scores[answer.category]["score"] += score
        category_scores[answer.category]["recommendUrl"] = (
        "https://www.youtube.com/watch?v=oYpnKrjt8Pk&list=PLNM2vFPCLb8x2gHDm_sDLs6zErWJ0ZpPX"
        if answer.category in ["문법", "어휘"] else 
        "https://www.youtube.com/playlist?list=PLJqW1DCBFwzl6wS-8IFMspxQNT2H6-zeS"
        )

    # 100점을 초과하지 않도록 조정
    if total_score > 100:
        excess = total_score - 100
        for category in category_scores:
            if category_scores[category]["score"] > 0:
                deduction = min(category_scores[category]["score"], excess)
                category_scores[category]["score"] -= deduction
                total_score -= deduction
                excess -= deduction
            if total_score == 100:
                break

    # 카테고리별 점수 리스트 변환
    detail_scores = [
        {"category": category, "score": data["score"], "recommendUrl": data["recommendUrl"]}
        for category, data in category_scores.items()
    ]
    user_data = crud.UserCreate(
        nickName=request.nickName,
        inputLevel=request.level,
        totalScore=total_score,
        readScore=sum([s["score"] for s in detail_scores if s["category"] == "어휘"]),
        writeScore=sum([s["score"] for s in detail_scores if s["category"] == "쓰기"]),
        vocaScore=sum([s["score"] for s in detail_scores if s["category"] == "문법"])
    )
    db_user = crud.save_user_test_result(db, user_data)
    
    response_print = {
        "nickName": db_user.nickName,
        "totalScore": db_user.totalScore,
        "readScore": db_user.readScore,
        "writeScore": db_user.writeScore,
        "vocaScore": db_user.vocaScore,
        "testCompleted": db_user.testCompleted
    }
    print(response_print)
   
    # 최종 응답
    response_data = {
        "user": {
            "nickName": request.nickName,
            "totalScore": total_score
        },
        "detailScore": detail_scores
    }

    return response_data

#uvicorn main:app --reload