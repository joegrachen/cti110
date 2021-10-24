# Calculating MPGs
# 10/03/2021
# CTI-110 P2HW1 - Miles Per Gallon
# Joseph Grachen
#

miles_driven = float(input('Enter miles driven: '))
gallons_entered = float(input('Enter gallons used: '))
cost_per_gallon = float(input('Enter cost per gallon: '))

gallons_used = miles_driven / gallons_entered
total_gas_cost = cost_per_gallon * gallons_entered
cost_per_mile = total_gas_cost / miles_driven

print('Miles per gallon:     ', round((miles_driven / gallons_entered), 2))
print('Total gas cost:       ', '$', round((total_gas_cost), 2))
print('Cost per mile:        ', '$', round((cost_per_mile), 2))

#pseudocode
#set input variables using float-point
#user inputs the variables for miles driven, gallons used, cost per gallon
#variables calculated for gallons used, total gas cost, cost per mile
#print miles per gallon, round to two decimal places
#print total gas cost, round to two decimal places
#print cost per mile, round to two decimal places
      
