from collections import Counter

from urllib3.exceptions import InsecureRequestWarning

# http 代理
proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",

}


def fun1(page):
    import requests

    url = "https://match.yuanrenxue.cn/jssm"

    headers = {
        "Host": "match.yuanrenxue.cn",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "yuanrenxue.project;",
        "sec-ch-ua-platform": "Windows",
        "Accept": "*/*",
        "Origin": "https://match.yuanrenxue.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://match.yuanrenxue.cn/match/3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
        "Cookie": "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1681695565; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1681695571; tk=8515465106525273049; m=89cc62ff73ff4f4865ea4cefef993306|1681818482000; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1681882750; sessionid=jrw3ogkc4utypcwnfd77j473yl0w4nq6; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1681970028"

    }

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    session = requests.session()
    session.headers = headers
    # res = session.post(url=url, proxies=proxies, verify=False)
    res = session.post(url=url,  verify=False)
    headers = {
        'Host': 'match.yuanrenxue.cn',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'yuanrenxue.project',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://match.yuanrenxue.cn/match/3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8',
        'Cookie': f'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1681695565; no-alert3=true; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1681695571; tk=8515465106525273049; m=89cc62ff73ff4f4865ea4cefef993306|1681818482000; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1681882750; sessionid={res.headers["Set-Cookie"][10:42]}; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1681971233'
    }

    # response = session.request("GET", f"https://match.yuanrenxue.cn/api/match/3?page={page}", headers=headers,
    #                            proxies=proxies, verify=False)
    response = session.request("GET", f"https://match.yuanrenxue.cn/api/match/3?page={page}", headers=headers,
                                verify=False)
    return response.json()


if __name__ == '__main__':
    all_data = []
    for page_item in range(1, 6):
        all_data.append(fun1(page=page_item))

    value_counter = Counter()
    for data in all_data:
        for item in data['data']:
            value_counter[item['value']] += 1

    # 找到出现次数最多的value
    most_common_value = value_counter.most_common(1)[0][0]

    print(f"出现次数最多的value为：{most_common_value}")
