import requests

def glados_checkin():
    url = "https://glados.rocks/api/user/checkin"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "你的Authorization令牌",  # 从教程获取，替换成你的
        "Cookie": "你的Cookie值",                  # 从浏览器开发者工具获取，替换成你的
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    json_body = {
        "token": "glados.one"
    }

    response = requests.post(url, headers=headers, json=json_body)
    if response.status_code == 200:
        print("签到成功:", response.json())
    else:
        print("签到失败，状态码:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    glados_checkin()
