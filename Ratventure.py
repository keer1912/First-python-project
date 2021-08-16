#S10194171A
#Keerthana Keshaini
#P11

import random
from random import randint

# +------------------------
# | Text for various menus 
# +------------------------
main_text = ["New Game",\
             "Resume Game",\
             "View Leaderboard",\
             "View Instructions",\
             "Exit Game"]

town_text = ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Enter Shop",\
             "Save Game",\
             "Exit Game"]

open_text = ["View Character",\
             "View Map",\
             "Move",\
             "Sense Orb",\
             "Exit Game"]

fight_text = ["Attack",\
              "Run"]

world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]


print("Welcome to Ratventure!")
print("----------------------")
print("Start a new game or resume!")
print('For new players , view the instructions to learn about this game before playing!')

def instructions():
    file=open("Instructions.txt")
    for line in file:
        line=line.strip('\n')
        print(line)

def main_menu():
    num = 1
    print()
    try:
        for i in main_text:
            print (str(num)+")"+i)
            num+=1
        choice=int(input("Enter Choice: "))
        if choice==1:
            new_game()
        elif choice==2:
            resume()
            town_menu()
        elif choice==3:
            leaderboard()
            town_menu()
        elif choice ==4:
            instructions()
            main_menu()
        elif choice==5:
            exit_game()
        else:
            print("Invalid Key, Try Again")
            main_menu()
        
    except ValueError:
        print ("Invalid Key, Try Again")
        main_menu()
        
def new_game():
    global running
    global stats 
    global rat_stats
    global rat_king
    global orbX
    global orbY
    orbX=0
    orbY=0
    running=False
    while (orbX <= 3 and orbY <= 3):
        orbX=randint(0,7)
        orbY=randint(0,7)
        if world_map[orbX][orbY]!=' ':
            orbX = 0
            orbY = 0
    print(orbX,orbY)  
    stats=[['Day',1],['Name','The Hero'],['Damage',2,4],['Defence',1],['HP',20],['Loot',0],['Orb',0],[0,0],[orbX,orbY],['Sword',0],['Steel Armour',0],['Flamethrower',0]]
    rat_stats=[['Damage',1,3],['Defence',1],['HP',10]]
    rat_king=[['Damage',8,12],['Defence',5],['HP',25]]
    world_map[stats[7][0]][stats[7][1]]='H/'+ world_map[stats[7][0]][stats[7][1]]
    town_menu()

#stats[6][0],stats[6][1],stats[7][0],stats[7][1]]    
def save():
    file=open('save.txt',mode='w')
    file.write('{},{}\n'.format(stats[0][0],stats[0][1]))#saving day
    file.write('{},{}\n'.format(stats[1][0],stats[1][1]))#saving name
    file.write('{},{},{}\n'.format(stats[2][0],stats[2][1],stats[2][2]))#saving dmg
    file.write('{},{}\n'.format(stats[3][0],stats[3][1]))#saving defence
    file.write('{},{}\n'.format(stats[4][0],stats[4][1]))#saving HP
    file.write('{},{}\n'.format(stats[5][0],stats[5][1]))# loot
    file.write('{},{}\n'.format(stats[6][0],stats[6][1]))#check orb acquired
    file.write('{},{}\n'.format(stats[7][0],stats[7][1]))#hero position
    file.write('{},{}\n'.format(stats[8][0],stats[8][1]))#orb position
    file.write('{},{}\n'.format(stats[9][0],stats[9][1]))#Sword
    file.write('{},{}\n'.format(stats[10][0],stats[10][1]))#Steel Armour
    file.write('{},{}\n'.format(stats[11][0],stats[11][1]))#Flamethrower
    file.close()
    print('You have saved your game')
    
def resume():
    #Global stats allow me to access this values and update them inside and outside function
    global stats 
    global rat_stats
    global rat_king
    global running
    global world_map
    running=False
    stats=[]
    world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]

    rat_stats=[['Damage',1,3],['Defence',1],['HP',10]]#resuming stats of rat
    rat_king=[['Damage',8,12],['Defence',5],['HP',25]]#resuming stats of rat King
    try:#checking if the file exists
        file=open('save.txt',mode='r')#opening the text file
        for line in file:
            line=line.strip('\n')#remove blank line
            line=line.split(',')#separating with comma
            for i in line:
                if i.isdigit():
                    line[line.index(i)]=int(i)
            stats.append(line)
        file.close()
        
    except FileNotFoundError:
        print("No save file found")
        main_menu()        
    world_map[stats[7][0]][stats[7][1]]='H/'+ world_map[stats[7][0]][stats[7][1]]

    if stats[4][1]<1:
       stats[4][1]=20
    
           
def exit_game():
    print('Exiting game...')
    exit()

def town_menu():#Making the town menu
    print()
    num = 1#initialist the list number
    print('Day {}: You are in a town.'.format(stats[0][1]))
    try:# This checks if the value is a int or str
        for i in town_text:
            print (str(num)+")"+i)
            num+=1
        choice=int(input("Enter Choice: "))
        print()
        
        if choice== 1:
            view_char()
            town_menu()
        elif choice == 2:
            view_map()
            town_menu()
        elif choice == 3:
            move()
        elif choice ==4:
            rest()
        elif choice ==5:
            market()            
        elif choice == 6:
            save()
            town_menu()
        elif choice== 7:
            exit_game()
        else:
            print("Invalid Key, Try Again")
            town_menu()
            
    except ValueError:
        print('Invalid Key try again!')
        print()
        town_menu()
        
        
#viewing character
def view_char():
    if stats[6][1]==1:
        print('{:>10}'.format(stats[1][1]))#Name
        print('{:>10}: {}-{}'.format(stats[2][0],stats[2][1],stats[2][2]))#damage
        print('{:>10}: {}'.format(stats[3][0],stats[3][1]))#defence
        print('{:>10}: {}'.format(stats[4][0],stats[4][1]))#HP
        print('You are holding Orb of Power.')
    else:
        print('{:>10}'.format(stats[1][1]))
        print('{:>10}: {}-{}'.format(stats[2][0],stats[2][1],stats[2][2]))
        print('{:>10}: {}'.format(stats[3][0],stats[3][1]))
        print('{:>10}: {}'.format(stats[4][0],stats[4][1]))
        
    if world_map[stats[7][0]][stats[7][1]]==' ':
        outdoormenu()

#printing +---- from worldmap    
def view_map():
    for i in world_map:#for every list in nested list, print this line
        print("+---+---+---+---+---+---+---+---+")
        for j in i: #for every element in each list
             print('|{:^3}'.format(j),end='')#with 3 spaces print this |
        print('|')
    print("+---+---+---+---+---+---+---+---+")#print last line of barrier    
#restt         
def rest():
    stats[0][1]+=1
    stats[4][1]=20
    print('You are fully healed.')
    town_menu()

def  fight_menu():
    global choice
    num=1
    for i in fight_text:
        print (str(num)+")"+i)
        num+=1
    choice=int(input("Enter Choice: "))
    
#movement
def move():
    global world_map
    global stats
    view_map()
    print()
    print("W = up; A = left; S = down; D = right")
    allowed_keys=['W','A','S','D']
    movement=input("Your move : ")
    movement=movement.upper()
    

    if movement not in allowed_keys:
        print('Invalid Key, Try Again!')
        print()
        move()

    #finding where the hero is at
    for i in world_map:# mini lists inside big list
        for j in i:#every element inside mini lists
            if 'H' in world_map[world_map.index(i)][i.index(j)]:#finding x y coordinate of 'Hero'
                stats[7][0]=world_map.index(i)#finding where 'H' is at , x coord
                stats[7][1]=i.index(j)#finding where 'H' is at , y coord
    
    if movement == 'S':
        #print ('{:>10}: {}'.format(stats[0][0],stats[0][1]))
        if stats[7][0] < 7:#ensure that x coord is < 7 to not exit last barrier 
            stats[0][1]+=1
            if world_map[stats[7][0]+1][stats[7][1]] == ' ':#check if down is empty
                
                if world_map[stats[7][0]][stats[7][1]] == 'H':#check if existing has Hero
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#Replace existing with blank
                    world_map[stats[7][0]+1][stats[7][1]]=world_map[stats[7][0]+1][stats[7][1]].replace(' ','H')#replacing down with Hero
                    view_map()
                    stats[7][0]+=1
                    get_orb()
                    rat_chances()
                else:# this condition is if existing has H/ (shared with town)
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H/',' ')#Replace shared with nothimg , thus town alone
                    world_map[stats[7][0]+1][stats[7][1]]=world_map[stats[7][0]+1][stats[7][1]].replace(' ','H')# Replacing down with Hero
                    view_map()
                    stats[7][0]+=1
                    get_orb()
                    rat_chances()
            else:#if not empty
                if world_map[stats[7][0]+1][stats[7][1]] == "K":
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#Replace existing with blank
                    world_map[stats[7][0]+1][stats[7][1]]=world_map[stats[7][0]+1][stats[7][1]].replace('K','H/K')#replacing down with Hero
                    stats[7][0]+=1
                    view_map()
                    rat_king_encounter()
                    
                else:
                    world_map[stats[7][0]+1][stats[7][1]]='H/'+ world_map[stats[7][0]+1][stats[7][1]]#share Hero with town and king
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#replace previous hero spot with blank
                    view_map()
                    stats[7][0]+=1
                    town_menu()
        else:
            print('You are trying to move out of the map!, Try again.')
            move()
            
    if movement == 'W':
        if stats[7][0] > 0:#ensure that x coord is positive
            stats[0][1]+=1
            if world_map[stats[7][0]-1][stats[7][1]] == ' ':#check empty                
                if world_map[stats[7][0]][stats[7][1]] == 'H':
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')
                    world_map[stats[7][0]-1][stats[7][1]]=world_map[stats[7][0]-1][stats[7][1]].replace(' ','H')
                    view_map()
                    stats[7][0]-=1
                    get_orb()
                    rat_chances()
                else:
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H/','')
                    world_map[stats[7][0]-1][stats[7][1]]=world_map[stats[7][0]-1][stats[7][1]].replace(' ','H')
                    view_map()
                    stats[7][0]-=1
                    get_orb()
                    rat_chances()
            else:
                world_map[stats[7][0]-1][stats[7][1]]= 'H/'+ world_map[stats[7][0]-1][stats[7][1]]
                world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')
                view_map()
                stats[7][0]-=1
                town_menu()
        else:
            print('You are trying to move out of the map!, Try again.')
            move()
            
    if movement == 'D':
        if stats[7][1] < 7:#ensure dont exit right hand side barrier
            stats[0][1]+=1
            if world_map[stats[7][0]][stats[7][1]+1] == ' ':#check empty
                
                if world_map[stats[7][0]][stats[7][1]] == 'H':
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')
                    world_map[stats[7][0]][stats[7][1]+1]=world_map[stats[7][0]][stats[7][1]+1].replace(' ','H')
                    view_map()
                    stats[7][1]+=1
                    get_orb()
                    rat_chances()
                else:
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H/','')
                    world_map[stats[7][0]][stats[7][1]+1]=world_map[stats[7][0]][stats[7][1]+1].replace(' ','H')
                    view_map()
                    stats[7][1]+=1
                    get_orb()
                    rat_chances()
            else:#if not empty
                if world_map[stats[7][0]][stats[7][1]+1] == "K":
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#Replace existing with blank
                    world_map[stats[7][0]][stats[7][1]+1]=world_map[stats[7][0]][stats[7][1]+1].replace('K','H/K')#replacing down with Hero
                    stats[7][1]+=1
                    view_map()
                    rat_king_encounter()
                else:
                    world_map[stats[7][0]][stats[7][1]+1]='H/'+ world_map[stats[7][0]][stats[7][1]+1]#share Hero with town and king
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#replace previous hero spot with blank
                    view_map()
                    stats[7][1]+=1
                    town_menu()                    
        else:
            print('You are trying to move out of the map!, Try again.')
            move()
            
    if movement == 'A':
        if stats[7][1] > 0:#ensure dont exit right left side barrier
            stats[0][1]+=1
            if world_map[stats[7][0]][stats[7][1]-1] == ' ':#check empty
                
                if world_map[stats[7][0]][stats[7][1]] == 'H':
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')
                    world_map[stats[7][0]][stats[7][1]-1]=world_map[stats[7][0]][stats[7][1]-1].replace(' ','H')
                    view_map()
                    stats[7][1]-=1
                    get_orb()
                    rat_chances()
                else:    
                    world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H/','')
                    world_map[stats[7][0]][stats[7][1]-1]=world_map[stats[7][0]][stats[7][1]-1].replace(' ','H')
                    view_map()
                    stats[7][1]-=1
                    get_orb()
                    rat_chances()

            else:#if it is not empty then
                world_map[stats[7][0]][stats[7][1]-1]='H/'+ world_map[stats[7][0]][stats[7][1]-1]#add the hero next to town
                world_map[stats[7][0]][stats[7][1]]=world_map[stats[7][0]][stats[7][1]].replace('H',' ')#for the previous coord remove the H and put empty.
                view_map()
                stats[7][1]-=1
                town_menu()

        else:
            print('You are trying to move out of the map!, Try again.')
            move()
    
def rat_chances():#Gives me a chances of encountering the rat when im in the open
    print('{}:{} You are out in the open'.format(stats[0][0],stats[0][1]))
    chances=randint(1,10)
    if chances <=8:
        rat_encounter()
    else:
        print("Yay you are free from rat today!")
        print()
        outdoor_menu()
        
def rat_encounter():#prints that im encountering a rat
    global rat_stats
    global stats
    num=1
    print('Encounter - Rat')
    print('{:>10}: {}-{}'.format(rat_stats[0][0],rat_stats[0][1],rat_stats[0][2]))
    print('{:>10}: {}'.format(rat_stats[1][0],rat_stats[1][1]))
    print('{:>10}: {}'.format(rat_stats[2][0],rat_stats[2][1]))
    print()
    try:
        fight_menu()
        if choice== 1 :
            rat_attack()
        elif choice == 2:
            run()
        else:
            print("Invalid Key, Try Again")
            fight_menu()
            
    except ValueError:
        print("Invalid Key , Try Again!")
        
        
def rat_attack():#Calculating all my rat and human stats
    global loot
    global stats#global to update
    human2Rat=randint(2,4)#dmg from human to rat
    Rat2Human=randint(1,3)#dmg from rat to human
    
    Rat2Human=Rat2Human-stats[3][1]#this value is the dmg dealt by the rat after offsetting his defence
    human2Rat=human2Rat-rat_stats[1][1]#this value is the dmg dealt by the human after offsetting its defence
    
    if (Rat2Human<0):
        Rat2Human=0
        
    if (human2Rat<0):
        human2Rat=0
        
    stats[4][1]= stats[4][1]-(Rat2Human)#calculating HP
    rat_stats[2][1] = rat_stats[2][1]-(human2Rat)#calculating HP of rat
    
    if stats[4][1] > 0:
        if rat_stats[2][1] > 0:
            if Rat2Human==0:
                print()
                print("You deal {} damage to the rat".format(human2Rat))
                print("You have defended yourself!".format(Rat2Human))
                print("You have {} HP left".format(stats[4][1]))
                print()
                rat_encounter()
            else:
                print()
                print("You deal {} damage to the rat".format(human2Rat))
                print("Ouch! The Rat hit you for {} damage".format(Rat2Human))
                print("You have {} HP left".format(stats[4][1]))
                print()
                rat_encounter()
        else:
            rat_stats[2][1]=0#rat dead
            print()
            print("You deal {} damage to the rat".format(human2Rat))
            print ("The Rat is dead! You are victorious")
            loot=randint(30,60)
            print("You have acquired {} Sen.".format(loot))
            print()
            rat_stats[2][1]=10
            stats[5][1]+=loot
            outdoor_menu()
    else:
        stats[4][1] < 1#dead
        print ("You have lost the fight, better luck next time.")
        print("You are returning to the main menu. Choose a new game or resume at the last saved town.")
        main_menu()
        
def run():
    global running
    global rat_king
    running= True #set that im running
    print('You run and hide')
    rat_stats[2][1]=10
    rat_king[2][1]=25
    outdoor_menu()
    
def outdoor_menu():
    global running
    try:
        num=1
        for i in open_text:
            print (str(num)+")"+i)
            num+=1
        choice=int(input("Enter Choice: "))
        print()
        if not (running):
            if choice== 1:
                view_char()
                outdoor_menu()
            elif choice == 2:
                view_map()
                outdoor_menu()
            elif choice == 3:
                move()
                rat_chances()
            elif choice ==4:
                sense_orb()
                outdoor_menu()
            elif choice ==5:
                print('You have exited the game')
            else:
                print("Invalid Key, Try Again")
                outdoor_menu()
                
        elif running:
            running=False
            if choice== 1:
                rat_encounter()
            elif choice == 2:
                rat_encounter()
            elif choice == 3:
                move()
                rat_chances()
            elif choice ==4:
                rat_encounter()
            elif choice ==5:
                print('You have exited the game')
            else:
                print("Invalid Key, Try Again")
                outdoor_menu()
                
    except ValueError:
        print('Invalid Key try again!')
        print()
        outdoor_menu()

def get_orb():#on the orb , add to my stats
    global stats
    if world_map[stats[7][0]][stats[7][1]] == world_map[stats[8][0]][stats[8][1]]:
        stats[2][1]+=5
        stats[2][2]+=5
        stats[3][1]+=5
        print()
        print("You found the Orb of power.")
        print("Your attack increases by 5.")
        print("Your defence increases by 5.")
        print()
        stats[6][1]+=1
            
def sense_orb():#finding where the orb is at
    global sense
    global stats
    if stats[6][1] != 1:
        if stats[7][0] < stats[8][0] and stats[7][1] == stats[8][1]:
            sense="South"
        elif stats[7][0] > stats[8][0] and stats[7][1] == stats[8][1]:
            sense ="North"
        elif stats[7][0] == stats[8][0] and stats[7][1] < stats[8][1]:
            sense="East"
        elif stats[7][0] == stats[8][0] and stats[7][1] > stats[8][1]:
            sense="West"
        elif stats[7][0] < stats[8][0] and stats[7][1] > stats[8][1]:
            sense="Southwest"
        elif stats[7][0] < stats[8][0] and stats[7][1] < stats[8][1]:
            sense="Southeast"
        elif stats[7][0] > stats[8][0] and stats[7][1] < stats[8][1]:
            sense="Northeast"
        elif stats[7][0] > stats[8][0] and stats[7][1] > stats[8][1]:
            sense="Northwest"        
        print()
        print("You sense that the Orb of power is to the {}.".format(sense))
        outdoor_menu()
        stats[0][1]+=1#add day
    else:
        print("You already have the orb!")
        outdoor_menu()
                            
def rat_king_attack():#rat king attack function to calculte all my stats and globalise to update
    global rat_king
    global stats
    human2RatKing=randint(stats[2][1],stats[2][2])#dmg from human to rat
    RatKing2Human=randint(rat_king[0][1],rat_king[0][2])#dmg from rat to human
    
    if stats[4][1] > 1:   #if human alive         
        if rat_king[2][1] >= 4:#if rat alive below 4 health,MAX DMG will confirm kill it. 
            if stats[6][1]!=1:# if i dont have the orb
                human2RatKing=0
                print('You do not have the Orb of Power - the Rat King is immune!')
                print('You deal 0 damage to the Rat King')
                stats[4][1]= stats[4][1]-RatKing2Human
                rat_king[2][1] = rat_king[2][1]-human2RatKing
                print('Ouch the Rat King hit you for {} damage'.format(RatKing2Human))
                print("You have {} HP left".format(stats[4][1]))
                rat_king_encounter()
                
            else:
                RatKing2Human=RatKing2Human-stats[3][1]#this value is the dmg dealt by the rat after offsetting his defence aka TRUE DAMAGE
                human2RatKing=human2RatKing-rat_king[1][1]#this value is the dmg dealt by the human after offsetting its defence aka TRUE DAMAGE

                if (RatKing2Human>1):
                    stats[4][1]= stats[4][1]-RatKing2Human
                if (human2RatKing>1):
                    rat_king[2][1] = rat_king[2][1]-human2RatKing
                
                if RatKing2Human==0:#if i can protect myself
                    print("You deal {} damage to the rat".format(human2RatKing))
                    print("You have defended yourself!".format(RatKing2Human))
                    print("You have {} HP left".format(stats[4][1]))
                    print()
                    rat_king_encounter()
                
                else:
                    print()
                    print("You deal {} damage to the rat".format(human2RatKing))
                    print("Ouch! The Rat hit you for {} damage".format(RatKing2Human))
                    print("You have {} HP left".format(stats[4][1]))
                    print()
                    rat_king_encounter()
                    
        else:
            rat_king[2][1]=0
            print('The Rat King is dead! You are victorious!')
            print('Congratulations, you have defeated the Rat King!')
            print('The world is saved you win!')
            print("You can start a new game again.")
        main_menu()
                
    elif stats[4][1] <= 0:
        stats[4][1]=0
        print ("You have lost the fight, better luck next time.")
        print("You are returning to the main menu. Choose a new game or resume at the last saved town.")
        main_menu()
        
def rat_king_encounter():#printing rat encounter 
    global rat_king
    print('{} {}:You see the Rat King'.format(stats[0][0],stats[0][1]))
    print('{}: {}-{}'.format(rat_king[0][0],rat_king[0][1],rat_king[0][2]))
    print('{}:{}'.format(rat_king[1][0],rat_king[1][1]))
    print('{}:{}'.format(rat_king[2][0],rat_king[2][1]))
    print()
    try:
        fight_menu()
        if choice== 1 :
             rat_king_attack()
        elif choice == 2:
             run()
        else:
            print("Invalid Key, Try Again")
            fight_menu()
            if choice== 1 :
                rat_king_attack()
            elif choice == 2:
                run()            
    except ValueError:
        print("Invalid Key, Try Again!")
        print()
        rat_king_encounter()
        
def accept_order():
    global confirm_order
    print("Confirm Order?")
    print("[1] Yes")
    print("[2] No")
    confirm_order=int(input("Select Option:"))
    print()
        
def market():#making store, updating stats along the way
    global stats
    global boost
    boost=[['Sword','Damage',10,200],['Steel Armour','Defence',2,100],['Flamethrower','Damage',20,300],]
    print('{:^45}'.format("| Welcome to the realm of weapons |"))
    print('{}'.format("You currently have: {} Sen\n".format(stats[5][1])))
    for i in boost:
        print("[{}] {:<15} +{:<3} {} {:>6} {}".format(boost.index(i)+1,i[0],i[2],i[1],i[3],"Sen"))  #print shop details    
    print("[4] Exit Shop")
    print()
    try:
        weapon_choice=int(input("Enter Choice: "))
        if weapon_choice==1:
            if stats[9][1]==0:#Only allow player to purchase once
                print("You have selected Sword")
                accept_order()                
                if confirm_order == 1:
                    if  stats[5][1]>=boost[0][3]:
                        stats[5][1]-=boost[0][3]
                        stats[9][1]+=1
                        stats[2][1]+=10
                        stats[2][2]+=10
                        print("Thank you for the purchase! Select another item to purchase or exit the shop :)")
                        print()
                        market()
                    else:
                        print("You dont have enough money to buy this!")
                        print()
                        market()
                else:
                    print("Select another weapon or exit store")
                    print()
                    market()                    
            else:
                print("You already have this item!")
                print()
                market()
                
        elif weapon_choice==2:     
            if stats[10][1]==0:
                print("You have selected Steel Armour")
                accept_order()                 
                if confirm_order==1:
                    if stats[5][1]>=boost[1][3]:
                        stats[5][1]-=boost[1][3]
                        stats[10][1]+=1
                        stats[3][1]+=2
                        print("Thank you for the purchase! Select another item to purchase or exit the shop :)")
                        print()
                        market()
                    else:
                        print("You dont have enough money to buy this!")
                        print()
                        market()
                else:
                    print("Select another weapon or exit store")
                    print()
                    market()          
            else:
                 print("You already have this item!")
                 print()
                 market()

        elif weapon_choice==3:     
            if stats[11][1]==0:
                print("You have selected flamethrower")
                accept_order()                    
                if confirm_order==1:
                    if stats[5][1]>=boost[1][3]:
                        stats[5][1]-=boost[2][3]
                        stats[11][1]+=1
                        stats[11][1]+=20
                        stats[2][1]+=20
                        print("Thank you for the purchase! Select another item to purchase or exit the shop :)")
                        print()
                        market()
                    else:
                        print("You dont have enough money to buy this!")
                        print()
                        market()
                else:
                    print("Select another weapon or exit store")
                    print()
                    market()          
            else:
                 print("You already have this item!")
                 print()
                 market()

        elif weapon_choice==4:#actually a section to exit shop
            print("Exiting Shop, returning to town!")
            print()
            town_menu()
        else:
            print("Invalid Key, Try Again")
    except ValueError:
        print("Invalid Key, Try Again!")
        
main_menu()

#def

