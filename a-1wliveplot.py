# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:13:58 2020

@author: jaija
"""

import matplotlib.pyplot as plt
import numpy as np
import serial



plt.ion()
fig = plt.figure()

x = list()
y= list()
z = list ()


ser = serial.Serial('COM4', 9600)
ser.close()
ser.open()

while True: 
    data = ser.readline()
    print(data.decode())
    
    x.append(data[:4].decode())
    y.append(data[6:10].decode())
    z.append(data[12:].decode())
    
    
    plt.scatter(float(data[:4].decode().strip(",")), float(data[6:10].decode().strip(",")), float(data[12:].decode().strip(",")))
    plt.show()
    plt.pause(.0001)
    
    

