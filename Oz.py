def add2things(thing1,thing2):
    sumthing=thing1+thing2
    return(sumthing)

def addNthings(listOfThings):
    for thingamcbob in listOfThings:
        print(thingamcbob)           
        
def klausClawsKlaus(klauz):
    for claws in klauz:
        return(claws)


def bob(listOfThings):
    foo=0
    for item in listOfThings:
        #print(item)
        foo=foo+item
    return(foo)
        
        
def scribInit(com):
    from Myro import*
    command = "com"+str(com)
    init(command)
    #init(com)
    #init("com1")
        