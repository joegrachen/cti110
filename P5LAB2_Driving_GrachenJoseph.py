def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    trip = driven_miles / miles_per_gallon
    cost = trip * dollars_per_gallon
    print('{:.2f}'.format(cost))


miles_per_gallon = float(input('Enter miles per gallon > '))
dollars_per_gallon = float(input('Enter cost per gallon > '))

driving_cost(10, miles_per_gallon, dollars_per_gallon)
driving_cost(50, miles_per_gallon, dollars_per_gallon)
driving_cost(400, miles_per_gallon, dollars_per_gallon)
