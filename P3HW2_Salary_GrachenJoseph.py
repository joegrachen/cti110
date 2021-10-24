# CTI-110
# P3HW2 - Salary
# Joseph Grachen
# 10/10/2021
#

def main():

    employee_name = input('Enter employees name: ')
    hours_worked = int(input('Enter number of hours worked: '))
    employee_payrate = int(input('Enter employees pay rate: '))

    if hours_worked <= 40:
        hours_overtime = 0
        overtime_pay = 0
        regular_pay = employee_payrate * hours_worked
        gross_pay = regular_pay
    else:
        hours_worked > 40
        hours_overtime = hours_worked - 40
        overtime_pay = (employee_payrate * 1.5) * hours_overtime
        regular_pay = employee_payrate * 40
        gross_pay = regular_pay + overtime_pay
    
    print('--------------------')
    print('Employee name: ', employee_name)
    print('--------------------')
    print('Hours worked', '{:.1f}'.format(hours_worked))
    print('Pay rate', '{:.1f}'.format(employee_payrate))  
    print('Overtime: ', '{:.1f}'.format(hours_overtime))
    print('Overtime Pay: $', '{:.2f}'.format(overtime_pay))
    print('Regular Hour Pay: $', '{:.2f}'.format(regular_pay))
    print('Gross Pay: $', '{:.2f}'.format(gross_pay))

main()

#pseudocode
#create input fields
#break output into two distinct lines of code based up OT or no OT
#set and calculate overtime variables first
#set and calculate regular pay variables second
#print output and associated variables with formatting decimal places
    
        
