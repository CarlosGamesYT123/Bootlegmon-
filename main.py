import random as r
import time as t
import sys as sus

wooloo = r.randint(1,4)
sobble_health = 50
nicket_health = 40
drednaw_health = 80
pickachu_health = 35
wooloo_health = 42
eternatus_health = 140
wooloo_attack = "tackle"
wooloo_attack2 = "headbutt"
wooloo_attack3 = "growl"
wooloo_attack4 = "Double-Edge"




while True:
  starter = input("Which starter do you want Scorbunny, sobble, grooky ")
  if starter == "sobble":
    print("you chose sobble")
    break
  elif starter == "scorbunny":
    print("you chose scorbunny")
    break
  elif starter == "grooky":
    print("you chose grooky")
    break
  else:
    print("that is not a starter choose another one")
print("you head into the tall grass and you encountered a wild pokemon")
t.sleep(4)
x = r.randint(1,5)
if x == 1:
  x=r.randint(1, 1000)
  if x>1000:
    print("You encountered a wild pickachu")
  else:
    print("You encountered a shiny pickachu")
elif x == 2:
  print("You encountered a wild wooloo")
elif x == 3:
  print("You encountered a wild nickit")
elif x == 4:
  print("You encountered a tough looking drednaw")
elif x == 5:
  print("You encountered a wild WOAH WHAT THE A WILD ETERNATUS")
while x == 2:
  answer = input("fight/catch/pokemon/run ")
  if answer == "fight" and starter == "sobble" and x == 2:
    print("what move do you want to use")
    print("scratch")
    print("growl")
    print("water gun")
    print("water pulse")
    fight = input()
    if fight == "water gun":
      print("that did 40 hp")
      wooloo_health -= 40
    elif wooloo == 2:
      print("wooloo used tackle")
      sobble_health -= 40
    elif wooloo == 3:
      print("wooloo used headbutt")
      sobble_health -= 70
    if sobble_health <= 0:
      print("you have no pokemon that can fight")
      sus.exit(':(')
      break
    if wooloo_health <= 0:
      print("The wild wooloo fainted we'll get em next time")
      break
  if answer == "catch":
    print("gotcha wooloo was caught!")
    break

while x == 3:
  answer2 = input("fight/catch/pokemon/run ")
  if answer2 == "fight" and starter == "sobble" and x == 2:
    print("what move do you want to use")
    print("scratch")
    print("growl")
    print("water gun")
    print("water pulse")
    fight2 = input()
    if fight2 == "water gun":
      print("that did 40 hp")
      nicket_health -= 40
    if nicket_health <= 0:
      print("The wild wooloo fainted we'll get em next time")
      break
  if answer2 == "catch":
    print("gotcha nicket was caught!")
    break

    import random as r
import time as t
import sys as sus

wooloo = r.randint(1,4)
sobble_health = 50
nicket_health = 40
drednaw_health = 80
pickachu_health = 35
wooloo_health = 42
eternatus_health = 140
wooloo_attack = "tackle"
wooloo_attack2 = "headbutt"
wooloo_attack3 = "growl"
wooloo_attack4 = "Double-Edge"




while True:
  starter = input("Which starter do you want Scorbunny, sobble, grooky ")
  if starter == "sobble":
    print("you chose sobble")
    break
  elif starter == "scorbunny":
    print("you chose scorbunny")
    break
  elif starter == "grooky":
    print("you chose grooky")
    break
  else:
    print("that is not a starter choose another one")
print("you head into the tall grass and you encountered a wild pokemon")
t.sleep(4)
x = r.randint(1,5)
if x == 1:
  x=r.randint(1, 1000)
  if x>1000:
    print("You encountered a wild pickachu")
  else:
    print("You encountered a shiny pickachu")
elif x == 2:
  print("You encountered a wild wooloo")
elif x == 3:
  print("You encountered a wild nickit")
elif x == 4:
  print("You encountered a tough looking drednaw")
elif x == 5:
  print("You encountered a wild WOAH WHAT THE A WILD ETERNATUS")
while x == 2:
  answer = input("fight/catch/pokemon/run ")
  if answer == "fight" and starter == "sobble" and x == 2:
    print("what move do you want to use")
    print("scratch")
    print("growl")
    print("water gun")
    print("water pulse")
    fight = input()
    if fight == "water gun":
      print("that did 40 hp")
      wooloo_health -= 40
    elif wooloo == 2:
      print("wooloo used tackle")
      sobble_health -= 40
    elif wooloo == 3:
      print("wooloo used headbutt")
      sobble_health -= 70
    if sobble_health <= 0:
      print("you have no pokemon that can fight")
      sus.exit(':(')
      break
    if wooloo_health <= 0:
      print("The wild wooloo fainted we'll get em next time")
      break
  if answer == "catch":
    print("gotcha wooloo was caught!")
    break

while x == 3:
  answer2 = input("fight/catch/pokemon/run ")
  if answer2 == "fight" and starter == "sobble" and x == 2:
    print("what move do you want to use")
    print("scratch")
    print("growl")
    print("water gun")
    print("water pulse")
    fight2 = input()
    if fight2 == "water gun":
      print("that did 40 hp")
      nicket_health -= 40
    if nicket_health <= 0:
      print("The wild wooloo fainted we'll get em next time")
      break
  if answer2 == "catch":
    print("gotcha nicket was caught!")
    break