# 环境监控系统主程序
# 功能：模拟获取并打印环境监控数据（温度、湿度）

def get_env_data():
    """模拟获取环境监控数据"""
    env_data = {
        "temperature": 25.6,  # 温度（℃）
        "humidity": 60.2,     # 湿度（%）
        "timestamp": "2026-01-21 15:30:00"  # 数据采集时间
    }
    return env_data

def print_env_info():
    """打印环境监控信息"""
    data = get_env_data()
    print("=== 环境监控数据 ===")
    print(f"采集时间：{data['timestamp']}")
    print(f"温度：{data['temperature']} ℃")
    print(f"湿度：{data['humidity']} %")

# 执行主函数
if __name__ == "__main__":
    print_env_info()