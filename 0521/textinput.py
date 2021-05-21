# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:46:06 2021

@author: Mac_1
"""

import turtle as t
t.shape('turtle')
t.clear()
s = t.textinput("","이름을 입력하세요.")
t.write("안녕하세요"+s+"님 반갑습니다.")
for i in range(4):
    t. forward(100)
    t.left(90)