# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 11:08:43 2018

@author: dchan
"""

'''
To calculate BMI of the given values.

'''



def calBMI(my_dict):
    BMI = list()     
    for wei,hei in my_dict.items():             
        wei_pounds = float(wei)*2.20462      
        hei_incs = float(hei)*0.39370
        res = (wei_pounds/(hei_incs**2))*703
        BMI.append(res) 
    #print(BMI)
    return BMI
Raw_WeightHeigh = {65:150,76:129,102:186,68:156,91:190} 
print(type(Raw_WeightHeigh))   
Raw_WeightHeigh_1 = {65:150,76:129,102:186,68:156,91:190} 
print(type(Raw_WeightHeigh_1))  
all_val = calBMI(Raw_WeightHeigh)
print(all_val)

all_bmi = map(calBMI,[Raw_WeightHeigh,Raw_WeightHeigh_1])
print(list(all_bmi))
print(type(all_bmi))
