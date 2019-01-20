# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    import requests
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    import os
    ua = UserAgent()
    header = {'User-Agent': str(ua.random)}
    # urlPttStock = 'https://www.ptt.cc/bbs/Stock/index.html'
    urlPttStock = 'https://www.ptt.cc/bbs/Stock/M.1547911939.A.5D2.html'

    while True:
        try:
            res = requests.get(urlPttStock, headers=header, timeout=10)
            if '批踢踢實業坊' not in res.text:
                continue
            else:
                soup = BeautifulSoup(res.text, 'html.parser')
                content = soup.find_all('div', attrs={'id':'main-container'})
                content_soup = BeautifulSoup(content, 'html.parser')
                print(content_soup.find_all('span', attrs={'class':'article-meta-value'}))

                os.sleep(1000)

                break
        except:
            print('error')