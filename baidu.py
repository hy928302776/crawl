import requests

if __name__ == '__main__':
    domainurl = "http://www.baidu.com/s?ie=utf-8&medium=0&rtt=1&bsst=1&rsv_dl=news_t_sk&cl=2&wd=%E5%AE%8C%E7%BE%8E%E4%B8%96%E7%95%8C&tn=news&rsv_bp=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&oq=&rsv_btype=t&f=8&inputT=3&rsv_sug4=697"
    url2 = "http://www.baidu.com/s?ie=utf-8&medium=0&rtt=4&bsst=1&rsv_dl=news_t_sk&cl=2&wd=002624&tn=news&rsv_bp=1&oq=&rsv_btype=t&f=8"
    print(url2)  # 用于检查
    response = requests.get(url2, verify=False, timeout=30)  # 禁止重定向
    print(response.text)
