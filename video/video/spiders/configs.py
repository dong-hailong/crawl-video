# -*- coding: utf-8 -*-

apps = dict(
	baidu = dict(
		position = 'main_w-overlay_w-20:20',
		logo = 'logo1.jpg',  #300x100
		path = '../tmp/baidu/%s/',
		),
	xinlang = dict(
		position = 'main_w-overlay_w-20:20',
		logo = 'logo2.jpg',  #200x80
		path = '../tmp/xinlang/%s/',
		),
	wangyi = dict(
		position = 'main_w-overlay_w-10:10',
		logo = 'logo3.jpg',  #140x40
		path = '../tmp/wangyi/%s/',
		),
	fenghuang = dict(
		position = 'main_w-overlay_w-10:10',
		logo = 'logo3.jpg',  #140x40
		path = '../tmp/fenghuang/%s/',
		),
	fhnews = dict(
		position = 'main_w-overlay_w-10:10',
		logo = 'logo3.jpg',  #140x40
		path = '../tmp/fhnews/%s/',
		),
)


# 左上角	10:10
# 右上角	main_w-overlay_w-10:10
# 左下角	10:main_h-overlay_h-10
# 右下角	main_w-overlay_w-10 : main_h-overlay_h-10