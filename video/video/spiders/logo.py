# -*- coding: utf-8 -*-
import os
import sys
import datetime
import subprocess   
from configs import *
  
def logo_video(argv):
	app_name = argv[1]
	category = argv[2]
	app = apps.get(app_name)
	logo = app['logo']
	position = app['position']
	path1 = app['path'] %category #原视频路径
	path2 = "../data/%s/" %category   #处理后视频路径
	fileList = os.listdir(path1)
	for file in fileList:
		position1 = " -i ../tmp/logo/%s -filter_complex overlay=%s "% (logo,position)
		sub = "ffmpeg -i " + path1 + file + position1 + path2 + file + ''
		videoresult = subprocess.Popen(args=sub, shell=True)

def remove_file(argv):
	app_name = argv[1]
	app = apps.get(app_name)
	path1 = app['path']
	fileList = os.listdir(path1)

	for file in fileList:
		os.remove(path1+file)


if __name__ == '__main__':
	logo_video(sys.argv)
	# remove_file(sys.argv)



# 左上角	10:10
# 右上角	main_w-overlay_w-10:10
# 左下角	10:main_h-overlay_h-10
# 右下角	main_w-overlay_w-10 : main_h-overlay_h-10