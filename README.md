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
아래 파일을 postmain post 방식으로 입력후 전송 테스트
[postbody.json](https://github.com/user-attachments/files/18963617/postbody.json)
