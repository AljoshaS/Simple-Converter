#Converts acres to square meters and square meters to acres.

def acres():
    
    res=input("To convert acres in square meters type '1',\nTo convert square meters in acres type '2'?\n")

    if res=='1':
        try:
            res1=float(input("Enter the value that you want to convert: \n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        result=res1*43560
        print("Your value {} in acres is {} in squate meters. Thank you.".format(res1,result))

    elif res=='2':
        try:
            res2=float(input("Enter the value that you want to convert: \n"))
        except ValueError:
                raise ValueError("You have given a wrong value. Thank you.")
        result=res2/4047
        print("Your value {} in square meters is {} in acres. Thank you.".format(res2,result))
        
    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return acres()
        if response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")
    #return acres()
