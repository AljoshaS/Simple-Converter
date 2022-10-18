#Percentage calculator.

def percentage():
    
    response=input("Calculate Percentage: Example 'What is 10% of 150' - type '1'\n"
                   "Calculate Percentage: Example 'What percent of 60 is 12' - type '2'\n"
                   "Calculate Percentage: Example '25 is 20% of what number' - type '3'\n")
    
    if response=='1':

        try:
            value=int(input("Enter the value that you want to calculate percentage of.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")
        try:
            value_of_percentage=int(input("Enter the value of the percentage.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")

        #The formula is for: the percentage is ? of a given value. The result is not a percentage.
        res1=value_of_percentage*value
        res2=int(res1/100)      
        print("The percentage {} % is {} in value of {}.".format(value_of_percentage,res2,value))

    elif response=='2':

        try:
            value=int(input("Enter the hole value. From the example the 60 goes here.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")
        try:
            value_for_percentage=int(input("Enter the value that you want to calculate the percentage of. From the example the 12 goes here.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")

        #The formula is for: the value is that percentage of given value. The result is a percentage.
        res2=value_for_percentage/value
        res3=res2*100
        print("The value {} is {} in percentage of the hole value {}.".format(value_for_percentage,res3,value))

    elif response=='3':

        try:
            value=int(input("Enter the hole value. From the example the 25 goes here.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")
        try:
            percentage_value=int(input("Enter the percentage. From the example 20% goes here.\n"))
        except ValueError:
            raise ValueError("You have entered wrong value")
            
        #The formula is for: check if a given value is ? percentage of what number?
        for_decimal=percentage_value/100
        res4=value/for_decimal
        print("The value {} in percentage is {}, from {}".format(value,percentage_value,res4))
    
    else:
        print("Thank you for your time.")
        response=input("Do you wish to start again? Y/N?\n")
        if response=='Y':
            return percentage()
        if response=='N':
            print("Thank you for your time.")
        else: 
            print("Thank you for using this app")

    #return percentage()

    
