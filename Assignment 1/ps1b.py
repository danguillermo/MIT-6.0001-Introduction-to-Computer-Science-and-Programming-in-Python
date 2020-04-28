# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:46:01 2020

@author: daniel
"""

# Problem Set 1, Part B
# Name: Daniel Guillermo
# Collaborators: Daniel Guillermo
# Time spent: 15 minutes

annual_salary = float(input('Input your annual salary: '))
portion_saved = float(input('How much of your salary, in decimal percentage, you want to save? '))
total_cost = float(input('Please input the total cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

current_savings = float(0)

portion_down_payment = float(0.25)

r=0.04 #yearly anual return, 4%

monthly_salary = annual_salary/12

num_of_months = int(0)

while (total_cost*portion_down_payment) > current_savings:
    monthly_saving_returns = (current_savings*r)/12
    
    if num_of_months!=0:
        if num_of_months%6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise
        
    current_savings += monthly_salary*portion_saved + monthly_saving_returns
    num_of_months += 1
    
print(' ')
print('Number of months:',num_of_months)