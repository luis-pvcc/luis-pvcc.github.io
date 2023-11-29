# Name: Christopher Miller, Amir Salamatolla Luis Lopez
# prog Purpose: This program computes PVCC cllege tuition & Fees based on number of credits


from audioop import ratecv
import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0 
scholarshipamt = 0
cost = 0
tuition_in = 0
tuition_out = 0
capital_fee = 0
activity_fee = 0
institution_fee = 0
total = 0
credits = 0
balance = 0
tuition = 0
###### define program functions #######
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('\nWould you like to calculate tuition & fees for another student? (Y/N): ')
        if yesno == "n" or yesno == "N":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Scholarship amount recieved: "))

def perform_calculations():
    
    global numcredits, scholarshipamt, cost, tuition_out, tuition_out, capital_fee, activity_fee, institution_fee, tuition
    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits 
        capital_fee = 0
    if inout == 2:
        tuition = RATE_TUITION_OUT * numcredits 
        capital_fee = RATE_CAPITAL_FEE * numcredits

    institution_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition + capital_fee + institution_fee + activity_fee
    balance = total - scholarshipamt
   

def display_results():
    global cost, inout, credits
    print('University Of Virginia')
    print('Tuition:           $ ' + format(tuition, '8,.2f'))
    print('Capital Fee:       $ ' + format(capital_fee, '8,.2f'))
    print('Institution Fee:   $ ' + format(institution_fee,'8,.2f'))
    print('Scholarship:       $ ' + format(scholarshipamt, '8,.2f'))
    print('Activity Fee:      $ ' + format(activity_fee, '8,.2f'))
    print('Balance Remaining: $ ' + format(balance, '8,.2f'))
    print(str(datetime.datetime.now))
main()
