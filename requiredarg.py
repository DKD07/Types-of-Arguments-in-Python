#In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

#Examople-1
#(It will show error because the number of arguments passed does not match the actual function definition)

#def name(fname, mname, lname):
#    print("Hello,", fname, mname, lname)
#name("Peter", "Quill")

#Example-2
#It will not show the error because the number of arguments passed matches to the actual function defintion
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name("Peter", "Ego", "Quill")
