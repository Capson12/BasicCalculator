
#Addition Calculator

a = 0

b = 0 

#result = a + b 

while(True):

    print("\n What Operation do you wanna do? \n Press 'A' for addition \n Press 'S' for Subtraction \n Press 'M' Multiplication \n Or \n Press 'D' for Division, then press 'Enter'")
    userInput = input()

    def subtraction():
        return int(a) - int(b)

    def multiplication():
        return int(a) * int(b)

    def division():
        return int(a) / int(b)

    def addition():
        return int(a) + int(b)



    if (userInput == "A"):
        print ("addition")
        a = input("Enter your first number: ")
        b = input("Enter your Second number: ")
        print("Your answer is: ", addition())

    elif(userInput == "S"):
        
        print ("subtraction")
        a = input("Enter your first number: ")
        b = input("Enter your Second number: ")
        print("Your answer is: ", subtraction())

    elif(userInput == "M"):
        print ("Multiplication")
        a = input("Enter your first number: ")
        b = input("Enter your Second number: ")
        print("Your answer is: ", multiplication())

    elif(userInput == "D"):
        print ("division")
        a = input("Enter your first number: ")
        b = input("Enter your Second number: ")
        print("Your answer is: ", division())

    else:
        print("Input not recognised!")

