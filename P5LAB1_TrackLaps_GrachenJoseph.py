def miles_to_laps(user_miles):
    laps_to_run = (user_miles / .25)
    print('{:.2f}'.format(laps_to_run))


miles_to_laps(10)
