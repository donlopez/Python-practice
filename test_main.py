my_list = [-1, 0, 1, 2]
new_list = [ number - 4 for number in my_list ]
print(new_list)

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number for number in my_list if number < 0 ]
print(new_list)


my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number * 4 for number in my_list if number > -1 ]
print(new_list)


my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number * 3 for number in my_list if (number > 0) and (number % 2 == 0) ]
print(new_list)


my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number + 3 for number in my_list if (number < -2) and (number % 2 == 1) ]
print(new_list)


try:
    number1 = int(input())
    print(number1 * 4)

    number2 = int(input())
    print(number2 * 4)
except:
    print('x')
print('e')


user_input = input()
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 4)
    except:
        print('x')
    user_input = input()
print('e')


user_input = input()
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 4)
    except:
        print('x')
    user_input = input()
print('e')


user_input = input()
try:
    while user_input != 'q':
        number = int(user_input)
        print(number * 2)
        user_input = input()
except:
    print('x')
print('e')


try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError('Invalid age')

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f'Avg: {avg_max_heart_rate}')

except ValueError as excpt:
    print(f'Error: {excpt}')
    
    
    

valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError('Invalid')

        valid_password = True
        print('Accepted')

    except ValueError as excpt:
        print(f'Error: {excpt}')
        
        

airport_codes = {}
airport_codes['Los Angeles'] = 'LAX'
airport_codes['Seattle'] = 'SEA'
airport_codes['London'] = 'LHR'

print(airport_codes['Seattle'])
print(airport_codes['Los Angeles'])



airport_codes = {
    'London': 'LHR',
    'Tokyo': 'NRT',
    'Paris': 'CDG'
}

print(airport_codes['Paris'])
print(airport_codes['London'])
airport_codes['Paris'] = 'ORY'
print(airport_codes['Paris'])




provincial_capitals = {
    'Manitoba': 'Winnipeg',
    'Ontario': 'Toronto',
    'Nunavut': 'Iqaluit',
    'Alberta': 'Edmonton'
}

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
    else:
        print('x')
    province_name = input()
    
    

# "New" means new compared to previous level
provincial_capitals = {
    'BC': 'Victoria',
    'Manitoba': 'Winnipeg',
    'Nunavut': 'Iqaluit',
    'Alberta': 'Edmonton'
}

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
        del provincial_capitals[province_name] # New line
    else:
        print('x')
    province_name = input()
    
    
    
airport_codes = {
    'Chicago': 'ORD',
    'Los Angeles': 'LAX',
    'Washington': 'IAD',
    'Amsterdam': 'AMS',
    'New York': 'JFK'
}

print(airport_codes.get('Chicago', 'na'))
print(airport_codes.get('Cincinnati', 'na'))
print(airport_codes.get('Washington', 'na'))



airport_codes = {
    'Seattle': 'SEA',
    'Atlanta': 'ATL',
    'Los Angeles': 'LAX',
    'Amsterdam': 'AMS',
    'London': 'LHR'
}

print(airport_codes.get('Seattle', 'na'))
print(airport_codes.pop('Seattle', 'na'))
print(airport_codes.get('Seattle', 'na'))




airport_codes = {
    'Chicago': 'ORD',
    'Vancouver': 'YVR',
    'New York': 'JFK',
    'Minneapolis': 'MSP',
    'Houston': 'IAH'
}

new_airport_codes = {
    'Tokyo': 'NRT',
    'Austin': 'AUS',
    'Seattle': 'SEA'
}

print(airport_codes.get('Paris', 'na'))
print(airport_codes.get('Tokyo', 'na'))
print(airport_codes.get('Minneapolis', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Paris', 'na'))
print(airport_codes.get('Tokyo', 'na'))
print(airport_codes.get('Minneapolis', 'na'))





airport_codes = {
    'London': 'LHR',
    'Dallas': 'DAL',
    'Paris': 'CDG',
    'Seattle': 'SEA',
    'Vancouver': 'YVR'
}

new_airport_codes = {
    'Austin': 'AUS',
    'Minneapolis': 'MSP',
    'Dallas': 'DFW'
}

print(airport_codes.get('Dallas', 'na'))
print(airport_codes.get('Austin', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Dallas', 'na'))
print(airport_codes.get('Austin', 'na'))




name = 'Sue'
print('Their name is {}'.format(name))


year = 1995
print('Sue was born in {:d}'.format(year))


number = 11
print('Decimal: 11, Binary: {:b}'.format(number))

weight_oz = 7.50
print('The fish weighs {:.2f} oz'.format(weight_oz))

number = 9
print('{:b}, {:d}, {:.2f}'.format(number, number, number))


thing = 'car'
adjective = 'small'
color = 'pink'
print('{1} {2} {0}'.format(thing, adjective, color))



print('{adjective} {color} {thing}'.format(adjective = 'wide', color = 'pink', thing = 'car'))