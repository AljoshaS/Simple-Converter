#Converts inch to centimeter and centimeter to inch.

def inchtocm():
    response=input("For inch to centimeter conversion type '1'\nFor centimeter to inch conversion type '2'\n")

    if response=='1':
        try:
            res1=float(input("Enter the value of inch you want to convert to Centimeter.\n"))
        except ValueError:
            raise ValueError("You have given a wrong value. Thank you.")
        conversion=res1*2.54
        print("Your value {} inch is {} centimeters.".format(res1,conversion))

    if response=='2':
        try:
            res2=float(input("Enter the value of centimeter you want to convert to inch.\n"))
        except ValueError:
            raise ValueError("You have given a wrong value. Thank you.")
        conversion=res2/2.54
        print("Your value {} inch is {} centimeters".format(res2,conversion))
        
    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y' or 'y':
            return inchtocm()
        if response=='N' or 'n':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")
            
    #return inchtocm()
    