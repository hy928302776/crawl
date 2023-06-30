import datetime
import json
import time
import urllib

import requests

if __name__ == '__main__':
    dateStr = "2023-06-30 16:58:11"
    crawUrl = "https://api.crawlbase.com/?token=gRg5wZGhA4tZby6Ihq_6IQ&"
    domainurl = "https://search-api-web.eastmoney.com/search/jsonp?cb=jQuery35107761762966427765_1687662386467"
    param = {"uid": "4529014368817886", "keyword": "002624", "type": ["cmsArticleWebOld"], "client": "web",
             "clientType": "web", "clientVersion": "curr", "param": {
            "cmsArticleWebOld": {"searchScope": "default", "sort": "default", "pageIndex": 1,
                                 "pageSize": 10,
                                 "preTag": "<em>", "postTag": "</em>"}}}
    u = urllib.parse.quote(f"{domainurl}&param={urllib.parse.quote(json.dumps(param))}")

    url = f"{crawUrl}url={u}"
    print(url)  # 用于检查
    response = requests.get(url, verify=False, timeout=30)  # 禁止重定向
    print(response.text)