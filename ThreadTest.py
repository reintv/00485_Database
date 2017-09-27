#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 01:14:18 2017

@author: root
"""

import threading

inputnum1 = input("number 1 please~")
inputnum2 = input("number 2 please~")
        
num1=int(inputnum1)
num2=int(inputnum2)

inputop = input("select : + , - , * , / ")
class operandThread(threading.Thread):

    def __init(self):
        threading.Thread.__init__(self)

    def run(self):
        if inputop == '+':
            print (inputnum1,' + ',inputnum2,' = ',(num1+num2))
        elif inputop == '-':
            print (inputnum1,' - ',inputnum2,' = ',(num1-num2))
        elif inputop == '*':
            print (inputnum1,' * ',inputnum2,' = ',(num1*num2))
        elif inputop == '/':
            print (inputnum1,' / ',inputnum2,' = ',(num1/float(num2)))
        else :
            print ("wrong operand")

        
t=operandThread()
t.start()
    
    
    
    