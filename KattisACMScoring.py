# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:30:20 2021

@author: dgary
"""
right = []
wrong = []
log = ''
rightNumbers = [] 
wrongCount = 0 
while log!='-1':
    log = input()
    if log!='-1':
        if 'right' in log.split() and not (log.split()[1] in rightNumbers):
            right.append(log.split())
            rightNumbers.append(log.split()[1])
        else:
            wrong.append(log.split())
for i in right:
    for x in wrong:
        if x[1] == i[1]:
            wrongCount +=1
score = (wrongCount * 20) 
for i in right:
    score+=int(i[0])
print(len(right),score)