#!/usr/bin/python
# -*- coding: utf-8 -*-
# Do not reinventing the wheel
import platform
import sys
print(platform.system())

print(platform.platform())
print(platform.version())
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.processor())
print(platform.uname())

os_type = platform.system()
print(os_type)

if os_type == "Linux":
    print("Linux")
elif os_type == "Windows":
    print("Windows")
else:
    exit("Unknown Operating System!")

print(sys.version_info)
print(sys.platform)

