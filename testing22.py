import random
def gameWin(Comp, you):

      if Comp == you:
            return None
      elif Comp=="s":
            if you=="w":
              return False
            elif you=="g":
              return True

      elif Comp=="w":
            if you=="g":
              return False
            elif you=="s":
              return True

      elif Comp=="g":
            if you=="s":
              return False
            elif you=="w":
                  return True
                  


print("Comp Turn : snake(s) water(w) or Gun(g)?")

randNo = random.randint(1,3)

if randNo==1:
      Comp="s"
elif randNo==2:
      Comp="w"
elif randNo== 3:
      Comp="g"

you = input("player's Turn : snake(s) water(w) or Gun(g)?")

a=gameWin(Comp, you)

print(f"computer choose\t {Comp}\n")
print(f"You choose\t {you}\n")

if a==None:
  print("the game is a tie")
elif a:
  print("you win")
else:
  print("you lose")