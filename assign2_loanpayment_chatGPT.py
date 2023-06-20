# -*- coding: utf-8 -*-
def calculate_monthly_repayment(PV, r, n):
    # Convert APR to monthly interest rate
    r = r / 100 / 12
    
    # Calculate the denominator term (1 - (1+r)^-n)
    denominator = 1 - (1 + r) ** -n
    
    # Calculate the monthly repayment amount
    Pmt = r * PV / denominator
    
    return Pmt

# Get user input for PV, r, and n
PV = float(input("Enter the loan amount (Present Value): $"))
r = float(input("Enter the annual interest rate (APR): "))
n = int(input("Enter the number of months: "))

# Call the function to calculate the monthly repayment amount
monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount: $", round(monthly_repayment, 2))
