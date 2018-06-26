#!/bin/sh

cd ../spiders/

echo '==============START=============='

#凤凰视频（娱乐）
/usr/local/bin/scrapy crawl fenghuang
# python logo.py fenghuang ent

# #凤凰新闻（影视,娱乐,游戏）
/usr/local/bin/scrapy crawl fhnews -a category=movie
# python logo.py fhnews movie
/usr/local/bin/scrapy crawl fhnews -a category=ent
# python logo.py fhnews ent
/usr/local/bin/scrapy crawl fhnews -a category=game
# python logo.py fhnews game

# #网易新闻（影视）
/usr/local/bin/scrapy crawl wangyi
# python logo.py wangyi movie

#新浪新闻（影视）
/usr/local/bin/scrapy crawl xinlang
# python logo.py xinlang movie

#百度视频（影视）
/usr/local/bin/scrapy crawl baidu
# python logo.py baidu movie

echo '==============DONE=============='