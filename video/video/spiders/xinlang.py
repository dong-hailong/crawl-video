# -*- coding: utf-8 -*-
import os
import scrapy
import json
import time

class XinlangSpider(scrapy.Spider):
    name = 'xinlang'
    start_urls = [
    'http://newsapi.sina.cn/?resource=feed&abt=229_271_155_191_231_141_16_323_13_23_237_332_203_297_299_277_279_241_31_128_205_149_207_249_171_135_341_251_113_343_253_143_18_255_21_347_307_217_349_287_37_29_222_45_61_267_291_65_111&abver=1529907660692&accessToken=2.00ShE5kGe3vYNCf4f49ae395hfy51D&authGuid=6412933621623337908&authToken=ca9f0645a88350816f66994fc9110d87&authUid=6412933627604415523&chwm=3023_0001&city=WMXX2972&connectionType=2&deviceId=5c0ead5e9b944fe528d45673f27321764f156f76&deviceModel=apple-6splus&from=6069293012&idfa=F6840BA6-D024-486E-BDB8-1C8E6E97DAAA&idfv=FD390329-E39D-4013-866F-CC3719BAC52A&imei=5c0ead5e9b944fe528d45673f27321764f156f76&location=39.940714%2C116.437324&loginType=1&osVersion=11.4&resolution=1242x2208&seId=a6b2eba336&ua=apple-6splus__SinaNews__6.9.2__iphone__11.4&unicomFree=0&weiboSuid=9ad2eab840&weiboUid=6182246380&wm=b207&rand=745&urlSign=ded7a8f2de&behavior=auto&channel=video_movie&creUserExt=&downTimes=1&downTotalTimes=1&lastTimestamp=&listCount=0&p=1&pullDirection=down&pullTimes=1&replacedFlag=0&s=20&upTimes=0&upTotalTimes=0'
    ]
    header = {}
    cookies = {}

    def remove_video(self):
        path = '../tmp/xinlang/movie/'
        fileList = os.listdir(path)
        for file in fileList:
            os.remove(path+file)

    def start_requests(self):
        print '**********Xinlang crawling**********'
        self.remove_video()
        for url in self.start_urls:
            for i in range(1):
                time.sleep(2)
                # timestamp = int(round(time.time() * 1000))
                # link = url.replace('1529907660692',str(timestamp))
                yield scrapy.Request(url, headers=self.header, cookies=self.cookies, dont_filter=True, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.body)
        for data in datas['data']['feed']:  #len(datas['data']['feed'])=10
            print data['title']
            url = data['videoInfo']['url']
            meta = {}
            meta['name'] = data['title'].replace(' ','')
            yield scrapy.Request(url, headers=self.header, meta=meta, callback=self.parse_data)

    def parse_data(self, response):
        path = "../tmp/xinlang/movie/%s.mp4" %response.meta['name']

        file = open(path, 'aw')

        file.write(response.body)

        file.close()

