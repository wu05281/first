import os, requests, bs4, threading

os.makedirs('xkcd', exist_ok=True)

def download_xkcd(startComic, endComic):
    for url_num in range(startComic,endComic):
        print('Downloading page https://xkcd.com/%s...' % url_num)
        res = requests.get('https://xkcd.com/%s/' % url_num)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
            continue
        # 根据id获取网页上的图片url
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')
        if len(comic_elem) == 0:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            print('Downloading comic image from url: %s' %comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()
            img_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(10000):
                img_file.write(chunk)
            img_file.close()

download_threads = []
# 0到1000，间隔100
for i in (0, 1000, 100):
    download_thread = threading.Thread(target=download_xkcd, args=(i, i+99))
    download_threads.append(download_thread)
    download_thread.start()
# 此处join的原理就是依次检验线程池中的线程是否结束，没有结束就阻塞直到线程结束，如果结束则跳转执行下一个线程的join函数。
for download_thread in download_threads:
    download_thread.join()

print('Done.')