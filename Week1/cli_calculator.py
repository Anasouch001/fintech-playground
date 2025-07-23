print("#" * 100)
x = int(input("give a value for x : "))
y = int(input("give a value for y : "))
addition = x + y 
multiplication= x * y
substraction = x - y 
division= x / y 
operation =input("whats the operation: ")
if operation == "addition" or operation == "a": 
    print(f"x + y = {addition}")
elif operation == "multiplication" or operation == "m":
    print(f"x * y = {multiplication}")
elif operation == "substraction" or  operation == "s":
    print(f"x - y ={substraction}")
elif  operation == "division" or  operation == "d" :
    print(f"x / y = {division}")
else :
    print("use a calculator ")