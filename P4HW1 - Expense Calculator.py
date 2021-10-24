#
#CTI-110
#P4HW1 - Expenses
#Joseph Grachen
#10/24/2021
#

def main ():
    
    start_bal = int(input('Enter starting amount in account $' ))  # User input for account balanace
    exp_in = int(input('Enter expense $'))                         # User input for amount of first expense
    c = 1                                                          # Running total of times program runs while loop

    new_bal = start_bal - exp_in                                   # Subtract expense from account

    ans = input('Do you want to enter another expense?(y/n) ')     # Ask if another expense is to be added

    while ans != 'n':                                              # If user choses 'n' then exit loop and print totals
        exp_2 = int(input('Enter expense $'))
        new_bal -= exp_2
        c += 1
        ans = input('Do you want to enter another expense?(y/n) ')
 
    print('')
    print('Amount in account before expenses subtracted $' + str(start_bal))     # Print amount in account BEFORE expense subtraction
    print('Number of expenses entered:', c)                                      # Print the number of expenses entered
    print('Amount in account after expenses are subtracted is $' + str(new_bal)) # Print the amount in account AFTER expense subtraction

main ()

# PSEUDOCODE as referenced throughout lines
# User input for account balanace
# User input for amount of first expense
# Running total of times program runs while loop
# Subtract expense from account
# Ask if another expense is to be added
# If user choses 'n' then exit loop and print totals
# Print amount in account BEFORE expense subtraction
# Print the number of expenses entered
# Print the amount in account AFTER expense subtraction
