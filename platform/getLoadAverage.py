#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-

import time
import psutil

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(psutil.boot_time())))

print(psutil.cpu_times())
print(psutil.disk_partitions())
print(psutil.disk_usage('D:\\'))

print(psutil.swap_memory())