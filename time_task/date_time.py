#! /usr/bin/env python3

import datetime

dt = datetime.datetime.now()
print('现在是%s年 %s月 %s日 %s点 %s分 %s秒' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))