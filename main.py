
import random as r
import time as t
import sys as sus
from replit import audio


evolve = r.randint(1, 40)
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
x = r.randint(1, 5)
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
    wooloo = r.randint(1, 4)
    answer = input("fight/catch/run ")
    if answer == "fight" and starter == "sobble" and x == 2:
    
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
    if answer == "catch":
        print("gotcha wooloo was caught!")
        break
    if evolve == 1:
        print("what sobble is evolving")
        print("congrats your sobble evovled to a drizzile")