Ask1 = input("Welcome to Python Class! May I have your name: ")
print("Welcome to the class "+ Ask1+"!")
Num1 = int(input("Choose your preferable number: "))
print (f"your number is {Num1}!")
Num2 = Num1 % 2

if Num2 == 1:
    print("It's a odd one!!!")
else:
    print("It is a Even number!!!")
