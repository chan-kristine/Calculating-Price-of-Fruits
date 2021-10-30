# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is __________.

def Value_Of_Apple():
    price_A = 20
    print(f"The price of an apple is {price_A} pesos.")
    return price_A


def Value_Of_Orange():
    price_O = 25
    print(f"The price of an orange is {price_O} pesos. ")
    return price_O


def quantity_of_A():
    ApplesQuantity = int(input("How many apples will you buy? "))
    return ApplesQuantity

def quantity_of_O():
    OrangesQuantity = int(input("How many oranges will you buy? "))
    return OrangesQuantity

def TotalPrice_():
    Apple_TP = price_A * ApplesQuantity
    Orange_TP = price_O * OrangesQuantity
    Total_Price = Apple_TP + Orange_TP
    return Total_Price


def display(Total_Price):
    print(f"The total amount is {Total_Price} pesos.")


# steps
# 1. show the price of an apple the set as variable.
price_A = Value_Of_Apple()
# 2. show the price of an orange then set as variable.
price_O = Value_Of_Orange()
# 3. ask how many apples will they buy then save to variable.
ApplesQuantity = quantity_of_A()
# 4. ask how many oranges will they buy then save to variable.
OrangesQuantity = quantity_of_O()
# 5. solve for the total price then save to variable.
Total_price = TotalPrice_()
# 6. display the total price
Total = display(Total_price)







