ID = input()
year = int(ID[1:3])
if year < 4:
    print('Graduated')
elif 7 >= year >= 4:
    if year == 7:
        print('Freshman')
    elif year == 6:
        print('Freshman')
    elif year == 5:
        print('Junior')
    elif year == 4:
        print('Senior')
else:
    print('Not Registered Yet')
