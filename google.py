import requests

if __name__ == '__main__':
    url2 = "https://www.google.com/search?q=002624&biw=927&bih=943&tbs=sbd%3A1%2Cqdr%3Ay&tbm=nws&sxsrf=APwXEddcIJHZ55oLS6VYThJ7c5B1gJ3jMw%3A1688120244411&ei=tKueZKvEGP_f4-EP4pmT2AI&ved=0ahUKEwir7oX84er_AhX_7zgGHeLMBCsQ4dUDCA0&oq=002624&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQDFAAWABgAGgAcAB4AIABAIgBAJIBAJgBAA&sclient=gws-wiz-news"
    url3 = "https://www.google.com/search?q=002624&amp;biw=927&amp;bih=943&amp;tbs=sbd%3A1%2Cqdr%3Ay&amp;tbm=nws&amp;sxsrf=APwXEddcIJHZ55oLS6VYThJ7c5B1gJ3jMw%3A1688120244411&amp;ei=tKueZKvEGP_f4-EP4pmT2AI&amp;ved=0ahUKEwir7oX84er_AhX_7zgGHeLMBCsQ4dUDCA0&amp;oq=002624&amp;gs_lcp=Cgxnd3Mtd2l6LW5ld3MQDFAAWABgAGgAcAB4AIABAIgBAJIBAJgBAA&amp;sclient=gws-wiz-news"
    url4 = "https://www.google.com/search?q=002624&amp;amp;biw=927&amp;amp;bih=943&amp;amp;tbs=sbd%3A1%2Cqdr%3Ay&amp;amp;tbm=nws&amp;amp;sxsrf=APwXEddcIJHZ55oLS6VYThJ7c5B1gJ3jMw%3A1688120244411&amp;amp;ei=tKueZKvEGP_f4-EP4pmT2AI&amp;amp;ved=0ahUKEwir7oX84er_AhX_7zgGHeLMBCsQ4dUDCA0&amp;amp;oq=002624&amp;amp;gs_lcp=Cgxnd3Mtd2l6LW5ld3MQDFAAWABgAGgAcAB4AIABAIgBAJIBAJgBAA&amp;amp;sclient=gws-wiz-news"
    print(url4)  # 用于检查
    response = requests.get(url4, verify=False, timeout=30)  # 禁止重定向
    print(response.text)
