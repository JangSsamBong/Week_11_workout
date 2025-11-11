# Python 공식 이미지 사용 (Flask 실행 환경)
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# Flask 및 필요한 라이브러리 설치
# requirements.txt 파일이 필요하지만, 여기서는 직접 설치 (Flask, Flask-CORS)
RUN pip install Flask Flask-CORS

# 프로젝트 파일 복사
# project_data.json, app.py, index.html을 컨테이너로 복사합니다.
COPY project_data.json .
COPY app.py .
COPY index.html .

# Flask 애플리케이션 실행 포트 노출
EXPOSE 80

# 서버 실행 명령어 (app.py의 __name__ == '__main__' 블록이 실행됨)
CMD ["python", "app.py"]