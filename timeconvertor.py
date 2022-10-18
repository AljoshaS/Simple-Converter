#Time conversion, the user will enter hours, minutes and seconds and the conveversion will be only in hours, minutes or seconds.

def timeconvertor():
    res=input("For Time to minutes type '1' \nFor time to hours type '2' \nFor time to seconds type '3' \n")
    
    if res=='1':
        try:
            hours=int(input("Enter the 'hours': "))
            minutes=int(input("Enter your 'minutes': "))
            seconds=int(input("Enter your 'seconds': "))
        except ValueError:
            raise ValueError("You have entered a wrong value")
        result=(hours*60)+minutes+(seconds/60)
        print("The result is {} minutes".format(result))
    elif res=='2':
        try:
            hours=int(input("Enter the 'hours': "))
            minutes=int(input("Enter your 'minutes': "))
            seconds=int(input("Enter your 'seconds': "))
        except ValueError:
            raise ValueError("You have entered a wrong value")
        result=hours+(minutes/60)+(seconds/3600)
        print("The result is {} hours".format(result))
    elif res=='3':
        try:
            hours=int(input("Enter the 'hours': "))
            minutes=int(input("Enter your 'minutes': "))
            seconds=int(input("Enter your 'seconds': "))
        except ValueError:
            raise ValueError("You have entered a wrong value")
        result=(hours*3600)+(minutes*60)+seconds
        print("The result is {} seconds".format(result))
    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return timeconvertor()
        elif response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")

    #return timeconvertor()
                