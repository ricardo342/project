#!/usr/bin/python
#coding=utf8
import requests
import os
import sqlite3
'''
# 变量
message = 'Hello World!'
print(message)

message = 'Hello Python World!'
print(message)
'''
'''
# 字符串
name = 'ADA lovelace'
print(name.title())     # 单词首字母大写
print(name.upper())     # 单词全部大写
print(name.lower())     # 单词全部小写

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name)
message = 'Hello,' + full_name.title() + "!"
print(message)
'''
'''
# 删除末尾空白
language = 'python '
print(language)
print(language.rstrip())  # 暂时删除
language_d = language.rstrip()
print(language_d)         # 永久删除
'''
'''
age = 23
message = 'Happy' + " " + str(age) + 'rd birthday!'
print(message)
'''
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1].upper())
message = 'My first bicycle was a' + " " + bicycles[0].title() + "."
print(message)
'''
'''
names = ['ada', 'bob', 'john', 'mike']
print(names[0])
print(names[1].title())
print(names[2].upper())
print(names[3].lower())

for x in range(-1,3):
    x = x + 1
    names[x]
    message = names[x] + "," + 'nice to meet you!'
    print(message)
'''
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for x in range(4):
    x = x
    bicycles[x]
    message = 'I would like to own a' + " " + bicycles[x]
    print(message)
'''
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = '666'
print(motorcycles)
motorcycles.append('docati')
print(motorcycles)
'''
'''
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('docati')
motorcycles.insert(1, '666')
del motorcycles[1]
print(motorcycles)
pop_motorcycle = motorcycles.pop(1)
print(pop_motorcycle)
print(motorcycles)
pop_motorcycle = motorcycles.pop(1)
message = 'The last motorcycle I owned was a' + " " + pop_motorcycle
print(message)
print(motorcycles)
too_expersive = 'docati'
motorcycles.remove('docati')
print(motorcycles)
print("A" + " " + too_expersive.title() + "is too expersive for me")
'''
'''
person = []
person.append('ada')
person.append('bob')
person.append('john')
print(person)
for x in range(3):
    x = x
    message = person[x].title() + "," + "can i invite you to dinner?"
    print(message)
people = 'bob'
person.remove('bob')
person.insert(1, 'mike')
print(people.title() + " " + 'unable to attend.')

for i in range(3):
    i = i
    message01 = person[i].title() + "," + "can i invite you to dinner?"
    print(message01)
print(person)

person.insert(0, 'mjq')
person.insert(2, 'wpt')
person.append('yzy')

for e in range(6):
    e = e
    message02 = person[e].title() + "," + "can i invite you to dinner?"
    print(message02)
    message03 = person[e].title() + "," + "sorry,i can only invite two guests."
    print(message03)

print(person)

for b in range(3):
    b = b
    print(b)
    sorry_person = person.pop(b)
    print(sorry_person)
    message04 = sorry_person + "," + "sorry, we can't invite you to dinner."
    print(message04)

print(person)
for c in range(3):
    c = c
    message05 = person[c].title() + "," + "can i invite you to dinner?"
    print(message05)
'''
'''
def test(person):
    for r in person[1:]:
        person.remove(r)
    return person
print(test(person))
'''
'''
for r in person[1:]:
    person.remove(r)
print(person)
'''
'''
for r in range(:-1):
    r = r
    del person[r]
print(person)
'''
'''
if conditional_test:
    do something
'''
'''
age = 19
if age >= 18:
    print("You are old enghou to vote!")
    print("Have you registered to vote yet?")
'''
'''
age = int(input("请问年龄:"))
if age < 4:
    price = 0
elif age <18:
    price = 5
else:
    price = 10

message = "Your admission cost is" + " " + "$" + str(price) + "."
print(message)
'''
'''
requested_topping = ['mushroom', 'extra_cheese']

if 'mushroom' in requested_topping:
    print("Adding mushrooms.")
if 'extra_cheese' in requested_topping:
    print("Adding extra_cheese.")

print('\nFinished making your pizza!')
'''
'''
alien_color = ['green', 'yellow', 'red']
color = input("请输入颜色:")

color == alien_color[0:]
if color == 'green':
    print('five')
elif color == 'yellow':
    print('ten')
elif color == 'red':
    print('fivteen')
else:
    print('error')
'''
'''
age = int(input("请输入年龄:"))
if age < 2:
    name = 'baby'
elif age < 4:
    name = 'children'
elif age < 13:
    name = 'youth'
elif age < 20:
    name = 'teenager'
elif age < 65:
    name = 'adult'
elif age >= 65:
    name = 'aged'

message = "He is a " + name + '.'
print(message)
'''
'''
favorite_fruits = ['apple', 'peach', 'lemon']
fruit = input('请输入一种水果:')
if fruit in favorite_fruits:
    print("You really like bananas!")
else:
    print('error')
'''
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding" + " " + topping + ".")

print("\nFinished making your pizza!")
'''
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''
'''
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
'''
'''
users = ['admin']
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + "," + " would you liketo seeastatus report?")
        else:
            print("Hello Eric, thank you for logging in again")
else:
    print("We need to find some users!")
'''
'''
current_users = ['admin', 'sa', 'mjq', 'wpt', 'QT']
new_users = ['Jone', 'David', 'sa', 'Franck', 'admin']
for new_user in new_users:
    if new_user.upper() in current_users:
        print('use')
    else:
        print('not use')
'''
'''
current_users = ['Jone', 'David', 'John', 'Franck', 'admin']
new_users = ['Lemon', 'JONE', 'Len', 'john', 'Hayley']
for new_users in new_users:
    if new_users.lower() in [current_user.lower() for current_user in current_users]:
        print("The name has created,please change the name.^_^")
    else:
        print("OK,the name which you named could use,please enter")
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')
'''
'''
alien_0 = {'color': 'green', 'points': 5}

new_point = alien_0['points']
message = "You just earned " + str(new_point) + " " + "points!"
print(message)
'''
'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 25
alien_0['y_position'] = 0
print(alien_0)
'''
'''
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
message = "The alien is " + alien_0['color'] + "."
print(message)
alien_0['color'] = 'yellow'
message_0 = "The alien is new " + alien_0['color'] + "."
print(message_0)
'''
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''
'''
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")
print("Total number of aliens: " + str(len(aliens)))
'''
'''
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    new_alien1 = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien1)
    print(aliens)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
'''
'''
pizza = {
    'curst': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("You ordered a " + pizza['curst'] + "-curst pizza with the following toppings" + ":")
for i in pizza['toppings']:
    print("\t" + i)
'''
'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        message = name.title() + "'s favorite languages are:"
        print(message)
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        for language in languages:
            message01 = name.title() + "'s favorite languages is " + language.title() + "."
            print(message01)
'''
'''
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
    }

for user_name, locations in users.items():
    message = "Username: " + user_name
    print(message)
    full_name = locations['first'].title() + " " + locations['last'].title()
    message01 = "Full name: " + full_name
    print("\t" + message01)
    message02 = "Location: " + locations['location'].title()
    print("\t" + message02)
'''
'''
user_0 = {
    'first_name': '马',
    'last_name': '佳钦',
    'age': 25,
    'city': '深圳',
    }

user_1 = {
    'first_name': '魏',
    'last_name': '培婷',
    'age': 24,
    'city': '深圳',
    }

user_2 = {
    'first_name': '马',
    'last_name': '佳辉',
    'age': 24,
    'city': '广州',
    }

people = []

people.append(user_0)
people.append(user_1)
people.append(user_2)

print(people)
'''
'''
pets = []

mike = {
    'name': 'cat',
    'user': 'mjq',
    }

sarah = {
    'name': 'dog',
    'user': 'wpt',
    }

pets.append(mike)
pets.append(sarah)

for animal in pets:
    message = animal['name'] + " is a " + animal['user']
    print(message)
'''
'''
favorite_places = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, places in favorite_places.items():
    if len(places) > 1:
        message = name + " like places are:"
        print(message)
        for place in places:
            message01 = "\t" + place
            print(message01)
    elif len(places) == 1:
        message02 = name + " like places is " + place + "."
        print(message02)
'''
'''
magicians = ['mike', 'john', 'sarah']

def make_great(names):
    for name in names:
        name = "the Great " + name
        print(name)
    return names

def show_magicians(names):
    for name in names:
        print(name.title())

show_magicians(magicians)
message = make_great(magicians)
'''
'''
def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names, new_names):
    while names:
        name = names.pop()
        name = "the Great " + name
        new_names.append(name)
        print(name.title())

magicians = ['mike', 'john', 'sarah']
magiciums = []

show_magicians(magicians)
make_great(magicians[:], magiciums)
'''
'''
def make_pizza(*toppings):
    message = "\nMaking a pizza with the following toppings: "
    print(message)
    for topping in toppings:
        print("-" + str(topping))

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
'''
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
'''
'''
def make_sandwichs(*foods):
    for food in foods:
        print(food)

make_sandwichs('beef')
make_sandwichs('beef', 'milk')
'''
'''
def make_car(name, model, **cars_info):
    car_info = {}
    car_info['name'] = name
    car_info['model'] = model
    for key, value in cars_info.items():
        car_info[key] = value
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''
'''
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
'''
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        message = self.name.title() + " is now sitting."
        print(message)

    def roll_over(self):
        message01 = self.name.title() + " is now rolled over!"
        print(message01)

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
'''
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        message01= "The " + self.restaurant_name.title() + " in operation."
        print(message01)

my_restaurant = Restaurant('erlang', '粤菜')
your_restaurant = Restaurant('erlang', '粤菜')
him_restaurant = Restaurant('erlang', '粤菜')
my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
him_restaurant.describe_restaurant()
'''
'''
class User():
    def __init__(self, first_name, last_name, user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info

    def describe_user(self):
        print(self.user_info)

    def greet_user(self):
        message = "Hello " + self.first_name.title() + " " + self.last_name + ", nice to meet you!"
        print(message)

mike_user = User('ricardo', '.M', 16)
john_user = User('ricardo', '.M', 15)
sarah_user = User('ricardo', '.M', 14)
mike_user.describe_user()
mike_user.greet_user()
john_user.describe_user()
john_user.greet_user()
sarah_user.describe_user()
sarah_user.greet_user()
'''
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        message = "This car has " + str(self.odometer_reading) + " miles on it."
        print(message)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def add_odometer(self, addmile):
        if addmile >= 0:
            self.odometer_reading += addmile
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
# my_new_car.get_descriptive_name()
message = my_new_car.get_descriptive_name()
print(message)
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.update_odometer(21)
my_new_car.read_odometer()
my_new_car.add_odometer(2)
my_new_car.read_odometer()
'''
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        message01= "The " + self.restaurant_name.title() + " in operation."
        print(message01)
    
    def read_restaurant(self):
        message = "Have " + str(restaurant.number_served) + " people eat."
        print(message)
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        if num >= 0:
            self.number_served += num
        else:
            print("No!")

restaurant = Restaurant('erlang', '粤菜')
# restaurant.number_served = 3
# message = "Have " + str(restaurant.number_served) + " people eat."
# print(message)
restaurant.set_number_served(3)
restaurant.read_restaurant()
restaurant.increment_number_served(-1)
restaurant.read_restaurant()
'''
'''
class User():
    def __init__(self, first_name, last_name, user_info, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.user_info)

    def greet_user(self):
        message = "Hello " + self.first_name.title() + " " + self.last_name + ", nice to meet you!"
        print(message)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(self.login_attempts)

user = User('ricardo', '.m', 16, 0)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()
'''
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        message = "This car has " + str(self.odometer_reading) + " miles on it."
        print(message)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def add_odometer(self, addmile):
        if addmile >= 0:
            self.odometer_reading += addmile
        else:
            print("You can't roll back an odometer!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 初始化父类属性
        self.battery_size = 70
    
    def describe_battery(self):
        message = "This car has a " + str(self.battery_size) + "-kWh battery."
        print(message)
    
    def read_odometer(self):
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.read_odometer()
'''
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        message = "This car has " + str(self.odometer_reading) + " miles on it."
        print(message)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def add_odometer(self, addmile):
        if addmile >= 0:
            self.odometer_reading += addmile
        else:
            print("You can't roll back an odometer!")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        message = "This car has a " + str(self.battery_size) + "-kWh battery."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
'''
'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        message01= "The " + self.restaurant_name.title() + " in operation."
        print(message01)
    
    def read_restaurant(self):
        message = "Have " + str(self.number_served) + " people eat."
        print(message)
    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        if num >= 0:
            self.number_served += num
        else:
            print("No!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def ice_cream(self, flavor):
        self.flavors.append(flavor)
        print(self.flavors)

ice = IceCreamStand('erlang', '粤菜')
ice.ice_cream('one')
ice.ice_cream('two')
ice.ice_cream('three')
'''
'''
class User():
    def __init__(self, first_name, last_name, user_info, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.user_info)

    def greet_user(self):
        message = "Hello " + self.first_name.title() + " " + self.last_name + ", nice to meet you!"
        print(message)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(self.login_attempts)
'''
'''
class Admin(User):
    def __init__(self, first_name, last_name, user_info, login_attempts):
        super().__init__(first_name, last_name, user_info, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        message = "Administrator permissions are as follows"
        message01 = "--------------\n"
        print(message)
        print(message01)
        for privilege in self.privileges:
            print(privilege)

user = Admin('ricardo', '.m', 16, 0)
user.show_privileges()
'''
'''
class User():
    def __init__(self, first_name, last_name, user_info, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.user_info)

    def greet_user(self):
        message = "Hello " + self.first_name.title() + " " + self.last_name + ", nice to meet you!"
        print(message)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(self.login_attempts)


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        message = "Administrator permissions are as follows"
        message01 = "--------------\n"
        print(message)
        print(message01)
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, user_info, login_attempts):
        super().__init__(first_name, last_name, user_info, login_attempts)
        self.privileges = Privileges()
    
    def show_privileges(self):
        message = "Administrator permissions are as follows"
        message01 = "--------------\n"
        print(message)
        print(message01)
        for privilege in self.privileges:
            print(privilege)

user = Admin('ricardo', '.m', 16, 0)
user.privileges.show_privileges()
'''
'''
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        message = "This car has " + str(self.odometer_reading) + " miles on it."
        print(message)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def add_odometer(self, addmile):
        if addmile >= 0:
            self.odometer_reading += addmile
        else:
            print("You can't roll back an odometer!")

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        message = "This car has a " + str(self.battery_size) + "-kWh battery."
        print(message)
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self, size):
        if size != 85:
            self.battery_size = 85
        else:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 初始化父类属性
        self.battery_size = 70
    
    def describe_battery(self):
        message = "This car has a " + str(self.battery_size) + "-kWh battery."
        print(message)
    
    def read_odometer(self):
        print("This car doesn't need a gas tank!")

battery = Battery()
battery.upgrade_battery(85)
battery.get_range()
'''
'''
from root import User
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        message = "Administrator permissions are as follows"
        message01 = "--------------\n"
        print(message)
        print(message01)
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, user_info, login_attempts):
        super().__init__(first_name, last_name, user_info, login_attempts)
        self.privileges = Privileges()
    
    def show_privileges(self):
        message = "Administrator permissions are as follows"
        message01 = "--------------\n"
        print(message)
        print(message01)
        for privilege in self.privileges:
            print(privilege)
'''
'''
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    message = name.title() + "'s favorite language is " + language.title() + "."
    print(message)
'''
'''
from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self, sides):
        self.sides = sides
        i = 0
        while i <= self.sides:
            i += 1
            x = randint(1,self.sides)
            print(x)

die = Die()
die.roll_die(20)
'''
'''
filename = 'alice.txt'
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
'''
'''
def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        message = "The file " + filename + " has about " + str(num_words) + " words."
        print(message)

# filename = 'alice.txt'
# count_words('alice.txt')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
'''
'''
try:
    num1 = int(input("Please input number: "))    
    num2 = int(input("Please input number: "))
except ValueError:
    print("num not int")
else:
    number = num1 + num2
    print(str(number))
'''
'''
active = True

while active:
    try:
        num1 = int(input("Please input number: "))    
        num2 = int(input("Please input number: "))
    except ValueError:
        print("num not int")
        active = True
    else:
        number = num1 + num2
        active = False
        print(str(number))
'''
'''
cats = 'cats.txt'
dogs = 'dogs.txt'

try:
    with open(cats) as c:
        contents_cats = c.read()
except FileNotFoundError:
    print("cats.txt not exist.")
else:
    print(contents_cats)
    
try:
    with open(dogs) as d:
        contents_dogs = d.read()
except FileNotFoundError:
    print("dogs.txt not exist.")
else:
    print(contents_dogs)
'''
'''
def file_exist(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print("The file is not exist.")
    else:
        print(contents)

filename = 'cats.txt'
file_exist(filename)
'''
'''
cats = 'cats.txt'
dogs = 'dogs.txt'

try:
    with open(cats) as c:
        contents_cats = c.read()
except FileNotFoundError:
    pass
else:
    print(contents_cats)
    
try:
    with open(dogs) as d:
        contents_dogs = d.read()
except FileNotFoundError:
    pass
else:
    print(contents_dogs)
'''
'''
filename= 'cat.txt'

with open(filename) as f:
    contents = f.read()

lines = contents.split()
number = lines.count('cat')
number1 = lines.lower().count('cat')
'''
'''
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)
print(numbers)
'''
'''
import json

username = input("What is your name? ")

filename = "name.json"

try:
    with open(filename) as f:
        name = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        json.dump(username, f)
        message = "We'll remember you when you come back, " + username + "!"
        print(message)
else:
    message01 = "Welcome back, " + name + "!"
    print(message01)
'''
'''
import json

def get_stored_username():
    filename = "name.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        retuen username

def greet_user(filename):
    username = get_stored_username()

    if username:
        message01 = "Welcome back, " + name + "!"
        print(message01)
    else:
        username = input("What is your name? ")

        with open(filename, 'w') as f:
            json.dump(username, f)
            message = "We'll remember you when you come back, " + username + "!"
            print(message)
'''
'''
import json

def get_number():
    filename = 'num.json'
    try:
        with open(filename) as i:
            number = json.load(i)
    except FileNotFoundError:
        return None
    else:
        return number

def number():
    number = get_number()
    if number:
        message = "I know your favorite number! It's " + number + "."
        print(message)
    else:
        with open(filename, 'w') as f:
        json.dump(num, f)
    
        with open(filename) as i:
            number = json.load(i)
            message = "I know your favorite number! It's " + number + "."
            print(message)
'''
'''
import json

def get_stored_username():
    filename = "name.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    return username

def greet_user(filename):
    username = get_stored_username()

    active = True
    
    while active:
        if username:
            message01 = "Welcome back, " + username + "!"
            print(message01)
        else:
            msg = input("This number is right?(yes or no) ")
            if msg == 'yes':
                username = input("What is your name? ")

                with open(filename, 'w') as f:
                    json.dump(username, f)
                    message = "We'll remember you when you come back, " + username + "!"
                    print(message)
                active = False
            else:
                username = get_new_username()
                with open(filename, 'w') as f:
                    json.dump(username, f)
                    message = "We'll remember you when you come back, " + username + "!"
                    print(message)
'''
'''
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first_name = input("Please give me a first name: ")
    if first_name == 'q':
        break
    last_name = input("Please give me a last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)
    msg = "\tNeatly formatted name: " + formatted_name + '.'
    print(msg)
'''
'''
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis joplin')

unittest.main()

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " "+ middle_name + "" + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
'''
'''
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis joplin')
    
    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
'''
'''
import unittest

from city_functions import city_function

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        #test_c_c = city_function('santiago', 'chile', '50000')
        #self.assertEqual(test_c_c, 'Santiago, Chile - population 50000')
        test_c_c = city_function('santiago', 'chile')
        self.assertEqual(test_c_c, 'Santiago, Chile')
    
    def test_city_country_population(self):
        test_c_c_p = city_function('santiago', 'chile', population='50000')
        self.assertEqual(test_c_c_p, 'Santiago, Chile - population 50000')

unittest.main()
'''
'''
from city_functions import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    responses = input("Language: ")
    if responses == 'q':
        break
    my_survey.store_response(responses)

message = "\nThank you to everyone who participated in the survey!"
print(message)
my_survey.show_results()
'''
'''
import unittest

from city_functions import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        question = "What language did you first learn to speak?"
        my_survey =AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
'''
'''
import unittest

from city_functions import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
'''
'''
import unittest

from city_functions import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('ma', 'jiaqin', 5000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.year_money, 10000)
        
    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.year_money, 15000)
        

unittest.main()
'''