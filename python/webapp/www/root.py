#!/usr/bin/python
#coding=utf8

import socket

host = 'github.com'

try:
    with open('C:/Windows/System32/drivers/etc/hosts', 'a+') as fp: 
        ip = socket.gethostbyname(host)
        fp.write(' '.join([ip, host, '\n']))
except BaseException as e:
    print(e)
else:
    print('sucess')