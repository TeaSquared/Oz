from Myro import *

def Story():
    location = "Cell"
    if location == "Cell":
        ans_1 = askQuestion("You wake up in a cell with no idea how you got there.",["Scream wildly.","Try to open door.","Look around calmly.","Exit"])
        if ans_1 == "Scream wildly.": 
            ans_2 = askQuestion("GUARD: Why are you screaming again Johnson, shut up or its off to solitary!",["Continue Screaming","Yes sir."])
            if ans_2 == "Continue Screaming":
                ans_3 = askQuestion("GUARD: Thats it! Off to Solitary! {You die in solitary D:}")
            if ans_2 == "Yes sir.":
                ans_1 = "Look around calmly."
        if ans_1 == "Look around calmly.":
            ans_4 = askQuestion("Do you look:",["In the corner","Under the bed","By the door"])
            if ans_4 == "In the corner":
                ans_5 = askQuestion("You see a spoon do you:",["Grab it","Look elsewhere"])
                if ans_5 == "Grab it":
                    spoonAchieved = True
                    ans_4 = "Under the bed"
                if ans_5 == "Look elsewhere":
                    ans_4 = "Under the bed"
            if ans_4 == "Under the bed":
                ans_6 = askQuestion("There is a loose brick!",["Pull it out","Look elsewhere"])
                if ans_6 == "Pull it out":
                    print("Incomplete Story Line")
                if ans_6 == "Look elsewhere":
                    ans_4 = "By the door"
            if ans_4 == "By the door":
                ans_7 = askQuestion("There is a gap in the bars!",["Slip through!","Look around hallway"])
                
                    
                         
                






 
 
 
 
 
 
 
 
 
 
 
Story()
