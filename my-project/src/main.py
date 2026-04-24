import pandas as pd
import requests
import io

# ==========================================
# 模拟日志数据 (Mock Logs)
# ==========================================
MOCK_LOG_DATA = """timestamp,error_type,message
2026-04-24 10:00:01,SyntaxError,invalid syntax at line 12
2026-04-24 10:05:22,ValueError,invalid literal for int() with base 10
2026-04-24 10:10:15,RuntimeError,network timeout after 30s
2026-04-24 10:12:00,ValueError,invalid literal for int() with base 10
2026-04-24 10:15:45,SyntaxError,unexpected EOF while parsing
2026-04-24 10:20:30,ValueError,division by zero
"""

class FaultAnalyzer:
    def __init__(self):
        self.df = None
        self.report_df = None

    def fetch_logs(self, url=None):
        """需求 1: 使用 requests 读取模拟日志"""
        print("--- 正在获取日志数据 ---")
        try:
            if url:
                response = requests.get(url)
                response.raise_for_status()
                data = response.text
            else:
                data = MOCK_LOG_DATA
            
            self.df = pd.read_csv(io.StringIO(data))
            print("日志读取成功！")
        except Exception as e:
            print(f"读取日志失败: {e}")

    def analyze_faults(self):
        """需求 2: 使用 pandas 统计错误频率"""
        if self.df is None:
            return None

        print("\n--- 正在分析错误频率 ---")
        # 将统计结果转换为 DataFrame 格式，方便后续保存
        # reset_index() 会将原本作为 index 的错误类型变成一列
        error_counts = self.df['error_type'].value_counts().reset_index()
        error_counts.columns = ['error_type', 'frequency']
        
        self.report_df = error_counts
        print(self.report_df)
        
        # 返回出现频率最高的错误类型
        return self.report_df.iloc[0]['error_type']

    def save_report(self, filename="report.csv"):
        """将统计结果保存为 CSV 文件"""
        if self.report_df is not None:
            try:
                self.report_df.to_csv(filename, index=False, encoding='utf-8-sig')
                print(f"\n[系统] 统计报告已成功保存至: {filename}")
            except Exception as e:
                print(f"保存失败: {e}")
        else:
            print("没有可用的分析数据进行保存。")

    def ai_agent_fix_suggestion(self, error_type):
        """需求 3: AI Agent 提供修复建议"""
        print(f"\n--- AI Agent 正在分析最高频错误: {error_type} ---")
        suggestions = {
            "SyntaxError": "建议：检查代码缩进、括号是否闭合以及冒号是否遗漏。",
            "ValueError": "建议：检查数据转换逻辑，并确保输入值格式正确。",
            "RuntimeError": "建议：检查网络连接状态或资源释放逻辑。"
        }
        suggestion = suggestions.get(error_type, "建议：请查看官方文档。")
        print(f"修复建议: {suggestion}")

def main():
    analyzer = FaultAnalyzer()
    
    # 1. 获取日志
    analyzer.fetch_logs()
    
    # 2. 分析日志并保存报告
    most_frequent_error = analyzer.analyze_faults()
    analyzer.save_report("report.csv")  # 执行保存逻辑
    
    # 3. AI 修复建议
    if most_frequent_error:
        analyzer.ai_agent_fix_suggestion(most_frequent_error)

if __name__ == "__main__":
    main()