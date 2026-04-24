## 1. 프로젝트 개요
본 프로젝트는 로그 데이터를 자동으로 분석하여 오류 발생 빈도를 통계하고,  
AI를 활용하여 주요 오류에 대한 수정 제안을 제공하는 도구입니다.  

사용자는 로그 파일을 입력하면 ValueError, SyntaxError, RuntimeError 등의 발생 횟수를 확인할 수 있으며,  
AI 기반으로 오류 해결 방향을 제시받을 수 있습니다.

---

## 2. 문제 정의
프로그램 실행 중 발생하는 다양한 오류는 개발 과정에서 중요한 디버깅 정보이다.  
하지만 로그를 수작업으로 분석하는 것은 비효율적이며 시간이 많이 소요된다.  

따라서 본 프로젝트는 로그 데이터를 자동으로 분석하고,  
오류 유형별 빈도를 시각적으로 제공하며,  
AI를 통해 해결 방법까지 제안하는 것을 목표로 한다.

---

## 3. 기술 스택 및 선택 이유

### Python (pandas)
- 로그 데이터를 구조적으로 분석하기 위해 사용
- 오류 유형별 빈도 계산 및 데이터 처리에 적합

### requests
- AI API(OpenRouter) 호출을 위해 사용

### Docker
- 실행 환경을 통일하여 어떤 컴퓨터에서도 동일하게 실행 가능하도록 하기 위해 사용
- 환경 의존성 문제 해결

---

## 4. 주요 기능
- 로그 파일 자동 분석
- 오류 유형별 발생 빈도 계산
- CSV 파일(report.csv) 생성
- AI 기반 오류 수정 제안 제공

---

## 5. 프로젝트 구조

```

my-project/
├── Dockerfile
├── requirements.txt
├── src/
│   └── main.py
├── docs/
│   ├── ai-usage-log.md
│   └── ralph-log.md
└── README.md

````

---

## 6. Docker 실행 방법

```bash
docker build -t log-analyzer .
docker run log-analyzer
````

Docker 컨테이너 내에서 Python 프로그램이 실행되며,
로그 분석 결과가 출력되고 report.csv 파일이 생성된다.

---

## 7. 실행 결과


실행 결과:
[실행결과사진](7;06.png)
(ai사용후에 결과사진)(9;09.png)

 ValueError, SyntaxError, RuntimeError 발생 빈도 출력
 report.csv 파일 생성
 AI 기반 오류 수정 제안 출력

---

## 8. 협업 과정 (Git & PR)

 feature/analyzer-logic 브랜치에서 기능 개발
 Dockerfile 추가 및 실행 환경 구성
 PR(Pull Request)을 통해 코드 리뷰 및 병합 진행
 팀원 간 역할 분담:

   팀원 A: 로그 분석 기능 구현
   팀원 B: Docker 및 문서 작성

---

## 9. AI 활용

 ChatGPT를 활용하여 Dockerfile 기본 구조 생성
 Docker build 과정에서 발생한 오류를 분석 및 수정
 AI API(OpenRouter)를 활용하여 오류 해결 제안 기능 구현

---

## 10. 반복 개선 (Ralph Mode)

반복적인 개선 과정을 통해 프로젝트 완성도를 높였다.

 반복 1: 로그 분석 기능 구현
 반복 2: AI 모델 변경 (DeepSeek → OpenRouter)
 반복 3: Docker 환경 구성 및 실행 오류 해결

---

## 11. 한계 및 개선 방향

 현재는 제한된 오류 유형만 분석 가능
 AI 응답 품질이 모델에 따라 달라질 수 있음
 향후 다양한 로그 형식 지원 및 웹 인터페이스 추가 가능




