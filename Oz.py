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
    
    #Binary to Decimal
def b2d(num):
    firstDigit = num[0]
    secondDigit =num[1]
    thirdDigit = num[2]
    fourthDigit = num[3]
    fifthDigit = num[4]
    sixthDigit = num[5]
    seventhDigit = num[6]
    eighthDigit = num[7]
    
    firstInteger = int(firstDigit)
    secondInteger = int(secondDigit)
    thirdInteger = int(thirdDigit)
    fourthInteger = int(fourthDigit)
    fifthInteger = int(fifthDigit)
    sixthInteger = int(sixthDigit)
    seventhInteger = int(seventhDigit)
    eighthInteger = int(eighthDigit)
    
    thingtoAddTo = 0
    
    if firstInteger == 1:
        thingtoAddTo += 128
    if secondInteger == 1:
        thingtoAddTo += 64
    if thirdInteger == 1:
        thingtoAddTo += 32
    if fourthInteger == 1:
        thingtoAddTo += 16
    if fifthInteger == 1:
        thingtoAddTo += 8
    if sixthInteger == 1:
        thingtoAddTo += 4
    if seventhInteger == 1:
        thingtoAddTo += 2
    if eighthInteger == 1:
        thingtoAddTo += 1
    thingtoAddTo *= 0.001
    return thingtoAddTo
    
    #Decimal to Binary
def d2b(num):
    binaryList = []
    if num < 1:
        num *= 1000
    if num >=128:
        num -= 128
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=64:
        num -= 64
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=32:
        num -= 32
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=16:
        num -= 16
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=8:
        num -= 8
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=4:
        num -= 4
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=2:
        num -= 2
        binaryList.append(1)
    else:
        binaryList.append(0)
    if num >=1:
        num -= 1
        binaryList.append(1)
    else:
        binaryList.append(0)
    finalValue = "" 
    for l in binaryList:
        finalValue += str(l)
    realFinal = (finalValue)
    return(realFinal)

    
            
    