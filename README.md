## 프로젝트 개요
본 프로젝트는 로그 데이터를 자동으로 분석하여 오류 발생 빈도를 통계하고,
AI를 활용하여 주요 오류에 대한 수정 제안을 제공하는 도구입니다.

## 사용 기술
- Python (pandas)
- Docker

## Docker 실행 방법
```bash
docker build -t log-analyzer .
docker run log-analyzer

실행 결과
ValueError, SyntaxError, RuntimeError 발생 빈도 출력
report.csv 파일 생성
AI 기반 오류 수정 제안 출력
![실행결과](07;06.png)
