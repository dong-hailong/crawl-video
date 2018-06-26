# -*- coding: utf-8 -*-
import os
import scrapy
import json


class FenghuangSpider(scrapy.Spider):
    name = 'fenghuang'
    start_urls = [
    # 'https://vcis.ifeng.com/api/homePageList?adapterNo=7.4.10&channelId=24&city=%E5%8C%97%E4%BA%AC%E5%B8%82&deviceId=f6840ba6d024486ebdb81c8e6e97daaa&isInReview=0&isNotModified=1&isShowAd=1&isShowHeadline=0&lastDoc=%3C%2C6cd3830d-e1c7-4f43-bfa8-50d5b3f5f3ac%3E%7C%3C%2C2c956c20-0e92-4750-9e46-16cf08743df5%3E%7C%3C%2C16fa79a2-39ed-4110-a36b-0c90c72a41e4%3E&nw=wifi&operation=up&pageSize=20&platformType=iPhone&positionId=0&protocol=1.0.8&province=&publishid=20001&uptimes=&userId=',
    'https://vcis.ifeng.com/api/homePageList?adapterNo=7.4.10&channelId=24&city=%E5%8C%97%E4%BA%AC%E5%B8%82&deviceId=f6840ba6d024486ebdb81c8e6e97daaa&isInReview=0&isNotModified=1&isShowAd=1&isShowHeadline=0&lastDoc=%3C%2C329e2ea8-1887-403c-b0ec-4f4fd562a7c6%3E%7C%3C%2Cb2025b81-1b61-406a-8d01-086f601fbfb3%3E%7C%3C%2C6fc734bb-baca-4cfe-ae82-f4f9945a921c%3E%7C%3C%2Cf97d10b9-d5cd-4562-a00f-50e06ad2fb76%3E&nw=wifi&operation=down&pageSize=20&platformType=iPhone&protocol=1.0.8&province=%E5%B1%B1%E4%B8%9C%E7%9C%81&publishid=20001&requireTime=1529916709954&uptimes=9&userId='
    ]
    header = {
    'User-Agent':'Video 2.5.8 rv:2.5.8.3 (iPhone; iOS 11.4; zh_CN) Cronet'
    }

    def remove_video(self):
        path = '../tmp/fenghuang/ent/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)

    def start_requests(self):
        print '**********Fenfhuang crawling**********'
        self.remove_video()
        for url in self.start_urls:
            for i in range(1):
                positionId = 'positionId=' + str(i * 20)
                link = url.replace('positionId=0',positionId)
                yield scrapy.Request(link, headers=self.header, dont_filter=True, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas['bodyList']: #len(datas['bodyList'])=20
            if not data['title']:
                continue
            print data['title']
            url = data['memberItem']['videoFiles'][0]['mediaUrl']
            meta = {}
            meta['name'] = data['title'].replace(' ','')
            yield scrapy.Request(url, headers=self.header, meta=meta, callback=self.parse_data)

    def parse_data(self, response):
        path = "../tmp/fenghuang/ent/%s.mp4" %response.meta['name']

        file = open(path, 'aw')

        file.write(response.body)

        file.close()

