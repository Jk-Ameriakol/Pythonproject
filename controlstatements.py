temperature = int(input("Enter temperature in Celsius: "))

if temperature > 25:
    print("It is too hot")
else:
    print("It is cold")

# A python program that checks three numbers and returns the smallest number
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 < num2 and num1 < num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 < num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

# A python program that checks three numbers and returns the largest number
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y and x > z:
    print(x, "is greatest number")
elif y > x and y > z:
    print(y, "is greatest number")
else:
    print(z, "is greatest number")

















