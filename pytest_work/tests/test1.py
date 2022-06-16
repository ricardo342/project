# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test1
@time:2022/6/16
@Author:majiaqin 170479
@Desc:测试文件
'''
import os

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

if __name__ == '__main__':
    # pytest 使用 . 标识测试成功（PASSED）
    os.system("pytest D:\\project\\pytest_work\\tests\\test1.py")
'''
示例如下:
============================= test session starts =============================
platform win32 -- Python 3.8.1, pytest-7.1.2, pluggy-1.0.0
rootdir: D:\project\pytest_work\tests
collected 1 item

test1.py .                                                               [100%]

============================== 1 passed in 0.02s ==============================
'''