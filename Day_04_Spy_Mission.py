import random
disguises = ["Guard", "Scientist", "Engineer"]
checkpoints = ["ID Scanner", "Biometric Scanner", "Security Guard"]
no_of_check = 0
facility = random.randint(0,2)

choice1 = int(input("You're a spy trying to infiltrate a secret facility.\nChoose your disguise:\n\n0 for Guard\n1 for Scientist\n2 for Engineer\n\n"))
if choice1 in {0,1,2}:
  print("\n-----CHECKPOINT 1-----\n")
  print(f"Your choice : {disguises[choice1]}")
  print(f"Security Checkpoint : {checkpoints[facility]}")

if choice1 >= 3 or choice1 <0:
  print("\n-----CHECKPOINT 1-----\n")
  print("No Disguise. You were caught at the checkpoint!")
  no_of_check = 0
elif choice1 == 0:
  if facility in {0,2}:
    print("Pass")
    no_of_check = 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check = 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice1 == 1:
  if facility == 1:
    print("Pass")
    no_of_check = 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check = 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice1 == 2:
  if facility == 2:
    print("Pass")
    no_of_check = 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check = 0
    print(f"Checkpoints Passed: {no_of_check}/3")
#CHOICE 2
facility2 = random.randint(0,2)
choice2 = int(input("\n----\n\nNext Checkpoint.\nChoose your disguise:\n\n0 for Guard\n1 for Scientist\n2 for Engineer\n\n"))
if choice2 in {0,1,2}:
  print("\n-----CHECKPOINT 2-----\n")
  print(f"Your choice : {disguises[choice2]}")
  print(f"Security Checkpoint : {checkpoints[facility2]}")

if choice2 >= 3 or choice2 <0:
  print("\n-----CHECKPOINT 2-----\n")
  print("No Disguise. You were caught at the checkpoint!")
  no_of_check+= 0
elif choice2 == 0:
  if facility2 in {0,2}:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice2 == 1:
  if facility2 == 1:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice2 == 2:
  if facility2 == 2:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")

#CHOICE 3
facility3 = random.randint(0,2)
choice3 = int(input("\n----\n\nLast Checkpoint.\nChoose your disguise:\n\n0 for Guard\n1 for Scientist\n2 for Engineer\n\n"))
if choice3 in {0,1,2}:
  print("\n-----CHECKPOINT 3-----\n")
  print(f"Your choice : {disguises[choice3]}")
  print(f"Security Checkpoint : {checkpoints[facility3]}")

if choice3 >= 3 or choice3 <0:
  print("\n-----CHECKPOINT 3-----\n")
  print("No Disguise. You were caught at the checkpoint!")
  no_of_check+= 0
elif choice3 == 0:
  if facility3 in {0,2}:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice3 == 1:
  if facility3 == 1:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")
elif choice3 == 2:
  if facility3 == 2:
    print("Pass")
    no_of_check+= 1
    print(f"Checkpoints Passed: {no_of_check}/3")
  else:
    print("Fail")
    no_of_check+= 0
    print(f"Checkpoints Passed: {no_of_check}/3")

print("\n----\n\n\n-----FINAL SCORE-----\n")
#ending message
if no_of_check in {2,3}:
  print(f"🕵️ MISSION COMPLETE\n\nCheckpoints Passed: {no_of_check}/3\n\n🚨 You escaped the facility!")
else:
  print(f"🕵️ MISSION FAILED\n\nCheckpoints Passed: {no_of_check}/3\n\n🚨 You got caught! And are now awaiting sentance!")

