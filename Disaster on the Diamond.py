# Ben Bruzewski
# Python Final Project - Disaster on the Diamond
# All assets were made by me, so no citations were needed.

# The text file, Game Explanation for DOTD, has all of the information regarding rubric elements as well as how to play the game.

# I would recommend keeping your shell window to the side as you'll need to input a name in there later if you win the game.


import pgzrun
from random import randint
import time #importing time for our scoreboard later on
global final_selection #making this global to ensure it works within our functions
global room_tracker #same for all of these variables which get changed inside if statements
global clue1_tracker
global clue2_tracker
global clue3_tracker
global clue4_tracker
global clue5_tracker
room_tracker = 0 #room_tracker will check the amount of clicks on the "continue" button by the player and take them to the correct room
clue1_tracker = 0 #these trackers are for the clues. Having a counter allows us to "open" a description of the item when it's clicked on!
clue2_tracker = 0
clue3_tracker = 0
clue4_tracker = 0
clue5_tracker = 0

WIDTH = 800 #screen size. I made the assets to this size so it's what I'm going with for the game
HEIGHT = 800

ship = Actor('ship') #here we're defining all the "actors" (images) for the game. Anything I want to take up the whole space will be in the center (400,400)
ship.pos = 400,400

arrow = Actor('continue') #the continue button. this will be on each screen and is how the player progresses
arrow.pos = 700,750

story1 = Actor('story1') #story screen
story1.pos = 400,400

story2 = Actor('story2') #story screen
story2.pos = 400,400

story3 = Actor('bridge') #the captain's bridge is our first room with a clue. The player is looking for the captain's log here (not too hard to find)
story3.pos = 400,400

clue1 = Actor('log') #this is the captain's log itself. The clues are our form of randomness in this game, as they'll be randomly generated in our rooms!
clue1.x = randint(400, 499) #the goal here is that I don't want it colliding with the chair. On the floor or on the table is fine though!
clue1.y = randint(450, 650) #With the y I wanted it to be below the ceiling or windows of the bridge

loginfo = Actor('loginfo')
loginfo.pos = 150,150

story4 = Actor('cabin1') #this is the cleaning lady's room. Here the player will find the work schedule showing that Martha was busy and has an alias for the time of the murder
story4.pos = 400,400

clue2 = Actor('schedule') #clue placement for the cleaning lady's schedule
clue2.x = randint(100,200)
clue2.y = randint(400,650)

story5 = Actor('cabin2') #this is Harry's room
story5.pos = 400,400

clue3 = Actor('controller') #Placement for Harry's game controller
clue3.x = randint(300,400)
clue3.y = randint(400,650)

scheduleinfo = Actor('scheduleinfo') #info box for the schedule
scheduleinfo.pos = 150,150

controllerinfo = Actor('controllerinfo') #info box for the controller
controllerinfo.pos = 150,150

story6 = Actor('cabin3') #This is Darla's room
story6.pos = 400,400

clue4 = Actor('smartphone') #Placement for Darla's smartphone
clue4.x = randint(500,650)
clue4.y = randint(400,650)

smartphoneinfo = Actor('smartphoneinfo') #Info for Darla's smartphone
smartphoneinfo.pos = 150,150

story7 = Actor('maindeck') #the final area the player will explore, the main deck of the ship
story7.pos = 400,400

clue5 = Actor('camera') #Placement for the CCTV camera clue
clue5.x = randint(300,500)
clue5.y = randint(300,350)

camerainfo = Actor('camerainfo') #Info for the camera
camerainfo.pos = 150,150

clue1_sum = Actor('clue1_sum') #Summary of all of the clues, which is just their sprite + info box 
clue1_sum.pos = 400,400

clue2_sum = Actor('clue2_sum')
clue2_sum.pos = 400,400

clue3_sum = Actor('clue3_sum')
clue3_sum.pos = 400,400

clue4_sum = Actor('clue4_sum')
clue4_sum.pos = 400,400

clue5_sum = Actor('clue5_sum')
clue5_sum.pos = 400,400

captain = Actor('captain_model') #Models of each character, placed in a lineup for the selection screen.
captain.pos = 75,300

martha = Actor('martha_model')
martha.pos = 225,300

harry = Actor('harry_model')
harry.pos = 375,300

darla = Actor('darla_model')
darla.pos = 525,300

michael = Actor('michael_model')
michael.pos = 675,300

winner = Actor('winner') #winner screen!
winner.pos = 400,400

loser = Actor('loser') #loser screen.
loser.pos = 400,400

start = time.time() #checking the start time for the scoreboard later. 

def on_mouse_down(pos): #mouse clicking function
    if arrow.collidepoint(pos): #if the player clicks on the arrow actor (our continue button. named arrow b/c continue is a built-in function)
        global room_tracker 
        room_tracker += 1 #add 1 to our room_tracker. Everything will be fine unless someone decides to spam the button. They'll have some trouble guessing the killer at the end, haha.
    if clue1.collidepoint(pos) and room_tracker ==3:
        global clue1_tracker
        clue1_tracker += 1
    if clue2.collidepoint(pos) and room_tracker ==4:
        global clue2_tracker
        clue2_tracker += 1
    if clue3.collidepoint(pos) and room_tracker ==5:
        global clue3_tracker
        clue3_tracker += 1
    if clue4.collidepoint(pos) and room_tracker ==6:
        global clue4_tracker
        clue4_tracker += 1
    if clue5.collidepoint(pos) and room_tracker ==7:
        global clue5_tracker
        clue5_tracker += 1
    if room_tracker == 9:
        global final_selection
        if captain.collidepoint(pos): #if the player clicks on each character on the selection screen
            final_selection = 'captain' #final_selection will become that character
        elif martha.collidepoint(pos):
            final_selection = 'martha'
        elif harry.collidepoint(pos):
            final_selection = 'harry'
        elif darla.collidepoint(pos):
            final_selection = 'darla'
        elif michael.collidepoint(pos):
            final_selection = 'michael'
def draw(): #defining our draw function. VERY important for this game
    screen.clear() #this initial section is our main menu/start screen basically
    ship.draw() #place the cruise ship
    arrow.draw() #place the continue arrow
    screen.draw.text("Disaster on the Diamond", fontsize=48, midtop = (400,0), align="center") #title text
    screen.draw.text("A Pygame Zero murder mystery game by Ben Bruzewski", (80,300), fontsize=32, align="center") #subtitle 

    if room_tracker == 1: #if the player has clicked once,
        screen.clear() #they'll see the first part of the story
        screen.fill("light blue")
        story1.draw() 
        arrow.draw()

    if room_tracker == 2:
        screen.clear() #same as above, but 2 clicks and more story.
        story2.draw()
        arrow.draw()

    if room_tracker == 3:
        screen.clear() #first actual room with a clue
        story3.draw() #placing the captain's bridge
        clue1.draw() #placing the captain's log within the room randomly (randomn position defined next to the actor line)
        arrow.draw()

    if clue1_tracker == 1: #if they've clicked on clue 1, create the info box regarding the clue.
        loginfo.draw()

    if room_tracker == 4: #the rest of these if statements follow a similar pattern
        screen.clear() #wipe the screen,
        story4.draw() #draw the scene,
        clue2.draw() #draw the clue,
        arrow.draw() #draw the continue arrow

    if clue2_tracker == 1:
        scheduleinfo.draw() #if they've clicked on the clue for this scene, give the info

    if room_tracker == 5:
        screen.clear()
        story5.draw()
        clue3.draw()
        arrow.draw()

    if clue3_tracker == 1:
        controllerinfo.draw()

    if room_tracker == 6:
        screen.clear()
        story6.draw()
        clue4.draw()
        arrow.draw()

    if clue4_tracker == 1:
        smartphoneinfo.draw()

    if room_tracker == 7:
        screen.clear()
        story7.draw()
        clue5.draw()
        arrow.draw()

    if clue5_tracker == 1:
        camerainfo.draw()

    if room_tracker == 8:
        screen.clear()
        screen.fill("gray")
        screen.draw.text("Evidence Summary.\n On the next screen you will choose which suspect did it, \n so read over any clues you might have forgotten.", fontsize=32, midtop = (400,0), align="center")
        if clue1_tracker >= 1: #if the player clicked on each clue,
            clue1_sum.draw() #draw that clue and its information on this summary page
        if clue2_tracker >= 1:
            clue2_sum.draw()
        if clue3_tracker >= 1:
            clue3_sum.draw()
        if clue4_tracker >= 1:
            clue4_sum.draw()
        if clue5_tracker >= 1:
            clue5_sum.draw()
        arrow.draw()

    if room_tracker == 9:
        screen.clear()
        screen.fill("dark red")
        screen.draw.text("Which suspect is the murderer?",fontsize = 48, center=(400,400) , align = "center")
        screen.draw.text("From left to right: \n The Captain, Martha, Harry, Darla, Michael", midtop=(400,125), fontsize = 40,align="center") 
        captain.draw() #if you look at the mouse click function, it'll show what happens when the player clicks on these drawings
        martha.draw()
        harry.draw()
        darla.draw()
        michael.draw()
        arrow.draw()
        
    if room_tracker == 10 and final_selection == 'darla': #if we're on screen 10 and you picked Darla as the murderer.... you win!!
        screen.clear()
        global time_elapsed
        end = time.time() #grabbing the time that the player finished the game at
        time_elapsed = end - start #calculating the time elapsed over the course of the game
        winner.draw() #this was without a doubt my favorite pixel art of any that I made for this game #here's our dictionary for pairing the winner's name with their time.
        screen.draw.text("Great work! \n You cracked the case and put Darla behind bars! \n After you hit continue, \n you'll be prompted to enter your name in the cmd window/shell for the scoreboard!", fontsize = 26 , midbottom=(400,675), align = "center", color = "yellow")
        arrow.draw()
    if room_tracker == 10 and final_selection != 'darla': #if we're on screen 10 and you picked someone besides Darla.. you picked the wrong person. Try again?
        screen.clear()
        screen.clear()
        loser.draw() #drawing the loss screen. 
        screen.draw.text("As you reflect on the case you worked on The Diamond, \n you can't help but feel like you chose wrong.", fontsize = 30, midbottom=(400,625), align="center", color = "orange")
        screen.draw.text("(You picked the wrong suspect. Better luck next time.)", fontsize = 30, midbottom=(400,690), align="center", color = "orange")
        #(Part of my plan here was to prompt a restart of the game, but the game kept locking up when I tried to utilize a while loop.)
        #(I'm not sure if this has to do with pgzero, but I could not get it where I wanted it, so I scrapped the reset button entirely.)
    if room_tracker == 11 and final_selection == 'darla':
        global winner_name
        global score
        screen.clear()
        screen.fill("light blue")
        screen.draw.text("SCOREBOARD", midtop = (400,0), fontsize = 64) #drawing the scoreboard using our DOTD_Scoreboard text file to import names and times.
        winner_name = input("Please type your name for the leaderboard! ") #the game may get stuck at the previous screen due to this input, but once you enter a name it should continue like normal.
        score = {winner_name:time_elapsed} #score dictionary 
        file = open('DOTD_Scoreboard.txt', 'a')
        for keys,values in score.items():
            file.write('%s : %.3f seconds \n' %(keys,values)) #writing to the leaderboard
        file.close()
        file2 = open('DOTD_Scoreboard.txt', 'r') #reading from the leaderboard
        height_addition = 0 #on each iteration of a name for the scoreboard, this variable will have some added to it so our names aren't on top of each other
        for line in file2: #for each line in the file....
            height_addition += 20 #adding 20 per iteration
            line = line.strip() #strip the lines of their \n's
            screen.draw.text(str(line), midtop=(400,(50+int(height_addition)))) #starting at 50 on the y, and adding our height additon for each new name
        file2.close()
    
pgzrun.go()
