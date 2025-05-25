import requests

# 配置 vLLM API 的 URL
VLLM_API_URL = "http://localhost:8000"  # 替换为实际的 vLLM 服务地址

def send_completion_request(prompt, model="facebook/opt-125m", max_tokens=50, temperature=0):
    """
    向 vLLM 的 /v1/completions 接口发送请求。

    Args:
        prompt (str): 输入的文本提示。
        model (str): 使用的模型名称。
        max_tokens (int): 生成的最大 token 数量。
        temperature (float): 控制生成的随机性。

    Returns:
        dict: vLLM 返回的响应数据。
    """
    # 构造请求数据
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        # 发送 POST 请求
        response = requests.post(VLLM_API_URL+"/v1/completions", json=payload)

        # 检查响应状态码
        if response.status_code == 200:
            return response.json()  # 返回 JSON 格式的响应数据
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求过程中发生错误: {e}")
        return None

def send_prepare_request(prompt, model="facebook/opt-125m", max_tokens=50, temperature=0):
    # 构造请求数据
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    try:
        # 发送 POST 请求
        response = requests.post(VLLM_API_URL+"/prepare", json=payload)

        # 检查响应状态码
        if response.status_code == 200:
            return response.json()  # 返回 JSON 格式的响应数据
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"请求过程中发生错误: {e}")
        return None

if __name__ == "__main__":
    # 示例输入
    prompt = "Once upon a time in a faraway land,"

    # 发送请求并获取响应
    response = send_prepare_request(prompt)

    # 打印响应结果
    if response:
        print("生成的文本:")
        for choice in response.get("choices", []):
            print(choice.get("text", ""))