print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

disition_01 = input("\nYou are at a crossroad. Where do you want to go? Type 'left' or 'right' : ")

if disition_01.lower() == "right":
  print("You fell into a hole. Game Over!")
          
elif disition_01.lower() == "left":
  print("You have come to a lake. There is an island in the middle of the lake.")
          
  disition_02 = input("\nType 'wait' to wait for a boat. Type 'swim' to swim across. : ")

  if disition_02.lower() == "swim":
          print("You get attacked by an angry trout. Game Over!")

  else:
            disition_03 = (input("\nYou arrive at the island unharmed. There is a house with 3 doors. One red, blue and yellow. Which colour do you choose? : "))
            if disition_03.lower() == "yellow":
                      print("You win")
            else:
                      print("Game Over!")