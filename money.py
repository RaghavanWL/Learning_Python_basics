import math
dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1
amount = int(input("enter amount in cents : "))

if (amount % dollar):
    no_of_dollar = math.floor(amount / dollar)
    amount %= dollar
    print("dollars = ", no_of_dollar)
if (amount % quarter):
    no_of_quarter = math.floor(amount / quarter)
    amount %= quarter
    print("quarter = ", no_of_quarter)
if (amount % dime):
    no_of_dime = math.floor(amount / dime)
    amount %= dime
    print("dime = ", no_of_dime)
if (amount % nickel):
    no_of_nickel = math.floor(amount / nickel)
    amount %= nickel
    print("nickel = ", no_of_nickel)
no_of_penny = amount
print("penny = ", no_of_penny)
# lol