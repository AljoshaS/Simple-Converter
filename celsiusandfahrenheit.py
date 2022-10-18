#Converts Celsius to Fahrenheit and Fahrenheit to Celsius.

def celiusandfahrenheit():

    response=input("To convert Celsius to Fahrenheit type '1'\nTo convert Fahrenheit to Celsius type '2'\n")
 
    if response=='1':
        try:
            res1=int(input("Enter the value that you want to convert.\n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        conversion=(res1*9/5)+32
        print("Your value {} converted to Fahrenheit is {}".format(res1,conversion))

    elif response=='2':
        try:
            res2=int(input("Enter the value that you want to convert.\n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        conversion=(res2-32)*5/9
        print("Your value {} converted to Celsius is {}".format(res2,conversion))

    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return celiusandfahrenheit()
        if response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")
            
    #return celiusandfahrenheit()

