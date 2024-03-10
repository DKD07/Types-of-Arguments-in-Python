#We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
def average(a=9,b=1):
    print("The average is: ",(a+b)/2)
average()
average(5,1) # It will print  the average of recent  value
average(5) # It denotes the "a" value and "b" value is given
average(b=9)
average(b=9,a=21)