# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png"
    ]

    from collections import defaultdict
    file_names = defaultdict(int)
    for url in urls:
        file_name = url.split('/')[-1]
        file_names[file_name] += 1

    file_names = sorted(file_names.items(), key=lambda d: -d[1])
    for i in range(3):
        print(file_names[i][0], file_names[i][1])