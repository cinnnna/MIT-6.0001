# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:14:18 2024

@author: qiyuan
"""
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream house: "))
portion_down_payment = 0.25
r = 0.04 #annual investment rate
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12

t = 0 #number of months for the saving plan
current_savings = 0 #include return on the investment and monthly savings

while current_savings <= down_payment:   
    savings_salary = monthly_salary * portion_saved #portion saved from salary
    current_savings = current_savings * (1 + r/12) + savings_salary
    t = t + 1
print ("Number of months:",t)