
import random as r
import time as t
import sys as sus
from replit import audio
grooky_health = 50
scorbunny_health = 50
sobble_health = 50
nicket_health = 40
drednaw_health = 80
pickachu_health = 35
wooloo_health = 42
eternatus_health = 140

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
x = r.randint(2, 2)
if x == 1:
    print("You encountered a wild pickachu")
elif x == 2:
    print("You encountered a wild wooloo")
elif x == 3:
    print("You encountered a wild nickit")
elif x == 4:
    print("You encountered a tough looking drednaw")
elif x == 5:
    print("You encountered a wild WOAH WHAT THE A WILD ETERNATUS")
audio.play_file('pokemon.wav',1)
while x == 2:
    master_ball = r.randint(1,1)
    ultra_balls = r.randint(1,2)
    great_balls = r.randint(1,3)
    catch = r.randint(1,5)
    wooloo = r.randint(1, 4)
    answer = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("wooloo's health " + str(wooloo_health))
    if answer == "run":
      sus.exit("you ran away")
    elif answer == "fight" and starter == "sobble" and x == 2:
    
        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight = input()
        if fight == "water pulse":
            print("that did 60 damage")
            wooloo_health -= 60
        if fight == "water gun":
            print("that did 40 hp")
            wooloo_health -= 40
        if wooloo == 4:
            print("wooloo used Double-Edge")
            sobble_health -= 23
        elif wooloo == 1:
            print("wooloo used take down")
            sobble_health -= 12
        elif wooloo == 2:
            print("wooloo used tackle")
            sobble_health -= 8
        elif wooloo == 3:
            print("wooloo used headbutt")
            sobble_health -= 20
        if sobble_health <= 0:
            audio.play_file('oof.wav',1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if wooloo_health <= 0:
            print("The wild wooloo fainted we'll get em next time")
            break
    elif answer == "catch" and catch == 1:
        print("gotcha wooloo was caught!")
        break
    elif answer == "catch" and catch == 2:
      print("close!")
    elif answer == "catch" and catch == 3:
      print("Aw that was So close!")
    elif answer == "catch" and catch == 4:
      print("That was so close keep it up!")
    elif answer == "catch" and catch == 5:
      print("Ok now that was way to close!")
    elif answer == "bag":
      print("you have 20 potions")
      print("you have 40 pokeballs")
      print("you have 30 great balls")
      print("you have 10 ultra balls")
      print("you have 1 master ball")
      bag = input("what do you want to use ")
      if bag == "potion" and sobble_health >= 30:
        print("healed pokemon")
        sobble_health += 20
      elif bag == "potion" and sobble_health == 31:
        print("healed pokemon")
        sobble_health += 19
      elif bag == "potion" and sobble_health == 32:
          print("healed pokemon")
          sobble_health += 18
      elif bag == "potion" and sobble_health == 33:
        print("healed pokemon")
        sobble_health += 17
      elif bag == "potion" and sobble_health == 34:
        print("healed pokemon")
        sobble_health += 16
      elif bag == "potion" and sobble_health == 35:
        print("healed pokemon")
        sobble_health += 15
      elif bag == "potion" and sobble_health == 36:
        print("healed pokemon")
        sobble_health += 14
      elif bag == "potion" and sobble_health == 37:
        print("healed pokemon")
        sobble_health += 13
      elif bag == "potion" and sobble_health == 38:
        print("healed pokemon")
        sobble_health += 12
      elif bag == "potion" and sobble_health == 39:
        print("healed pokemon")
        sobble_health += 11
      elif bag == "potion" and sobble_health == 40:
        print("healed pokemon")
        sobble_health += 10
      elif bag == "potion" and sobble_health == 41:
        print("healed pokemon")
        sobble_health += 9
      elif bag == "potion" and sobble_health == 42:
        print("healed pokemon")
        sobble_health += 8
      elif bag == "potion" and sobble_health == 43:
        print("healed pokemon")
        sobble_health += 7
      elif bag == "potion" and sobble_health == 44:
        print("healed pokemon")
        sobble_health += 6
      elif bag == "potion" and sobble_health == 45:
        print("healed pokemon")
        sobble_health += 5
      elif bag == "potion" and sobble_health == 46:
        print("healed pokemon")
        sobble_health += 4
      elif bag == "potion" and sobble_health == 47:
        print("healed pokemon")
        sobble_health += 3
      elif bag == "potion" and sobble_health == 48:
        print("healed pokemon")
        sobble_health += 2
      elif bag == "potion" and sobble_health == 49:
        print("healed pokemon")
        sobble_health += 1
      elif bag == "potion" and sobble_health == 50:
        print("your pokemon is at full health")
      elif bag == "master ball" and master_ball == 1:
        print("gotcha wooloo was caught")
      elif bag == "ultra balls" and ultra_balls == 1:
        print("gotcha wooloo was caught!")
      elif ultra_balls == 2:
        print("Aw so close!")
      elif bag == "great balls" and great_balls == 1:
        print("gotcha wooloo was caught!")
        break
      elif answer == "catch" and great_balls == 2:
        print("close!")
      elif answer == "catch" and catch == 3:
        print("Aw that was So close!")