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
      
#Had to close a pathway as it was getting too much. I am focusing on the other two ways

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
      
def cultRoom():
  directions = ["forward","backward"]
  print("You come into a large circular room, with a giant alter in the middle. The room is coved in candles and smells of blood.")
  print("What is this place?")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/forward")
    userInput = input()
    if userInput == "backward":
      tunnelScene()
    elif userInput == "forward":
     alterScene()
    else:
      print("Please enter a valid option.")
      
#This section is more of a horror movie vibe.

def alterScene():
  directions = ["forward","backward"]
  print("You move in to take a closer look at the alter. ")
  print("The alter is large, human-sized even. Why would they have something like that here?")
  print("You spin around to take in the whole room and notice a wine bottle in the corner, a modern wine bottle.")
  print("Someone was down here! Maybe there is a way out around here?")
  userInput = ""
  while userInput not in directions:
    print("Options: backward/forward")
    userInput = input()
    if userInput == "backward":
      print("You quickly turn around, and powerwalk out of the room.")
      print("This room has too many red flags!")
      print("Nope! Not doing that. There has to be a better way out!")
      tunnelScene()
    elif userInput == "forward":
      print("What could be in there?")
      print()
     crawlspaceScene()
    else:
      print("Please enter a valid option.")
      
#I have one large more sections then this pathway will be complete.

def crawlspaceScene():
  directions = ["forward", "backward"]
  print("You move into look at the wine bottle. There must be a way out.")
  print("As I bend down to take a look, I notice a small crawl space off to the side.")
  print()
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
     print("The small opens into another room. In the middle is a pedestal with a book on it.")
     print("What is this book doing here?")
     print()
     bookScene()
    elif userInput == "backward":
        print("This room has too many red flags! I'm out of here!")
        tunnelScene()
    else:
      print("Please enter a valid option.")
      
def bookScene():
  directions = ["forward"]
  print("You move closer to the book. It's an old leather book. You open the book")
  print("The pages are yellowed, and the writing seems to be in Latin?")
  print("The more you flip through the book, the more your veins fill with dread and terror.")
  print()
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
     print("You slam the book shut.")
     print("You shouldn't be here.")
     print()
     sacrificeScene()
    else:
      print("Please enter a valid option.")

def sacrificeScene():
  directions = ["fight","flee"]
  print("You slam the book shut and and look around.")
  print("You hear a voice behind you, 'not like the reading material?'")
  print("You spin around and see a large, dark figure in a robe")
  print("They smile and say, 'You're not supposed to be here.' ")
  print()
  userInput = ""
  while userInput not in actions:
    print("Options: flee/fight")
    userInput = input()
    if userInput == "fight":
      if weapon:
        print("The cultist moves forward, and you fight with everything you have.")
        print("Just as you feel you might lose, you remember the knife.")
        print("You drive the knife into the chest of the cultist")
        print("Your would-be murder lets of a roar of rage and pain.")
        print("As he dies, you nice a piece of paper sticking out of his robes.")
        print("It's a map! Now you can leave this awful place.")
        print("Congratulations! You have completed the Cultist Fight Ending")
        print("Though your courage is admirable, you may not have had to fight your way out.")
        print("Do you want to try again?")
        print("")
      else:
        print("The ghoul-like creature wrestles you to the ground.")
        print("The cultist seems to deprive a sick joy from seeing your fear.")
        print("They begin to chock you, you scratch and claw at them, but it does seem to phase them.")
        print("As you lose consciousness, you hear 'What a marvelous sacrifice!'")
        print("You have been killed you.")
        print("")
        print("If only you had found the knife.... OOPS spoilers!")
        print("Do you want to try again?")
        print("")
      quit()
    elif userInput == "flee":
      print("You run around the cultist as fast as you can, and you make it to the crawlspace!")
      print("Just a little further! just as you reach the end, he drags you by your feet back.")
      print("You kick and scream, but they just laugh.")
      print("They let you of your feet, and you get to you feet. Only to be met with a fist to the face.")
      print("You go down and he drives on top of you. You don't get up again.")
      print("")
      print("Oh no! You have been killed by the cultist.")
      print("If only you had read the warning signs")
      print("Seriously, the 'smell of blood wasn't a clue?")
      print("Well, curiosity may have killed the cat, but satisfaction brought it back.")
      print("Want to try again?")
      print()
      quit()
    else:
      print("Please enter a valid option.")
      
 #I added another fight scene to play of the knife idea. I wanted the game to have more thrill.  

def ghoulScene():
  directions = ["forward","backward"]
  print("The whispers get louder. You whip your head around looking for the source.")
  print("The whisper come together in a twisted chorus. They beckon me to come closer.")
  print("Do I dare move forward? ")
  print("")
  print()
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("Multiple ghoul-like creatures start emerging as you enter the room.")
      print("They lunge for you and you only have a single moment to scream before they tare into you! ")
      print("You are killed.")
      print("")
      print("Oh no! You have completed the Killed Ending.")
      print("Are you brave enough to restart for a better ending?")
      print("")
      quit()
    elif userInput == "backward":
      hauntedRoom()
    else:
      print("Please enter a valid option.")
     
#Added onto the ghoul idea to added another pathway.    
      
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
      
def skeltonScene():
  directions = ["right", "forward","backward"]
  print("You see a skeleton. They have a camera case around their neck. Guess they didn't make it out.")
  print("")
  userInput = ""
  while userInput not in directions:
    print("Options: right/forward/backward")
    userInput = input()
    if userInput == "forward":
      darknessScene()
    elif userInput == "backward":
      cameraScene()
    elif userInput == "right":
      hiddendoorScene()
    else:
      print("Please enter a valid option.")
      
#Added more lore into the camera comment. 
#Edited again to to add a secret tunnel ending

def darknessScene():
  directions = ["forward","backward"]
  print("You move forward, but the torches you have been lighting no longer work.")
  print("You try and pry the torch off of the wall, but the mental has rushed solid. It's not budging.")
  print("Do I go into the darkness or head back?")
  userInput = ""
  while userInput not in directions:
    print("Options: forward/backward")
    userInput = input()
    if userInput == "forward":
      print("You tentatively go forward.")
      print("You know you must keep moving. You don't know what, but you won't let your fate be like Camera Guy.")
      print("As you move forward, you feel a breeze. You must be close to an exit.")
      print("You break into a run, but soon the ground beneath your feet vanishes.")
      print("")
      print("Oh no, you fell of a cliff.")
      print("Maybe running in the dark is a bad idea.")
      print("Would you like to try again?")
      quit()
    elif userInput == "backward":
      skeltonScene()
    else:
      print("Please enter a valid option.")
      
#Darkness is big part of horror, so I added that as a part.
    
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
  print("You notices the torches lining across the walls. You move put up your lighter to the ancient torch.")
  print("It lights! That's good, the battery on your phone is in single digits.")
  print("Once light has illuminated you way. You notice a crossroads, and you can choose to go down any of the four hallways.") 
  print("Where would you like to go?")
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
      
#Added a way to know why the character can see without making it harder.

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
