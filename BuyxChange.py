# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ____ apples and your change is ____ pesos.


def amount_of_Money():
    Money_ = int(input("How much money do you have? "))
    return Money_

def price_of_Apple():
    Apple_price = int(input("How much is an apple? "))
    return Apple_price

def Total_of_Apples():
    Total_A = money // apple_Price
    return Total_A

def Change():
    _change = money % apple_Price
    return _change

def display(t_apples, change):
    print(f"You can buy {t_apples} apples and your change is {change} pesos.")


# steps
# 1. ask for the amount of money you have then save to variable
money = amount_of_Money()
# 2. ask for the price of an apple then save to variable
apple_Price = price_of_Apple()
# 3. solve for the total amount of apples you can buy then save to variable
t_apples = Total_of_Apples()
# 4. solve for the change then save to variable
change = Change()
# 5. display the total number of apples and the change
display(t_apples, change)