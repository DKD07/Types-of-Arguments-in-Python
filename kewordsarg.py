#We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
name(mname = "Peter", lname = "Wesker", fname = "Jade")