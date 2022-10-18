#Volume calculation.

def volume():
    try:  
        lenght=float(input("Enter the Lenght side value: "))
        width=float(input("Enter the Width side value" ))
        height=float(input("Enter the height side value: "))
    except ValueError:
        raise ValueError("You have entered wrong value.")
    result=lenght*width*height
    print("Your volume is {}.".format(result))