# AI 활용 기록 (AI Usage Log)

### 1. 코드 구조 재설계 보조
- **Prompt**: "Python의 `input()` 함수를 사용하여 지속적으로 대화하는 루프를 만들고, 이전 pandas 통계 결과를 OpenAI에 컨텍스트로 전달하는 방법은?"
- **AI 기여**: `ai_chat_session` 함수의 골격을 제공했으며, AI의 역할을 SRE 엔지니어로 정의하기 위해 `system role` 사용을 제안함.

### 2. 기술적 오류 해결 (Debugging)
- **Prompt**: "os.getenv가 None을 반환하며 OpenAIError가 발생할 때 원인과 해결 방법은?"
- **AI 기여**: 환경 변수 호출 메커니즘을 설명해주었으며, 민감한 정보를 소스 코드에서 분리하여 터미널의 `export` 명령어로 주입하는 보안 가이드를 제공함.

### 3. 환경 최적화
- **Prompt**: "macOS(Python 3.14) 환경에서 `pip freeze`를 통해 FastAPI와 OpenAI 라이브러리 버전을 고정하는 방법은?"
- **AI 기여**: 팀원 B와 동일한 개발 환경을 유지할 수 있도록 `requirements.txt` 업데이트 과정을 가이드함.