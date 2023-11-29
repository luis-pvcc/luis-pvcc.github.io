# Name: Amir Salamatolla, Luis Lopez
# Prog Purpose: pizza
import datetime

############ define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
S_PIZZA= 9.99
M_PIZZA = 12.99
L_PIZZA= 17.99
X_PIZZA= 21.99
DRINKS= 3.99
B_STICKS= 6.99



# define global variables
pizza_size= ""
num_pizza= 0
num_drinks= 0
num_bstick= 0

cost_pizza= 0
cost_drinks= 0
cost_bstick= 0

subtotal = 0
sales_tax = 0
total = 0

############ define program functions ############


def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "N":
            more = False
            print('Thank you for your order. Enjoy your food!')
   
def get_user_data():
    global pizza_size, num_pizza, num_drinks, num_bstick
    menu1= "\n\n********* Pizza Sizes *********\n\t S\tSmall\t $ 9.99\n\t M\tMedium\t $12.99"
    menu2= "\n\t L\tLarge\t $17.99\n\t X\tXLarge\t $21.99"
    menu3= "\nEnter the pizza size (S, M, L, X ): "
    wholemenu = menu1 + menu2 + menu3
    pizza_size = input(wholemenu)
    num_pizza = int(input("Number of Pizzas: "))
    num_drinks = int(input("Number of Drinks: "))
    num_bstick = int(input("Number of Breadsticks: "))

def perform_calculations():
    global subtotal, sales_tax, total, cost_pizza, cost_bstick, cost_drinks
    if pizza_size=="S" or pizza_size=="s":
        cost_pizza = S_PIZZA * num_pizza
    if pizza_size=="M" or pizza_size=="m":
        cost_pizza = M_PIZZA * num_pizza
    if pizza_size=="L" or pizza_size=="l":
        cost_pizza = L_PIZZA * num_pizza
    if pizza_size=="X" or pizza_size=="x":
        cost_pizza = X_PIZZA * num_pizza

    cost_drinks = DRINKS * num_drinks
    cost_bstick = B_STICKS * num_bstick
    subtotal = cost_pizza + cost_drinks + cost_bstick
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** Palermo Pizza ****')
    print('World Famous Pizza from Palermo Pizza')
    print(line)
    print('Pizzas           $ ' + format(cost_pizza, moneyformat))
    print('Drinks           $ ' + format(cost_drinks, moneyformat))
    print('Breadsticks      $ ' + format(cost_bstick, moneyformat))
    print('Subtotal         $ ' + format(subtotal, moneyformat))
    print('Sales Tax        $ ' + format(sales_tax, moneyformat))
    print('Total            $ ' + format(total, moneyformat))
    print(line)
    print(str(datetime.datetime.now()))


############ call on main program to execute ############
main()
