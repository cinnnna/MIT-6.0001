# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:31:38 2024

@author: qiyuan
"""

annual_salary = float(input("The starting annual salary: "))
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = 0.25
r = 0.04 #annual investment rate
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12


start = 0
end = 10000

flag = 0
while (start <= end):
    
    mid = int((start+end) / 2)
    
    semi_annual_raise = 0.07

    total_cost = 1000000
    portion_down_payment = 0.25
    r = 0.04 #annual investment rate
    down_payment = total_cost * portion_down_payment
    monthly_salary = annual_salary / 12
     
    t_mid = 0 #number of months for the saving plan
    current_savings = 0 #include return on the investment and monthly savings
    portion_saved = mid / 10000
    while current_savings <= down_payment+100:   
        savings_salary = monthly_salary * portion_saved #portion saved from salary
        current_savings = current_savings * (1 + r/12) + savings_salary
        t_mid = t_mid + 1
        if t_mid % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    
    print(f"start: {start}, end: {end}, mid: {mid}， tmid: {t_mid}")
    if t_mid == 36:
        print(mid)
        flag = 1
        break
    elif t_mid > 36:
        start = mid
    else:
        end = mid
        
if flag == 0:
    print("It is not possible to pay the down payment in three years.")































