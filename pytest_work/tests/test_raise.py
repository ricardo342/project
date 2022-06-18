# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test_raise
@time:2022/6/18
@Author:majiaqin 170479
@Desc:pytest异常捕获
'''
import pytest
'''pytest异常捕获使用pytest.raises'''
def test_raise():
    with pytest.raises(TypeError) as e:
        connect('localhost', '6379')
    exec_msg = e.value.args[0]
    assert exec_msg == 'port type must be int'

if __name__ == '__main__':
    pass