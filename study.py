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

