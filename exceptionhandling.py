try:
    print(number)

except:
    print("An error has occurred")



try:
    num1 = 45
    num2 = 0
    print(num1 / num2)

except:
    print("A ZeroDivisionError has occurred")
finally:
    print("success")