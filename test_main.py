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



number = 3
new_number = number * 4
print(new_number)


number = 1.0
new_number = number * 5.0
print(new_number)



number = 4.0
new_number = number * 1
print(new_number)



number = 5.8
new_number = int(number)
print(new_number)



number = 5
new_number = float(number)
print(new_number)



number_string = input()
number_float = float(number_string)
number_int = int(number_float)
print(number_string)
print(number_float)
print(number_int)



colors = ['red', 'blue', 'cyan', 'grey']
for color in colors:
    print(color)
    
    

word = 'Cache'
for char in word:
    print(char, end='_')
print()



weights = [3, 1, 4, 2]
result = 0
for weight in weights:
    result -= weight
print(result)



colors = ['blue', 'grey', 'pink', 'tan']
for color in reversed(colors):
    print(color)
    


cities = {
    'Austin': 982,
    'Nairobi': 584,
    'Chicago': 550,
    'London': 5259,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)



count = 0
for i in range(2):
   for j in range(4):
      count = count + 1
print(count)



count = 0
for i in range(4, 6):
   for j in range(5):
      count = count + 1
print(count)




i = 0
count = 0
while i < 3:
   for j in range(4):
      count = count + 1
   i = i + 1
print(count)




letter1 = 'j'
while letter1 < 'l':
    letter2 = 's'
    while letter2 <= 't':
        print(f'{letter1}{letter2}')
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
    
    
    

i = 2
while i < 15:
    j = 3
    while j <= 10:
        print(f'{i}{j}')
        j = j + 5
    i = i + 20
    
    
    
num_rows = int(input())
num_columns = int(input())

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Inner loop for columns
    for j in range(num_columns):
        # chr(65) is 'A', so adding j to 65 gives the letters in sequence
        print(f'{i}{chr(65 + j)}', end=' ')
    print()  # This will move to the next line after each row is completed





item_info = 'Mug 7 19'

item_tokens = item_info.split()
item = item_tokens[0]
quantity = item_tokens[1]
price = item_tokens[2]

print(f'{item} stock: {quantity}')
print(f'Price: {price}')




phone_number = '202-555-0106'

separator = ';'
phone_number_tokens = phone_number.split('-')
print(separator.join(phone_number_tokens))




class Person:
   def __init__(self):
      self.name = ''

person1 = Person()
username = 'Amy'

person1.name = username
print(f'You are {person1.name}')



class Person:
   def __init__(self):
      self.name = ''

person1 = Person()
username = 'Ina'
different_username = 'Ava'

person1.name = username
print(person1.name)
person1.name = different_username
print(person1.name)




class Person:
   def __init__(self):
      self.first = ''
      self.last = ''

   def get_full_name(self):
      return f'{self.last}, {self.first}'

person1 = Person()
user_first_name = 'Ina'
user_last_name = 'Stark'

person1.first = user_first_name
person1.last = user_last_name
print(person1.get_full_name())




class Person:
   def __init__(self):
      self.first_name = ''

   def print_name(self):
      print(f'I am {self.first_name}')

person1 = Person()
person1.first_name = 'Joe'
person1.print_name()



class Person:
   def __init__(self):
      self.first_name = ''
      self.last_name = ''

   def get_full_name(self):
      return '(' + self.last_name + ', ' + self.first_name + ')'

user_first_name = 'Ron'
user_last_name = 'Parker'

person1 = Person()
person1.first_name = user_first_name 
person1.last_name = user_last_name 
print(f'He is {person1.get_full_name()}')




class Person:
   def __init__(self):
      self.first_name = ''

   def get_first_name(self):
      return self.first_name

user_name = 'Joe'
different_user_name = 'Max'

person1 = Person()
person1.first_name = user_name 
print(f'He is not {person1.get_first_name()}')
person1.first_name = different_user_name 
print(f'He is {person1.get_first_name()}')




class Person:
   def __init__(self):
      self.first_name = ''
      self.last_name = ''

   def get_full_name(self):
      return '(' + self.last_name + ', ' + self.first_name + ')'

a_first_name = 'Sue'
another_first_name = 'Max'
a_last_name = 'Wayne'
another_last_name = 'Banner'

person1 = Person()
person2 = Person()

person1.first_name = a_first_name
person1.last_name = a_last_name
person2.first_name = another_first_name
person2.last_name = another_last_name

print(f'You are {person1.get_full_name()}')
print(f'I am {person2.get_full_name()}')




class Shape:
    def __init__(self):
       self.color = None

shape1 = Shape()
shape2 = Shape()
shape2.color = 'violet'

print(shape1.color)
print(shape2.color)




class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

rectangle1 = Rectangle(4, 10)
rectangle2 = Rectangle(6, 14)

print(rectangle2.width)
print(rectangle1.length)




class Rectangle:
    def __init__(self, length=10, width=7):
        self.length = length
        self.width = width

rectangle1 = Rectangle(9)
rectangle2 = Rectangle()
rectangle3 = Rectangle(2, 12)

print(rectangle2.length)
print(rectangle3.length)
print(rectangle1.length)




class Rectangle:
    def __init__(self, color, length=12, width=5):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('black')
rectangle2 = Rectangle('yellow', 5, 3)
rectangle3 = Rectangle('blue', 9)

print(rectangle1.color)
print(rectangle1.width)
print(rectangle2.width)
print(rectangle3.width)




class Rectangle:
    def __init__(self, color, length=10, width=7):
        self.color = color
        self.length = length
        self.width = width

rectangle1 = Rectangle('green')
rectangle2 = Rectangle('purple', width=5, length=1)
rectangle3 = Rectangle('black', length=4, width=9)

print(rectangle1.length, rectangle1.width)
print(rectangle2.length, rectangle2.width)
print(rectangle3.length, rectangle3.width)



def change_value(x):
    return x + 1

print(change_value(4))



def change_values(x, y):
    return x + y

print(change_values(1, 2))




def change_values(x, y):
    result = x + y
    return result

print(change_values(4, 1))




class Shape:
    def __init__(self):
       self.color = None

shape1 = Shape()
shape2 = Shape()
shape2.color = 'indigo'

print(shape1.color)
print(shape2.color)




# "New" means new compared to previous level
class Shape:
    # New: Add class variable
    default_color = 'violet'

    def __init__(self):
        self.color = None

a_shape = Shape()
print(a_shape.color)

a_shape.color = Shape.default_color
print(a_shape.color)

a_shape.color = 'teal'
print(a_shape.color)



class Shape:
    default_color = 'maroon'

    def __init__(self):
        self.color = None

a_shape = Shape()
a_shape.color = 'gray'

print(Shape.default_color)
print(a_shape.default_color)
print(a_shape.color)



# "New" means new compared to previous level
class Shape:
    default_color = 'indigo'

    def __init__(self):
        # New: change from None
        self.color = self.default_color

a_shape = Shape()
print(a_shape.color)
a_shape.color = 'gray'
print(a_shape.color)


class Shape:
    default_color = 'maroon'

    def __init__(self):
        self.color = self.default_color

shape1 = Shape()
Shape.default_color = 'gray'
shape2 = Shape()

print(shape2.color)
print(Shape.default_color)
print(shape1.color)



# "New" means new compared to previous level
class Shape:
    default_color = 'orange'
    # New: Add class variable
    background_color = 'white'

    def __init__(self):
        self.color = self.default_color

    # New: Add instance method
    def print_description(self):
        print(f'{self.color} on {self.background_color}')

a_shape = Shape()
a_shape.print_description()

a_shape.color = 'gold'
a_shape.print_description()

Shape.background_color = 'mocha'
a_shape.print_description()



# "New" means new compared to previous level
class Shape:
    default_color = 'violet'
    # New: Change from background_color
    count = 0

    def __init__(self):
        Shape.count += 1
        self.number = self.count
        self.color = self.default_color

    def print_description(self):
        print(f'{self.number} of {self.count} - {self.color}')

shape1 = Shape()
shape2 = Shape()
shape2.color = 'maroon'

print(Shape.count)
shape1.print_description()
shape2.print_description()




start_time = int(input())
end_time = int(input())

print('Time steps:', end=' ')

for curr_time in range(start_time, end_time + 1, 4):
    print(curr_time, end=' ')
print()



first_item = int(input())
last_item = int(input())
items_picked = 0

for item in range(first_item, last_item + 1, 4):
    print(f'Checking item: {item}')
    items_picked += 1

print(f'Total items picked: {items_picked}')
