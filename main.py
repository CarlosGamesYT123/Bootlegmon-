import random as r
import time as t
import sys as sus
from replit import audio
import replit

grooky_health = 50
scorbunny_health = 50
sobble_health = 50
nicket_health = 40
drednaw_health = 80
pickachu_health = 35
wooloo_health = 42
eternatus_health = 140
potions = 20
master_balls = 1
ultra_ball = 10
great_ball = 30
source = audio.play_file('pokemoncenter.wav',1)

print(' Another project from the team behind THE MONEY\n Hopefuly we won\'t get sued\n Enjoy BOOTLEGMON\n NOTE:this is a FAN MADE PROJECT(do not sue us pls)\n we are in beta so don\'t go nuts')
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
t.sleep(5)
replit.clear()
print('preparing for death')
oof = audio.play_file('oof.wav',1)
t.sleep(5)
replit.clear()
print('loading music')
source = audio.play_file('pokemoncenter.wav',1)
t.sleep(5)
replit.clear()
print('let\'s play!')
t.sleep(1)
replit.clear()

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
source.set_paused(True)
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
audio.play_file('pokemon.wav', 1)
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
            sus.exit
        elif bag == "ultra ball" and ultra_balls == 1:
            print("gotcha wooloo was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag == "great ball" and great_balls == 1:
            print("gotcha wooloo was caught!")
            break
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
while x == 1:
    master_ball2 = r.randint(1, 1)
    ultra_balls2 = r.randint(1, 2)
    great_balls2 = r.randint(1, 3)
    catch2 = r.randint(1, 5)
    pickachu = r.randint(1, 4)
    answer2 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("pickachu's health " + str(pickachu_health))
    if answer2 == "run":
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
            pickachu_health -= 4
        if fight2 == "sucker punch":
            print("that did 30 damage")
            pickachu_health -= 30
        if fight2 == "water pulse":
            print("that did 20 damage")
            pickachu_health -= 20
        if fight2 == "water gun":
            print("that did 10 hp")
            pickachu_health -= 10
        if pickachu == 4:
            print("pickachu used thunder bolt")
            print("That was super effective!")
            sobble_health -= 46
        elif pickachu == 1:
            print("pickachu used electro ball")
            print("that was super effective!")
            sobble_health -= 42
        elif pickachu == 2:
            print("pickacu used iron tail")
            sobble_health -= 30
        elif pickachu == 3:
            print("pickachu used electro web")
            print("That was super effecive!")
            sobble_health -= 40
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if pickachu_health <= 0:
            print("The wild pickachu fainted we'll get em next time")
            break
    elif answer2 == "catch" and catch2 == 1:
        print("gotcha pickachu was caught!")
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
            print("gotcha pickachu was caught!")
            sus.exit
        elif bag2 == "ultra ball" and ultra_balls == 1:
            print("gotcha pickachu was caught!")
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag2 == "great ball" and great_balls == 1:
            print("gotcha pickachu was caught!")
            sus.exit
        elif bag2 == "great ball" and great_balls == 2:
            great_ball -= 1
            print("close!")
        elif bag2 == "great ball" and great_balls == 3:
            ultra_ball -= 1
            print("Aw that was So close!")
        elif great_ball <= 0:
            print("you can't use that you have no more!")
        elif ultra_ball <= 0:
            print("you can't use that you have no more!")
        elif potions <= 0:
            print("you can't use that you have no more!")
while x == 3:
    master_ball3 = r.randint(1, 1)
    ultra_balls3 = r.randint(1, 2)
    great_balls3 = r.randint(1, 3)
    catch3 = r.randint(1, 5)
    nicket = r.randint(1, 4)
    answer3 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("nicket's health " + str(nicket_health))
    if answer3 == "run":
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
            nicket_health -= 4
        if fight3 == "sucker punch":
            print("that did 30 damage")
            nicket_health -= 30
        if fight3 == "water pulse":
            print("that did 20 damage")
            nicket_health -= 20
        if fight3 == "water gun":
            print("that did 10 hp")
            nicket_health -= 10
        if nicket == 4:
            print("nicket used double kick")
            print("it hit twice!")
            sobble_health -= 10
        elif nicket == 1:
            print("nicket used tail whip")
            sobble_health -= 12
        elif nicket == 2:
            print("nicket used tackle")
            sobble_health -= 8
        elif nicket == 3:
            print("nicket used dark pulse")
            sobble_health -= 25
        if sobble_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if nicket_health <= 0:
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
            sus.exit
        elif bag3 == "ultra ball" and ultra_balls3 == 1:
            print("gotcha nickit was caught!")
            sus.exit
        elif ultra_balls3 == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag3 == "great ball" and great_balls3 == 1:
            print("gotcha nicket was caught!")
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
while x == 4:
    master_ball4 = r.randint(1, 1)
    ultra_balls4 = r.randint(1, 2)
    great_balls4 = r.randint(1, 3)
    catch4 = r.randint(1, 5)
    drednaw = r.randint(1, 4)
    answer4 = input("fight/catch/bag/run ")
    print("sobble's health " + str(sobble_health))
    print("drednaw's health " + str(drednaw_health))
    if answer4 == "run":
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
while x == 5:
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
            ultra_ball -= 1
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
    elif answer6 == "catch" and catch == 1:
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
    pickachu2 = r.randint(1, 4)
    answer7 = input("fight/catch/bag/run ")
    print("scorbunny's health " + str(scorbunny_health))
    print("pickachu's health " + str(pickachu_health))
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
            pickachu_health -= 4
        if fight7 == "fire punch":
            print("that did 30 damage")
            pickachu_health -= 30
        if fight6 == "ember":
            print("that did 20 damage")
            pickachu_health -= 20
        if fight6 == "double kick":
            print("it hit twice!")
            print("that did 20 hp")
            pickachu_health -= 10
        if pickachu2 == 4:
            print("wooloo used Double-Edge")
            scorbunny_health -= 23
        elif pickachu2 == 1:
            print("wooloo used take down")
            scorbunny_health -= 12
        elif pickachu2 == 2:
            print("wooloo used tackle")
            scorbunny_health -= 8
        elif pickachu2 == 3:
            print("wooloo used headbutt")
            scorbunny_health -= 20
        if scorbunny_health <= 0:
            audio.play_file('oof.wav', 1)
            print("you have no pokemon that can fight")
            sus.exit(':(')
        if pickachu_health <= 0:
            print("The wild wooloo fainted we'll get em next time")
            break
    elif answer6 == "catch" and catch == 1:
        print("gotcha pickachu was caught!")
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
            print("gotcha pickachu was caught!")
            break
            sus.exit
        elif bag7 == "ultra ball" and ultra_balls == 1:
            print("gotcha pickachu was caught!")
            break
            sus.exit
        elif ultra_balls == 2:
            ultra_ball -= 1
            print("Aw so close!")
        elif bag7 == "great ball" and great_balls == 1:
            print("gotcha pickachu was caught!")
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