# While loop
from variables import language

#Increment
number = 20
while number >= 25:
    print(number)
    number += 1

#Decrement
count = 105
while count >= 100:
    print("Number", count)
    count -= 1

#For loop
for num in range(1,5):
    print(num)

for x in range(1,10,2):
    print(x)

#List
language =["Python","Kotlin","PHP"]
for lang in language:
    print(lang)
