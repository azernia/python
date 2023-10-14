"""
Python requests 模块的使用
"""
import requests
from threading import Thread


def req_baidu():
    url = "https://www.baidu.com"
    body = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    print(resp.text)


if __name__ == "__main__":
    for i in range(5):
        # 生成5个线程对象
        thread = Thread(target=req_baidu)
        # 执行线程
        thread.start()
