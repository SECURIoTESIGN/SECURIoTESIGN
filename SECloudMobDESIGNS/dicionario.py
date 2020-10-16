def add(a, b) :
    return a + b
def substract(a, b) :
    return a - b
def divide(a, b) :
    return a / b
def multiplication(a, b) :
    return a * b
def increase(a, b) :
    return a ** b
 
 
math_functions = {1 : add, 2 : substract, 3:divide, 4:multiplication, 5:increase}

print ("Enter first number!")
a = float(input("First number = "))
b = float(input("Second Number = "))
print("You entered:", a, " and ", b)
print("::Menu::")
print("1 - Add")
print("2 - Substract")
print("3 - Divide")
print("4 - Multipy")
print("5 - Increase")
print("6 - Exit")
user_func = int(input('What math operation?:'))
if user_func == 6 :
    exit()
if user_func >6:
     
print("Your Solution is: ",math_functions[user_func](a, b))