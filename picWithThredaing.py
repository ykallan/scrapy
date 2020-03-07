from lxml import etree
import requests
import time
import os
import threading
import queue


def get_img_in_page(i=1):
    global base_url
    while not q_page.empty():
        url_lists = q_page.get()
        # print('开始爬取第页面了')
        for url_list in url_lists:
            page = requests.get(url=base_url + url_list, headers=headers, timeout=5)
            page.encoding = 'utf-8'
            page = etree.HTML(page.text)
            title = page.xpath('//h1/text()')[0]

            if '?' in title:
                title = title.replace('?', 'a')
            print(title)
            dir_path = storage + title
            flag = os.path.exists(dir_path)
            if not flag:
                os.mkdir(dir_path)
            # 获取每个图片的scr
            time.sleep(1)
            img_srcs = page.xpath('//div[@class="content"]/a/img/@src')
            print(len(img_srcs))
            if len(img_srcs) == 0:
                img_srcs = page.xpath('//div[@class="content"]/img/@src')
                print('没有a的长度:'+str(len(img_srcs)))
            for img_src in img_srcs:

                img_data = requests.get(img_src, timeout=8).content
                # print(img_src)
                img_name = img_src.split('/')[-1]
                with open(dir_path + '/' + img_name+'.jpg', 'wb') as f:
                    f.write(img_data)
                time.sleep(1)
        print('页面爬取完毕，开始下一页')


def get_next_lists():
    start_time = time.time()
    # base_url_pre = 'http://j3f4.com/Wzlist/oumeixingai-'
    base_url_pre = 'http://j3f4.com/Wzlist/yazhousetu-'
    print('开始获取页面链接列表')
    for i in range(2, 74, 1):
        this_page = requests.get(url=base_url_pre + str(i) + '.html', headers=headers, timeout=5)
        this_resp = etree.HTML(this_page.text)
        this_lists = this_resp.xpath('//ul[@class="newslist"]/li/a/@href')
        q_page.put(this_lists)
        # get_img_in_page(i)
    print('获取页面链接列表完成')
    end_time = time.time()
    total_time = end_time - start_time
    print('用时：' + str(total_time))


def chec():
    storage = './pic/'
    dir_lists = os.listdir(storage)
    for dir_list in dir_lists:
        full_path = storage+dir_list
        try:
            os.rmdir(full_path)
        except OSError as f:
            pass


if __name__ == '__main__':

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    # 创建页面队列池
    q_page = queue.Queue()
    storage = './pic/'
    if not os.path.exists(storage):
        os.mkdir(storage)
    base_request = 'http://j3f4.com/Wzlist/oumeixingai.html'
    base_url = 'http://j3f4.com'
    response = requests.get(url=base_request, headers=headers, )
    resp = etree.HTML(response.text)
    url_lists = resp.xpath('//ul[@class="newslist"]/li/a/@href')
    q_page.put(url_lists)
    get_next_lists()

    # 多线程下载图片
    t1 = threading.Thread(target=get_img_in_page)
    t2 = threading.Thread(target=get_img_in_page)
    t3 = threading.Thread(target=get_img_in_page)
    t4 = threading.Thread(target=get_img_in_page)
    t5 = threading.Thread(target=get_img_in_page)
    t6 = threading.Thread(target=get_img_in_page)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    chec()

