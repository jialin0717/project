import os
import pandas as pd
import openai

# 1. 日志分析逻辑：带自动容错处理 (Iteration 7 实现)
def analyze_logs_locally():
    file_path = 'logs.csv'
    # 如果文件不存在，自动生成模拟数据，确保演示不中断 (Iteration 7)
    if not os.path.exists(file_path):
        print("⚠️ [系统提示/시스템] 未找到 logs.csv，正在生成模拟数据进行分析...")
        df = pd.DataFrame({
            'error_type': ['ValueError', 'ValueError', 'SyntaxError', 'RuntimeError', 'ValueError'],
            'message': ['Invalid cast', 'Null pointer', 'Missing semicolon', 'Stack overflow', 'Input error']
        })
    else:
        df = pd.read_csv(file_path)
    
    counts = df['error_type'].value_counts().to_dict()
    print(f"\n✅ --- 统计结果 / 분석 결과 ---\n{counts}")
    return counts

# 2. 交互式 AI 诊断会话 (Iteration 8 & 14 实现)
def ai_chat_session(stats):
    print("\n🤖 --- 已进入 AI 诊断模式 (输入 'exit' 退出) ---")
    print("🤖 --- AI 진단 모드 시작 ('exit' 입력 시 종료) ---")
    
    # 严格遵循 Secrets Management 规范，从环境变量读取 Key (Iteration 8)
    # 正确用法：括号内是变量名字符串，用于匹配终端 export 的名字
    api_key = os.getenv("DEEPSEEK_API_KEY") 
    
    if not api_key:
        print("❌ 错误: 未检测到环境变量 DEEPSEEK_API_KEY。")
        print("❌ 오류: DEEPSEEK_API_KEY 환경 변수가 설정되지 않았습니다.")
        return

    # 初始化 DeepSeek 客户端 (兼容 OpenAI SDK)
    # Iteration 14: 供应商无关设计，指定 DeepSeek 的 API 地址
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com" 
    )
    
    while True:
        user_input = input("\n👤 您想了解这些报错的什么信息？ / 무엇이 궁금하신가요?\n> ")
        
        # 退出判断
        if user_input.lower() in ['exit', 'quit', '退出', '종료']:
            print("👋 退出诊断模式。 / 진단 모드를 종료합니다.")
            break
            
        try:
            # 调用 DeepSeek 对话模型 (Iteration 14)
            response = client.chat.completions.create(
                model="deepseek-chat", 
                messages=[
                    {
                        "role": "system", 
                        "content": (
                            "你是一名资深的 SRE 工程师。当前系统的错误统计如下：{stats}。"
                            "请根据统计结果提供专业的根因分析和修复建议。回答请使用中文。"
                        ).format(stats=stats)
                    },
                    {"role": "user", "content": user_input}
                ]
            )
            
            # 打印 AI 的诊断建议
            print(f"\n💡 AI 建议 / AI 조언: \n{response.choices[0].message.content}")
            
        except Exception as e:
            print(f"❌ AI 调用失败 / 호출 실패: {e}")

if __name__ == "__main__":
    # 执行流程：先统计，再进入交互诊断
    current_stats = analyze_logs_locally()
    ai_chat_session(current_stats)