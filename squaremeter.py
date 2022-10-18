#Calculate Square meter.

def squaremeter():
    try:
        lenght=float(input("Enter the Lenght side value: "))
        width=float(input("Enter the Width side value: "))
    except ValueError:
        raise ValueError("You have entered wrong value.")
    result=lenght*width
    print("The area is {} square meters.".format(result))
    #return squaremeter()
    