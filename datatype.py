
number = 67  #Integer
second = 45.98 #Float
greeting = "Hello there" #String
isPythonInteresting = True #Boolean

#Data Structures - Multiple values stored in a single variable
cars = ["Toyota","Nissan"] #List - Ordered and changeable
fruits = ("banana","apple","mango") #Tuple - Ordered and unchargeable
countries = {"Kenya","Tunisia","Algeria"} #Set - Unordered and Unchangeable
student = {
    "firstname" : "Jane",
    "age" : 25,
    "course" : "Web Development",
    "gender" : "Female",
} #Dictionary - Key-value pair

print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])



print(number)
print(second)
print(greeting)
print(isPythonInteresting)

#Determining a datatype
print(type(countries))
print(type(student))

#Typecasting - Converting from one datatype to another
print(float(number))
print(int(second))