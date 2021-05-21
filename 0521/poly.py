# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:32:50 2021

@author: Mac_1
"""

import turtle as t
t.shape('turtle')
t.clear()
n = int(input("몇은 각형을 그리겠어요"))

for i in range(n):
    t.forward(100)
    t.left(360//n)
