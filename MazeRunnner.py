from Myro import *


def TonyIsEvil():
    while True:
        left,right=getLine()
        if left==1 and right==1:
            motors(-.5,-0.5)
            wait(0.5)
        elif left==1 and right==0:
            motors(-0.8,0.4)
        elif left==0 and right==1:
            motors(0.4,-0.75)
        elif left==0 and right==0:
            motors(2*Random.random()-1,2*Random.random()-1)
            wait(0.5)
        print(left,right)
        
        
        
def chickenBiscuit():
    while True:
        left,right=getLine()
        if left==1 and right==0:
                motors(-1.6,-1.1)
        if left==0 and right==1:
                motors(-1,-0.5)
        if left==1 and right==1:
                motors(-1000,-1000)
        if left==0 and right==0:
                motors(0.5,-0.5)
                        
                
                
def chickenBiscuitTONY():
    counter=0
    while True:
        left,right=getLine()
        if left==1 and right==0:
                motors(-0.8,-0.1)
                counter=counter+1
        if left==0 and right==1:
                motors(-0.1,-0.8)
                counter=counter-1
        if left==1 and right==1:
                motors(-2,-2)
        if left==0 and right==0:
            if counter==1:
                    motors(0.2,0.9)
                    counter=counter+1
            if counter==-1:
                    motors(0.9,0.2)
                    counter=counter+1
                
def chickenBiscuitForward():
    while True:
        left,right=getLine()
        if left==1 and right==0:
                motors(1,0.5)
        if left==0 and right==1:
                motors(1,0.5)
        if left==1 and right==1:
                motors(2,2)
        if left==0 and right==0:
                motors(0.9,0.2)

def chickenBiscuitTEST():
    while True:
        left,right=getLine()
        print(left,right)
        if left==1 and right==0:
                turnLeft(0.8,0.01)
        if left==0 and right==1:
                turnRight(0.8,0.01)
        if left==1 and right==1:
                motors(-1000,-1000)
        if left==0 and right==0:
                motors(0.6,-1)
                       
def crossRoad():
    from Myro import*
    onLine=False
    onWhite=False
    left,right=getLine()
    if left==0 and right==0:
        onLine=True
    else:
        onWhite=True
    counter=0
    while True:
        motors(-1,-1)
        #lineCount=[]
        left,right=getLine()
        #lineCount.append([left,right])
        if left==0 and right==0:
            if onWhite==True:
                counter+=1
                onWhite=False
                print(counter)
        if counter==12:
            motors(0.8,0.8)
            wait(2)
            stop()
            chickenBiscuitTEST    
        else:
            onWhite=True
            onLine=False
        """if onLine==True:
            counter+=1
            stop()
            motors(-1,-1)
        if onWhite==True:
            counter+=1
            stop()
            motors(-1,-1)
        if counter==9:
            turnRight(0.5,0.5)
"""
crossRoad()                