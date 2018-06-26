# -*- coding: utf-8 -*-
import os
import scrapy
import json
import time

class FenfhuangnewsSpider(scrapy.Spider):
    name = 'fhnews'
    category = 'movie'
    movie_start_urls = [
    'https://api.iclient.ifeng.com/ClientNews?id=VIDEOMOVI&action=down&pullNum=1&ts=2018-06-15%2011%3A21%3A43&gv=6.1.8&av=0&proid=ifengnewsdiscovery&os=ios_11.4&vt=5&screen=1242x2208&publishid=4002&uid=f6840ba6d024486ebdb81c8e6e97daaa&nw=wifi&st=1529378503&sn=4bc6b9c2c8c444a5f56e526629b21906&dlt=35.725852&dln=116.909277&dcy=%E6%B3%B0%E5%AE%89%E5%B8%82&dpr=%E5%B1%B1%E4%B8%9C%E7%9C%81'
    ]
    ent_start_urls = [
    'https://api.iclient.ifeng.com/ClientNews?id=VIDEOENT&action=down&pullNum=1&province=%E5%B1%B1%E4%B8%9C%E7%9C%81&city=%E6%B3%B0%E5%AE%89%E5%B8%82&district=%E5%AE%81%E9%98%B3%E5%8E%BF&sptype=1&gv=6.1.8&av=6.1.8&uid=865737022353834&deviceid=865737022353834&proid=ifengnews&os=android_19&df=androidphone&vt=5&screen=720x1280&publishid=6101&nw=wifi&loginid=&st=1529378503&sn=bad1b11045176e25cb62bafe89ce680f&dlt=35.726413&dln=116.908794&dcy=%E6%B3%B0%E5%AE%89%E5%B8%82&dpr=%E5%B1%B1%E4%B8%9C%E7%9C%81'
    ]
    game_start_urls = [
    'https://api.iclient.ifeng.com/ClientNews?id=VIDEOSHORTGAME&action=down&pullNum=1&ts=2018-06-15%2010%3A50%3A17&gv=6.1.8&av=0&proid=ifengnewsdiscovery&os=ios_11.4&vt=5&screen=1242x2208&publishid=4002&uid=f6840ba6d024486ebdb81c8e6e97daaa&nw=wifi&st=1529378503&sn=01afc87e552965a5378a5b693f627bc9&dlt=35.725902&dln=116.908896&dcy=%E6%B3%B0%E5%AE%89%E5%B8%82&dpr=%E5%B1%B1%E4%B8%9C%E7%9C%81'
    ]
    header = {}
    cookies = {}

    def __init__(self, category='movie'):
        self.category = category
        if category == 'movie':
            self.start_urls = self.movie_start_urls
        elif category == 'ent':
            self.start_urls = self.ent_start_urls
        elif category == 'game':
            self.start_urls = self.game_start_urls

    def remove_video(self):
        path = '../tmp/fhnews/movie/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)
        
        path = '../tmp/fhnews/ent/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)
        
        path = '../tmp/fhnews/game/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)

    def start_requests(self):
        print '**********Fenfhuangnews crawling**********'
        self.remove_video()
        for url in self.start_urls:
            for i in range(1):
                time.sleep(2)
                pullNum = 'pullNum=' + str(i)
                datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) .split(' ')[0]
                timestamp = str(time.time()).split('.')[0]
                link = url.replace('pullNum=1',pullNum).replace('2018-06-15',datetime).replace('1529378503',timestamp)
                yield scrapy.Request(link, headers=self.header, cookies=self.cookies, dont_filter=True, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.body)
        try:
            for data in datas[0]['item']: #len(datas[0]['item'])=6
                print data['title']
                url = data['link']['mp4']
                meta = {}
                meta['name'] = data['title'].replace(' ','')
                yield scrapy.Request(url, headers=self.header, meta=meta, callback=self.parse_data)
        except:
            pass

    def parse_data(self, response):
        if self.category == 'movie':
            path = "../tmp/fhnews/movie/%s.mp4" %response.meta['name']
        elif self.category == 'ent':
            path = "../tmp/fhnews/ent/%s.mp4" %response.meta['name']
        elif self.category == 'game':
            path = "../tmp/fhnews/game/%s.mp4" %response.meta['name']

        file = open(path, 'aw')

        file.write(response.body)

        file.close()

