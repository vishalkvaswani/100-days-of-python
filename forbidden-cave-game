import random

enemies = ["Goblin", "Orc", "Skeleton", "Dragon", "Vampire", "Zombie"]

user_name = input("========== Welcome to the Forbidden Cave ==========\n\nType your name?\n")

enemy_extra = int(
  input(
    f"Would you like a custom Enemy Character? "
    f"0 For Yes, 1 for No\n")
)

if enemy_extra == 0:
  
  enemy_name = input("What's your custom Enemy? Type the name:\n")
  enemy1 = enemy_name
  
elif enemy_extra == 1:
  enemy1 = random.choice(enemies)
  
else:
  print(
    f"You failed to determine your custom enemy.\n"
    f"The algorithm is now choosing an enemy for you.\n"
    f"Wait & Watch. 😈")
  enemy1 = random.choice(enemies)

player_hp = 100

enemy1_hp = 100

print(f"Your enemy is {enemy1}.")

for i in range(5):
  
  critical = random.randint(1, 5)
  player_attack = random.randint(10,30)
  
  if critical == 5:
    enemy1_hp-= (2*player_attack)
    print(
      f"========== ROUND {i+1} ==========\n\n{user_name} attacks "
      f"{enemy1}!\n\n💥 CRITICAL Double HIT to {enemy1}!\n"
      f"\nDamage: 2x {player_attack}\n"
      f"\n{enemy1} HP: {enemy1_hp}\n\n------\n"
    )
    
  else:
    enemy1_hp-= player_attack
    print(
      f"========== ROUND {i+1} ==========\n\n{user_name} attacks "
      f"{enemy1}!\n\nNormal HIT to {enemy1}!\n\nDamage: "  
      f"{player_attack}\n"
      f"\n{enemy1} HP: {enemy1_hp}\n\n------\n"
    )
   
  if enemy1_hp <= 0:
    print(f"💀{enemy1} has been defeated!\n🏆 YOU WIN!")
    break

  critical1 = random.randint(1, 5)
  enemy_attack = random.randint(5,25)  
  
  if critical1 == 5:
    player_hp-= (2*enemy_attack)
    
    print(
      f"{enemy1} attacks {user_name}!\n\n💥 CRITICAL Double HIT "
      f"to {user_name}!\n\n"
      f"Damage: 2x {enemy_attack}\n\nYour HP: {player_hp}\n"
    )
    
  else:
    player_hp-= enemy_attack
    
    print(
      f"{enemy1} attacks {user_name}!\n\nNormal HIT "
      f"to {user_name}!\n\n"
      f"Damage: {enemy_attack}\n\nYour HP: {player_hp}\n"
    )

  if player_hp <= 0:
    print("💀 You have been defeated!\nGAME OVER")
    break
    
if player_hp <= 0:
  player_hp = 0

if enemy1_hp <= 0:
  enemy1_hp = 0
  
print(
  f"\n========================\nBATTLE "
  f"RESULT\n========================"
  f"\n\nPlayer: {user_name}\n"
  f"Enemy: {enemy1}\n"
  f"\nYour HP: {player_hp}\n"
  f"Enemy HP: {enemy1_hp}\n\n"
  f"Rounds survived: {i+1}"
     )  


if enemy1_hp <= 0:
    print("🏆 VICTORY!")
elif player_hp <= 0:
    print("💀 DEFEATED!")
else:
    print("Not Bad! You failed to defeat the enemy.")
    print("You must train more and come back!")
