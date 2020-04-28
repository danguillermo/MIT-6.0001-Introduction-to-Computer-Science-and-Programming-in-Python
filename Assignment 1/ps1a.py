# -*- coding: utf-8 -*-

# Problem Set 1, Part A
# Name: Daniel Guillermo
# Collaborators: Daniel Guillermo
# Time spent: 10 minutes

annual_salary = float(input('Input your annual salary: '))
portion_saved = float(input('How much of your salary, in decimal percentage, you want to save? '))
total_cost = float(input('Please input the total cost of your dream home: '))

current_savings = float(0)

portion_down_payment = float(0.25)

r=0.04 #yearly anual return, 4%

monthly_salary = annual_salary/12

num_of_months = int(0)

while (total_cost*portion_down_payment) > current_savings:
    monthly_saving_returns = (current_savings*r)/12
    current_savings += monthly_salary*portion_saved + monthly_saving_returns
    num_of_months += 1
    
print(' ')
print('Number of months:',num_of_months)