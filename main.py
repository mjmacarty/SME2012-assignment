"""
Created on Fri Apr  3 16:41:19 2020

@author: mjmacarty
"""
pv = float(input("Please enter current investment value: "))
time = int(input("Please enter years until retirement: "))
rate = float(input("Please enter expected rate of return: "))

fv = pv * (1 + rate/100) ** time

print("Your ending value based on inputs is: ${:,.0f}".format(fv))

answer = input("Would you like to add money each year? ")

if answer == "no":
    print ("Thank you! Have a nice day")
    
else:
    annual = int(input("How much do you plan to add each year? "))
    ending_values = []
    for year in range(time):
        ending_values.append((pv+annual) * (1+rate/100))
        pv = ending_values[-1]
    print("Your revised ending value is: ${:,.0f}".format(ending_values[-1]))
    print("Thank you! Have a nice day")