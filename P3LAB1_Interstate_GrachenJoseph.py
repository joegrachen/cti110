highway_number = int(input())

if highway_number >= 1 and highway_number <= 99:
    if highway_number % 2 == 0:
        print('I-' + str(highway_number), 'is primary, going east/west.')
    else:
        print('I-' + str(highway_number), 'is primary, going north/south.')
        
elif highway_number % 1 == 0 and highway_number % 2 == 0:
    print(highway_number, 'is not a valid interstate highway number.')
    
elif highway_number >= 100 and highway_number <= 999:
    primary_number = highway_number
    highway_number %= 100
    if highway_number % 2 == 0:
        print('I-' + str(primary_number), 'is auxiliary, serving I-' + str(highway_number) + ', going east/west.')
    else:
        print('I-' + str(primary_number), 'is auxiliary, serving I-' + str(highway_number) + ', going north/south.')
 
else:
    print(highway_number, 'is not a valid interstate highway number.')
