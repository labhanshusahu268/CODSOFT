
    
def calculator():

    a = int(input("enter the value of a :"))
    b = int(input("enter the value of b :"))
    
    user_choice = input("plz enter symbol among them (+,-,*,/,%) or (add, sub, mult, div, mod) : ").lower()

    if user_choice in ("+", "add"):
        print("Addition is : ",a+b)

    elif user_choice in ("-", "sub"):
        print("Subtraction is : ", a-b)

    elif user_choice in ("*", "mult"):
        print("Multiplication is : ", a*b)

    elif user_choice in ("/", "div"):
        if b != 0:
            print("Division is:", a / b)
        else:
            print("Cannot divide by zero!")

    elif user_choice in ("%", "mod"):
        if b != 0:
            print("Modulo is:", a % b)
        else:
            print("Cannot modulo by zero!")

    else:
        print("invalid choice :")

calculator()

while True:
    print("  want to perform operation again :")
    c = input("(yes/no)")
    if c == "yes":
        calculator()
    else:
        break


    


