캡스톤 프로젝트 소개 웹 (EC2 Docker, 또는 로컬) 
본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.

##1. 작품주제(Subject)
- 제목: 루틴팜
- 요약: 게임형 일정관리 앱 — 사용자의 일정을 “농장 육성 게임”처럼 즐겁게 관리할 수 있도록 구성

##2. 실용적 근거 (Rationale)
- 문제: 기존의 일정관리 앱은 딱딱하며 동기부여가 어려움
- 근거(수치/설문/사례): 구글 캘린더는 UI가 딱딱하고 심플하여 개인 일상을 관리하기 아쉬움
				타임트리는 개인보다는 협업에 중점
- 기대 가치: 일정관리 앱 시장의 지속적 성장 (https://www.verifiedmarketreports.com/ko/product/calendar-app-market/)

## 3. 핵심기능 (Features)
- 기능 1: 루틴 관리 시스템
	   - 사용자가 매일 또는 주간 루틴을 등록 및 관리 가능
	   - 루틴 완료 시 “작물 성장” 또는 “포인트 보상” 형태로 시각적 피드백 제공
- 기능 2: 경험치 및 레벨 시스템
	    - 루틴 달성 시 경험치 획득 → 유저 레벨 상승
	    - 레벨에 따라 농장 확장, 새로운 아이템 잠금 해제 등 보상 제공
- 기능 3: 통계 및 피드백 대시보드
	    - 주간/월간 루틴 수행률 시각화
	    - 카테고리별 루틴 성공률 분석 및 개선 가이드 제공

## 4. 구현환경 (Environment)
- Front-End (프론트엔드): React.js, TypeScript
- Back-End (백엔드): Node.js (Express.js), PostgreDB, JWT 기반 로그인
- Runtime (런타임): Docker 기반 컨테이너 환경, Node 20.x, Nginx Reverse Proxy
- Deploy(배포): 로컬 / AWS EC2 / (선택) AWS ECS

## 5. 팀원 구성 및 역할 (Team)
- 이름 : 김준형 - 프론트엔드 개발 (UI/UX, React, 배포 설정)
- 이름 : 이현규 - 백엔드 개발 (API 설계, DB 관리, 서버 운영)

## 6. 실행 방법 (Run)

docker compose up-build-d
# http://localhost:5000 < 프로젝트에 맞는 포트 또는 배포된 public IP >