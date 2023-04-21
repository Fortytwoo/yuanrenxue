import time

import subprocess
import json

import execjs


def call_js_function(function_name, *args):
    # 在JavaScript文件中加载特定函数
    with open('run.js', 'r') as f:
        js_code = f.read()
    ctx = execjs.compile(js_code)
    # 调用特定函数并返回结果
    return ctx.call(function_name, *args)


def get_data(timestr, page):
    import requests

    url = f"https://match.yuanrenxue.cn/api/match/2?page={page}"

    headers = {
        'authority': 'match.yuanrenxue.cn',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
        'cache-control': 'no-cache',
        'cookie': f'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1681695565; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1681695571; tk=8515465106525273049; sessionid=jxfv2g6c4ui1gxw1fboya80fdv43oqbm; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1681808568; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1681808615; m={call_js_function("endata", str(timestr))}|{timestr}',
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.cn/match/2',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'yuanrenxue.project;'
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()


if __name__ == '__main__':
    sum = 0
    for item in range(1, 6):
        timestr = int(time.time()) * 1000
        total = 0  # 初始化总和为0
        for item in get_data(timestr, page=str(item))['data']:
            total += item['value']
        sum = total + sum

    print(sum)
