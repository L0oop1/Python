# You type in the name of the monster
monster = input("Name a monster: ")

# Printing the name you typed
print("A wild", monster,"has appeaared")

# What should you do
action = input("Run or attack? ")

# Making it use what you said
if action == "attack":
  print("You defeated the monster!")
if action == "run":
  print("You ran away!")

print("---L0oop1---")
