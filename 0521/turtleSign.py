# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:29:12 2021

@author: Mac_1
"""

import turtle as t
 
t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 암수입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100, -100)
t.write(" 거북이가 여기로 오면 응수입니다.")

t.goto(0.0)
t.pendown()
s = t.textinput("부호", "점수를 입력하세요")
n = int(s)

if n >0 :
   t.goto(100, 100)
elif n == 0:
   t.goto(100, 0)
else:
   t.goto(100, -100)
    
t.exitoncick() 