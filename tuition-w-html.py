# Name: Christopher Miller, Amir Salamatolla Luis Lopez
# prog Purpose: This program computes PVCC college tuition & Fees based on the number of credits

import datetime

# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
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

# create output file
outfile = 'tuition.html'
f = None


###### define program functions #######
def main():
    open_outfile()
    more_students = True

    while more_students:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('\nWould you like to calculate tuition & fees for another student? (Y/N): ')
        if yesno.lower() != "y":
            more_students = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()


def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Tuition and Fees Calculation </title>\n')
    f.write('<style> body{background-color: #f0f0f0; font-family: Arial, sans-serif; color: #ffffff; '
            'background-image: url("pvcc.jpg"); background-size: cover;} '
            'table{border-collapse: collapse; width: 50%; margin: 20px auto;} th, td{border: 1px solid #dddddd; '
            'text-align: left; padding: 8px;} th{background-color: #042d86; color: white;} </style> </head>\n')
    f.write('<body>\n')


def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter 1 for IN-STATE; enter 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Scholarship amount received: "))


def perform_calculations():
    global numcredits, scholarshipamt, cost, tuition_out, tuition_out, capital_fee, activity_fee, institution_fee, tuition
    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits
        capital_fee = 0
    elif inout == 2:
        tuition = RATE_TUITION_OUT * numcredits
        capital_fee = RATE_CAPITAL_FEE * numcredits

    institution_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition + capital_fee + institution_fee + activity_fee
    balance = total - scholarshipamt


def display_results():
    global cost, inout, credits
    f.write('<h2>PVCC College Tuition & Fees Report</h2>\n')
    f.write('<table>\n')
    f.write('<tr><th>Description</th><th>Amount</th></tr>\n')
    f.write('<tr><td>Tuition</td><td>${:,.2f}</td></tr>\n'.format(tuition))
    f.write('<tr><td>Capital Fee</td><td>${:,.2f}</td></tr>\n'.format(capital_fee))
    f.write('<tr><td>Institution Fee</td><td>${:,.2f}</td></tr>\n'.format(institution_fee))
    f.write('<tr><td>Activity Fee</td><td>${:,.2f}</td></tr>\n'.format(activity_fee))
    f.write('<tr><td>Scholarship Amount</td><td>${:,.2f}</td></tr>\n'.format(scholarshipamt))
    f.write('<tr><th>Total</th><th>${:,.2f}</th></tr>\n'.format(total))
    f.write('<tr><th>Balance Remaining</th><th>${:,.2f}</th></tr>\n'.format(balance))
    f.write('</table>\n')
    f.write('<p>Date/Time: {}</p>\n'.format(str(datetime.datetime.now())))
    f.write('</body></html>')


# call the main program to execute
main()