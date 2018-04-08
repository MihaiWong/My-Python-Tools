import requests
from bs4 import BeautifulSoup as bs

API = "http://www.xicidaili.com/nn/1"


def get_ip():
    header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/61.0.3163.91 Safari/537.36'
    headers = {'User-Agent': header}
    r = requests.get(API, headers=headers)
    html = bs(r.text, 'lxml')
    tr_list = html.find_all("tr")
    for tr in tr_list:
        tds = tr.text.split('\n')
        new_tds = list(filter(lambda x: x != '', list(tds)))
        if len(new_tds) == 7:
            dicts = {'IP地址': new_tds[0], '端口': new_tds[1], '服务器地址': new_tds[2], '是否匿名': new_tds[3],
                     '类型': new_tds[4], '存活时间': new_tds[5], '验证时间': new_tds[6]}
            print(dicts)
        else:
            continue
        print("-==-==-=-=-=-=-")


if __name__ == '__main__':
    get_ip()
