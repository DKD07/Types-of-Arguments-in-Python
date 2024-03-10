#Arbitary Arguents
def name(*name):
    print("Hello!",name[0],name[1],name[2])
name("James","Dinesh","Raj")

#Keyword Arbitary Arguments
def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname="Dinesh",fname="Abhisek",lname="Shashank")