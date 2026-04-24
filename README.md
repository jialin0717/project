## 프로젝트 개요
본 프로젝트는 로그 데이터를 자동으로 분석하여 오류 발생 빈도를 통계하고,
AI를 활용하여 주요 오류에 대한 수정 제안을 제공하는 도구입니다.

## 사용 기술
- Python (pandas)
- Docker
- 
- ## 기술 선택 이유
- pandas: 데이터 처리 및 오류 빈도 분석에 적합
- Docker: 환경 의존성을 제거하고 동일한 실행 환경을 보장

## Docker 실행 방법
```bash
docker build -t log-analyzer .
docker run log-analyzer

실행 결과
ValueError, SyntaxError, RuntimeError 발생 빈도 출력
report.csv 파일 생성
AI 기반 오류 수정 제안 출력
![실행결과사진](7;06.png)
