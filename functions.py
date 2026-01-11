import math
"""Radha is planning to buy a house that costs $1,260,000. She is 
considering two options to purchase her purchase.

-Option1. Maka an immediate down payment of $300,000 and take a 8-year loan
with interest rate of 10%(compounded monthly) for the remaining amount

-Option2. Take a 10 year loan with interest rate of 8%(compounde monthly)
for the entire amount.

Both of these loans have to be paid back in in equal monthly installments (EMIs).
Which loan has a lower EMI among the two?"""

def loan_emi(amount, duration, rate, down_payment=0):
    """Calculates the equal monthly installments (EMI) for a loan
    
    Arguments:
        amount - Total amount to be spent (loan + down_payment)
        duration - Duration of the loan (in months)
        rate - Rate of interest (monthly)
        down_payment (optional) - Optional intial payment (deducted from amount)
    """
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi

emi1 = loan_emi(amount=1.26e6, duration=8*12, rate=0.1/12, down_payment=3e5)
emi2 = loan_emi(amount=1.26e6, duration=10*12, rate=0.08/12)

print(f'emi1: {emi1}')
print(f'emi2: {emi2}')

if emi1 < emi2:
    print(f'Option1 has a lower EMI: ${emi1}')
else:
    print(f'Option2 has a lower EMI: ${emi2}')


"""Shaun is currently paying back a home loan for a house he took
a few years ago. The cost of the house was $800,000. Shaun made a down_payment of 25%
of the cost, and financed the remaining amount using a 6-year loan with an interest
rate of 7% per annum (compounded monthly). Shaun is now buying a car worth $60,000,
which he is planning to finance using a 1-year loan with an interest rate of 12%
per annum. Both loans are paid back in EMIs. What is the total monthly payment
Shaun makes towards loan repayment"""

cost_of_house = 8e5
house_down_payment = .25 * cost_of_house
house_loan_duration = 6*12 # months
house_loan_rate = 0.07/12 # monthly

emi_house = loan_emi(
    amount= cost_of_house,
    duration=house_loan_duration,
    rate=house_loan_rate,
    down_payment=house_down_payment
)
print(f'House EMI: ${emi_house}')

cost_of_car = 60000
car_loan_duration = 1*12 # months
car_loan_rate = .12/12 # monthly

emi_car = loan_emi(amount=cost_of_car, duration=car_loan_duration, rate=car_loan_rate)
print(f'Car EMI: ${emi_car}')

print(f'\nShaun makes a total monthly payment of ${emi_car + emi_house} per month.')


"""If you borrow $100,000 using a 10-year loan with an interest rate of 9%
per annum, what is the total amount you end up paying as interest?"""

emi_with_interest = loan_emi(amount=100000, duration=10*12, rate=0.09/12)
emi_without_interest = loan_emi(amount=100000, duration=10*12, rate=0./12)
print('Loan with interest: ${}\nLoan without interest: ${}'.format(emi_with_interest, emi_without_interest))