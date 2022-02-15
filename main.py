import os
import random as r
import time as t
import sys as sus
from replit import audio
import replit

grookey_health = 50
scorbunny_health = 50
sobble_health = 50
nickit_health = 40
drednaw_health = 80
pikachu_health = 35
wooloo_health = 42
eternatus_health = 140
potions = 20
master_balls = 1
ultra_ball = 10
great_ball = 30
source = audio.play_file('pokemoncenter.wav',1)

print(' Another project from the team behind THE MONEY\n Hopefuly we won\'t get sued\n 2740 lines of code Please Enjoy BOOTLEGMON\n NOTE:this is a FAN MADE PROJECT(do not sue us pls)')
t.sleep(10)
source.set_paused(True)
#print('\n' * 100)
replit.clear()
t.sleep(1)

replit.clear()
print('preparing pokemons')
t.sleep(5)
replit.clear()
print('fluffing pillows')
t.sleep(5)
replit.clear()
print('loading modules')
t.sleep(6)
replit.clear()
print('preparing for death')
oof = audio.play_file('oof.wav',1)
t.sleep(10)
replit.clear()
print('loading music')
source = audio.platy_file('pokemoncenter.wav',1)
t.sleep(5)
replit.clear()
print('let\'s play!')
t.sleep(1)
replit.clear()

while True:
    starter = input("Which starter do you want Scorbunny, sobble, grookey ")
    if starter == "sobble":
        print("you chose sobble")
        break
    elif starter == "scorbunny":
        print("you chose scorbunny")
        break
    elif starter == "grookey":
        print("you chose grookey")
        break
    else:
        print("that is not a starter choose another one")
print("you head into the tall grass and you encountered a wild pokemon")
source.set_paused(True)
t.sleep(4)
x = r.randint(1,5)
if x == 1:
    print("You encountered a wild pikachu")
elif x == 2:
    print("You encountered a wild wooloo")
elif x == 3:
    print("You encountered a wild nickit")
elif x == 4:
    print("You encountered a tough looking drednaw")
elif x == 5:
    print("You encountered a wild WOAH WHAT THE A WILD ETERNATUS")
fight_music = audio.play_file('pokemon.wav', 1)
while x == 2 and starter == "sobble" :
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch = r.randint(1, 5)
    wooloo = r.randint(1, 4)
    answer = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("wooloo's health " + str(wooloo_health))
    if answer == "run":
        fight_music.set_paused(True)
        sus.exit("you ran away")
    elif answer == "fight" and starter == "sobble" and x == 2:

        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight = input()
        if fight == "pound":
            print("that did 4 damage")
            wooloo_health -= 4
        if fight == "sucker punch":
            print("that did 30 damage")
            wooloo_health -= 30
        if fight == "water pulse":
            print("that did 20 damage")
            wooloo_health -= 20
        if fight == "water gun":
            print("that did 10 hp")
            wooloo_health -= 10
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
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            fight_music.set_paused(True)
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
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag = input("what do you want to use ")
        if bag == "potion" and sobble_health <= 30:
            print("healed pokemon")
            sobble_health += 20
            potions -= 1
        elif bag == "potion" and sobble_health == 31:
            print("healed pokemon")
            sobble_health += 19
            potions -= 1
        elif bag == "potion" and sobble_health == 32:
            print("healed pokemon")
            sobble_health += 18
            potions -= 1
        elif bag == "potion" and sobble_health == 33:
            print("healed pokemon")
            sobble_health += 17
            potions -= 1
        elif bag == "potion" and sobble_health == 34:
            print("healed pokemon")
            sobble_health += 16
            potions -= 1
        elif bag == "potion" and sobble_health == 35:
            print("healed pokemon")
            sobble_health += 15
            potions -= 1
        elif bag == "potion" and sobble_health == 36:
            print("healed pokemon")
            sobble_health += 14
            potions -= 1
        elif bag == "potion" and sobble_health == 37:
            print("healed pokemon")
            sobble_health += 13
            potions -= 1
        elif bag == "potion" and sobble_health == 38:
            print("healed pokemon")
            sobble_health += 12
            potions -= 1
        elif bag == "potion" and sobble_health == 39:
            print("healed pokemon")
            sobble_health += 11
            potions -= 1
        elif bag == "potion" and sobble_health == 40:
            print("healed pokemon")
            sobble_health += 10
            potions -= 1
        elif bag == "potion" and sobble_health == 41:
            print("healed pokemon")
            sobble_health += 9
            potions -= 1
        elif bag == "potion" and sobble_health == 42:
            print("healed pokemon")
            sobble_health += 8
            potions -= 1
        elif bag == "potion" and sobble_health == 43:
            print("healed pokemon")
            sobble_health += 7
            potions -= 1
        elif bag == "potion" and sobble_health == 44:
            print("healed pokemon")
            sobble_health += 6
            potions -= 1
        elif bag == "potion" and sobble_health == 45:
            print("healed pokemon")
            sobble_health += 5
            potions -= 1
        elif bag == "potion" and sobble_health == 46:
            print("healed pokemon")
            sobble_health += 4
            potions -= 1
        elif bag == "potion" and sobble_health == 47:
            print("healed pokemon")
            sobble_health += 3
            potions -= 1
        elif bag == "potion" and sobble_health == 48:
            print("healed pokemon")
            sobble_health += 2
            potions -= 1
        elif bag == "potion" and sobble_health == 49:
            print("healed pokemon")
            sobble_health += 1
            potions -= 1
        elif bag == "potion" and sobble_health == 50:
            print("your pokemon is at full health")
        elif bag == "master ball" and master_ball == 1:
            print("gotcha wooloo was caught!")
            break
            fight_music.set_paused(True)
            sus.exit
        elif bag == "ultra ball" and ultra_balls == 1:
            print("gotcha wooloo was caught!")
            break
            fight_music.set_paused(True)
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag == "great ball" and great_balls == 1:
            print("gotcha wooloo was caught!")
            break
            fight_music.set_paused(True)
            sus.exit
        elif bag == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 1 and starter == 'sobble':
    master_ball2 = r.randint(1, 1)
    ultra_balls2 = r.randint(1, 2)
    great_balls2 = r.randint(1, 3)
    catch2 = r.randint(1, 5)
    pikachu = r.randint(1, 4)
    answer2 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("pikachu's health " + str(pikachu_health))
    if answer2 == "run":
        fight_music.set_paused(True)
        sus.exit("you ran away")
    elif answer2 == "fight" and starter == "sobble" and x == 1:
        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight2 = input()
        if fight2 == "pound":
            print("that did 4 damage")
            pikachu_health -= 4
        if fight2 == "sucker punch":
            print("that did 30 damage")
            pikachu_health -= 30
        if fight2 == "water pulse":
            print("that did 20 damage")
            pikachu_health -= 20
        if fight2 == "water gun":
            print("that did 10 hp")
            pikachu_health -= 10
        if pikachu == 4:
            print("pikachu used thunder bolt")
            print("That was super effective!")
            sobble_health -= 46
        elif pikachu == 1:
            print("pikachu used electro ball")
            print("that was super effective!")
            sobble_health -= 42
        elif pikachu == 2:
            print("pickacu used iron tail")
            sobble_health -= 30
        elif pikachu == 3:
            print("pikachu used electro web")
            print("That was super effecive!")
            sobble_health -= 40
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            fight_music.set_paused(True)
            sus.exit(':(')
        if pikachu_health <= 0:
            print("The wild pikachu fainted we'll get em next time")
            break
    elif answer2 == "catch" and catch2 == 1:
        print("gotcha pikachu was caught!")
        break
    elif answer2 == "catch" and catch2 == 2:
        print("close!")
    elif answer2 == "catch" and catch2 == 3:
        print("Aw that was So close!")
    elif answer2 == "catch" and catch2 == 4:
        print("That was so close keep it up!")
    elif answer2 == "catch" and catch2 == 5:
        print("Ok now that was way to close!")
    elif answer2 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag2 = input("what do you want to use ")
        if bag2 == "potion" and sobble_health <= 30:
            print("healed pokemon")
            sobble_health += 20
            potions -= 1
        elif bag2 == "potion" and sobble_health == 31:
            print("healed pokemon")
            sobble_health += 19
            potions -= 1
        elif bag2 == "potion" and sobble_health == 32:
            print("healed pokemon")
            sobble_health += 18
            potions -= 1
        elif bag2 == "potion" and sobble_health == 33:
            print("healed pokemon")
            sobble_health += 17
            potions -= 1
        elif bag2 == "potion" and sobble_health == 34:
            print("healed pokemon")
            sobble_health += 16
            potions -= 1
        elif bag2 == "potion" and sobble_health == 35:
            print("healed pokemon")
            sobble_health += 15
            potions -= 1
        elif bag2 == "potion" and sobble_health == 36:
            print("healed pokemon")
            sobble_health += 14
            potions -= 1
        elif bag2 == "potion" and sobble_health == 37:
            print("healed pokemon")
            sobble_health += 13
            potions -= 1
        elif bag2 == "potion" and sobble_health == 38:
            print("healed pokemon")
            sobble_health += 12
            potions -= 1
        elif bag2 == "potion" and sobble_health == 39:
            print("healed pokemon")
            sobble_health += 11
            potions -= 1
        elif bag2 == "potion" and sobble_health == 40:
            print("healed pokemon")
            sobble_health += 10
            potions -= 1
        elif bag2 == "potion" and sobble_health == 41:
            print("healed pokemon")
            sobble_health += 9
            potions -= 1
        elif bag2 == "potion" and sobble_health == 42:
            print("healed pokemon")
            sobble_health += 8
            potions -= 1
        elif bag2 == "potion" and sobble_health == 43:
            print("healed pokemon")
            sobble_health += 7
            potions -= 1
        elif bag2 == "potion" and sobble_health == 44:
            print("healed pokemon")
            sobble_health += 6
            potions -= 1
        elif bag2 == "potion" and sobble_health == 45:
            print("healed pokemon")
            sobble_health += 5
            potions -= 1
        elif bag2 == "potion" and sobble_health == 46:
            print("healed pokemon")
            sobble_health += 4
            potions -= 1
        elif bag2 == "potion" and sobble_health == 47:
            print("healed pokemon")
            sobble_health += 3
            potions -= 1
        elif bag2 == "potion" and sobble_health == 48:
            print("healed pokemon")
            sobble_health += 2
            potions -= 1
        elif bag2 == "potion" and sobble_health == 49:
            print("healed pokemon")
            sobble_health += 1
            potions -= 1
        elif bag2 == "potion" and sobble_health == 50:
            print("your pokemon is at full health")
        elif bag2 == "master ball" and master_ball == 1:
            print("gotcha pikachu was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif bag2 == "ultra ball" and ultra_balls == 1:
            print("gotcha pikachu was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag2 == "great ball" and great_balls == 1:
            print("gotcha pikachu was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif bag2 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag2 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 3 and starter == "sobble":
    master_ball3 = r.randint(1, 1)
    ultra_balls3 = r.randint(1, 2)
    great_balls3 = r.randint(1, 3)
    catch3 = r.randint(1, 5)
    nickit = r.randint(1, 4)
    answer3 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("nickit's health " + str(nickit_health))
    if answer3 == "run":
        fight_music.set_paused(True)
        sus.exit("you ran away")
    elif answer3 == "fight" and starter == "sobble" and x == 3:

        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight3 = input()
        if fight3 == "pound":
            print("that did 4 damage")
            nickit_health -= 4
        if fight3 == "sucker punch":
            print("that did 30 damage")
            nickit_health -= 30
        if fight3 == "water pulse":
            print("that did 20 damage")
            nickit_health -= 20
        if fight3 == "water gun":
            print("that did 10 hp")
            nickit_health -= 10
        if nickit == 4:
            print("nickit used double kick")
            print("it hit twice!")
            sobble_health -= 10
        elif nickit == 1:
            print("nickit used tail whip")
            sobble_health -= 12
        elif nickit == 2:
            print("nickit used tackle")
            sobble_health -= 8
        elif nickit == 3:
            print("nickit used dark pulse")
            sobble_health -= 25
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            fight_music.set_paused(True)
            sus.exit(':(')
        if nickit_health <= 0:
            print("The wild nickit fainted we'll get em next time")
            break
    elif answer3 == "catch" and catch3 == 1:
        print("gotcha nickit was caught!")
        break
    elif answer3 == "catch" and catch3 == 2:
        print("close!")
    elif answer3 == "catch" and catch3 == 3:
        print("Aw that was So close!")
    elif answer3 == "catch" and catch3 == 4:
        print("That was so close keep it up!")
    elif answer3 == "catch" and catch3 == 5:
        print("Ok now that was way to close!")
    elif answer3 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag3 = input("what do you want to use ")
        if bag3 == "potion" and sobble_health <= 30:
            print("healed pokemon")
            sobble_health += 20
            potions -= 1
        elif bag3 == "potion" and sobble_health == 31:
            print("healed pokemon")
            sobble_health += 19
            potions -= 1
        elif bag3 == "potion" and sobble_health == 32:
            print("healed pokemon")
            sobble_health += 18
            potions -= 1
        elif bag3 == "potion" and sobble_health == 33:
            print("healed pokemon")
            sobble_health += 17
            potions -= 1
        elif bag3 == "potion" and sobble_health == 34:
            print("healed pokemon")
            sobble_health += 16
            potions -= 1
        elif bag3 == "potion" and sobble_health == 35:
            print("healed pokemon")
            sobble_health += 15
            potions -= 1
        elif bag3 == "potion" and sobble_health == 36:
            print("healed pokemon")
            sobble_health += 14
            potions -= 1
        elif bag3 == "potion" and sobble_health == 37:
            print("healed pokemon")
            sobble_health += 13
            potions -= 1
        elif bag3 == "potion" and sobble_health == 38:
            print("healed pokemon")
            sobble_health += 12
            potions -= 1
        elif bag3 == "potion" and sobble_health == 39:
            print("healed pokemon")
            sobble_health += 11
            potions -= 1
        elif bag3 == "potion" and sobble_health == 40:
            print("healed pokemon")
            sobble_health += 10
            potions -= 1
        elif bag3 == "potion" and sobble_health == 41:
            print("healed pokemon")
            sobble_health += 9
            potions -= 1
        elif bag3 == "potion" and sobble_health == 42:
            print("healed pokemon")
            sobble_health += 8
            potions -= 1
        elif bag3 == "potion" and sobble_health == 43:
            print("healed pokemon")
            sobble_health += 7
            potions -= 1
        elif bag3 == "potion" and sobble_health == 44:
            print("healed pokemon")
            sobble_health += 6
            potions -= 1
        elif bag3 == "potion" and sobble_health == 45:
            print("healed pokemon")
            sobble_health += 5
            potions -= 1
        elif bag3 == "potion" and sobble_health == 46:
            print("healed pokemon")
            sobble_health += 4
            potions -= 1
        elif bag3 == "potion" and sobble_health == 47:
            print("healed pokemon")
            sobble_health += 3
            potions -= 1
        elif bag3 == "potion" and sobble_health == 48:
            print("healed pokemon")
            sobble_health += 2
            potions -= 1
        elif bag3 == "potion" and sobble_health == 49:
            print("healed pokemon")
            sobble_health += 1
            potions -= 1
        elif bag3 == "potion" and sobble_health == 50:
            print("your pokemon is at full health")
        elif bag3 == "master ball" and master_ball3 == 1:
            print("gotcha nickit was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif bag3 == "ultra ball" and ultra_balls3 == 1:
            print("gotcha nickit was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif ultra_balls3 == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag3 == "great ball" and great_balls3 == 1:
            print("gotcha nickit was caught!")
            fight_music.set_paused(True)
            sus.exit
        elif bag3 == "great ball" and great_balls3 == 2:
            great_ball -= 1
            print("close!")
        elif bag3 == "great ball" and great_balls3 == 3:
            ultra_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 4 and starter == "sobble":
    master_ball4 = r.randint(1, 1)
    ultra_balls4 = r.randint(1, 2)
    great_balls4 = r.randint(1, 3)
    catch4 = r.randint(1, 5)
    drednaw = r.randint(1, 4)
    answer4 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("drednaw's health " + str(drednaw_health))
    if answer4 == "run":
        fight_music.set_paused(True)
        sus.exit("you ran away")
    elif answer4 == "fight" and starter == "sobble" and x == 4:
        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight4 = input()
        if fight4 == "pound":
            print("that did 4 damage")
            drednaw_health -= 4
        if fight4 == "sucker punch":
            print("that did 30 damage")
            drednaw_health -= 30
        if fight4 == "water pulse":
            print("that did 20 damage")
            drednaw_health -= 20
        if fight4 == "water gun":
            print("that did 10 hp")
            drednaw_health -= 10
        if drednaw == 4:
            print("drednaw used hydro pump")
            sobble_health -= 10
        elif drednaw == 1:
            print("drednaw used aqua tail")
            sobble_health -= 12
        elif drednaw == 2:
            print("drednaw used tackle")
            sobble_health -= 8
        elif drednaw == 3:
            print("drednaw used water pulse")
            sobble_health -= 25
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if drednaw_health <= 0:
            print("The wild drednaw fainted we'll get em next time")
            break
    elif answer4 == "catch" and catch4 == 1:
        print("gotcha drednaw was caught!")
        break
    elif answer4 == "catch" and catch4 == 2:
        print("close!")
    elif answer4 == "catch" and catch4 == 3:
        print("Aw that was So close!")
    elif answer4 == "catch" and catch4 == 4:
        print("That was so close keep it up!")
    elif answer4 == "catch" and catch4 == 5:
        print("Ok now that was way to close!")
    elif answer4 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag4 = input("what do you want to use ")
        if bag4 == "potion" and sobble_health <= 30:
            print("healed pokemon")
            sobble_health += 20
            potions -= 1
        elif bag4 == "potion" and sobble_health == 31:
            print("healed pokemon")
            sobble_health += 19
            potions -= 1
        elif bag4 == "potion" and sobble_health == 32:
            print("healed pokemon")
            sobble_health += 18
            potions -= 1
        elif bag4 == "potion" and sobble_health == 33:
            print("healed pokemon")
            sobble_health += 17
            potions -= 1
        elif bag4 == "potion" and sobble_health == 34:
            print("healed pokemon")
            sobble_health += 16
            potions -= 1
        elif bag4 == "potion" and sobble_health == 35:
            print("healed pokemon")
            sobble_health += 15
            potions -= 1
        elif bag4 == "potion" and sobble_health == 36:
            print("healed pokemon")
            sobble_health += 14
            potions -= 1
        elif bag4 == "potion" and sobble_health == 37:
            print("healed pokemon")
            sobble_health += 13
            potions -= 1
        elif bag4 == "potion" and sobble_health == 38:
            print("healed pokemon")
            sobble_health += 12
            potions -= 1
        elif bag4 == "potion" and sobble_health == 39:
            print("healed pokemon")
            sobble_health += 11
            potions -= 1
        elif bag4 == "potion" and sobble_health == 40:
            print("healed pokemon")
            sobble_health += 10
            potions -= 1
        elif bag4 == "potion" and sobble_health == 41:
            print("healed pokemon")
            sobble_health += 9
            potions -= 1
        elif bag4 == "potion" and sobble_health == 42:
            print("healed pokemon")
            sobble_health += 8
            potions -= 1
        elif bag4 == "potion" and sobble_health == 43:
            print("healed pokemon")
            sobble_health += 7
            potions -= 1
        elif bag4 == "potion" and sobble_health == 44:
            print("healed pokemon")
            sobble_health += 6
            potions -= 1
        elif bag4 == "potion" and sobble_health == 45:
            print("healed pokemon")
            sobble_health += 5
            potions -= 1
        elif bag4 == "potion" and sobble_health == 46:
            print("healed pokemon")
            sobble_health += 4
            potions -= 1
        elif bag4 == "potion" and sobble_health == 47:
            print("healed pokemon")
            sobble_health += 3
            potions -= 1
        elif bag4 == "potion" and sobble_health == 48:
            print("healed pokemon")
            sobble_health += 2
            potions -= 1
        elif bag4 == "potion" and sobble_health == 49:
            print("healed pokemon")
            sobble_health += 1
            potions -= 1
        elif bag4 == "potion" and sobble_health == 50:
            print("your pokemon is at full health")
        elif bag4 == "master ball" and master_ball == 1:
            print("gotcha drednaw was caught!")
            sus.exit
        elif bag4 == "ultra ball" and ultra_balls == 1:
            print("gotcha drednaw was caught!")
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag == "great ball" and great_balls == 1:
            print("gotcha drednaw was caught!")
            sus.exit
        elif bag4 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag4 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 5 and starter == "sobble": 
    master_ball5 = r.randint(1, 1)
    ultra_balls5 = r.randint(1, 2)
    great_balls5 = r.randint(1, 3)
    catch5 = r.randint(1, 5)
    eternatus = r.randint(1, 4)
    answer5 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("eternatus's health " + str(eternatus_health))
    if answer5 == "run":
        sus.exit("you ran away")
    elif answer5 == "fight" and starter == "sobble" and x == 5:
        print("what move do you want to use")
        print("pound")
        print("sucker punch")
        print("water gun")
        print("water pulse")
        fight5 = input()
        if fight5 == "pound":
            print("that did 4 damage")
            eternatus_health -= 4
        if fight5 == "sucker punch":
            print("that did 30 damage")
            eternatus_health -= 30
        if fight5 == "water pulse":
            print("that did 20 damage")
            eternatus_health -= 20
        if fight5 == "water gun":
            print("that did 10 hp")
            eternatus_health -= 10
        if eternatus == 4:
            print("eternatus used dynamax canon")
            sobble_health -= 20
        elif eternatus == 1:
            print("eternatus used eternabeam")
            sobble_health -= 40
        elif eternatus == 2:
            print("eternatus used dragon tail")
            sobble_health -= 8
        elif eternatus == 3:
            print("eternatus used poison jab")
            sobble_health -= 25
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if eternatus_health <= 0:
            print("The wild eternatus fainted we'll get em next time")
            break
    elif answer5 == "catch" and catch5 == 1:
        print("gotcha eternatus was caught!")
        break
    elif answer5 == "catch" and catch5 == 2:
        print("close!")
    elif answer5 == "catch" and catch5 == 3:
        print("Aw that was So close!")
    elif answer5 == "catch" and catch5 == 4:
        print("That was so close keep it up!")
    elif answer5 == "catch" and catch5 == 5:
        print("Ok now that was way to close!")
    elif answer5 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag5 = input("what do you want to use ")
        if bag5 == "potion" and sobble_health <= 30:
            print("healed pokemon")
            sobble_health += 20
            potions -= 1
        elif bag5 == "potion" and sobble_health == 31:
            print("healed pokemon")
            sobble_health += 19
            potions -= 1
        elif bag5 == "potion" and sobble_health == 32:
            print("healed pokemon")
            sobble_health += 18
            potions -= 1
        elif bag5 == "potion" and sobble_health == 33:
            print("healed pokemon")
            sobble_health += 17
            potions -= 1
        elif bag5 == "potion" and sobble_health == 34:
            print("healed pokemon")
            sobble_health += 16
            potions -= 1
        elif bag5 == "potion" and sobble_health == 35:
            print("healed pokemon")
            sobble_health += 15
            potions -= 1
        elif bag5 == "potion" and sobble_health == 36:
            print("healed pokemon")
            sobble_health += 14
            potions -= 1
        elif bag5 == "potion" and sobble_health == 37:
            print("healed pokemon")
            sobble_health += 13
            potions -= 1
        elif bag5 == "potion" and sobble_health == 38:
            print("healed pokemon")
            sobble_health += 12
            potions -= 1
        elif bag5 == "potion" and sobble_health == 39:
            print("healed pokemon")
            sobble_health += 11
            potions -= 1
        elif bag5 == "potion" and sobble_health == 40:
            print("healed pokemon")
            sobble_health += 10
            potions -= 1
        elif bag5 == "potion" and sobble_health == 41:
            print("healed pokemon")
            sobble_health += 9
            potions -= 1
        elif bag5 == "potion" and sobble_health == 42:
            print("healed pokemon")
            sobble_health += 8
            potions -= 1
        elif bag5 == "potion" and sobble_health == 43:
            print("healed pokemon")
            sobble_health += 7
            potions -= 1
        elif bag5 == "potion" and sobble_health == 44:
            print("healed pokemon")
            sobble_health += 6
            potions -= 1
        elif bag5 == "potion" and sobble_health == 45:
            print("healed pokemon")
            sobble_health += 5
            potions -= 1
        elif bag5 == "potion" and sobble_health == 46:
            print("healed pokemon")
            sobble_health += 4
            potions -= 1
        elif bag5 == "potion" and sobble_health == 47:
            print("healed pokemon")
            sobble_health += 3
            potions -= 1
        elif bag5 == "potion" and sobble_health == 48:
            print("healed pokemon")
            sobble_health += 2
            potions -= 1
        elif bag5 == "potion" and sobble_health == 49:
            print("healed pokemon")
            sobble_health += 1
            potions -= 1
        elif bag5 == "potion" and sobble_health == 50:
            print("your pokemon is at full health")
        elif bag5 == "master ball" and master_ball == 1:
            print("gotcha eternatus was caught!")
            sus.exit
        elif bag5 == "ultra ball" and ultra_balls == 1:
            print("gotcha eternatus was caught!")
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag5 == "great ball" and great_balls == 1:
            print("gotcha eternatus was caught!")
            sus.exit
        elif bag == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 2 and starter == "scorbunny":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch6 = r.randint(1, 5)
    wooloo2 = r.randint(1, 4)
    answer6 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("wooloo's health " + str(wooloo_health))
    if answer6 == "run":
        sus.exit("you ran away")
    elif answer6 == "fight" and starter == "scorbunny" and x == 2:

        print("what move do you want to use")
        print("pound")
        print("ember")
        print("fire punch")
        print("double kick")
        fight6 = input()
        if fight6 == "pound":
            print("that did 4 damage")
            wooloo_health -= 4
        if fight6 == "fire punch":
            print("that did 30 damage")
            wooloo_health -= 30
        if fight6 == "ember":
            print("that did 20 damage")
            wooloo_health -= 20
        if fight6 == "double kick":
            print("it hit twice!")
            print("that did 20 hp")
            wooloo_health -= 10
        if wooloo2 == 4:
            print("wooloo used Double-Edge")
            scorbunny_health -= 23
        elif wooloo2 == 1:
            print("wooloo used take down")
            scorbunny_health -= 12
        elif wooloo2 == 2:
            print("wooloo used tackle")
            scorbunny_health -= 8
        elif wooloo2 == 3:
            print("wooloo used headbutt")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if wooloo_health <= 0:
            print("The wild wooloo fainted we'll get em next time")
            break
    elif answer6 == "catch" and catch6 == 1:
        print("gotcha wooloo was caught!")
        break
    elif answer6 == "catch" and catch6 == 2:
        print("close!")
    elif answer6 == "catch" and catch6 == 3:
        print("Aw that was So close!")
    elif answer6 == "catch" and catch6 == 4:
        print("That was so close keep it up!")
    elif answer6 == "catch" and catch6 == 5:
        print("Ok now that was way to close!")
    elif answer6 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag6 = input("what do you want to use ")
        if bag6 == "potion" and scorbunny_health <= 30:
            print("healed pokemon")
            scorbunny_health += 20
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 31:
            print("healed pokemon")
            scorbunny_health += 19
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 32:
            print("healed pokemon")
            scorbunny_health += 18
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 33:
            print("healed pokemon")
            scorbunny_health += 17
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 34:
            print("healed pokemon")
            scorbunny_health += 16
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 35:
            print("healed pokemon")
            scorbunny_health += 15
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 36:
            print("healed pokemon")
            scorbunny_health += 14
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 37:
            print("healed pokemon")
            scorbunny_health += 13
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 38:
            print("healed pokemon")
            scorbunny_health += 12
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 39:
            print("healed pokemon")
            scorbunny_health += 11
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 40:
            print("healed pokemon")
            scorbunny_health += 10
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 41:
            print("healed pokemon")
            scorbunny_health += 9
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 42:
            print("healed pokemon")
            scorbunny_health += 8
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 43:
            print("healed pokemon")
            scorbunny_health += 7
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 44:
            print("healed pokemon")
            scorbunny_health += 6
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 45:
            print("healed pokemon")
            scorbunny_health += 5
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 46:
            print("healed pokemon")
            scorbunny_health += 4
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 47:
            print("healed pokemon")
            scorbunny_health += 3
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 48:
            print("healed pokemon")
            scorbunny_health += 2
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 49:
            print("healed pokemon")
            scorbunny_health += 1
            potions -= 1
        elif bag6 == "potion" and scorbunny_health == 50:
            print("your pokemon is at full health")
        elif bag6 == "master ball" and master_ball == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif bag6 == "ultra ball" and ultra_balls == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag6 == "great ball" and great_balls == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif bag6 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag6 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 1 and starter == "scorbunny":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch7 = r.randint(1, 5)
    pikachu2 = r.randint(1, 4)
    answer7 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("pikachu's health " + str(pikachu_health))
    if answer7 == "run":
        sus.exit("you ran away")
    elif answer7 == "fight" and starter == "scorbunny" and x == 1:

        print("what move do you want to use")
        print("pound")
        print("ember")
        print("fire punch")
        print("double kick")
        fight7 = input()
        if fight7 == "pound":
            print("that did 4 damage")
            pikachu_health -= 4
        if fight7 == "fire punch":
            print("that did 30 damage")
            pikachu_health -= 30
        if fight7 == "ember":
            print("that did 20 damage")
            pikachu_health -= 20
        if fight7 == "double kick":
            print("it hit twice!")
            print("that did 20 hp")
            pikachu_health -= 10
        if pikachu2 == 4:
            print("pikachu used iron tail")
            scorbunny_health -= 23
        elif pikachu2 == 1:
            print("pikachu used thunder bolt")
            scorbunny_health -= 12
        elif pikachu2 == 2:
            print("pikachu used electro web")
            scorbunny_health -= 8
        elif pikachu2 == 3:
            print("pikachu used electro ball")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if pikachu_health <= 0:
            print("The wild pikachu fainted we'll get em next time")
            break
    elif answer7 == "catch" and catch7 == 1:
        print("gotcha pikachu was caught!")
        break
    elif answer7 == "catch" and catch7 == 2:
        print("close!")
    elif answer7 == "catch" and catch7 == 3:
        print("Aw that was So close!")
    elif answer7 == "catch" and catch7 == 4:
        print("That was so close keep it up!")
    elif answer7 == "catch" and catch7 == 5:
        print("Ok now that was way to close!")
    elif answer7 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag7 = input("what do you want to use ")
        if bag7 == "potion" and scorbunny_health <= 30:
            print("healed pokemon")
            scorbunny_health += 20
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 31:
            print("healed pokemon")
            scorbunny_health += 19
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 32:
            print("healed pokemon")
            scorbunny_health += 18
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 33:
            print("healed pokemon")
            scorbunny_health += 17
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 34:
            print("healed pokemon")
            scorbunny_health += 16
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 35:
            print("healed pokemon")
            scorbunny_health += 15
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 36:
            print("healed pokemon")
            scorbunny_health += 14
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 37:
            print("healed pokemon")
            scorbunny_health += 13
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 38:
            print("healed pokemon")
            scorbunny_health += 12
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 39:
            print("healed pokemon")
            scorbunny_health += 11
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 40:
            print("healed pokemon")
            scorbunny_health += 10
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 41:
            print("healed pokemon")
            scorbunny_health += 9
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 42:
            print("healed pokemon")
            scorbunny_health += 8
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 43:
            print("healed pokemon")
            scorbunny_health += 7
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 44:
            print("healed pokemon")
            scorbunny_health += 6
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 45:
            print("healed pokemon")
            scorbunny_health += 5
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 46:
            print("healed pokemon")
            scorbunny_health += 4
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 47:
            print("healed pokemon")
            scorbunny_health += 3
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 48:
            print("healed pokemon")
            scorbunny_health += 2
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 49:
            print("healed pokemon")
            scorbunny_health += 1
            potions -= 1
        elif bag7 == "potion" and scorbunny_health == 50:
            print("your pokemon is at full health")
        elif bag7 == "master ball" and master_ball == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif bag7 == "ultra ball" and ultra_balls == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag7 == "great ball" and great_balls == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif bag7 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag7 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 3 and starter == "scorbunny":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch8 = r.randint(1, 5)
    nickit2 = r.randint(1, 4)
    answer8 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("nickit's health " + str(nickit_health))
    if answer8 == "run":
        sus.exit("you ran away")
    elif answer8 == "fight" and starter == "scorbunny" and x == 3:

        print("what move do you want to use")
        print("pound")
        print("ember")
        print("fire punch")
        print("double kick")
        fight8 = input()
        if fight8 == "pound":
            print("that did 4 damage")
            nickit_health -= 4
        if fight8 == "fire punch":
            print("that did 30 damage")
            nickit_health -= 30
        if fight8 == "ember":
            print("that did 20 damage")
            nickit_health -= 20
        if fight8 == "double kick":
            print("it hit twice!")
            print("that did 40 hp")
            print("that was super effective!")
            nickit_health -= 40
        if nickit2 == 4:
            print("nickit used night slash")
            scorbunny_health -= 23
        elif nickit2 == 1:
            print("nickit used beat up")
            scorbunny_health -= 12
        elif nickit2 == 2:
            print("nickit used sucker punch")
            scorbunny_health -= 8
        elif nickit2 == 3:
            print("nickit used foul play")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if nickit_health <= 0:
            print("The wild nickit fainted we'll get em next time")
            break
    elif answer8 == "catch" and catch8 == 1:
        print("gotcha nickit was caught!")
        break
    elif answer8 == "catch" and catch8 == 2:
        print("close!")
    elif answer8 == "catch" and catch8 == 3:
        print("Aw that was So close!")
    elif answer8 == "catch" and catch8 == 4:
        print("That was so close keep it up!")
    elif answer8 == "catch" and catch8 == 5:
        print("Ok now that was way to close!")
    elif answer8 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag8 = input("what do you want to use ")
        if bag8 == "potion" and scorbunny_health <= 30:
            print("healed pokemon")
            scorbunny_health += 20
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 31:
            print("healed pokemon")
            scorbunny_health += 19
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 32:
            print("healed pokemon")
            scorbunny_health += 18
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 33:
            print("healed pokemon")
            scorbunny_health += 17
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 34:
            print("healed pokemon")
            scorbunny_health += 16
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 35:
            print("healed pokemon")
            scorbunny_health += 15
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 36:
            print("healed pokemon")
            scorbunny_health += 14
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 37:
            print("healed pokemon")
            scorbunny_health += 13
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 38:
            print("healed pokemon")
            scorbunny_health += 12
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 39:
            print("healed pokemon")
            scorbunny_health += 11
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 40:
            print("healed pokemon")
            scorbunny_health += 10
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 41:
            print("healed pokemon")
            scorbunny_health += 9
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 42:
            print("healed pokemon")
            scorbunny_health += 8
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 43:
            print("healed pokemon")
            scorbunny_health += 7
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 44:
            print("healed pokemon")
            scorbunny_health += 6
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 45:
            print("healed pokemon")
            scorbunny_health += 5
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 46:
            print("healed pokemon")
            scorbunny_health += 4
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 47:
            print("healed pokemon")
            scorbunny_health += 3
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 48:
            print("healed pokemon")
            scorbunny_health += 2
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 49:
            print("healed pokemon")
            scorbunny_health += 1
            potions -= 1
        elif bag8 == "potion" and scorbunny_health == 50:
            print("your pokemon is at full health")
        elif bag8 == "master ball" and master_ball == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif bag8 == "ultra ball" and ultra_balls == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag8 == "great ball" and great_balls == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif bag8 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag8 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 4 and starter == "scorbunny":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch9 = r.randint(1, 5)
    drednaw2 = r.randint(1, 4)
    answer9 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("drednaw's health " + str(drednaw_health))
    if answer9 == "run":
        sus.exit("you ran away")
    elif answer9 == "fight" and starter == "scorbunny" and x == 4:

        print("what move do you want to use")
        print("pound")
        print("ember")
        print("fire punch")
        print("double kick")
        fight9 = input()
        if fight9 == "pound":
            print("that did 4 damage")
            drednaw_health -= 4
        if fight9 == "fire punch":
            print("that did 30 damage")
            drednaw_health -= 30
        if fight9 == "ember":
            print("that did 20 damage")
            drednaw_health -= 20
        if fight9 == "double kick":
            print("it hit twice!")
            print("that did 20 hp")
            drednaw_health -= 10
        if drednaw2 == 4:
            print("drednaw used rock tomb")
            scorbunny_health -= 23
        elif drednaw2 == 1:
            print("dredaw used liquidation")
            scorbunny_health -= 12
        elif drednaw2 == 2:
            print("drednaw used water gun")
            scorbunny_health -= 8
        elif drednaw2 == 3:
            print("drednaw used hydro pump")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if drednaw_health <= 0:
            print("The wild drednaw fainted we'll get em next time")
            break
    elif answer9 == "catch" and catch9 == 1:
        print("gotcha drednaw was caught!")
        break
    elif answer9 == "catch" and catch9 == 2:
        print("close!")
    elif answer9 == "catch" and catch9 == 3:
        print("Aw that was So close!")
    elif answer9 == "catch" and catch9 == 4:
        print("That was so close keep it up!")
    elif answer9 == "catch" and catch9 == 5:
        print("Ok now that was way to close!")
    elif answer9 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag9 = input("what do you want to use ")
        if bag9 == "potion" and scorbunny_health <= 30:
            print("healed pokemon")
            scorbunny_health += 20
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 31:
            print("healed pokemon")
            scorbunny_health += 19
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 32:
            print("healed pokemon")
            scorbunny_health += 18
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 33:
            print("healed pokemon")
            scorbunny_health += 17
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 34:
            print("healed pokemon")
            scorbunny_health += 16
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 35:
            print("healed pokemon")
            scorbunny_health += 15
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 36:
            print("healed pokemon")
            scorbunny_health += 14
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 37:
            print("healed pokemon")
            scorbunny_health += 13
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 38:
            print("healed pokemon")
            scorbunny_health += 12
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 39:
            print("healed pokemon")
            scorbunny_health += 11
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 40:
            print("healed pokemon")
            scorbunny_health += 10
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 41:
            print("healed pokemon")
            scorbunny_health += 9
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 42:
            print("healed pokemon")
            scorbunny_health += 8
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 43:
            print("healed pokemon")
            scorbunny_health += 7
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 44:
            print("healed pokemon")
            scorbunny_health += 6
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 45:
            print("healed pokemon")
            scorbunny_health += 5
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 46:
            print("healed pokemon")
            scorbunny_health += 4
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 47:
            print("healed pokemon")
            scorbunny_health += 3
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 48:
            print("healed pokemon")
            scorbunny_health += 2
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 49:
            print("healed pokemon")
            scorbunny_health += 1
            potions -= 1
        elif bag9 == "potion" and scorbunny_health == 50:
            print("your pokemon is at full health")
        elif bag9 == "master ball" and master_ball == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif bag9 == "ultra ball" and ultra_balls == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag9 == "great ball" and great_balls == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif bag9 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag9 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 5 and starter == "scorbunny":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch10 = r.randint(1, 5)
    eternatus2 = r.randint(1, 4)
    answer10 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("eternatus's health " + str(eternatus_health))
    if answer10 == "run":
        sus.exit("you ran away")
    elif answer10 == "fight" and starter == "scorbunny" and x == 5:

        print("what move do you want to use")
        print("pound")
        print("ember")
        print("fire punch")
        print("double kick")
        fight10 = input()
        if fight10 == "pound":
            print("that did 4 damage")
            eternatus_health -= 4
        if fight10 == "fire punch":
            print("that did 30 damage")
            eternatus_health -= 30
        if fight10 == "ember":
            print("that did 20 damage")
            eternatus_health -= 20
        if fight10 == "double kick":
            print("it hit twice!")
            print("that did 20 hp")
            eternatus_health -= 10
        if eternatus2 == 4:
            print("eternatus used poison tail")
            scorbunny_health -= 23
        elif eternatus2 == 1:
            print("eternatus used dynamax cannon")
            scorbunny_health -= 12
        elif eternatus2 == 2:
            print("eternatus used dragon pulse")
            scorbunny_health -= 8
        elif eternatus2 == 3:
            print("eternatus used eternabeam")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if eternatus_health <= 0:
            print("The wild drednaw fainted we'll get em next time")
            break
    elif answer10 == "catch" and catch10 == 1:
        print("gotcha eternatus was caught!")
        break
    elif answer10 == "catch" and catch10 == 2:
        print("close!")
    elif answer10 == "catch" and catch10 == 3:
        print("Aw that was So close!")
    elif answer10 == "catch" and catch10 == 4:
        print("That was so close keep it up!")
    elif answer10 == "catch" and catch10 == 5:
        print("Ok now that was way to close!")
    elif answer10 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag10 = input("what do you want to use ")
        if bag10 == "potion" and scorbunny_health <= 30:
            print("healed pokemon")
            scorbunny_health += 20
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 31:
            print("healed pokemon")
            scorbunny_health += 19
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 32:
            print("healed pokemon")
            scorbunny_health += 18
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 33:
            print("healed pokemon")
            scorbunny_health += 17
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 34:
            print("healed pokemon")
            scorbunny_health += 16
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 35:
            print("healed pokemon")
            scorbunny_health += 15
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 36:
            print("healed pokemon")
            scorbunny_health += 14
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 37:
            print("healed pokemon")
            scorbunny_health += 13
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 38:
            print("healed pokemon")
            scorbunny_health += 12
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 39:
            print("healed pokemon")
            scorbunny_health += 11
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 40:
            print("healed pokemon")
            scorbunny_health += 10
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 41:
            print("healed pokemon")
            scorbunny_health += 9
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 42:
            print("healed pokemon")
            scorbunny_health += 8
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 43:
            print("healed pokemon")
            scorbunny_health += 7
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 44:
            print("healed pokemon")
            scorbunny_health += 6
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 45:
            print("healed pokemon")
            scorbunny_health += 5
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 46:
            print("healed pokemon")
            scorbunny_health += 4
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 47:
            print("healed pokemon")
            scorbunny_health += 3
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 48:
            print("healed pokemon")
            scorbunny_health += 2
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 49:
            print("healed pokemon")
            scorbunny_health += 1
            potions -= 1
        elif bag10 == "potion" and scorbunny_health == 50:
            print("your pokemon is at full health")
        elif bag10 == "master ball" and master_ball == 1:
            print("gotcha eternatus was caught!")
            break
            sus.exit
        elif bag10 == "ultra ball" and ultra_balls == 1:
            print("gotcha eternatus was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag10 == "great ball" and great_balls == 1:
            print("gotcha eternatus was caught!")
            break
            sus.exit
        elif bag10 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag10 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 2 and starter == "grookey":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch11 = r.randint(1, 5)
    wooloo3 = r.randint(1, 4)
    answer11 = input("fight/catch/bag/run ")
    print("grookey's health " + str(grookey_health))
    print("wooloo's health " + str(wooloo_health))
    if answer11 == "run":
        sus.exit("you ran away")
    elif answer11 == "fight" and starter == "grookey" and x == 2:
        print("what move do you want to use")
        print("scratch")
        print("branch poke")
        print("razor leaf")
        print("magical leaf")
        fight11 = input()
        if fight11 == "scratch":
            print("that did 4 damage")
            wooloo_health -= 4
        if fight11 == "razor leaf":
            print("that did 25 damage")
            wooloo_health -= 25
        if fight11 == "branch poke":
            print("that did 12 damage")
            wooloo_health -= 12
        if fight11 == "magical leaf":
            print("that did 27 hp")
            wooloo_health -= 27
        if wooloo3 == 4:
            print("wooloo used Double-Edge")
            grookey_health -= 23
        elif wooloo3 == 1:
            print("wooloo used take down")
            grookey_health -= 12
        elif wooloo3 == 2:
            print("wooloo used tackle")
            grookey_health -= 8
        elif wooloo3 == 3:
            print("wooloo used headbutt")
            grookey_health -= 20
        if grookey_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if wooloo_health <= 0:
            print("The wild wooloo fainted we'll get em next time")
            break
    elif answer11 == "catch" and catch11 == 1:
        print("gotcha wooloo was caught!")
        break
    elif answer11 == "catch" and catch11 == 2:
        print("close!")
    elif answer11 == "catch" and catch11 == 3:
        print("Aw that was So close!")
    elif answer11 == "catch" and catch11 == 4:
        print("That was so close keep it up!")
    elif answer11 == "catch" and catch11 == 5:
        print("Ok now that was way to close!")
    elif answer11 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag11 = input("what do you want to use ")
        if bag11 == "potion" and grookey_health <= 30:
            print("healed pokemon")
            grookey_health += 20
            potions -= 1
        elif bag11 == "potion" and grookey_health == 31:
            print("healed pokemon")
            grookey_health += 19
            potions -= 1
        elif bag11 == "potion" and grookey_health == 32:
            print("healed pokemon")
            grookey_health += 18
            potions -= 1
        elif bag11 == "potion" and grookey_health == 33:
            print("healed pokemon")
            grookey_health += 17
            potions -= 1
        elif bag11 == "potion" and grookey_health == 34:
            print("healed pokemon")
            grookey_health += 16
            potions -= 1
        elif bag11 == "potion" and grookey_health == 35:
            print("healed pokemon")
            grookey_health += 15
            potions -= 1
        elif bag11 == "potion" and grookey_health == 36:
            print("healed pokemon")
            grookey_health += 14
            potions -= 1
        elif bag11 == "potion" and grookey_health == 37:
            print("healed pokemon")
            grookey_health += 13
            potions -= 1
        elif bag11 == "potion" and grookey_health == 38:
            print("healed pokemon")
            grookey_health += 12
            potions -= 1
        elif bag11 == "potion" and grookey_health == 39:
            print("healed pokemon")
            grookey_health += 11
            potions -= 1
        elif bag11 == "potion" and grookey_health == 40:
            print("healed pokemon")
            grookey_health += 10
            potions -= 1
        elif bag11 == "potion" and grookey_health == 41:
            print("healed pokemon")
            grookey_health += 9
            potions -= 1
        elif bag11 == "potion" and grookey_health == 42:
            print("healed pokemon")
            grookey_health += 8
            potions -= 1
        elif bag11 == "potion" and grookey_health == 43:
            print("healed pokemon")
            grookey_health += 7
            potions -= 1
        elif bag11 == "potion" and grookey_health == 44:
            print("healed pokemon")
            grookey_health += 6
            potions -= 1
        elif bag11 == "potion" and grookey_health == 45:
            print("healed pokemon")
            grookey_health += 5
            potions -= 1
        elif bag11 == "potion" and grookey_health == 46:
            print("healed pokemon")
            grookey_health += 4
            potions -= 1
        elif bag11 == "potion" and grookey_health == 47:
            print("healed pokemon")
            grookey_health += 3
            potions -= 1
        elif bag11 == "potion" and grookey_health == 48:
            print("healed pokemon")
            grookey_health += 2
            potions -= 1
        elif bag11 == "potion" and grookey_health == 49:
            print("healed pokemon")
            grookey_health += 1
            potions -= 1
        elif bag11 == "potion" and grookey_health == 50:
            print("your pokemon is at full health")
        elif bag11 == "master ball" and master_ball == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif bag11 == "ultra ball" and ultra_balls == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag11 == "great ball" and great_balls == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif bag11 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag11 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 1 and starter == "grookey":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch12 = r.randint(1, 5)
    pikachu3 = r.randint(1, 4)
    answer12 = input("fight/catch/bag/run ")
    print("grookey's health " + str(grookey_health))
    print("pikachu's health " + str(pikachu_health))
    if answer12 == "run":
        sus.exit("you ran away")
    elif answer12 == "fight" and starter == "grookey" and x == 1:

        print("what move do you want to use")
        print("scratch")
        print("branch poke")
        print("razor leaf")
        print("magical leaf")
        fight12 = input()
        if fight12 == "scratch":
            print("that did 4 damage")
            pikachu_health -= 4
        if fight12 == "razor leaf":
            print("that did 25 damage")
            pikachu_health -= 25
        if fight12 == "branch poke":
            print("that did 12 damage")
            pikachu_health -= 12
        if fight12 == "magical leaf":
            print("that did 27 hp")
            pikachu_health -= 27
        if pikachu3 == 4:
            print("pikachu used thunder bolt")
            print("that's not very effective")
            grookey_health -= 13
        elif pikachu3 == 1:
            print("pikachu used electro web")
            print("that's not very effective")
            grookey_health -= 13
        elif pikachu3 == 2:
            print("pikachu used iron tail")
            print("that's not very effective")
            grookey_health -= 8
        elif pikachu3 == 3:
            print("pikachu used electro ball")
            print("that's not very effective")
            grookey_health -= 10
        if grookey_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if pikachu_health <= 0:
            print("The wild pikachu fainted we'll get em next time")
            break
    elif answer12 == "catch" and catch12 == 1:
        print("gotcha pikachu was caught!")
        break
    elif answer12 == "catch" and catch12 == 2:
        print("close!")
    elif answer12 == "catch" and catch12 == 3:
        print("Aw that was So close!")
    elif answer12 == "catch" and catch12 == 4:
        print("That was so close keep it up!")
    elif answer12 == "catch" and catch12 == 5:
        print("Ok now that was way to close!")
    elif answer12 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag12 = input("what do you want to use ")
        if bag12 == "potion" and grookey_health <= 30:
            print("healed pokemon")
            grookey_health += 20
            potions -= 1
        elif bag12 == "potion" and grookey_health == 31:
            print("healed pokemon")
            grookey_health += 19
            potions -= 1
        elif bag12 == "potion" and grookey_health == 32:
            print("healed pokemon")
            grookey_health += 18
            potions -= 1
        elif bag12 == "potion" and grookey_health == 33:
            print("healed pokemon")
            grookey_health += 17
            potions -= 1
        elif bag12 == "potion" and grookey_health == 34:
            print("healed pokemon")
            grookey_health += 16
            potions -= 1
        elif bag12 == "potion" and grookey_health == 35:
            print("healed pokemon")
            grookey_health += 15
            potions -= 1
        elif bag12 == "potion" and grookey_health == 36:
            print("healed pokemon")
            grookey_health += 14
            potions -= 1
        elif bag12 == "potion" and grookey_health == 37:
            print("healed pokemon")
            grookey_health += 13
            potions -= 1
        elif bag12 == "potion" and grookey_health == 38:
            print("healed pokemon")
            grookey_health += 12
            potions -= 1
        elif bag12 == "potion" and grookey_health == 39:
            print("healed pokemon")
            grookey_health += 11
            potions -= 1
        elif bag12 == "potion" and grookey_health == 40:
            print("healed pokemon")
            grookey_health += 10
            potions -= 1
        elif bag12 == "potion" and grookey_health == 41:
            print("healed pokemon")
            grookey_health += 9
            potions -= 1
        elif bag12 == "potion" and grookey_health == 42:
            print("healed pokemon")
            grookey_health += 8
            potions -= 1
        elif bag12 == "potion" and grookey_health == 43:
            print("healed pokemon")
            grookey_health += 7
            potions -= 1
        elif bag12 == "potion" and grookey_health == 44:
            print("healed pokemon")
            grookey_health += 6
            potions -= 1
        elif bag12 == "potion" and grookey_health == 45:
            print("healed pokemon")
            grookey_health += 5
            potions -= 1
        elif bag12 == "potion" and grookey_health == 46:
            print("healed pokemon")
            grookey_health += 4
            potions -= 1
        elif bag12 == "potion" and grookey_health == 47:
            print("healed pokemon")
            grookey_health += 3
            potions -= 1
        elif bag12 == "potion" and grookey_health == 48:
            print("healed pokemon")
            grookey_health += 2
            potions -= 1
        elif bag12 == "potion" and grookey_health == 49:
            print("healed pokemon")
            grookey_health += 1
            potions -= 1
        elif bag12 == "potion" and grookey_health == 50:
            print("your pokemon is at full health")
        elif bag12 == "master ball" and master_ball == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif bag12 == "ultra ball" and ultra_balls == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag12 == "great ball" and great_balls == 1:
            print("gotcha pikachu was caught!")
            break
            sus.exit
        elif bag12 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag12 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 3 and starter == "grookey":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch13 = r.randint(1, 5)
    nickit3 = r.randint(1, 4)
    answer13 = input("fight/catch/bag/run ")
    print("grookey's health " + str(grookey_health))
    print("nickit's health " + str(nickit_health))
    if answer13 == "run":
        sus.exit("you ran away")
    elif answer13 == "fight" and starter == "grookey" and x == 3:

        print("what move do you want to use")
        print("scratch")
        print("branch poke")
        print("razor leaf")
        print("magical leaf")
        fight13 = input()
        if fight13 == "scratch":
            print("that did 4 damage")
            nickit_health -= 4
        if fight13 == "razor leaf":
            print("that did 25 damage")
            nickit_health -= 25
        if fight13 == "branch poke":
            print("that did 13 damage")
            nickit_health -= 12
        if fight13 == "magical leaf":
            print("that did 27 hp")
            nickit_health -= 27
        if nickit3 == 4:
            print("nickit used night slash")
            grookey_health -= 13
        elif nickit3 == 1:
            print("nickit used beat up")
            grookey_health -= 13
        elif nickit3 == 2:
            print("nickit used foul play")
            grookey_health -= 8
        elif nickit3 == 3:
            print("nickit used sucker punch")
            grookey_health -= 10
        if grookey_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if nickit_health <= 0:
            print("The wild nickit fainted we'll get em next time")
            break
    elif answer13 == "catch" and catch13 == 1:
        print("gotcha nickit was caught!")
        break
    elif answer13 == "catch" and catch13 == 2:
        print("close!")
    elif answer13 == "catch" and catch13 == 3:
        print("Aw that was So close!")
    elif answer13 == "catch" and catch13 == 4:
        print("That was so close keep it up!")
    elif answer13 == "catch" and catch13 == 5:
        print("Ok now that was way to close!")
    elif answer13 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag13 = input("what do you want to use ")
        if bag13 == "potion" and grookey_health <= 30:
            print("healed pokemon")
            grookey_health += 20
            potions -= 1
        elif bag13 == "potion" and grookey_health == 31:
            print("healed pokemon")
            grookey_health += 19
            potions -= 1
        elif bag13 == "potion" and grookey_health == 32:
            print("healed pokemon")
            grookey_health += 18
            potions -= 1
        elif bag13 == "potion" and grookey_health == 33:
            print("healed pokemon")
            grookey_health += 17
            potions -= 1
        elif bag13 == "potion" and grookey_health == 34:
            print("healed pokemon")
            grookey_health += 16
            potions -= 1
        elif bag13 == "potion" and grookey_health == 35:
            print("healed pokemon")
            grookey_health += 15
            potions -= 1
        elif bag13 == "potion" and grookey_health == 36:
            print("healed pokemon")
            grookey_health += 14
            potions -= 1
        elif bag13 == "potion" and grookey_health == 37:
            print("healed pokemon")
            grookey_health += 13
            potions -= 1
        elif bag13 == "potion" and grookey_health == 38:
            print("healed pokemon")
            grookey_health += 12
            potions -= 1
        elif bag13 == "potion" and grookey_health == 39:
            print("healed pokemon")
            grookey_health += 11
            potions -= 1
        elif bag13 == "potion" and grookey_health == 40:
            print("healed pokemon")
            grookey_health += 10
            potions -= 1
        elif bag13 == "potion" and grookey_health == 41:
            print("healed pokemon")
            grookey_health += 9
            potions -= 1
        elif bag13 == "potion" and grookey_health == 42:
            print("healed pokemon")
            grookey_health += 8
            potions -= 1
        elif bag13 == "potion" and grookey_health == 43:
            print("healed pokemon")
            grookey_health += 7
            potions -= 1
        elif bag13 == "potion" and grookey_health == 44:
            print("healed pokemon")
            grookey_health += 6
            potions -= 1
        elif bag13 == "potion" and grookey_health == 45:
            print("healed pokemon")
            grookey_health += 5
            potions -= 1
        elif bag13 == "potion" and grookey_health == 46:
            print("healed pokemon")
            grookey_health += 4
            potions -= 1
        elif bag13 == "potion" and grookey_health == 47:
            print("healed pokemon")
            grookey_health += 3
            potions -= 1
        elif bag13 == "potion" and grookey_health == 48:
            print("healed pokemon")
            grookey_health += 2
            potions -= 1
        elif bag13 == "potion" and grookey_health == 49:
            print("healed pokemon")
            grookey_health += 1
            potions -= 1
        elif bag13 == "potion" and grookey_health == 50:
            print("your pokemon is at full health")
        elif bag13 == "master ball" and master_ball == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif bag13 == "ultra ball" and ultra_balls == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag13 == "great ball" and great_balls == 1:
            print("gotcha nickit was caught!")
            break
            sus.exit
        elif bag13 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag13 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 4 and starter == "grookey":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch14 = r.randint(1, 5)
    drednaw3 = r.randint(1, 4)
    answer14 = input("fight/catch/bag/run ")
    print("grookey's health " + str(grookey_health))
    print("drednaw's health " + str(drednaw_health))
    if answer14 == "run":
        sus.exit("you ran away")
    elif answer14 == "fight" and starter == "grookey" and x == 4:

        print("what move do you want to use")
        print("scratch")
        print("branch poke")
        print("razor leaf")
        print("magical leaf")
        fight14 = input()
        if fight14 == "scratch":
            print("that did 4 damage")
            drednaw_health -= 4
        if fight14 == "razor leaf":
            print("that did 45 damage")
            print("that was super effective!")
            drednaw_health -= 25
        if fight14 == "branch poke":
            print("that did 26 damage")
            print("that was super effective!")
            drednaw_health -= 12
        if fight14 == "magical leaf":
            print("that did 56 hp")
            print("that was super effecive!")
            drednaw_health -= 27
        if drednaw3 == 4:
            print("drednaw used hydro pump")
            grookey_health -= 13
        elif drednaw3 == 1:
            print("drednaw used water gun")
            grookey_health -= 13
        elif drednaw3 == 2:
            print("drednaw used rock tomb")
            grookey_health -= 30
        elif drednaw3 == 3:
            print("drednaw used liquidation")
            grookey_health -= 10
        if grookey_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if drednaw_health <= 0:
            print("The wild drednaw fainted we'll get em next time")
            break
    elif answer14 == "catch" and catch14 == 1:
        print("gotcha drednaw was caught!")
        break
    elif answer14 == "catch" and catch14 == 2:
        print("close!")
    elif answer14 == "catch" and catch14 == 3:
        print("Aw that was So close!")
    elif answer14 == "catch" and catch14 == 4:
        print("That was so close keep it up!")
    elif answer14 == "catch" and catch14 == 5:
        print("Ok now that was way to close!")
    elif answer14 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag14 = input("what do you want to use ")
        if bag14 == "potion" and grookey_health <= 30:
            print("healed pokemon")
            grookey_health += 20
            potions -= 1
        elif bag14 == "potion" and grookey_health == 31:
            print("healed pokemon")
            grookey_health += 19
            potions -= 1
        elif bag14 == "potion" and grookey_health == 32:
            print("healed pokemon")
            grookey_health += 18
            potions -= 1
        elif bag14 == "potion" and grookey_health == 33:
            print("healed pokemon")
            grookey_health += 17
            potions -= 1
        elif bag14 == "potion" and grookey_health == 34:
            print("healed pokemon")
            grookey_health += 16
            potions -= 1
        elif bag14 == "potion" and grookey_health == 35:
            print("healed pokemon")
            grookey_health += 15
            potions -= 1
        elif bag14 == "potion" and grookey_health == 36:
            print("healed pokemon")
            grookey_health += 14
            potions -= 1
        elif bag14 == "potion" and grookey_health == 37:
            print("healed pokemon")
            grookey_health += 13
            potions -= 1
        elif bag14 == "potion" and grookey_health == 38:
            print("healed pokemon")
            grookey_health += 12
            potions -= 1
        elif bag14 == "potion" and grookey_health == 39:
            print("healed pokemon")
            grookey_health += 11
            potions -= 1
        elif bag14 == "potion" and grookey_health == 40:
            print("healed pokemon")
            grookey_health += 10
            potions -= 1
        elif bag14 == "potion" and grookey_health == 41:
            print("healed pokemon")
            grookey_health += 9
            potions -= 1
        elif bag14 == "potion" and grookey_health == 42:
            print("healed pokemon")
            grookey_health += 8
            potions -= 1
        elif bag14 == "potion" and grookey_health == 43:
            print("healed pokemon")
            grookey_health += 7
            potions -= 1
        elif bag14 == "potion" and grookey_health == 44:
            print("healed pokemon")
            grookey_health += 6
            potions -= 1
        elif bag14 == "potion" and grookey_health == 45:
            print("healed pokemon")
            grookey_health += 5
            potions -= 1
        elif bag14 == "potion" and grookey_health == 46:
            print("healed pokemon")
            grookey_health += 4
            potions -= 1
        elif bag14 == "potion" and grookey_health == 47:
            print("healed pokemon")
            grookey_health += 3
            potions -= 1
        elif bag14 == "potion" and grookey_health == 48:
            print("healed pokemon")
            grookey_health += 2
            potions -= 1
        elif bag14 == "potion" and grookey_health == 49:
            print("healed pokemon")
            grookey_health += 1
            potions -= 1
        elif bag14 == "potion" and grookey_health == 50:
            print("your pokemon is at full health")
        elif bag14 == "master ball" and master_ball == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif bag14 == "ultra ball" and ultra_balls == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag14 == "great ball" and great_balls == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif bag14 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag14 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 5 and starter == "grookey":
    master_ball = r.randint(1, 1)
    ultra_balls = r.randint(1, 2)
    great_balls = r.randint(1, 3)
    catch15 = r.randint(1, 5)
    eternatus3 = r.randint(1, 4)
    answer15 = input("fight/catch/bag/run ")
    print("grookey's health " + str(grookey_health))
    print("eternatus's health " + str(eternatus_health))
    if answer15 == "run":
        sus.exit("you ran away")
    elif answer15 == "fight" and starter == "grookey" and x == 5:
        print("what move do you want to use")
        print("scratch")
        print("branch poke")
        print("razor leaf")
        print("magical leaf")
        fight14 = input()
        
        if fight14 == "scratch":
            print("that did 5 damage")
            eternatus_health -= 4
        if fight14 == "razor leaf":
            print("that did 25 damage")
            eternatus_health -= 25
        if fight14 == "branch poke":
            print("that did 12 damage")
            eternatus_health -= 12
        if fight14 == "magical leaf":
            print("that did 27 hp")
            eternatus_health -= 27
        if eternatus3 == 4:
            print("eternatus used dynamax cannon")
            grookey_health -= 13
        elif eternatus3 == 1:
            print("eternatus used dragon tail")
            grookey_health -= 13
        elif eternatus3 == 2:
            print("eternatus used venoshock")
            print("That was super effective!")
            grookey_health -= 40
        elif eternatus3 == 3:
            print("eternatus used eternabeam")
            grookey_health -= 40
        if grookey_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if eternatus_health <= 0:
            print("The wild eternatus fainted we'll get em next time")
            break
    elif answer15 == "catch" and catch15 == 1:
        print("gotcha eternatus was caught!")
        break
    elif answer15 == "catch" and catch15 == 2:
        print("close!")
    elif answer15 == "catch" and catch15 == 3:
        print("Aw that was So close!")
    elif answer15 == "catch" and catch15 == 4:
        print("That was so close keep it up!")
    elif answer15 == "catch" and catch15 == 5:
        print("Ok now that was way to close!")
    elif answer15 == "bag":
        print("you have " + str(potions) + " potions")
        print("you have " + str(great_ball) + " great balls")
        print("you have " + str(ultra_ball) + " ultra balls")
        print("you have " + str(master_balls) + " master ball")
        bag15 = input("what do you want to use ")
        if bag15 == "potion" and grookey_health <= 30:
            print("healed pokemon")
            grookey_health += 20
            potions -= 1
        elif bag15 == "potion" and grookey_health == 31:
            print("healed pokemon")
            grookey_health += 19
            potions -= 1
        elif bag15 == "potion" and grookey_health == 32:
            print("healed pokemon")
            grookey_health += 18
            potions -= 1
        elif bag15 == "potion" and grookey_health == 33:
            print("healed pokemon")
            grookey_health += 17
            potions -= 1
        elif bag15 == "potion" and grookey_health == 34:
            print("healed pokemon")
            grookey_health += 16
            potions -= 1
        elif bag15 == "potion" and grookey_health == 35:
            print("healed pokemon")
            grookey_health += 15
            potions -= 1
        elif bag15 == "potion" and grookey_health == 36:
            print("healed pokemon")
            grookey_health += 14
            potions -= 1
        elif bag15 == "potion" and grookey_health == 37:
            print("healed pokemon")
            grookey_health += 13
            potions -= 1
        elif bag15 == "potion" and grookey_health == 38:
            print("healed pokemon")
            grookey_health += 12
            potions -= 1
        elif bag15 == "potion" and grookey_health == 39:
            print("healed pokemon")
            grookey_health += 11
            potions -= 1
        elif bag15 == "potion" and grookey_health == 40:
            print("healed pokemon")
            grookey_health += 10
            potions -= 1
        elif bag15 == "potion" and grookey_health == 41:
            print("healed pokemon")
            grookey_health += 9
            potions -= 1
        elif bag15 == "potion" and grookey_health == 42:
            print("healed pokemon")
            grookey_health += 8
            potions -= 1
        elif bag15 == "potion" and grookey_health == 43:
            print("healed pokemon")
            grookey_health += 7
            potions -= 1
        elif bag15 == "potion" and grookey_health == 44:
            print("healed pokemon")
            grookey_health += 6
            potions -= 1
        elif bag15 == "potion" and grookey_health == 45:
            print("healed pokemon")
            grookey_health += 5
            potions -= 1
        elif bag15 == "potion" and grookey_health == 46:
            print("healed pokemon")
            grookey_health += 4
            potions -= 1
        elif bag15 == "potion" and grookey_health == 47:
            print("healed pokemon")
            grookey_health += 3
            potions -= 1
        elif bag15 == "potion" and grookey_health == 48:
            print("healed pokemon")
            grookey_health += 2
            potions -= 1
        elif bag15 == "potion" and grookey_health == 49:
            print("healed pokemon")
            grookey_health += 1
            potions -= 1
        elif bag15 == "potion" and grookey_health == 50:
            print("your pokemon is at full health")
        elif bag15 == "master ball" and master_ball == 1:
            print("gotcha drednaw was caught!")
            break
            sus.exit
        elif bag15 == "ultra ball" and ultra_balls == 1:
            print("gotcha eternatus was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag15 == "great ball" and great_balls == 1:
            print("gotcha eternatus was caught!")
            break
            sus.exit
        elif bag15 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag15 == "great ball" and great_balls == 3:
            great_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
print("that was the end of bootlegmon hope you liked it we might put out a bootlegmon 2 if it gets enough likes credits: hegdehawk11:music adder Carlos:Main Coder Oscar:Beta Tester William:Beta Tester Asher:Alpha Tester")