import datetime

# Define rate tuples
ROOM_RATES = (195, 250, 350)
TAX_RATES = (0.065, 0.1125)

# Define files and list
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = []

# Program functions
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()

def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    for i in guest_in:
        guest.append(i.strip().split(","))

def perform_calculations():
    global grandtotal
    grandtotal = 0

    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])

        if room_type == "SR":
            subtotal = ROOM_RATES[0] * num_nights
        elif room_type == "DR":
            subtotal = ROOM_RATES[1] * num_nights
        else:
            subtotal = ROOM_RATES[2] * num_nights

        salestax = subtotal * TAX_RATES[0]
        occupancy = subtotal * TAX_RATES[1]
        total = subtotal + salestax + occupancy

        grandtotal += total

        guest[i].append(subtotal)
        guest[i].append(salestax)
        guest[i].append(occupancy)
        guest[i].append(total)

def open_out_file():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> tr:hover {background-color: #7db47f;} tr {border-bottom: 1px solid #ddd;}td { text-align:center }.center { text-align: center; } body {font-family: Arial, sans-serif;background-image: url(hotel2.jpg)}table, th, td {border: 1.5px solid black;border-collapse: collapse;}</style>\n')
    f.write('</head><body style="font-family: Arial, sans-serif;">\n')
    f.write('<table border="2" style="color: #ffffff; background-color:#006d00; margin: auto; width: 40%;">\n')
    f.write('<tr> <td colspan="7" class="center"><h2>Emerald Beach Hotel & Resort</h2>\n')
    f.write('<table border="2" style="color: #ffffff; background-color:#999999; margin: auto; width: 70%;">\n')
    f.write('<tr><th>Name</th><th>Room Type</th><th>Number of Nights</th><th>Subtotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>\n')

def create_output_html():
    global f

    currency = "{:,.2f}"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    for g in guest:
        f.write('<tr><td>' + g[0] + '</td><td>' + g[2] + '</td><td>' + g[3] + '</td><td>' + currency.format(g[4]) +
                '</td><td>' + currency.format(g[5]) + '</td><td>' + currency.format(g[6]) + '</td><td>' +
                currency.format(g[7]) + '</td></tr>\n')

    f.write("<tr><td>Grand Total: " + currency.format(grandtotal) + "</tr></td>")
    f.write("<td>Generated on: " + day_time + "</td>")
    f.write('</table><br/>')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

# Call the main program to execute
main()