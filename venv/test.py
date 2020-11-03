
import sys, pygame





























''''''

''''
class Game_Character:
    def __init__(self, name1, super_power1, weapon1):
        self.name = name1
        self.super_power = super_power1
        self.weapon= weapon1
    def getSuperPower(self):
        print("This character's superpower is: ", + self.super_power)
character1 = Game_Character("Cool Guy", "Strength", "Blaster")

character1.getSuperPower()



















































''''''

  #add

 #remove

#get length

lists_of_prizes = ["f", "b", "g"]

selection = input()
print(selection)

if int(selection) == 1:
    print("You won a" , lists_of_prizes[0])
elif selection == "2":
    print("You won a" , lists_of_prizes[1])
elif selection == "3":
    print("You won", lists_of_prizes[2])
elif selection == "4":
    print("You won", lists_of_prizes)



''''''
yeet_yeet = ["eat", "sleep", "repeat"]
print("Yeet: \n")

condition = 1
while condition < len(yeet_yeet):
    print(yeet_yeet[condition])
    break

if(condition == 1):
        print("\nYou have reached the end of your list")
condition += 1










''''''




Burger = "Burger"
Name = "Moses"
print("Good day monsieur. Who will I be serving today?")
yeet_confirmation = input()
if yeet_confirmation == Name:
    print("Good day", Name ,)
else:
    print("Forgive me, I didn't catch that. Could you please say that again?")
    Moses = input()
print("Ohhhhhhhhh Moses. I thought I heard something else.")


print("What would you like to order on this fine day?")
food_confirmation = input()
if food_confirmation == Burger:
    print("Ah yes. Our most ordered dish. Coming right up!")
else:
    print("I'm sorry can you repeat that? My old age is doing a number on my hearing abilities.")
    Burger = input()


print("Oh ok. you said a burger right? Not........booger?")

food2_confirmation = input()
if food2_confirmation == "yes":
    print("Ah yes. Our most ordered dish. Coming right up!")
else:
    print("Say that one more time please.")
    YYYEEESSS = input()
print("*butler runs off to the kitchen")

































































'''



