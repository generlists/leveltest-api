# AI 레벨 테스트 점수 채점 코드
fastapi ,  chatgpt 를 사용하여 채점,문제 ,분석 결과를 만든다.<br>
 **1. git 파일 다운로드** <br>
  `$git clone https://github.com/generlists/leveltest-api` <br>
 **2.  open ai API 요청을 위한 .env 파일 만들기** <br>
    $ cd  leveltest-api  <br>
    $leveltest-api$ mkdir .env <br>
    $leveltest-api$ open .env <br>
OPENAI_API_KEY={OPEN AI API 키 입력} <br>

**3. requirement.txt 에 있는 필수 라이브러리 설치** <br>
**4. 서버 시작** <br>
**[Start fastapi server]** <br>
uvicorn main:app --host 0.0.0.0 --port 8000 <br>
**[fastapi server in houp mode]** <br>
nohup uvicorn main:app --host 0.0.0.0 --port 8000 & <br>

필요에 따라서 aws  EC2 서버에 적용하여 테스트 할 수있다. <br>
**[테스트 ]** <br>
post man 으로 가능 <br>
http://localhost:8000/user-answer <br>
아래 파일을 postmain post 방식으로 입력후 전송 테스트 <br>
[postbody.json](https://github.com/user-attachments/files/18963617/postbody.json) <br>
