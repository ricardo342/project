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