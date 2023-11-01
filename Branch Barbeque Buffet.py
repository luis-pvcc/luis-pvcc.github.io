# Name: Luis Lopez


# Define global variables
ADULT_MEAL_PRICE = 19.95
CHILD_MEAL_PRICE = 11.95
SERVICE_FEE_RATE = 0.10  # 10%
SALES_TAX_RATE = 0.062  # 6.2%

def main():
    more_customers = True

    while more_customers:
        get_user_data()
        perform_calculations()
        display_results()

        yes_no = input("\nWould you like to serve another customer (Y or N)? ")
        if yes_no.lower() == "n":
            more_customers = False
            print("Thank you for your business. Have a great day!")

def get_user_data():
    global num_adults, num_children
    num_adults = int(input("Number of adults in the party: "))
    num_children = int(input("Number of children in the party: "))

def perform_calculations():
    global adult_cost, child_cost, subtotal, service_fee, sales_tax, total
    adult_cost = num_adults * ADULT_MEAL_PRICE
    child_cost = num_children * CHILD_MEAL_PRICE
    subtotal = adult_cost + child_cost
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    print('-------------------------------')
    print('**** MEAL COST CALCULATOR *****')
    print('Buffalo Wild Wings')
    print('-------------------------------')
    print('Meal Cost (Adults)    $ '   + format(adult_cost, '.2f'))
    print('Meal Cost (Children)  $ ' + format(child_cost, '.2f'))
    print('Subtotal              $ '     + format(subtotal, '.2f'))
    print('Service Fee (10%)     $ '    + format(service_fee, '.2f'))
    print('Sales Tax (6.2%)      $ '    + format(sales_tax, '.2f'))
    print('Total                 $ '     + format(total, '.2f'))

# Call the main function to run the program
main()