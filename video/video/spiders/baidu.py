# -*- coding: utf-8 -*-
import os
import scrapy
import json
import time
from urllib import unquote

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    start_urls = [
    'http://app.video.baidu.com/shortlist/?vendor_id=8AB1BD18-E3BA-4BA0-87E6-E210D121C7F2&version=7.17.1&appchID=1099a&channel=meizhuang&pn=1&tpull=feed&time=1529395187.862022&terminal=iphnative&md=iPhone&cuid=ce2a075cf1800cb6965315c069515a101bc5b3f5&reqPath=shortlist%2F&ios_ver=11.4&fstapktime=1528810958.327434'
    ]
    header = {}
    cookies = {}

    def remove_video(self):
        path = '../tmp/baidu/movie/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)

    def start_requests(self):
        print '**********baidu crawling**********'
        self.remove_video()
        for url in self.start_urls:
            for i in range(1):
                time.sleep(0.5)
                timestamp = str(time.time()).split('.')[0]
                link = url.replace('1529395187',timestamp)
                yield scrapy.Request(link, headers=self.header, cookies=self.cookies, dont_filter=True, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas['videos']:  #len(len(datas['videos']))=18
            print data['title']
            url = data['url']
            meta = {}
            meta['name'] = data['title'].replace(' ','')
            yield scrapy.Request(url, headers=self.header, meta=meta, callback=self.parse_item)

    def parse_item(self, response):
        url = unquote(response.body.split('var flashUrl = ')[-1].split(';')[0].split('video=')[-1].replace("'",""))
        meta = {}
        meta['name'] = response.meta['name']
        yield scrapy.Request(url, headers=self.header, meta=meta, dont_filter=True, callback=self.parse_data)

    def parse_data(self, response):
        path = "../tmp/baidu/movie/%s.mp4" %response.meta['name']

        file = open(path, 'aw')

        file.write(response.body)

        file.close()

