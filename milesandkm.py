#Converts miles to kilometers and kilometers to miles.

def milesandkm():  
    response=input("To convert Miles to Kilometers type '1'\nTo convert Kilometers to Miles type '2'\n")

    if response=='1':
        try:
            res1=float(input("Enter the value of Miles you want to convert to Kilometers.\n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        conversion=res1*1.6
        print("Your value {} Miles is {} Kilometers".format(res1,conversion))

    elif response=='2':
        try:
            res2=res1=float(input("Enter the value of Kilometers you want to convert to Miles.\n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")    
        conversion=res2*0.62137
        print("Your value {} Kilometers is {} Miles".format(res2,conversion))

    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return milesandkm()
        if response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")
            
    #return milesandkm()