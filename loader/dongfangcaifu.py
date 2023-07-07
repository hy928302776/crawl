import datetime
import json
import re
import sys
import urllib.parse
import requests
from bs4 import BeautifulSoup
from langchain.docstore.document import Document

from storage import store

normalUrl = "https://api.crawlbase.com/?token=gRg5wZGhA4tZby6Ihq_6IQ&url="
def download_page(url, para=None):
    crawUrl = f"{normalUrl}{urllib.parse.quote(url)}"
    if para:
        response = requests.get(crawUrl, params=para)
    else:
        response = requests.get(crawUrl)
    # response.encoding = response.apparent_encoding
    if response.status_code == 200:
        return response.text
    else:
        print("failed to download the page")


def eastmoney(code: str, type: str):  # 两个参数分别表示开始读取与结束读取的页码

    headers = ['date', 'source', 'link', 'title', 'text', 'code', 'createTime',]
    # 遍历每一个URL
    total = 0
    domainurl = "https://search-api-web.eastmoney.com/search/jsonp?cb=jQuery35107761762966427765_1687662386467"
    pageIndex = 1
    pageSize = 10
    flag = True

    while flag:
        param = {"uid": "4529014368817886", "keyword": code, "type": ["cmsArticleWebOld"], "client": "web",
                 "clientType": "web", "clientVersion": "curr", "param": {
                "cmsArticleWebOld": {"searchScope": "default", "sort":"time", "pageIndex": pageIndex,
                                     "pageSize": pageSize,
                                     "preTag": "<em>", "postTag": "</em>"}}}
        link = f"{domainurl}&param={urllib.parse.quote(json.dumps(param))}"

        print(f"link:{link}")  # 用于检查
        crawUrl = f"{normalUrl}{urllib.parse.quote(link)}"
        response = requests.get(crawUrl, verify=False, timeout=30)  # 禁止重定向
        print(response.text)
        content = re.findall('jQuery35107761762966427765_1687662386467\((.*)\)', response.text)[0]
        print(content)
        # 读取的是json文件。因此就用json打开啦
        result = json.loads(content)
        # 找到原始页面中数据所在地
        if result['code'] == 0:
            data = result['result']['cmsArticleWebOld']
            print(f"获取第{pageIndex}页的数据，大小为{len(data)}")
            storageList:list[Document] = []
            for i in range(0, len(data)):

                try:
                    date = data[i]['date']
                    if type == "1":
                        s_time = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').date()
                        now_time = datetime.datetime.now().date()
                        if s_time < now_time:
                            print(f"当天数据已经处理完成，跳出循环")
                            flag = False
                            break

                    total += 1
                    print(f"开始处理第{total}条数据：{data[i]}")
                    # 数据处理
                    print(f"获取第{total}条数据的link内容：{link}")
                    text = get_text(data[i]['url'])
                    source = data[i]['url']
                    title = data[i]['title']
                    # 写入
                    doc = Document(page_content=text,
                                   metadata={"source": source,
                                             "date": date,
                                             "title": title})
                    storageList.append(doc)

                    print(f"第{total}条数据处理完成")

                except Exception as e:
                    print(
                        f"获取第【{pageIndex}】页的第【{i}】条数据,title:{data[i]['title']},url:{data[i]['url']}时异常，异常信息：{e}")
            #存入矢量库
            if len(storageList)>0:
                store(storageList)

        if len(data) < pageSize:
            break
        pageIndex += 1

    print(f"处理完成，一共处理{total}条数据")


def get_text(url):
    soup = BeautifulSoup(download_page(url))
    pattern = re.compile("txtinfos")  # 按标签寻找
    all_comments = soup.find_all("div", {'class': pattern})
    if all_comments and len(all_comments) > 0:
        text1 = all_comments[0]
        con = text1.get_text()  # 只提取文字
    else:
        con = soup.get_text()
    return con


if __name__ == "__main__":
    # code = input('请输入股票代码：')
    # Start = input('请输入起始页：')
    # size = input('请输入每页大小：')
    # End = input('请输入结束页：')
    code = sys.argv[1]  # 股票代码
    type = sys.argv[2]  # 增量1，全量2
    eastmoney(code, type)
    # output_csv(result)
