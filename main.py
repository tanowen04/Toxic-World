# Programmed by Owen Tan
# IMPORTANT: PLEASE ZOOM OUT IN ORDER TO SEE THE ENTIRE SCREEN
# How to play:
# Use the WASD keys to control your character
# Press the Spacebar to inspect things about your surroundings
# When battling, use your mouse to click on the action that you character will perform
# Press the Spacebar to advance text
import pygame
from pygame import *
from replit import audio
import os
#from PIL import Image
import sys
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
init()
running = True
done = 0
name = ''
yesNo = ""
clock = pygame.time.Clock()
textFont = font.SysFont("Times New Roman",30)
direction = ''
xBattle1 = 0
yBattle1 = 0
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

# Character stats
mainHP = 100
mainMaxHP = 100
mainMP = 100
mainMaxMP = 100
mainAtk = 10
mainMag = 10
mainDef = 5

char2HP = 70
char2MaxHP = 70
char2MP = 120
char2MaxMP = 120
char2Atk = 5
char2Mag = 20
char2Def = 4

char3HP = 120
char3MaxHP = 120
char3MP = 110
char3MaxMP = 110
char3Atk = 8
char3Mag = 8
char3Def = 5

bossHP = 500

dead = []

mainBattle = 1
char2Battle = 0
char3Battle = 0
char4Battle = 0
# Colours
RED = (255, 0, 0)
DARKRED = (180, 0, 0)
DARKERRED = (50, 0, 0)
YELLOW = (255, 255, 0)
DARKYELLOW = (200, 200, 0)
DARKERYELLOW = (175, 175, 0)
ORANGE = (255, 128, 0)
PURPLE = (100, 0, 200)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
DARKBLUE = (0,0,130)
GREEN = (0, 255, 0)
DARKGREEN = (2.5,20,5)
WHITE = (255, 255, 255)
LIGHTGREY = (227, 227, 227)
LIGHTYGREY = (200, 200, 200)
GREY = (138, 138, 138)
DARKGREY = (70, 70, 70)
LIGHTBROWN = (174, 26, 26)
BROWN = (87, 13, 13)
DARKBROWN = (42, 6, 6)
NIGHT = (14, 0, 50)
NIGHTSHADOW = (7, 3, 25)
# Screen
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
display.flip()

# Images
garbageBag = image.load('garbagebag.png')
garbage = transform.scale(garbageBag, (50,50))

slimeMonster = image.load('Slime monster.png')
slimeMon = transform.scale(slimeMonster, (100,100))
slimeMonSmall = transform.scale(slimeMonster,(50,50))
boss = transform.scale(slimeMonster, (300,300))
bossSmall = transform.scale(slimeMonster, (150,150))

mainFront = image.load('Main character front.png')
mainFrontWalk = image.load('Main character front walk.png')
front = [mainFrontWalk, mainFront]
mainLeft= image.load('Main character left.png')
mainLeftWalk = image.load('Main character left walk.png')
left = [mainLeftWalk, mainLeft]
mainRight = image.load('Main character right.png')
mainRightWalk = image.load('Main character right walk.png')
right = [mainRightWalk, mainRight]
mainBack = image.load('Main character back.png')
mainBackWalk = image.load('Main character back walk.png')
back = [mainBackWalk, mainBack]
mainBattleRight = transform.scale(mainRight, (100,150))

character2Front = image.load('Char 2 Front.png')
character2FrontWalk = image.load('Char 2 Front Walk.png')
char2Front = [character2FrontWalk, character2Front]
character2Left = image.load('Char 2 Left.png')
character2LeftWalk = image.load('Char 2 Left Walk.png')
char2Left = [character2LeftWalk, character2Left]
character2Right = image.load('Char 2 Right.png')
character2RightWalk = image.load('Char 2 Right Walk.png')
char2Right = [character2RightWalk, character2Right]
character2Back = image.load('Char 2 Back.png')
character2BackWalk = image.load('Char 2 Back Walk.png')
char2Back = [character2BackWalk, character2Back]
char2BattleRight = transform.scale(character2Right, (100,150))

character3Front = image.load('char 3 front.png')
character3FrontWalk = image.load('char 3 front walk.png')
char3Front = [character3FrontWalk, character3Front]
character3Left = image.load('char 3 left.png')
character3LeftWalk = image.load('char 3 left walk.png')
char3Left = [character3LeftWalk, character3Left]
character3Right = image.load('char 3 right.png')
character3RightWalk = image.load('char 3 right walk.png')
char3Right = [character3RightWalk, character3Right]
character3Back = image.load('char 3 back.png')
character3BackWalk = image.load('char 3 back walk.png')
char3Back = [character3BackWalk, character3Back]
char3BattleRight = transform.scale(character3Right, (100,150))

punchImg = image.load('Punch.png')
punch1 = transform.scale(punchImg, (100,100))

# Tree pictures
largeTree1 = image.load('Large leafless tree.png')
skinnyTree1 = image.load("Skinny leafless tree.png")
largeTree = transform.scale(largeTree1, (150,165))
skinnyTree = transform.scale(skinnyTree1, (90,180))
giantTree1 = image.load("Giant tree.png")
giantTree = transform.scale(giantTree1, (300,300))

# Backgrounds
def startBackground(a):
    draw.rect(screen,DARKGREEN,(0,0,1000,700))
    if a == 1:
        screen.blit(slimeMonSmall, (650, 200))
    screen.blit(largeTree, (20,0))
    screen.blit(skinnyTree, (770,0))
    screen.blit(largeTree, (810,50))
    screen.blit(skinnyTree, (60,100))
    screen.blit(largeTree, (80,150))
    screen.blit(skinnyTree, (840,200))
    screen.blit(largeTree, (760,250))
    screen.blit(skinnyTree, (60,300))
    screen.blit(largeTree, (30,350))
    screen.blit(skinnyTree, (800,400))
    screen.blit(largeTree, (750,490))
    screen.blit(skinnyTree, (70,500))

def secBackground():
    draw.rect(screen,DARKGREEN,(0,0,1000,700))
    screen.blit(giantTree,(350,100))
    screen.blit(largeTree, (20,500))
    screen.blit(skinnyTree, (40,530))
    screen.blit(largeTree, (50,0))
    screen.blit(skinnyTree, (10,60))
    screen.blit(skinnyTree, (800,60))
    screen.blit(largeTree, (900,30))
    screen.blit(largeTree, (830,510))
    screen.blit(skinnyTree, (890,540))

def thirdBackground():
    draw.rect(screen,DARKGREEN,(0,0,1000,700))
    draw.rect(screen,BLUE,(800,0,200,700))

def fourthBackground():
    draw.rect(screen,DARKGREEN,(0,0,1000,700))
    draw.polygon(screen,GREY,((250,0),(750,0),(650,300),(350,300)))
    draw.circle(screen,BLACK,(500,200), 100)
    draw.rect(screen,BLACK,(400,200,200,100))

def fifthBackground():
    draw.rect(screen,DARKGREEN,(0,0,1000,700))

# Moves
mainAttackMoves = ["Punch", "Inspect"]
mainMagicMoves = []
char2AttackMoves = ["Punch"]
char2MagicMoves = ["Curse"]
char3AttackMoves = ["Punch"]
char3MagicMoves = ["Heal All", "Restore MP"]
punch = "Deals low physical damage to one enemy"
inspect = "Finds the enemy's weaknesses, element, and HP"
lunge = "Deals medium physical damage to one enemy"
curse = "Deals low dark damage to one enemy"
healAll = "Heals 30 HP to all allies"
restoreMP = "Restores 30 MP to the ally with the lowest MP"
defenceUp = "Increases the defence of one ally for the rest of the battle"
burn = "Deals low fire damage to one enemy"
# Items
bag = []
slimeHP = 100
slimeInspect = "HP:", slimeHP, "\tWeakness: Fire"
# Title screen background
def nuclearWaste(x,y,lx,ly):
    draw.rect(screen, BLACK, (x - 2, y - 2, lx + 4, ly + 4))
    draw.rect(screen, YELLOW, (x, y, lx, ly))
    lxthird = lx/3
    draw.rect(screen, DARKYELLOW, (x + lxthird*2, y, lxthird, ly))
    draw.line(screen, DARKERYELLOW, (x, y + (ly/3)), (x + lx, y + (ly/3)), 3)
    draw.line(screen, DARKERYELLOW, (x, y + (ly/3)*2), (x + lx, y + (ly/3)*2), 3)
    draw.circle(screen, BLACK, (x + (lx/2), y + (ly/2)), (lx/10))
    draw.polygon(screen, BLACK, [(x + (lx/10), y + (ly/4)*2), (x + (lx/3), y + (ly/5)), (x + (lx/2), y + (ly/2))])
    draw.polygon(screen, BLACK, [(x + (lx/10)*9, y + (ly/4)*2), (x + (lx/3)*2, y + (ly/5)), (x + (lx/2), y + (ly/2))])
    draw.polygon(screen, BLACK, [(x + (lx/7)*2, y + (ly/4)*3), (x + (lx/7)*5, y + (ly/4)*3), (x + (lx/2), y + (ly/2))])
    display.flip()
draw.rect(screen, BLACK, (0,0,1000,700))
display.flip()
# Title screen text
nightShadowR = 7
nightShadowG = 3
nightShadowB = 25
while nightShadowR != 255:
    titleFont = font.SysFont("Times New Roman",130)
    string = "My Game"    
    text = titleFont.render(string, 1, (nightShadowR, nightShadowG, nightShadowB))
    screen.blit(text, Rect(250, 100, 0, 0))
    display.flip()
    nightShadowR += 1
    nightShadowG -= 0.001
    nightShadowB -= 0.05
    time.wait(10)
nightShadowR = 7
nightShadowG = 3
nightShadowB = 25
while nightShadowB != 227:
    draw.rect(screen, (nightShadowR, nightShadowG, nightShadowB), (200, 350, 600, 250))
    nightShadowR += 1
    nightShadowG += 1
    nightShadowB += 1
    display.flip()
newGameFont = font.SysFont("Times New Roman",90)
string = "New Game"    
text = newGameFont.render(string, 1, BLACK)
screen.blit(text, Rect(290, 420, 0, 0))
display.flip()

# Allows the user to click on "New Game" and enter their name
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        
        if event.type == MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if x > 200 and x < 800 and y > 350 and y < 600:
                draw.rect(screen, BLACK, (0,0,1000,700))
                display.flip()
                nameFont = font.SysFont("Times New Roman",30)
                done += 1
                string = "Enter Your Name: "    
                text = nameFont.render(string, 1, WHITE)
                screen.blit(text, Rect(350, 150, 0, 0)) 
                display.flip()
        if event.type == pygame.KEYDOWN and done != 0 and event.key != 13:
            name += event.unicode
            if event.key == pygame.K_BACKSPACE:
                name = name[:-2]
                draw.rect(screen,BLACK,(580,150,1000,50))
            text = nameFont.render(name, 1, WHITE)
            screen.blit(text, Rect(580, 150, 0, 0)) 
            display.flip()
        if event.type == pygame.KEYDOWN and event.key == 13:
            string = "Are you sure your name is %s?" %name
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(280, 200, 0, 0))
            string = "YES     NO"
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(410, 250, 0, 0))             
            display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if x < 470 and x > 410 and y < 280 and y > 250:
                yesNo = "yes"
            elif x < 550 and x > 500 and y < 280 and y > 250:
                yesNo = "no"
        if yesNo == "yes":
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            running = False
        elif yesNo == "no":
            name = ""
            draw.rect(screen,BLACK, (0,0,1000,700))
            nameFont = font.SysFont("Times New Roman",30)
            string = "Enter Your Name: "
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(350, 150, 0, 0)) 
            display.flip()
            yesNo = ""
time.wait(2000)
draw.rect(screen,GREY,(20,500,960,180))
draw.rect(screen,LIGHTGREY,(30,510,940,160))
draw.rect(screen,GREY,(40,480,200,50))
draw.rect(screen,LIGHTGREY,(45,485,190,40))
display.flip()
characters = [name, "char2"]
def textBox(xyz, name1):
    string1 = ''
    string2 = ''
    running = True
    num = 0
    for i in xyz:
        draw.rect(screen,GREY,(20,500,960,180))
        draw.rect(screen,LIGHTGREY,(30,510,940,160))
        draw.rect(screen,GREY,(40,480,200,50))
        draw.rect(screen,LIGHTGREY,(45,485,190,40))
        text = textFont.render(name1, 1, BLACK)
        screen.blit(text, Rect(55, 490, 0, 0))
        findSpace = xyz[60:].find(" ")
        if num > 60 and len(string1) == findSpace + 60:
            string2 += i
            text = textFont.render(string1, 1, BLACK)
            screen.blit(text, Rect(80, 550, 0, 0))            
            text = textFont.render(string2, 1, BLACK)
            screen.blit(text, Rect(75, 590, 0, 0))
            time.wait(30)
            display.flip()
        else:
            string1 += i
            text = textFont.render(string1, 1, BLACK)
            screen.blit(text, Rect(80, 550, 0, 0))
            time.wait(30)
            display.flip()
        num += 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                sound = audio.play_file("Dialogue Skip Sound.wav")
                if event.unicode == " ":
                    running1 = True
                    while running1:
                        for event in pygame.event.get():
                            if event.type == KEYUP:
                                if event.unicode == " ":
                                    running = False
                                    running1 = False

# Battle function
def battleScreen(a,b,c,d,mon,num):
    xBattle = 0
    yBattle = 0
    xMonster = 600
    yMonster = 100
    numMon = num
    global mainHP
    global mainMaxHP
    global char2HP
    global char2MaxHP
    global mainMP
    global mainMaxMP
    global char2MP
    global char2MaxMP
    global char3HP
    global char3MaxHP
    global char3MP
    global char3MaxMP
    global dead
    global bossHP
    bossAttack = 15
    bossMusic = ''
    attackMenu = False
    magicMenu = False
    bagMenu = False
    slimeHP = 100
    numMonDead = 0
    numCharsBattle = []
    if a == 1:
        numCharsBattle.append(name)
    if b == 1:
        numCharsBattle.append("Xander")
    elif b == 2:
        numCharsBattle.append("???")
    if c == 1:
        numCharsBattle.append("Merisa")
    numCharsBattle.append(" ")
    bossMusic = audio.play_file("Final Boss tentative.mp3")
    # Character moving function
    def charAttackAnimation(a,b,c,d,i):
        xloc1 = 100
        xloc2 = 100
        xloc3 = 100
        xloc4 = 100
        # Draws the characters
        for f in range(21):
            ylocAttack = 20
            draw.rect(screen,BLACK,(0,0,300,420))
            if d == 1:
                quit()
            if c == 1:
                screen.blit(char3BattleRight, (xloc3,ylocAttack))
                ylocAttack += 100
            if b == 1 or b == 2:
                screen.blit(char2BattleRight, (xloc2,ylocAttack))
                ylocAttack += 100
            if a == 1:
                screen.blit(mainBattleRight, (xloc1,ylocAttack))
                ylocAttack += 100
            if i == name and f < 10:
                xloc1 += 10
                time.wait(20)
            elif i == name and f > 9:
                xloc1 -= 10
                time.wait(20)
            if i == "Xander" and f < 10 or i == "???" and f < 10:
                xloc2 += 10
                time.wait(20)
            elif i == "Xander" and f > 9 or i == "???" and f > 9:
                xloc2 -= 10
                time.wait(20)
            if i == "Merisa" and f < 10:
                xloc3 += 10
                time.wait(20)
            elif i == "Merisa" and f > 9:
                xloc3 -= 10
                time.wait(20)
            if i == "Char 4" and f < 10:
                xloc1 += 10
                time.wait(20)
            elif i == "Char 4" and f > 9:
                xloc1 -= 10
                time.wait(20)
            display.flip()
    #Gives the enemy an attack animation
    def enemyAttackAnimation(enemy,number,numChars,numMon):
        xMon1 = 600
        xMon2 = 780
        xMon3 = 600
        xMon4 = 780
        global mainHP
        global mainMaxHP
        global char2HP
        global char2MaxHP
        global mainMP
        global mainMaxMP
        global char2MP
        global char2MaxMP
        global char3HP
        global char3MaxHP
        global char3MP
        global char3MaxMP
        global dead
        global mainDef
        global mainHP
        global char2Def
        global char2HP
        global char3Def
        global char3HP
        global numCharsBattle
        global a
        global b
        global c
        global d
        global bossHP
        numCharsBattle = []
        if numChars == 1:
            numCharsBattle.append(name)
        if numChars == 2:
            numCharsBattle.append(name)
            numCharsBattle.append("Xander")
        if numChars == 3:
            numCharsBattle.append(name)
            numCharsBattle.append("Xander")
            numCharsBattle.append("Merisa")
        # Draws the enemy
        for g in range(numMon):
            for f in range(21):
                if enemy == "Slime":
                    yMon = 100
                    draw.rect(screen,BLACK,(500,0,500,400))
                    if numMon >= 1 and numMonDead == 0:
                        screen.blit(slimeMon, (xMon1,yMon))
                    if numMon >= 2 and numMonDead == 0 or numMonDead == 1:
                        screen.blit(slimeMon, (xMon2,yMon))
                        yMon += 150
                    if numMon >= 3 and numMonDead == 0 or numMonDead == 2 or numMonDead == 1:
                        screen.blit(slimeMon, (xMon3,yMon))
                    if numMon == 4 and numMonDead == 0 or numMonDead == 3 or numMonDead == 2 or numMonDead == 1:
                        screen.blit(slimeMon, (xMon4,yMon))
                    if g == 0 and f < 10 and numMonDead == 0:
                        xMon1 -= 5
                        time.wait(15)
                    elif g == 0 and f > 9 and numMonDead == 0:
                        xMon1 += 5
                        time.wait(15)
                    if g == 1 and f < 10 and numMonDead == 0 or g == 0 and numMonDead == 1 and f < 10:
                        xMon2 -= 5
                        time.wait(15)
                    elif g == 1 and f > 9 and numMonDead == 0 or g == 0 and numMonDead == 1 and f > 9:
                        xMon2 += 5
                        time.wait(15)
                    if g == 2 and f < 10 and numMonDead == 0 or g == 1 and numMonDead == 1 and f < 10 or g == 0 and numMonDead == 2 and f < 10:
                        xMon3 -= 5
                        time.wait(15)
                    elif g == 2 and f > 9 and numMonDead == 0 or g == 1 and numMonDead == 1 and f > 9 or g == 0 and numMonDead == 2 and f > 9:
                        xMon3 += 5
                        time.wait(15)
                    if g == 3 and f < 10 and numMonDead == 0 or g == 2 and numMonDead == 1 and f < 10 or g == 1 and numMonDead == 2 and f < 10 or g == 0 and numMonDead == 3 and f < 10:
                        xMon4 -= 5
                        time.wait(15)
                    elif g == 3 and f > 9 and numMonDead == 0 or g == 2 and numMonDead == 1 and f > 9 or g == 1 and numMonDead == 2 and f > 9 or g == 0 and numMonDead == 3:
                        xMon4 += 5
                        time.wait(15)
                    display.flip()
                if enemy == "Boss":
                    yMon = 100
                    draw.rect(screen,BLACK,(500,0,500,400))
                    screen.blit(boss, (xMon1,yMon))
                    if f < 10:
                        xMon1 += 7
                        time.wait(15)
                    if f > 9:
                        xMon1 -= 7
                        time.wait(15)
            enemyAttack = random.choice(numCharsBattle)
            if enemyAttack == "Slime" and enemy == "Slime":
                enemyAttack = random.choice(numCharsBattle)
            if enemyAttack == "Slime" and enemy == "Boss":
                mainHP -= (bossAttack - mainDef)
                char2HP -= (bossAttack - mainDef)
                char3HP -= (bossAttack - char3Def)
            if enemyAttack == name and enemy == "Slime":
                enemyAttackPower = 10 - mainDef
                mainHP -= enemyAttackPower
            if enemyAttack == name and enemy == "Boss":
                mainHP -= (bossAttack*1.5 - mainDef)
            if enemyAttack == "???" and enemy == "Slime" or enemyAttack == "Xander" and mon == "Slime":
                enemyAttackPower = 10 - char2Def
                char2HP -= enemyAttackPower
            if enemyAttack == "Xander" and enemy == "Boss":
                char2HP -= (bossAttack*1.5 - char2Def)
            if enemyAttack == "Merisa" and enemy == "Slime":
                char3HP -= (10 - char3Def)
            if enemyAttack == "Merisa" and enemy == "Boss":
                char3HP -= (bossAttack*1.5 - char3Def)
      
    # Battle beginning animation
    for i in range(71):
        draw.rect(screen,BLACK,(xBattle,yBattle,100,100))
        display.flip()
        xBattle += 100
        if xBattle == 1000:
            yBattle += 100
            xBattle = 0
        time.wait(20)    
    battleFont = font.SysFont("Times New Roman",30)
    battleFontSmall = font.SysFont("Times New Roman",15)
    running3 = True
    # Writes the different actions you can do during the fight
    while running3:
        if mon == "Boss" and bossHP <= 0:
            running3 = False
            running2 = False
        if slimeHP <= 0 and num == 1:
            running3 = False
            running2 = False
        elif slimeHP <= 0 and num != 1:
            running2 = True
            slimeHP = 100
            numMonDead += 1
            numMon -= 1
            num -= 1
        numCharsBattle = []
        
        # Makes a list for the battle sequence. First person on the list goes first, second person goes second etc
        if a == 1 and dead.count(name) != 1:
            numCharsBattle.append(name)
        if b == 1 and dead.count("Xander") != 1:
            numCharsBattle.append("Xander")
        elif b == 2:
            numCharsBattle.append("???")
        if c == 1:
            numCharsBattle.append("Merisa")
        if mon == "Slime":
            numCharsBattle.append("Slime")
        ylocation = 20
        xlocationName = 50
        if numCharsBattle[0] == "Slime":
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            nightShadowR = 7
            nightShadowG = 3
            nightShadowB = 25
            while nightShadowR != 255:
                titleFont = font.SysFont("Times New Roman",130)
                string = "Game Over"    
                text = titleFont.render(string, 1, (nightShadowR, nightShadowG, nightShadowB))
                screen.blit(text, Rect(240, 100, 0, 0))
                display.flip()
                nightShadowR += 1
                nightShadowG -= 0.001
                nightShadowB -= 0.05
                time.wait(10)
            time.wait(2000)
            quit()
        # Draws the character's HP and MP bars
        for i in numCharsBattle:
            ylocation = 20
            xlocationName = 50
            draw.rect(screen,BLACK,(0,0,1000,700))
            if d == 1:
                quit()
            if c == 1:
                screen.blit(char3BattleRight, (100,ylocation))
                display.flip()
                ylocation += 100
            if b == 1 or b == 2:
                screen.blit(char2BattleRight, (100,ylocation))
                display.flip()
                ylocation += 100
            if a == 1:
                screen.blit(mainBattleRight, (100,ylocation))
                display.flip()
                ylocation += 100
            # Draws the character's HP and MP bars
            if a == 1:
                draw.rect(screen,GREY,(xlocationName,420,200,90))
                draw.rect(screen,LIGHTGREY,(xlocationName+5,425,190,90))
                string = name    
                text = battleFont.render(string, 1, BLACK)
                screen.blit(text, Rect(xlocationName+15, 430, 0, 0))
                string = "HP: %i/%i MP: %i/%i" %(mainHP, mainMaxHP, mainMP, mainMaxMP)
                text = battleFontSmall.render(string, 1, BLACK)
                screen.blit(text, Rect(65, 460, 0, 0))
                xlocationName += 200
                display.flip()
            if b == 1:
                string = "Xander"
                draw.rect(screen,GREY,(xlocationName,420,200,90))
                draw.rect(screen,LIGHTGREY,(xlocationName+5,425,190,75))
                text = battleFont.render(string, 1, (0, 0, 0))
                screen.blit(text, Rect(xlocationName+15, 430, 0, 0))
                string = "HP: %i/%i MP: %i/%i" %(char2HP, char2MaxHP, char2MP, char2MaxMP)
                text = battleFontSmall.render(string, 1, BLACK)
                screen.blit(text, Rect(xlocationName+15, 460, 0, 0))   
                xlocationName += 200
            elif b == 2:
                string = "???"
                draw.rect(screen,GREY,(xlocationName,420,200,90))
                draw.rect(screen,LIGHTGREY,(xlocationName+5,425,190,75))
                text = battleFont.render(string, 1, (0, 0, 0))
                screen.blit(text, Rect(xlocationName+15, 430, 0, 0))
                string = "HP: %i/%i MP: %i/%i" %(char2HP, char2MaxHP, char2MP, char2MaxMP)
                text = battleFontSmall.render(string, 1, BLACK)
                screen.blit(text, Rect(xlocationName+15, 460, 0, 0))
                xlocationName += 200   
                display.flip()
            if c == 1:
                string = "Merisa"
                draw.rect(screen,GREY,(xlocationName,420,200,90))
                draw.rect(screen,LIGHTGREY,(xlocationName+5,425,190,75))
                text = battleFont.render(string, 1, (0, 0, 0))
                screen.blit(text, Rect(xlocationName+15, 430, 0, 0))
                string = "HP: %i/%i MP: %i/%i" %(char3HP, char3MaxHP, char3MP, char3MaxMP)
                text = battleFontSmall.render(string, 1, BLACK)
                screen.blit(text, Rect(xlocationName+15, 460, 0, 0))
                xlocationName += 200   
                display.flip()
            draw.rect(screen,BLACK,(600,100,400,300))
            draw.rect(screen,GREY,(10,500,980,190))
            draw.rect(screen,LIGHTGREY,(20,510,960,170))
            display.flip()

            # If all enemies are dead, the function stops
            if slimeHP <= 0 and num == 1:
                running3 = False
                running2 = False
            elif slimeHP <= 0 and num != 1:
                running2 = True
                slimeHP = 100
                numMonDead += 1
                numMon -= 1
                num -= 1
            if numMonDead == 0:
                xMonster = 600
                yMonster = 100
            if numMonDead == 1:
                xMonster = 780
                yMonster = 100
            if numMonDead == 2:
                xMonster = 600
                yMonster = 250
            if numMonDead == 3:
                yMonster = 780
                yMonster = 250
            
            # Draws the enemies
            if mon == "Slime":
                for l in range(num):
                    screen.blit(slimeMon, (xMonster,yMonster))
                    display.flip()
                    if xMonster == 600:
                        xMonster += 180
                    elif xMonster == 780:
                        xMonster = 600
                        yMonster += 150
            if mon == "Boss":
                screen.blit(boss, (600,100))
                display.flip()
            if numMonDead == 0:
                xMonster = 600
                yMonster = 100
            if numMonDead == 1:
                xMonster = 780
                yMonster = 100
            if numMonDead == 2:
                xMonster = 600
                yMonster = 250
            if numMonDead == 3:
                yMonster = 780
                yMonster = 250
            battleMenu = True
            running2 = True

            #Ends the battle if the enemies HP is 0
            while running2:
                if bossHP <= 0 and mon == "Boss":
                    running3 = False
                    running2 = False
                if slimeHP <= 0 and num == 1:
                    running3 = False
                    running2 = False
                elif slimeHP <= 0 and num != 1:
                    running2 = True
                    slimeHP = 100
                    numMonDead += 1
                    numMon -= 1
                    num -= 1
                if i == "Slime":
                    running2 = False
                for event in pygame.event.get(): 
                    if event.type == QUIT:
                        bossMusic.set_paused(True)
                    # Opens the battle menu                
                    if battleMenu == True:
                        string = i + "'s turn"
                        text = battleFont.render(string, 1, BLACK)
                        screen.blit(text, Rect(40, 520, 0, 0))
                        string = "Attack"
                        text = battleFont.render(string, 1, BLACK)
                        screen.blit(text, Rect(820, 520, 0, 0))
                        string = "Magic"
                        text = battleFont.render(string, 1, BLACK)
                        screen.blit(text, Rect(820, 560, 0, 0))       
                        string = "Bag"
                        text = battleFont.render(string, 1, BLACK)
                        screen.blit(text, Rect(820, 600, 0, 0))       
                        string = "Run"
                        text = battleFont.render(string, 1, BLACK)
                        screen.blit(text, Rect(820, 640, 0, 0))       
                        display.flip()

                    #Says different things when you hover over them in the menu        
                    if event.type == MOUSEMOTION and battleMenu == True:
                        (x, y) = pygame.mouse.get_pos()                   
                        if x < 920 and x > 820 and y < 550 and y > 520:  
                            string = "Attack: Moves that deal damage that scale with the user's attack power"
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(40, 560, 0, 0))
                            display.flip()
                        elif x < 900 and x > 820 and y < 590 and y > 560: 
                            string = "Magic: Moves that scale with the user's magic power and waste MP"
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(40, 560, 0, 0))
                            display.flip()
                        elif x < 870 and x > 820 and y < 630 and y > 600:
                            string = "Bag: Use items that restore HP, MP, or have other benefits"
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(40, 560, 0, 0))
                            display.flip()
                        elif x < 870 and x > 820 and y < 670 and y > 640:  
                            string = "Run: Run away from enemies"
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(40, 560, 0, 0))
                            display.flip()
                        else:
                            draw.rect(screen,LIGHTGREY,(20,550,800,120))
                            display.flip()
                    # Opens the different menus
                    if event.type == MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()   
                        xlocMoves = 75
                        ylocMoves = 530
                        # Opens the attack menu
                        if x < 920 and x > 820 and y < 550 and y > 520:
                            attackMenu = True
                            magicMenu = False
                            bagMenu = False
                            battleMenu = False
                            draw.rect(screen,LIGHTGREY,(20,510,960,170))
                            attackNum = 0
                            draw.rect(screen,BLACK,(35,525,30,10))
                            draw.polygon(screen,BLACK,((25,530),(40,519),(40,540)))

                            # Writes out all the moves that they can perform
                            if i == name:
                                for j in mainAttackMoves:
                                    string = mainAttackMoves[attackNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if attackNum == 0 or attackNum == 2:
                                        xlocMoves += 500
                                    if attackNum == 1 or attackNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    attackNum += 1
                                    display.flip()
                            if i == "Xander" or i == "???":
                                for j in char2AttackMoves:
                                    string = char2AttackMoves[attackNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if attackNum == 0 or attackNum == 2:
                                        xlocMoves += 500
                                    if attackNum == 1 or attackNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    attackNum += 1
                                    display.flip()
                            if i == "Merisa":
                                for j in char3AttackMoves:
                                    string = char3AttackMoves[attackNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if attackNum == 0 or attackNum == 2:
                                        xlocMoves += 500
                                    if attackNum == 1 or attackNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    attackNum += 1
                                    display.flip()
                            xlocMoves = 75
                            ylocMoves = 530
                            
                        # Returns to the battle menu
                        if x < 65 and x > 25 and y < 540 and y > 520 and attackMenu == True or x < 65 and x > 25 and y < 540 and y > 520 and magicMenu == True or x < 65 and x > 25 and y < 540 and y > 520 and bagMenu == True:
                            battleMenu = True
                            attackMenu = False
                            magicMenu = False
                            bagMenu = False
                            draw.rect(screen,LIGHTGREY,(20,510,960,170))
                            display.flip()
                            
                        # Opens the magic menu                  
                        if x < 920 and x > 820 and y < 590 and y > 560:
                            magicMenu = True
                            attackMenu = False
                            bagMenu = False
                            battleMenu = False
                            draw.rect(screen,LIGHTGREY,(20,510,960,170))
                            magicNum = 0
                            draw.rect(screen,BLACK,(35,525,30,10))
                            draw.polygon(screen,BLACK,((25,530),(40,519),(40,540)))

                            # Writes out all the moves they can perform
                            if i == name:
                                for i in mainMagicMoves:
                                    string = mainMagicMoves[magicNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if magicNum == 0 or magicNum == 2:
                                        xlocMoves += 500
                                    if magicNum == 1 or magicNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    magicNum += 1
                                    display.flip()
                                if len(mainMagicMoves) == 0:
                                    string = "You have no magic moves"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(75, 530, 0, 0))
                            if i == "Xander" or i == "???":
                                for j in char2MagicMoves:
                                    string = char2MagicMoves[magicNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if magicNum == 0 or magicNum == 2:
                                        xlocMoves += 500
                                    if magicNum == 1 or magicNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    magicNum += 1
                                    display.flip()
                            if i == "Merisa":
                                for j in char3MagicMoves:
                                    string = char3MagicMoves[magicNum]
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(xlocMoves, ylocMoves, 0, 0))
                                    if magicNum == 0 or magicNum == 2:
                                        xlocMoves += 500
                                    if magicNum == 1 or magicNum == 3:
                                        ylocMoves += 70
                                        xlocMoves = 75
                                    magicNum += 1
                                    display.flip()
                            xlocMoves = 75
                            ylocMoves = 530
                        
                        # Bag
                        if x < 920 and x > 820 and y < 630 and y > 600:
                            magicMenu = False
                            attackMenu = False
                            bagMenu = True
                            battleMenu = False
                            draw.rect(screen,LIGHTGREY,(20,510,960,170))
                            draw.rect(screen,BLACK,(35,525,30,10))
                            draw.polygon(screen,BLACK,((25,530),(40,519),(40,540)))
                            #Counting the number of potions you have
                            numHP = bag.count("HP Potion")
                            numMP = bag.count("MP Potion")
                            numRev = bag.count("Revival Potion")
                            string = "HP Potion (%i)" %numHP
                            text = battleFont.render(string, 1, BLACK)
                            screen.blit(text, Rect(75, 530, 0, 0))
                            string = "MP Potion (%i)" %numMP
                            text = battleFont.render(string, 1, BLACK)
                            screen.blit(text, Rect(575, 530, 0, 0))
                            string = "Revival Potion (%i)" %numRev
                            text = battleFont.render(string, 1, BLACK)
                            screen.blit(text, Rect(75, 600, 0, 0))
                        xlocMoves = 75
                        ylocMoves = 530
                    
                        # Run
                        if x < 920 and x > 820 and y < 670 and y > 640:
                            if b != 2 and mon != "Boss":
                                #Gives you a chance of not being able to run away
                                runChance = random.choice(["Run", "Trapped"])
                                if runChance == "Run":
                                    draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                    string = "You ran away successfully!"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(75, 530, 0, 0))
                                    display.flip()
                                    time.wait(2000)
                                    draw.rect(screen,BLACK,(0,0,1000,700))
                                    display.flip()
                                    bossMusic.set_paused(True)
                                    return
                                else:
                                    draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                    string = "You can't escape!"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(75, 530, 0, 0))
                                    display.flip()
                                    time.wait(2000)
                                    running2 = False

                    # Attack menu
                    if attackMenu == True and event.type == MOUSEMOTION:
                        (x,y) = pygame.mouse.get_pos()
                        if x > 75 and x < 175 and y > 530 and y < 560:
                            string = punch
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(75, 575, 0, 0))  
                            display.flip()
                        elif x > 575 and x < 675 and y > 530 and y < 560:
                            if mainAttackMoves[1] == "Inspect" and i == name:
                                string = inspect
                            elif mainAttackMoves[1] == "Lunge" and i == name:
                                string = lunge
                            else:
                                string = ''
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(575, 575, 0, 0))  
                            display.flip()                  
                        else:
                            draw.rect(screen,LIGHTGREY,(75,575,900,30))
                            draw.rect(screen,LIGHTGREY,(75,645,900,30))
                            display.flip()
                            
                    # Attack Moves
                    if attackMenu == True and event.type == MOUSEBUTTONDOWN:
                        (x,y) = pygame.mouse.get_pos()
                        if x > 75 and x < 175 and y > 530 and y < 560:
                            # Makes the characters punch
                            if i == name:
                                if mainAttackMoves[0] == "Punch":
                                    if mon == "Slime":
                                        slimeHP -= mainAtk
                                        charAttackAnimation(a,b,c,d,i)
                                        punchSound = audio.play_file("Punch sound game.wav")
                                        screen.blit(punch1, (xMonster,yMonster))
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        text = battleFont.render(str(mainAtk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 100, yMonster, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False 
                                    if mon == "Boss":
                                        bossHP -= mainAtk
                                        charAttackAnimation(a,b,c,d,i)
                                        punchSound = audio.play_file("Punch sound game.wav")
                                        screen.blit(punch1, (xMonster + 90,yMonster + 100))
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        text = battleFont.render(str(mainAtk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 200, yMonster + 10, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False                               
                            if i == "Xander" or i == "???":
                                if  char2AttackMoves[0] == "Punch":
                                    if mon == "Slime":
                                        charAttackAnimation(mainBattle,char2Battle,char3Battle,char4Battle,i)
                                        slimeHP -= char2Atk
                                        screen.blit(punch1, (xMonster,yMonster))
                                        display.flip()
                                        audio.play_file("Punch sound game.wav")
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        text = battleFont.render(str(char2Atk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 100, yMonster, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False
                                    if mon == "Boss":
                                        bossHP -= char2Atk
                                        charAttackAnimation(a,b,c,d,i)
                                        punchSound = audio.play_file("Punch sound game.wav")
                                        screen.blit(punch1, (xMonster + 90,yMonster + 100))
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        text = battleFont.render(str(mainAtk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 200, yMonster + 10, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False    

                            if i == "Merisa":
                                if char3AttackMoves[0] == "Punch":
                                    if mon == "Slime":
                                        charAttackAnimation(mainBattle,char2Battle,char3Battle,char4Battle,i)
                                        slimeHP -= char3Atk
                                        punchSound = audio.play_file("Punch sound game.wav")
                                        screen.blit(punch1, (xMonster,yMonster))
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        text = battleFont.render(str(char3Atk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 100, yMonster, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False
                                    if mon == "Boss":
                                        bossHP -= char3Atk
                                        charAttackAnimation(a,b,c,d,i)
                                        punchSound = audio.play_file("Punch sound game.wav")
                                        screen.blit(punch1, (xMonster + 90,yMonster + 100))
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        text = battleFont.render(str(char3Atk), 1, (RED))
                                        screen.blit(text, Rect(xMonster + 200, yMonster + 10, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        display.flip()
                                        running2 = False
                                        attackMenu = False    

                        if x > 575 and x < 675 and y > 530 and y < 560:
                            # Allows you to inspect the enemy to see their weaknesses and HP
                            if i == name:
                                if mainAttackMoves[1] == "Inspect":
                                    if mon == "Slime":
                                        draw.rect(screen,GREY,(10,500,980,190))
                                        draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                        string = "HP: %i   Weakness: Fire" %slimeHP
                                        text = battleFont.render(string, 1, BLACK)
                                        screen.blit(text, Rect(60, 540, 0, 0))
                                        display.flip()
                                        time.wait(3000)
                                        running2 = False
                                        attackMenu = False
                                    if mon == "Boss":
                                        draw.rect(screen,GREY,(10,500,980,190))
                                        draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                        string = "HP: %i   Weakness: None" %bossHP
                                        text = battleFont.render(string, 1, BLACK)
                                        screen.blit(text, Rect(60, 540, 0, 0))
                                        display.flip()
                                        time.wait(3000)
                                        running2 = False
                                        attackMenu = False          
                            
                    # Magic menu
                    if magicMenu == True and event.type == MOUSEMOTION:
                        (x,y) = pygame.mouse.get_pos()
                        if x > 75 and x < 175 and y > 530 and y < 560:
                            # Says different things when you hover over an item in the list of magic moves
                            if char2MagicMoves[0] == "Curse" and i == "Xander" or char2MagicMoves[0] == "Curse" and i == "???":
                                string = curse
                            if i == "Merisa":
                                string = healAll
                            if len(mainMagicMoves) != 0:
                                if i == name and mainMagicMoves[0] == "Burn":
                                    string = burn
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(75, 575, 0, 0))  
                            display.flip()
                        elif x > 575 and x < 675 and y > 530 and y < 560:
                            if i == "Merisa":
                                string = restoreMP
                            text = battleFontSmall.render(string, 1, BLACK)
                            screen.blit(text, Rect(575, 575, 0, 0))  
                            display.flip()
                        else:
                            draw.rect(screen,LIGHTGREY,(75,575,900,30))
                            draw.rect(screen,LIGHTGREY,(75,645,900,30))
                            display.flip()
                            
                    # Magic Moves
                    if magicMenu == True and event.type == MOUSEBUTTONDOWN:
                        (x,y) = pygame.mouse.get_pos()
                        if x > 75 and x < 175 and y > 530 and y < 560:
                            # Allows the characters to perform magic attacks
                            if i == name and mainMP >= 20:
                                if mon == "Slime":
                                    charAttackAnimation(mainBattle,char2Battle,char3Battle,char4Battle,i)
                                    slimeHP -= (mainMag*2)
                                    draw.circle(screen,ORANGE,(xMonster + 50, yMonster + 50), 60)
                                    display.flip()
                                    time.wait(300)
                                    draw.circle(screen,BLACK,(xMonster + 50, yMonster + 50), 60)
                                    screen.blit(slimeMon, (xMonster,yMonster))
                                    text = battleFont.render(str(char2Mag), 1, (ORANGE))
                                    screen.blit(text, Rect(xMonster + 100, yMonster, 0, 0)) 
                                    display.flip()
                                    time.wait(300)
                                    draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                    screen.blit(slimeMon, (xMonster,yMonster))
                                    display.flip()
                                if mon == "Boss":
                                    bossHP -= mainMag*1.5
                                    draw.circle(screen,ORANGE,(730, 250), 60)
                                    display.flip()
                                    time.wait(300)
                                    screen.blit(boss, (xMonster,yMonster))
                                    text = battleFont.render(str(char2Mag), 1, (ORANGE))
                                    screen.blit(text, Rect(xMonster + 200, yMonster + 50, 0, 0)) 
                                    display.flip()
                                    time.wait(300)
                                    screen.blit(boss, (xMonster,yMonster))
                                    display.flip()
                                mainMP -= 20
                                running2 = False
                                magicMenu = False
                            if i == "Merisa" and char3MP >= 40:
                                for i in range(30):
                                    if mainHP != mainMaxHP:
                                        mainHP += 1
                                for i in range(30):
                                    if char2HP != char2MaxHP:
                                        char2HP += 1
                                for i in range(30):
                                    if char3HP != char3MaxHP:
                                        char3HP += 1
                                char3MP -= 40
                                running2 = False
                                magicMenu = False
                            elif i == "Merisa" and char3MP < 40:
                                draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                string = "You do not have enough MP!"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(75, 530, 0, 0))  
                                display.flip()
                                time.wait(2000)
                                magicMenu = False
                                draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                string = i + "'s turn"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(40, 520, 0, 0))
                                string = "Attack"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 520, 0, 0))
                                string = "Magic"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 560, 0, 0))       
                                string = "Bag"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 600, 0, 0))       
                                string = "Run"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 640, 0, 0))       
                                display.flip()
                            if i == "Xander" or i == "???":
                                if char2MagicMoves[0] == "Curse" and char2MP >= 20:
                                    if mon == "Slime":
                                        charAttackAnimation(mainBattle,char2Battle,char3Battle,char4Battle,i)
                                        slimeHP -= char2Mag
                                        draw.circle(screen,PURPLE,(xMonster + 50, yMonster + 50), 60)
                                        display.flip()
                                        time.wait(300)
                                        draw.circle(screen,BLACK,(xMonster + 50, yMonster + 50), 60)
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        text = battleFont.render(str(char2Mag), 1, (PURPLE))
                                        screen.blit(text, Rect(xMonster + 100, yMonster, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        draw.rect(screen,BLACK,(xMonster,yMonster,150,150))
                                        screen.blit(slimeMon, (xMonster,yMonster))
                                        display.flip()
                                        char2MP -= 20
                                        running2 = False
                                        magicMenu = False
                                    else:
                                        charAttackAnimation(mainBattle,char2Battle,1,char4Battle,i)
                                        bossHP -= char2Mag
                                        draw.circle(screen,PURPLE,(730, 250), 60)
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        text = battleFont.render(str(char2Mag), 1, (PURPLE))
                                        screen.blit(text, Rect(xMonster + 200, yMonster + 50, 0, 0)) 
                                        display.flip()
                                        time.wait(300)
                                        screen.blit(boss, (xMonster,yMonster))
                                        display.flip()
                                        char2MP -= 20
                                        running2 = False
                                        magicMenu = False
                                elif char2MagicMoves[0] == "Curse" and char2MP < 20:
                                    draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                    string = "You do not have enough MP!"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(75, 530, 0, 0))  
                                    display.flip()
                                    time.wait(2000)
                                    magicMenu = False
                                    draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                    string = i + "'s turn"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(40, 520, 0, 0))
                                    string = "Attack"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(820, 520, 0, 0))
                                    string = "Magic"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(820, 560, 0, 0))       
                                    string = "Bag"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(820, 600, 0, 0))       
                                    string = "Run"
                                    text = battleFont.render(string, 1, BLACK)
                                    screen.blit(text, Rect(820, 640, 0, 0))       
                                    display.flip()
                        if x > 575 and x < 675 and y > 530 and y < 560:
                            if i == "Merisa" and char3MP >= 20:
                                if char3MP < mainMP and char3MP < char2MP:
                                    char3MP += 40
                                elif char2MP < mainMP:
                                    char2MP += 40
                                else:
                                    mainMP += 40
                                char3MP -= 20
                                running2 = False
                                magicMenu = False
                            elif i == "Merisa" and char3MP < 20:
                                draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                string = "You do not have enough MP!"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(75, 530, 0, 0))  
                                display.flip()
                                time.wait(2000)
                                magicMenu = False
                                draw.rect(screen,LIGHTGREY,(20,510,960,170))
                                string = i + "'s turn"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(40, 520, 0, 0))
                                string = "Attack"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 520, 0, 0))
                                string = "Magic"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 560, 0, 0))       
                                string = "Bag"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 600, 0, 0))       
                                string = "Run"
                                text = battleFont.render(string, 1, BLACK)
                                screen.blit(text, Rect(820, 640, 0, 0))       
                                display.flip()
                    # Bag menu
                    if bagMenu == True and event.type == MOUSEBUTTONDOWN:
                        (x,y) = pygame.mouse.get_pos()
                        if x > 75 and x < 175 and y > 530 and y < 560 and numHP != 0:
                            if i == name:
                                for k in range(30):
                                    if mainHP != mainMaxHP:
                                        mainHP += 1
                            if i == "Xander" or i == "???":
                                for k in range(30):
                                    if char2HP != char2MaxHP:
                                        char2HP += 1
                            if i == "Merisa":
                                for k in range(30):
                                    if char3HP != char3MaxHP:
                                        char3HP += 1
                            bag.remove("HP Potion")
                            running2 = False
                            bagMenu = False
                        elif x > 575 and x < 675 and y > 530 and y < 560 and numMP != 0:
                            bag.remove("MP Potion")
                            if i == name:
                                for k in range(50):
                                    if mainMP != mainMaxMP:
                                        mainMP += 1
                            if i == "Xander" or i == "???":
                                for k in range(50):
                                    if char2MP != char2MaxMP:
                                        char2MP += 1
                            if i == "Merisa":
                                for k in range(50):
                                    if char3MP != char3MaxMP:
                                        char3MP += 1
                            running2 = False
                            bagMenu = False
                        elif x > 75 and x < 175 and y > 600 and y < 630 and numRev != 0:
                            bag.remove("Revival Potion")
                            if dead[0] == name:
                                mainHP = 100
                                a = 1
                            if dead[0] == "Xander":
                                char2HP = 70
                                b = 1
                            if dead[0] == "Merisa":
                                char3HP = 110
                                c = 1
                            running2 = False
                            bagMenu = False     
                        else:
                            draw.rect(screen,LIGHTGREY,(75,575,900,25))
                            draw.rect(screen,LIGHTGREY,(75,645,900,25))
                            display.flip()
        enemyAttackAnimation(mon, num, a + b + c + d, numMon)
        if mainHP <= 0 and a == 1:
            a = 0
            dead.append(name)
        if char2HP <= 0 and b == 1:
            b = 0
            dead.append("Xander")
        if char3HP <= 0 and c == 1:
            c = 0
            dead.append("Merisa")
    bossMusic.set_paused(True)
    draw.rect(screen,GREY,(10,500,980,190))
    draw.rect(screen,LIGHTGREY,(20,510,960,170))
    display.flip()
    time.wait(500)
    draw.rect(screen,BLACK,(500,0,500,400))
    display.flip()
    draw.rect(screen,GREY,(10,500,980,190))
    draw.rect(screen,LIGHTGREY,(20,510,960,170))
    string = "You Won!"
    text = battleFont.render(string, 1, BLACK)
    screen.blit(text, Rect(60, 540, 0, 0))
    display.flip()
    time.wait(3000)
    draw.rect(screen,BLACK,(0,0,1000,700))
    display.flip()
                    
# Game begins
mainBattle = 1
char2Battle = 1
char3Battle = 0
char4Battle = 0
textBox("Where am I?", name)
draw.rect(screen, BLACK, (0,0,1000,700))
display.flip()
time.wait(2000)
# main character looks around
startBackground(1)
screen.blit(mainFront, (500,350))
display.flip()
time.wait(1000)
startBackground(1)
screen.blit(mainLeft, (500,350))
display.flip()
time.wait(1000)
startBackground(1)
screen.blit(mainRight, (500,350))
display.flip()
time.wait(1000)
startBackground(1)
screen.blit(mainFront, (500,350))
display.flip()
time.wait(1000)
# Dialogue
textBox("I'm in some type of forest.", name)
textBox("I'd better look around.", name)
textBox("Use the WASD keys to move and the SPACE key to interact.", "Game")
startBackground(1)
screen.blit(mainFront,(500,350))
display.flip()
xloc = 500
yloc = 350
button = 0
running = True
# Allows you to walk around
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and xloc < 300 or event.type == KEYDOWN and xloc > 700:
            # Allows you to investigate the trees by pressing the space button while near them
            if event.unicode == " ":
                textBox("These trees are dry and shriveled.", name)
                textBox("I haven't seen a real tree in a long time.", name)
                startBackground(1)
                screen.blit(mainFront, (xloc,yloc))
                display.flip()
        if event.type == KEYDOWN and xloc < 700 and xloc > 620 and yloc < 250 and yloc > 170:
            if event.unicode == " ":
                for i in range(71):
                    draw.rect(screen,BLACK,(xBattle1,yBattle1,100,100))
                    display.flip()
                    xBattle1 += 100
                    if xBattle1 == 1000:
                        yBattle1 += 100
                        xBattle1 = 0
                    time.wait(20)
                moveUp = False
                moveDown = False
                moveRight = False
                moveLeft = False
                running = False
        if event.type == QUIT:
            running1 = False
        if event.type == KEYDOWN:  
            if event.unicode == "a":
                moveLeft = True
            if event.unicode == "d":
                moveRight = True
            if event.unicode == "s":
                moveDown = True
            if event.unicode == "w":
                moveUp = True
        if event.type == KEYUP:
            if event.key == 97:
                moveLeft = False
            if event.key == 100:
                moveRight = False
            if event.key == 119:
                moveUp = False
            if event.key == 115:
                moveDown = False
    if moveLeft == True and xloc >= 240:
        for i in left:
            startBackground(1)
            display.flip()
            screen.blit(i, (xloc,yloc))
            display.flip()
            time.wait(150)
            xloc -= 10
    if moveRight == True and xloc <= 730:
        for i in right:
            startBackground(1)
            display.flip()
            screen.blit(i, (xloc,yloc))
            display.flip()
            time.wait(150)
            xloc += 10
    if moveUp == True and yloc >= 0:
        for i in back:
            startBackground(1)
            display.flip()
            screen.blit(i, (xloc,yloc))
            display.flip()
            time.wait(150)
            yloc -= 10
    if moveDown == True and yloc <= 660:
        for i in front:
            startBackground(1)
            display.flip()
            screen.blit(i, (xloc,yloc))
            display.flip()
            time.wait(150) 
            yloc += 10  
time.wait(500)
screen.blit(mainBattleRight, (100,120))
screen.blit(slimeMon, (700,120))
display.flip()
time.wait(1000)
# Character finds a slime
textBox("Huh?", name)
textBox("What is this thing?", name)
textBox("Hey! Watch out!", "???")
char2Battle = 2
textBox("?", name)
# Character 2 appears
draw.rect(screen,BLACK,(0,0,1000,700))
screen.blit(char2BattleRight, (100,20))
screen.blit(mainBattleRight, (100,120))
screen.blit(slimeMon, (700,120))
display.flip()
textBox("Who are you?", name)
textBox("We'll talk later, for now, we should get rid of this.", "???")
draw.rect(screen,BLACK,(0,0,1000,700))
screen.blit(char2BattleRight, (100,20))
screen.blit(mainBattleRight, (100,120))
screen.blit(slimeMon, (700,120))
battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",1)
time.wait(1000)
startBackground(0)
screen.blit(mainLeft, (xloc,yloc))
xloc2 = xloc - 60
yloc2 = yloc
screen.blit(character2Right, (xloc2, yloc2))
display.flip()
time.wait(500)
textBox("What are you doing here? It's dangerous to wander around here alone.", "???")
textBox("I'm sorry, I didn't realize that there were random slimes that attacked you.", name)
textBox("Well anyway, I'm glad that I found you before it was too late. Follow me, I need to show you something.", "???")
while yloc2 > -65:
    for i in char2Back:
        startBackground(0)
        screen.blit(i, (xloc2, yloc2))
        screen.blit(mainBack, (xloc, yloc))
        display.flip()
        yloc2 -= 15
        time.wait(100)
running = True
runningStart = True
while running:
    while runningStart:
        for event in pygame.event.get():
            if event.type == KEYDOWN and xloc < 300 or event.type == KEYDOWN and xloc > 700:
                if event.unicode == " ":
                    textBox("These trees are dry and shriveled.", name)
                    textBox("I haven't seen a real tree in a long time.", name)
                    time.wait(1000)
                    startBackground(0)
                    screen.blit(mainFront, (xloc,yloc))
                    display.flip()
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:  
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
        if moveLeft == True and xloc >= 240:
            for i in left:
                startBackground(0)
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 730:
            for i in right:
                startBackground(0)
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                startBackground(0)
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                startBackground(0)
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        # makes it so that when you walk to the edge of the screen, you move to a new area
        if yloc <= 10:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            yloc = 660
            xloc = 495
            running = False
            runningStart = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

# Cutscene
secBackground()
screen.blit(character2Back,(495, 420))
screen.blit(mainBack, (xloc, yloc))
display.flip()
time.wait(1000)
textBox("!", name)
secBackground()
screen.blit(mainBack, (xloc, yloc))
screen.blit(character2Back,(495, 420))
time.wait(500)
display.flip()
for i in range(10):
    for i in back:
        secBackground()
        screen.blit(i, (xloc, yloc))
        screen.blit(character2Back,(495, 420))
        display.flip()
        yloc -= 10
        time.wait(200)
secBackground()
screen.blit(character2Left, (495, 420))
screen.blit(mainBack, (495, 460))
display.flip()
time.wait(500)
secBackground()
screen.blit(character2Front, (495, 420))
screen.blit(mainBack, (495, 460))
display.flip()
time.wait(500)
textBox("Wow, I've never seen a tree like this before.", name)
textBox("Yeah, me neither. Nowadays, trees that aren't electronic are rare.", "???")
textBox("Yeah, I wonder why this tree is the only one that has leaves. All the trees around it are dry and shriveled", name)
textBox("How did you get here anyway?", "???")
textBox("I'm not sure, I just woke up and found myself here.", name)
textBox("Hey, me too. I've been here for a couple of hours already.", "???")
textBox("Wow, you too? I wonder how we ended up here.", name)
textBox("Well now that we're both here, how about we try to get out of here together?", "???")
draw.rect(screen,LIGHTGREY,(30,510,940,160))
# Allows you to answer yes or no
string = "Yes"
text = nameFont.render(string, 1, BLACK)
screen.blit(text, Rect(780, 550, 0, 0))
string = "No"
text = nameFont.render(string, 1, BLACK)
screen.blit(text, Rect(780, 600, 0, 0))
display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            if x > 780 and x < 870 and y > 550 and y < 580:
                textBox("Yeah, good idea. We should stick together so we can stay safe.", name)
                textBox("Good, I was afraid you would say no.", "???")
                running = False
            if x > 780 and x < 840 and y > 600 and y < 630:
                textBox("No way! I don't even know who you are.", name)
                textBox("Well, we'll die if you disagree.", "???")
                textBox("Oh, well in that case, I'll help you!", name)
                textBox("Great!", "???")
                running = False
textBox("Oh yeah, I never caught your name.", name)
textBox("Oh right, I'm Xander, nice to meet you!", "Xander")
textBox("Xander joined your party.", "Game")
char2Battle = 1
textBox("Here, I'll heal both of us.", "Xander")
textBox("Your HP and MP were maxed out.", "Game")
mainHP = mainMaxHP
mainMP = mainMaxMP
char2HP = char2MaxHP
char2MP = char2MaxMP
textBox("Here are some potions, you can use these when you're in battle.", "Xander")
textBox("You recieved 5 HP Potions, 5 MP Potions, and 3 Revival Potions.", "Game")
# Character 2 gives you potions
bag.append("HP Potion")
bag.append("HP Potion")
bag.append("HP Potion")
bag.append("HP Potion")
bag.append("HP Potion")
bag.append("MP Potion")
bag.append("MP Potion")
bag.append("MP Potion")
bag.append("MP Potion")
bag.append("MP Potion")
bag.append("Revival Potion")
bag.append("Revival Potion")
bag.append("Revival Potion")
textBox("You can use these potions by accessing the \'bag\' menu when fighting.", "Xander")
textBox("HP Potions will restore your health. Use them when your HP is low.", "Xander")
textBox("MP Potions will restore your MP. Magic moves use up MP, so if you do not have any MP, you cannot use any magic moves.", "Xander")
textBox("Revival Potions will revive you if your HP falls to 0. If everybody's HP falls to 0, it's game over.", "Xander")
textBox("Revival Potions are very valuable, so do not waste them.", "Xander")
textBox("I am pretty weak at physical battling, and am much stronger at using magic.", "Xander")
textBox("When I'm fighting, using magic is the way to go for me.", "Xander")
textBox("If you feel that we can't win a battle, press the \'run\' button.", "Xander")
textBox("There is a chance that we will not be able to run away. If that happens, keep trying.", "Xander")
textBox("For now, let's start by searching in other areas.", "Xander")
textBox("Press \'T\' on your keyboard if you want to talk to me.", "Xander")
secBackground()
screen.blit(mainBack, (495, 460))
display.flip()
running = True
running2 = True
running3 = False
running4 = False
running5 = False
firstTalk = True
area2Explored = False
area3Explored = False
area4Explored = False
while running:
    while running2:
        for event in pygame.event.get():
            # When all areas are explored, the next scene happens
            if area2Explored == True and area3Explored == True and area4Explored == True:
                running = False
                running2 = False
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    # If you press T for the first time, the characters will say something different than if you had already pressed it before
                    if firstTalk == True:
                        textBox("Where should we go first?", name)
                        textBox("Let's start by walking to some other areas.", "Xander")
                        textBox("Walk to the edge of the screen to go to a new area.", "Xander")
                        secBackground()
                        screen.blit(mainFront, (xloc, yloc))
                        display.flip()
                        firstTalk = False
                    else:
                        textBox("I've never seen a tree so large before!", name)
                        textBox("Yeah, these trees are so rare nowadays because of how much technology has advanced", "Xander")
                        textBox("Pollution and e-waste have wiped out most of them, and now all the trees we're used to are electronic", "Xander")
                        secBackground()
                        screen.blit(mainFront, (xloc, yloc))
                        display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 10:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        secBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 990:
            for i in right:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc >= 985:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            thirdBackground()
            xloc = 20
            screen.blit(mainRight, (xloc, yloc))
            display.flip()
            running2 = False
            running3 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
        if yloc <= 15:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            fourthBackground()
            yloc = 640
            screen.blit(mainBack, (xloc, yloc))
            display.flip()
            running2 = False
            running4 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
        if xloc <= 15:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            fifthBackground()
            xloc = 960
            screen.blit(mainLeft, (xloc, yloc))
            display.flip()
            running2 = False
            running5 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
    while running3 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN and xloc > 700:
                if event.unicode == " ":
                    textBox("What a huge lake!", name)
                    textBox("Yeah, dirty too. There's so much trash floating around in there.", "Xander")
                    textBox("What if we don't find our way out of here? Will we have to resort to drinking this water?", name)
                    textBox("... I'd rather not think about that possibility", "Xander")
                    thirdBackground()
                    screen.blit(mainFront, (xloc,yloc))
                    display.flip()
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Hey, there's a lake over there.", name)
                    textBox("Yeah, but it looks like it's full of trash.", "Xander")
                    textBox("Hey, that probably means we're near civilization at least.", name)
                    thirdBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        thirdBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 800:
            for i in right:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc <= 5:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            xloc = 980
            screen.blit(mainLeft, (xloc, yloc))
            display.flip()
            area2Explored = True
            running2 = True
            running3 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

    while running4 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Is that a cave?", name)
                    textBox("Looks like it. And I don't want to know what's inside.", "Xander")
                    textBox("Me neither, let's avoid it for now.", name)
                    fourthBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        fourthBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 800:
            for i in right:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 300:
            for i in back:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if yloc >= 645:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            yloc = 20
            screen.blit(mainFront, (xloc, yloc))
            display.flip()
            area3Explored = True
            running2 = True
            running4 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

    while running5 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("There's nothing here.", name)
                    textBox("Yeah, we'll have to look somewhere else.", "Xander")
                    fifthBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        fifthBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 1000:
            for i in right:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc >= 985:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            xloc = 20
            screen.blit(mainRight, (xloc, yloc))
            display.flip()
            area4Explored = True
            running2 = True
            running5 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

# Character 3 appears
screen.blit(character3Back, (480, 400))
display.flip()
textBox("Hey, who's that?", "Xander")
secBackground()
screen.blit(character3Back, (480, 400))
screen.blit(character2Back, (440, 450))
screen.blit(mainBack, (530, 450))
display.flip()
time.wait(500)
screen.blit(character3Right, (480, 400))
screen.blit(character2Back, (440, 450))
screen.blit(mainBack, (530, 450))
time.wait(100)
screen.blit(character3Front, (480, 400))
screen.blit(character2Back, (440, 450))
screen.blit(mainBack, (530, 450))
time.wait(100)
textBox("Oh thank goodness, there's more people here", "???")
textBox("Did you also wake up here?", "Xander")
textBox("Yes! I was so scared with all the slimes around. I sook shelter beneath this tree.", "???")
textBox("What's your name?", name)
textBox("I'm Merisa, what are your names?", "Merisa")
textBox(("My name is %s and this is Xander." %name), name)
textBox("So are you two going to try to find your way out of this forest?", "Merisa")
textBox("Yes! Would you like to join us?", "Xander")
textBox("Of course! I wouldn't be able to survive on my own out here.", "Merisa")
textBox("Merisa joined the party", "Game")
char3Battle = 1
textBox("I'm not very strong, but I can heal you when you're fighting.", "Merisa")
textBox("Let's try to find a way out. I need to get home soon!", "Merisa")
secBackground()
xloc = 530
yloc = 450
screen.blit(mainBack, (xloc, yloc))
display.flip()

running = True
running2 = True
running3 = False
running4 = False
running5 = False
while running:
    while running2:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Hey Merisa, have you ever seen a tree this big and full of leaves before?", name)
                    textBox("Not in a while, no. The last time I saw a tree like this was probably in 2100.", "Merisa")
                    textBox("Wow, how old are you? You were alive back then?", "Xander")
                    textBox("...", "Merisa")
                    secBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        secBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 990:
            for i in right:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                secBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc >= 985:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            thirdBackground()
            xloc = 20
            screen.blit(mainRight, (xloc, yloc))
            display.flip()
            running2 = False
            running3 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
        if yloc <= 15:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            fourthBackground()
            yloc = 640
            screen.blit(mainBack, (xloc, yloc))
            display.flip()
            running2 = False
            running4 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
        if xloc <= 15:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            fifthBackground()
            xloc = 960
            screen.blit(mainLeft, (xloc, yloc))
            display.flip()
            running2 = False
            running5 = True
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False
    while running3 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN and xloc > 700:
                if event.unicode == " ":
                    textBox("Gross, is that horrible smell coming from the lake?", "Merisa")
                    textBox("Yep, this lake sure is disgusting", "Xander")
                    thirdBackground()
                    screen.blit(mainFront, (xloc,yloc))
                    display.flip()
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Ugh, what's that awful smell?", "Merisa")
                    textBox("Probably coming from that lake over there.", "Xander")
                    thirdBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        thirdBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 800:
            for i in right:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                thirdBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc <= 5:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            xloc = 980
            screen.blit(mainLeft, (xloc, yloc))
            display.flip()
            running2 = True
            running3 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

    while running4 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN and yloc < 400:
                if event.unicode == " ":
                    running = False
                    running4 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Have you explored that cave yet?", "Merisa")
                    textBox("Nope, it looks way too dangerous to explore.", name)
                    textBox("Are you sure? What if the way out of the forest is in there?", "Merisa")
                    textBox("A loud growling sound is heard coming from inside the cave.", "Game")
                    textBox("On second thought. Maybe we shouldn't go in after all.", "Merisa")
                    fourthBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                    # When you investigate the cave, you move on to the next scene
                    running = False
                    running4 = False
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        fourthBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 800:
            for i in right:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if yloc >= 645:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            yloc = 20
            screen.blit(mainFront, (xloc, yloc))
            display.flip()
            running2 = True
            running4 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

    while running5 == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("There's nothing here.", name)
                    textBox("Yeah, we'll have to look somewhere else.", "Xander")
                    fifthBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
            if event.type == KEYDOWN:
                if event.unicode == "a" or event.unicode == "d" or event.unicode == "s" or event.unicode == "w":
                    randEncounter = random.randint(1,100)
                    if randEncounter <= 5:
                        moveLeft = False
                        moveRight = False
                        moveUp = False
                        moveDown = False
                        battleScreen(mainBattle,char2Battle,char3Battle,char4Battle,"Slime",random.randint(1,2))
                        fifthBackground()
                        screen.blit(mainFront, (xloc,yloc))
                        display.flip()
        if moveLeft == True and xloc >= 0:
            for i in left:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 1000:
            for i in right:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                fifthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if xloc >= 985:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            xloc = 20
            screen.blit(mainRight, (xloc, yloc))
            display.flip()
            running2 = True
            running5 = False
            moveUp = False
            moveDown = False
            moveRight = False
            moveLeft = False

screen.blit(bossSmall, (425, 350))
screen.blit(mainBack,(415, 450))
screen.blit(character2Back,(365, 450))
screen.blit(character3Back,(465, 450))
display.flip()
textBox("Ahh!", "Merisa")
textBox("W-what on earth?", "Xander")
battleScreen(mainBattle, char2Battle, char3Battle, char4Battle, "Boss", 1)
fourthBackground()
screen.blit(mainBack,(415, 450))
screen.blit(character2Back,(365, 450))
screen.blit(character3Back,(465, 450))
display.flip()
textBox("That was the largest slime I've ever seen.", name)
textBox("Hey, I think I see light coming out from that cave. Maybe it will lead to the outside?", "Xander")
textBox("Hey, you're right! Now that the giant slime is out of the way, let's try exploring it.", "Merisa")
fourthBackground()
screen.blit(mainBack,(415, 450))
display.flip()
xloc = 415
yloc = 450
running = True
while running == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                running1 = False
            if event.type == KEYDOWN and yloc < 400:
                if event.unicode == " ":
                    running = False
                    running4 = False
            if event.type == KEYDOWN:
                if event.unicode == "t":
                    textBox("Let's try exploring that cave!", "Merisa")
                    fourthBackground()
                    screen.blit(mainFront, (xloc, yloc))
                    display.flip()
                    running = False
                    running4 = False
                if event.unicode == "a":
                    moveLeft = True
                if event.unicode == "d":
                    moveRight = True
                if event.unicode == "s":
                    moveDown = True
                if event.unicode == "w":
                    moveUp = True
            if event.type == KEYUP:
                if event.key == 97:
                    moveLeft = False
                if event.key == 100:
                    moveRight = False
                if event.key == 119:
                    moveUp = False
                if event.key == 115:
                    moveDown = False
        if moveLeft == True and xloc >= 0:
            for i in left:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc -= 10
        if moveRight == True and xloc <= 800:
            for i in right:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                xloc += 10
        if moveUp == True and yloc >= 0:
            for i in back:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150)
                yloc -= 10
        if moveDown == True and yloc <= 660:
            for i in front:
                fourthBackground()
                display.flip()
                screen.blit(i, (xloc,yloc))
                display.flip()
                time.wait(150) 
                yloc += 10
        if yloc <= 400 and xloc < 600 and xloc > 400:
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            time.wait(1000)
            secBackground()
            xloc = 20
            screen.blit(mainRight, (xloc, yloc))
            display.flip()
            running = False
draw.rect(screen,BLACK(0,0,1000,700))
display.flip()
time.wait(1000)
titleFont = font.SysFont("Times New Roman",130)
# The game ends
string = "The End"    
text = titleFont.render(string, 1, [nightShadowR, nightShadowG, nightShadowB])
screen.blit(text, Rect(260, 100, 0, 0))
display.flip()
time.wait(1000)
textBox("You escaped!", "Game")
quit()