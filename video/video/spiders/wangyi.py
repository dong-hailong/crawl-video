# -*- coding: utf-8 -*-
import os
import scrapy
import json
import time

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    start_urls = [
    'https://c.m.163.com/recommend/getChanListNews?channel=T1457068979049&subtab=Video_Movies&passport=&devId=WiaVC0DV2NI9IIIOdfLo6qSq0CrowZfNZVbqWTmpGiNB0GQ/aDJiKtbWMfBIkZTM&version=37.2&spever=false&net=wifi&lat=SkKAD/LWeh3WA2qCJwLR9A%3D%3D&lon=7v7b9e79LQALHSB9CYCEag%3D%3D&ts=1529059519&sign=Ue8BF36Z7LK/kpZa6Y8VojUVn52qoqUbedveTHcfAsl48ErR02zJ6/KXOnxX046I&encryption=1&canal=appstore&offset=0&size=10&fn=4'
    ]
    header = {}
    cookies = {}

    def remove_video(self):
        path = '../tmp/wangyi/movie/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)

    def start_requests(self):
        print '**********Wangyi crawling**********'
        self.remove_video()
        for url in self.start_urls:
            for i in range(1):
                time.sleep(1)
                yield scrapy.Request(url, headers=self.header, cookies=self.cookies, dont_filter=True, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas[u'视频']:  #len(datas[u'视频'])=10
            print data['title']
            url = data['mp4_url']
            meta = {}
            meta['name'] = data['title'].replace(' ','')
            yield scrapy.Request(url, headers=self.header, meta=meta, callback=self.parse_data)

    def parse_data(self, response):
        path = "../tmp/wangyi/movie/%s.mp4" %response.meta['name']

        file = open(path, 'aw')

        file.write(response.body)

        file.close()

