# CTI-110
# P4HW2 - Salary Calculator
# Joseph Grachen
# 10/24/2021
#

def main():

    # Enter initial input
    employee_name = str(input('Enter employees name or "None" to terminate: '))
    c = 0

    # Create empty lists
    ot_pay = [ ]
    reg_pay = [ ]
    gro_pay = [ ]

    # Enter sentinel while loop
    while employee_name != 'None':
        hours_worked = int(input('How many hours did ' + employee_name + ' work? '))
        employee_payrate = int(input('What is ' + employee_name + ' pay rate? '))       
    
        if hours_worked <= 40:
            c += 1
            hours_overtime = 0
            overtime_pay = 0
            regular_pay = employee_payrate * hours_worked
            gross_pay = regular_pay

            # Add values to lists
            ot_pay.append(overtime_pay)
            reg_pay.append(regular_pay)
            gro_pay.append(gross_pay)

            # Print outputs
            print('')
            print('Employee name: ', employee_name)
            print('--------------------')
            print('Hours worked', '{:.1f}'.format(hours_worked))
            print('Pay rate', '{:.1f}'.format(employee_payrate))  
            print('Overtime: ', '{:.1f}'.format(hours_overtime))
            print('Overtime Pay: $', '{:.2f}'.format(overtime_pay))
            print('Regular Hour Pay: $', '{:.2f}'.format(regular_pay))
            print('Gross Pay: $', '{:.2f}'.format(gross_pay))
            print('')
            employee_name = str(input('Enter employees name or "None" to terminate: ')) 
            
        else:
            c += 1
            hours_worked > 40
            hours_overtime = hours_worked - 40
            overtime_pay = (employee_payrate * 1.5) * hours_overtime
            regular_pay = employee_payrate * 40
            gross_pay = regular_pay + overtime_pay

            # Add values to lists
            ot_pay.append(overtime_pay)
            reg_pay.append(regular_pay)
            gro_pay.append(gross_pay)

            # Print outputs
            print('')
            print('Employee name: ', employee_name)
            print('--------------------')
            print('Hours worked', '{:.1f}'.format(hours_worked))
            print('Pay rate', '{:.1f}'.format(employee_payrate))  
            print('Overtime: ', '{:.1f}'.format(hours_overtime))
            print('Overtime Pay: $', '{:.2f}'.format(overtime_pay))
            print('Regular Hour Pay: $', '{:.2f}'.format(regular_pay))
            print('Gross Pay: $', '{:.2f}'.format(gross_pay))
            print('')
            employee_name = str(input('Enter employees name or "None" to terminate: '))
            
    # Print sum of lists and number of employees entered         
    print('Total number of employees entered:', c)
    print('Total amount paid for overtime: $', '{:.2f}'.format(sum(ot_pay)))
    print('Total amount paid for regular hours: $', '{:.2f}'.format(sum(reg_pay)))
    print('Total amount paid in gross: $', '{:.2f}'.format(sum(gro_pay)))




main()

# PSEUDOCODE as referenced throughout code
# Enter initial input
# Create empty lists
# Enter sentinel while loop
# Add values to lists
# Print outputs
# Add values to lists
# Print outputs
    
        
