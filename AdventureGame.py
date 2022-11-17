weapon = True
#This will now allow the player to pick up a knife. Which can be used in one of the escape routes.

def strangeCreature():
  actions = ["fight","flee"]
  global weapon
  print("A strange ghoul-like creature has appeared. You can either run or fight it. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("You spring into an epic battle of wills with this ghoulish monster.")
        print("Just as you feel you might lose, you remember the knife.")
        print("You drive the knife into the chest of the ghoul and the beast lets out a pained howl as it drops dead.")
        print("Congratulations! You have completed the Fight Ending")
        print("Though your courage is admirable, you may not have had to fight your way out.")
        print("Do you want to try again?")
        print("")
      else:
        print("The ghoul-like creature wrestles you to the ground.")
        print("It seems to deprive a sick joy from seeing your fear and almost seems to laugh as it goes for the kill.")
        print("You have been killed you.")
        print("")
        print("If only you had found the knife.... OOPS spoilers!")
        print("Do you want to try again?")
        print("")
      quit()
    elif userInput == "flee":
      showSkeletons()
    else:
      print("Please enter a valid option.")
# Expanded the fight scene to be more impactful and let the player to know about other endings. 
      
def showSkeletons():
  directions = ["backward","forward"]
  global weapon
  print("You see a wall of skeletons as you walk into the room. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/backward/forward")
    userInput = input()
    if userInput == "left":
      print("You find that this door opens into a wall. You open some of the drywall to discover a knife.")
      weapon = True
    elif userInput == "backward":
      introScene()
    elif userInput == "forward":
      strangeCreature()
    else:
      print("Please enter a valid option.")
      

def hauntedRoom():
  directions = ["right","left","backward"]
  print("You hear strange voices. You think you have awoken some of the dead. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      bridgeScene()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")
      
def bridgeScene():
  directions = ["forward","backward"]
  print("You come up to a old bridge made of rope and wood; part of the bridge have rotten away.")
  print("You give the bridge a good shake, and it seems to hold in place.")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You take a deep breathe, steal yourself, and take your first onto the bridge.")
      print("Despite its condition and age, its holding strong.")
      print("")
      print("As you finish crossing the bridge, the ropes snap.")
      print("You look down and watch as the bridge collapse. There is no turning back now.")
      print("Well at least it held until you got across!")
      tunnelScene()
    elif userInput == "backward":
      hauntedRoom()
    else:
      print("Please enter a valid option.")
      
#Expanded onto the gameplay area to add another way for the player to get out eventually.

def tunnelScene():
  directions = ["right","left","forward"]
  print("You take a look around.")
  print("You are faced with a crossroads. Which way to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/forward")
    userInput = input()
    if userInput == "right":
      stonewallScene()
    elif userInput == "left":
      ladderScene()
    elif userInput == "forward":
     cultRoom()
    else:
      print("Please enter a valid option.")
      
#Expanded upon the bridge pathway to create more options

def ladderScene():
  directions = ["forward","backward"]
  print("You move along the left against the cliff. You wonder if you will ever get out of here.")
  print("")
  print("Just as your losing hope, you see something moving.")
  print("What could that be?")
  print()
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      sprint("You cautiously move forward. As you get closer you see it!")
      print("A ladder! You take hold and climb up.")
      print("You have escaped!.")
      print("")
      print("Congradulations! You have completed the Ladder Ending.")
      print("There are still many secrets to find.")
      print("Do you dare to reenter?")
      quit()
    elif userInput == "backward":
      tunnelScene()
    else:
      print("Please enter a valid option.")
 #I want to expand upon the rumors of cultists using the catacombs.  
def stonewallScene():
    directions = ["backward"]
  print("You move along the cliff. Looking for a way out.")
  print("You come up to a stone wall. Looks like this way was a dead end.")
  userInput = ""
  while userInput not in directions:
    print("Options: backward")
    userInput = input()
    elif userInput == "backward":
      tunnelScene
    else:
      print("Please enter a valid option.")
      
#Had to close a pathway as it was getting too much. I am focusing on the other two ways.      
      
def cameraScene():
  directions = ["forward","backward"]
  print("You see a camera that has been dropped on the ground. Someone has been here recently. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      showShadowFigure()
    else:
      print("Please enter a valid option.")
      
def showShadowFigure():
  directions = ["right","backward"]
  print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/backward")
    userInput = input()
    if userInput == "right":
      cameraScene()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")


def introScene():
  directions = ["left","right","forward"]
  print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/backward/forward")
    userInput = input()
    if userInput == "left":
      showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
    elif userInput == "backward":
      print("You find that this door opens into a wall.")
    else: 
      print("Please enter a valid option.")

if __name__ == "__main__":
  while True:
    print("Welcome to the Catacombs!")
    #changed it to match our game theme.
    print("As an foreign traveller, you have decided to visit the Catacombs of Paris.")
    #creating the game story.
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()
