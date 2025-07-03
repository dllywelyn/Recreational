#make function for each bank, with monthly deposits, rate of interest in % and time in months 
def interest(bank, deposit, rate, month):
    # make totals global so they can be used outside of function
    global total_deposit, total_interest
    # set cumilative ineterest at zero before loop begins, so it has a value
    c_i = 0
    # divide interest rate by 12 to get apr per month, to work out interest cumilated at the end of the month
    annual_rate = rate/12
    # set loop for interest each month
    for i in range(month):
        #principal is the amount already in the bank before interest is added (interest is 0 initially)
        principal = deposit + c_i
        # show 'cumilative interest' as total: principal plus ineterest.
        # In which case, 5% would be 105%, hence '1+interest'
        c_i = principal * (1 + annual_rate/100)
        #round to 2 decimal places for currency
        c_i = round(c_i, 2)
    # For user convenience, show total deposits and interest separately
    total_deposit = deposit * month
    total_interest = round((c_i - total_deposit), 2)
    print(f"Value is {c_i - total_deposit}, before being round down to two decimal places: {total_interest}")
    print(f"\033[1m{bank}\033[0m \n Your total deposit over {month} months is: £{total_deposit}, earning £{total_interest} interest. \n \
Your total with interest is £{c_i}\n")


def total(a):
    interest("Natwest", 150, 6.5, a)
    ntotal_deposit = round(total_deposit, 2)
    ntotal_interest = round(total_interest, 2)
    interest("Co-op", 250, 7, a)
    ctotal_deposit = round(total_deposit, 2)
    ctotal_interest = round(total_interest, 2)
    interest("Lloyds", 400, 6, a)
    ltotal_deposit = round(total_deposit, 2)
    ltotal_interest = round(total_interest, 2)
    interest("First Direct", 350, 7, a)
    ftotal_deposit = round(total_deposit, 2)
    ftotal_interest = round(total_interest, 2)
    totald = round(ntotal_deposit+ctotal_deposit+ltotal_deposit+ftotal_deposit, 2)
    totali = round(ntotal_interest+ctotal_interest+ltotal_interest+ftotal_interest, 2)
    print (f"Your total deposit across all acounts is \033[1m£{totald}\033[0m")
    print (f"Your total interest is \033[1m£{totali}\033[0m")

total(12)
