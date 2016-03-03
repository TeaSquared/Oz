from Myro import *
from Graphics import *

robot = getRobot()
if robot == None:
    init("com25")
    
from math import *
from imageProcessing import *
from setBlob import *


def followBlob():
    setupBlob()
    blobTrack()
    #doTogether(updateConfigure,blobTrack2)
                                                                                                    
def blobTrack():

    while(True):
        B=takePicture("blob")
        m,x,y=blobSeg(B, True)
        print(m,x,y)

        show(B,"blobImage")
        
"""def balloon():
       
    while(True):
        B=takePicture("blob")
        m,x,y=blobSeg(B, True)
        if x>180 and x<240:
            motors(1,1)
        else: 
            stop()
            motors(0.5,0)    
"""
        
        
def blobby():
    while(True):
        B=takePicture("blob")
        m,x,y=blobSeg(B, True)
        if x>258:
            turnLeft(((x-228)/22), 0.25)
        if x<178:
            turnRight(((228-x)/22),0.25)
        if x>178 and x<258:
             print("Target LOCKED")  
             motors(1000,1000)
             beep(99,99)
        elif x==0:
            motors(0.1,-0.1)
        #elif x==0:
            #print("Locking on target")
        #print("BLOB")
             
def blobby3():
    counter=0
    while(True):
        B=takePicture("blob")
        m,x,y=blobSeg(B, True)
        if x>278:
            motors(-1,1) 
            counter=counter+1     
        elif x<158:
            motors(1,-1)
        elif x>158 and x<278:
             motors(100,100)
             counter=0 
        elif x==0:
            counter=counter+1   
        elif counter==5:
            motors(100,100)
            print("Locking on target")
        #print("BLOB")
                          
def runAway():
    
    while(True):
        B=takePicture("blob")
        m,x,y=blobSeg(B, True)
        if x>268:
            motors(-0.5,-0.05)
        
        elif x<168:
            motors(-0.05,-0.5)
        elif x>168 and x<268:
             motors(-100,-100)
             
        print("error")

def spinInPlace():
    motors(1,-1)
             