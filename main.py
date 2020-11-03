from Checkout import Option0
from Checkout import Option1
from Checkout import Option2

########################################################################################################################

print("Hello, which Laptop would you like to access?:")

Laptops_to_choose = [Option0.name, Option1.name, Option2.name]

print("Option1: " + Option0.name, ", ", Option0.num, ", ", Option0.condition, "\nOption2: " + Option1.name, ", ", Option1.num, ", ", Option1.condition, "\nOption3: " + Option2.name, ", ", Option2.num, ", ", Option2.condition, "\n ", "\nType answer here (Name of brand only): ")

selection = input()

if selection == "Microsoft":
    print("Accessing", Laptops_to_choose[0])
elif selection == "Macbook":
    print("Accessing", Laptops_to_choose[1])
elif selection == "HP":
    print("Accessing", Laptops_to_choose[2])

while Laptops_to_choose != "Microsoft" "Macbook" "HP":
    print("Does it look like that's a choice? -_-?")
    print("\nWhich Laptop would you like to access?:")
    print("Option1: " + Option0.name, ", ", Option0.num, ", ", Option0.condition, "\nOption2: " + Option1.name, ", ", Option1.num, ", ", Option1.condition, "\nOption3: " + Option2.name, ", ", Option2.num, ", ", Option2.condition, "\n ", "\nType answer here (Name of brand only): ")

    selection = input()

    if selection == "Microsoft":
        print("Accessing", Laptops_to_choose[0])
        break
    elif selection == "Macbook":
        print("Accessing", Laptops_to_choose[1])
        break
    elif selection == "HP":
        print("Accessing", Laptops_to_choose[2])
        break


########################################################################################################################

print("\nWhat would you like to do?")
print("-Watch Netflix", "\n-Play Minecraft", "\n-Text my friends", "\n-Check out")
Options_to_choose = ["Watch Netflix", "Play Minecraft", "Text my friends", "Check out"]
Moz = input()

while Moz != "Watch Netflix" "Play Minecraft" "Text my friends" "Check out":

    if Moz == "Check out":
       print("\nChecking out of", selection)
       break

    while Moz == "Watch Netflix":
       print("\nSorry, you don't have Netflix", "\nPlease try again:")
       print("\nWhat would you like to do?")
       print("-Watch Netflix", "\n-Play Minecraft", "\n-Text my friends", "\n-Check out")
       Moz = input()
       break

    while Moz == "Play Minecraft":
       print("\nSorry, you don't have Minecraft", "\nPlease try again:")
       print("\nWhat would you like to do?")
       print("-Watch Netflix", "\n-Play Minecraft", "\n-Text my friends", "\n-Check out")
       Moz = input()
       break

    while Moz == "Text my friends":
       print("\nSorry, you don't have friends", "\nPlease try again:")
       print("\nWhat would you like to do?")
       print("-Watch Netflix", "\n-Play Minecraft", "\n-Text my friends", "\n-Check out")
       Moz = input()
       break

    while Moz != "Watch Netflix" "Play Minecraft" "Text my friends" "Check out":
        print("\nSorry, that's not an option", "\nPlease try again:")
        print("\nWhat would you like to do?")
        print("-Watch Netflix", "\n-Play Minecraft", "\n-Text my friends", "\n-Check out")
        Moz = input()
        break

print("\nLoading...")

print("\nCheck out complete")

print("Have a nice day!")














