#Converts Pounds to Kilograms and Kilograms to Pounds.

def poundsandkg():
    response=input("To convert Pounds to Kilograms type '1'\nTo convert Kilograms to Pounds type '2'\n")

    if response =='1':
        try:
            res1=int(input("Enter your value\n"))   
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        result=res1/2.205
        print("{} pounds is {} kilograms".format(res1,result))

    elif response=='2':
        try:
            res2=int(input("Enter yor value\n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        result=res2*2.205
        print("{} kilograms is {} pounds".format(res2,result))
        
    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return poundsandkg()
        if response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")
            
        #return poundsandkg()


