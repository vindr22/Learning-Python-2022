# operators and if statements
weight = int(input('what is your weight? '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == "K":
    converted = weight * 2.205
    print('weight in lbs is ' + str(converted))
else:
    converted = weight / 2.205
    print('weight in kg is ' + str(converted))
