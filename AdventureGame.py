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
      print("Multiple goul-like creatures start emerging as you enter the room. You are killed.")
      quit()
    elif userInput == "left":
      print("You made it! You've found an exit.")
      quit()
    elif userInput == "backward":
      introScene()
    else:
      print("Please enter a valid option.")

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
