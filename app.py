import json
from flask import Flask, jsonify, send_file, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
# CORS 설정: 모든 출처 허용 (API 테스트 용이성을 위해)
CORS(app) 

# 프로젝트 데이터를 로드합니다.
with open('project_data.json', 'r', encoding='utf-8') as f:
    PROJECT_DATA = json.load(f)

# 메인 페이지 및 기타 웹 페이지 경로 처리
@app.route('/')
@app.route('/<path:path>')
def serve_page(path=''):
    """
    모든 웹 요청을 단일 index.html로 라우팅합니다.
    클라이언트 측에서 URL 경로에 따라 내용을 렌더링합니다.
    """
    # /api/ 경로는 Flask API가 처리하도록 분리
    if path.startswith('api/'):
        # API 경로로 들어온 웹 요청은 404를 반환하거나 메인으로 리다이렉트 (여기서는 404)
        return "API path only", 404
    
    # 정적 파일 경로가 아닌 경우 index.html을 반환
    if '.' not in path:
        return send_file('index.html')
    
    # 그 외 정적 파일 요청 (만약 있다면)은 Flask가 자동으로 처리
    return send_file(path)


# API 경로 처리: /api/<page_name>
@app.route('/api/<page_name>', methods=['GET'])
def api_endpoint(page_name):
    """
    요청된 페이지 이름에 해당하는 JSON 데이터를 반환합니다.
    """
    page_key = page_name.lower()
    
    # 요청된 페이지 이름이 project_data.json에 정의된 키(subject, rationale 등)와 일치하는지 확인
    if page_key in PROJECT_DATA:
        # 해당 섹션의 전체 데이터를 반환합니다 (title_ko, path, data 포함)
        return jsonify(PROJECT_DATA[page_key]), 200
    
    # 정의된 API 경로가 아닐 경우
    return jsonify({"error": "Page not found", "available_apis": PROJECT_DATA['api_endpoints']}), 404

# 메인 API 엔드포인트: 프로젝트 제목과 API 목록 제공
@app.route('/api/main', methods=['GET'])
def api_main():
    """
    메인 페이지 정보를 반환합니다 (프로젝트 제목, API 엔드포인트 목록).
    """
    main_info = {
        "project_title": PROJECT_DATA['project_title'],
        "api_endpoints": PROJECT_DATA['api_endpoints'],
        "sections": {key: {"title": val["title_ko"], "path": val["path"]} 
                     for key, val in PROJECT_DATA.items() 
                     if isinstance(val, dict) and "path" in val}
    }
    return jsonify(main_info), 200

# Flask 개발 서버 실행 (Docker 환경에서 사용)
if __name__ == '__main__':
    # Docker/배포 환경에서 0.0.0.0 바인딩을 사용하여 외부 접속 허용
    app.run(host='0.0.0.0', port=80)