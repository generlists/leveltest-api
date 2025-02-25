# AI 레벨 테스트 점수 채점 코드
fastapi ,  chatgpt 를 사용하여 채점,문제 ,분석 결과를 만든다.
 **1. git 파일 다운로드**
  `$git clone https://github.com/generlists/leveltest-api`
 **2.  open ai API 요청을 위한 .env 파일 만들기**
    $ cd  leveltest-api
    $leveltest-api$ mkdir .env
    $leveltest-api$ open .env
OPENAI_API_KEY={OPEN AI API 키 입력}

**3. requirement.txt 에 있는 필수 라이브러리 설치**
**4. 서버 시작**
**[Start fastapi server]**
uvicorn main:app --host 0.0.0.0 --port 8000
**[fastapi server in houp mode]**
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &

필요에 따라서 aws  EC2 서버에 적용하여 테스트 할 수있다.
**[테스트 ]**
post man 으로 가능
http://localhost:8000/user-answer
header
Content-Type  :  application/json
Accept : application/json
body 에 아래 json 입력
{
"nickName": "이쁘니",
"level": "몇개의 단어 정도알고 있음",
"answer": [
{
"questionIndex": 0,
"question": "1.다음 문장에서 빈칸에 들어갈 올바른 단어를 고르세요.\n\"He ___ to the store yesterday.\"",
"category": "문법",
"type": "객관식",
"userAnswer": "went",
"correctAnswer": "went"
},
{
"questionIndex": 1,
"question": "2. 다음 문장에서 빈칸에 들어갈 올바른 단어를 고르세요.\n\"She ___ a book.\"",
"category": "문법",
"type": "객관식",
"userAnswer": "read",
"correctAnswer": "reads"
},
{
"questionIndex": 2,
"question": "3.빈칸에 들어갈 올바른 전치사를 고르세요.\n\"We are interested ___ learning English.\"",
"category": "문법",
"type": "객관식",
"userAnswer": "in",
"correctAnswer": "in"
},
{
"questionIndex": 3,
"question": "4. 다음 문장에서 빈칸에 들어갈 올바른 단어를 고르세요.\n\"I ___ a student.\"",
"category": "문법",
"type": "객관식",
"userAnswer": "am",
"correctAnswer": "am"
},
{
"questionIndex": 4,
"question": "5.다음 문장을 올바르게 고치세요.\n\"He don't like apples.\"",
"category": "문법",
"type": "주관식",
"userAnswer": "He dosen't't like apples",
"correctAnswer": "doesn't"
},
{
"questionIndex": 5,
"question": "6. \"Big\"의 반의어는 무엇인가요?",
"category": "어휘",
"type": "객관식",
"userAnswer": "Small",
"correctAnswer": "Small"
},
{
"questionIndex": 6,
"question": "7.다음 중 \"지속적인\"의 영어 표현은 무엇인가요?",
"category": "어휘",
"type": "객관식",
"userAnswer": "Permanent",
"correctAnswer": "Continuous"
},
{
"questionIndex": 7,
"question": "8.\"Beautiful\"과 비슷한 의미를 가진 단어는 무엇인가요?",
"category": "어휘",
"type": "객관식",
"userAnswer": "Attractive",
"correctAnswer": "Attractive"
},
{
"questionIndex": 8,
"question": "9.\"행복\"이라는 뜻의 영어 단어는 무엇인가요?",
"category": "어휘",
"type": "객관식",
"userAnswer": "happiness",
"correctAnswer": "happiness"
},
{
"questionIndex": 9,
"question": "10. \"Fast\"의 동의어는 무엇인가요?",
"category": "어휘",
"type": "객관식",
"userAnswer": "Quick",
"correctAnswer": "Quick"
},
{
"questionIndex": 10,
"question": "11. 다음 단어를 사용하여 문장을 작성하세요.\n\n\"apple\"",
"category": "쓰기",
"type": "주관식",
"userAnswer": "i am appple",
"correctAnswer": "apple"
},
{
"questionIndex": 11,
"question": "12. 다음 단어를 사용하여 문장을 작성하세요.\n\n\"run\"",
"category": "쓰기",
"type": "주관식",
"userAnswer": "i am running now",
"correctAnswer": "run"
},
{
"questionIndex": 12,
"question": "13. 다음 단어를 사용하여 문장을 작성하세요.\n\n\"happy\"",
"category": "쓰기",
"type": "주관식",
"userAnswer": "i am a happy",
"correctAnswer": "happy"
},
{
"questionIndex": 13,
"question": "14. 다음 단어를 사용하여 문장을 작성하세요.\n\n\"dog\"",
"category": "쓰기",
"type": "주관식",
"userAnswer": "i dong",
"correctAnswer": "dog"
},
{
"questionIndex": 14,
"question": "15. 다음 단어를 사용하여 문장을 작성하세요.\n\n\"cat\"",
"category": "쓰기",
"type": "주관식",
"userAnswer": "i love cats",
"correctAnswer": "cat"
}
]
}
