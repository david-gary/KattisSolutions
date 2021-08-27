# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:53:57 2021

@author: dgary
"""
while True:
    start = input()
    change = 0
    if int(start) == -1:
        break
    else: 
        lines = int(start)
        tot = 0
        for i in range(lines):
            speed, time = map(int, input().split(" "))
            change = abs(change - time)
            result = (speed*change)
            print(result)