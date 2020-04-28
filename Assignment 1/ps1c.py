# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:31:21 2020

@author: daniel
"""

# Problem Set 1, Part C
# Name: Daniel Guillermo
# Collaborators: Daniel Guillermo
# Time spent: 25 minutes

annual_salary = float(input('Input your annual salary: '))
total_cost = 1000000 #Total cost of dream home 1M
semi_annual_raise = .07 #Semi-annual raise in decimal
current_savings = float(0) #start with 0 savings
portion_down_payment = float(0.25) #25% down payment
r=0.04 #yearly anual return, 4%

epsilon=100 #tolerance of bisection
low=int(0) #portion saved low
high=int(10000) #portion saved high

guess = abs(high + low)//2 #fist guess potion saved of salary

num_of_guesses=0

if annual_salary*3 < total_cost*portion_down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(total_cost*portion_down_payment-current_savings) >= epsilon:
        portion_saved=guess/10000
        #have to reset conditions every time it loops in the while loop
        monthly_salary = annual_salary/12
        current_savings = float(0) #start with 0 savings
    
        for months in range(37): # Calculating savings after 36 months
            monthly_saving_returns = (current_savings*r)/12
        
            if months!=0:
                if months%6 == 0:
                    monthly_salary += monthly_salary*semi_annual_raise
                
                current_savings += monthly_salary*portion_saved + monthly_saving_returns
    
        num_of_guesses += 1 #bisection search
        if current_savings < total_cost*portion_down_payment:
            low= guess
        else:
            high = guess
            guess=abs(high + low)//2
    
    print(' ')
    print('Best savings rate:',portion_saved)
    print(' ')
    print('Steps in Bisection search:',num_of_guesses)

