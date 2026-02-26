# Arlind Zalli
# 5/31/24
# Adventure: A gem collection game
# ==========
# Enhancements:
# Lists 
# Functions 
# Nice graphics 
# Sound        
# Window icon
# Saveable highscore
# Custom font
# ==========

import pygame
import math
import random
import time

pygame.init()
g = open("score.txt", "r")
gemscore = str(g.read())
# Initializing pygame and importing the necessary libraries.
size = (1000, 800) # Creates a 1000 x 800 pixel window.
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Adventure') # Setting the window title to Adventure.
custom_font = pygame.font.Font("Font.ttf", 100) # Defining the font for the title, setting it to size 100.
# This helped me: https://www.makeuseof.com/pygame-fonts-text-effects-how-load/
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGREEN = (217, 234, 211)
LIGHTYELLOW = (255, 242, 206)
LIGHTRED = (243, 204, 204)
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 255)
# Defining colors used for the game. 
pregamechoices = [1, True, 1, True, False, False] # This is a list containing all of the possible pre game choices that the user can make in the pregame screen.
# First one is Difficulty, next is Timer, and the next is day length, next one is if music is on, and the final list item is if hitboxes are on.
keys = [False, False, False, False] # This is a list representing which of the WASD keys are being pressed. If it is false, the key is not being pressed.
# The list is in order W - S - A - D
music = pygame.mixer.Sound("Music.mp3") # Importing the music.
background = [] # This is a list that will later be added to to define the background of the screen when the user is not in game. This is the background that shows up when they are in settings, pregame menu and how to play.
grassTile1 = pygame.image.load("GrassTile1.png")
grassTile2 = pygame.image.load("GrassTile2.png")
grassTile3 = pygame.image.load("GrassTile3.png")
grassTile4 = pygame.image.load("GrassTile4.png")
grassTile5 = pygame.image.load("GrassTile5.png")
# Loading the images of the grass tiles used in game and in the menus.
grass = [grassTile1, grassTile2, grassTile3, grassTile4, grassTile5]
# Creating a list of these tiles.
tree = pygame.image.load("Tree1.png")
rock = pygame.image.load("Rock1.png")
cotton = pygame.image.load("Cotton1.png")
# Loading the resources that the user can harvest in game.
# Trees, rocks, and cotton are the 3 resources that they can harvest.
tree = pygame.transform.scale(tree, [100, 100])
rock = pygame.transform.scale(rock, [80, 80])
cotton = pygame.transform.scale(cotton, [60, 60])
# Scaling the resources to be the preferred scales.
resources = [tree, rock, cotton] # This creates a list of the resources called resources.
wood = pygame.image.load("Wood1.png")
stone = pygame.image.load("Stone1.png")
iron = pygame.image.load("Iron1.png")
stick = pygame.image.load("Stick1.png")
club = pygame.image.load("Club1.png")
stonepick = pygame.image.load("Stonepick1.png")
stonespear = pygame.image.load("Stonespear1.png")
mine = pygame.image.load("Mine1.png")
gem = pygame.image.load("Gem1.png")
ironsword = pygame.image.load("Ironsword1.png")
ironpick = pygame.image.load("Ironpick1.png")
planks = pygame.image.load("Woodplanks1.png")
bed = pygame.image.load("Bed1.png")
# Loading all of the possible items that the user can hold in their inventory.
wood = pygame.transform.scale(wood, [60, 60])
stone = pygame.transform.scale(stone, [60, 60])
iron = pygame.transform.scale(iron, [60, 30])
stick = pygame.transform.scale(stick, [60, 60])
club = pygame.transform.scale(club, [60, 60])
stonepick = pygame.transform.scale(stonepick, [60, 60])
stonespear = pygame.transform.scale(stonespear, [15, 60]) # This item is not 60 x 60 because it would appear as stretched out due to the dimensions of its file.
stonespear = pygame.transform.rotate(stonespear, 45) # I rotated it 45 degrees for it to fit within the slots in the users inventory.
mine = pygame.transform.scale(mine, [60, 60])
gem = pygame.transform.scale(gem, [60, 60])
ironpick = pygame.transform.scale(ironpick, [60, 60])
ironsword = pygame.transform.scale(ironsword, [60, 60])
planks = pygame.transform.scale(planks, [60, 60])
bed = pygame.transform.scale(bed, [60, 60])
pygame.display.set_icon(gem)
# Setting the scale of all of these items to 60 x 60.
items = ["", wood, stone, iron, stick, cotton, club, stonepick, stonespear, mine, gem, ironsword, ironpick, planks, bed]
# Creating a list all of the possible items in image files. The first item of the list is empty because if there was an item with id 0 it would be confused with an empty inventory slot.
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, [80, 80])
# Loading an image of the player and scaling it to 80 x 80.
playerrotation = pygame.transform.rotate(player, 0)
# Creating a variable for the rotation of the player. This will be used later.
zombie = pygame.image.load("zombie.png")
zombie = pygame.transform.scale(zombie, [80, 80])
# Loading an image of the zombie, and scaling it to 80 x 80.
playerX = 0
playerY = 0 
# Creating variables for the X and Y coordiantes of the player.
mining = 0
health = 10
# Creating variables for the player mining, and their health points.
global i
i = 0
# Making the variable i global, as it will be used in many functions, and setting it to 0.

row = 0
col = 0
# Creating variables row and col to generate the background of the menus.

for col in range(0, 800, 44): # Starting at 0 and ending on or past 800, and going by 44 each time, this variable will represent the columns. (col)
    for row in range(0, 1000, 44): # Starting at 0 and ending on or past 1000, and going by 44 each time, this variable will represent the rows. (row)
        background.append(grass[random.randrange(0, 5)]) # Add a random item of the 5 items in the list grass to the list background.
        screen.blit(background[i], [row, col]) # Blit the ith item of background, which was added to earlier, and place it at coordinates row and col.
        i += 1 # Increment i by 1.
# The reason that col starts at 0 and ends on or past 800 with an increment of 44 each time is because the height of the screen is 800 pixels, and each grass tile is 44 pixels long.
# The reason that row starts at 0 and ends on or past 1000 with an increment of 44 each time is because the height of the screen is 1000 pixels, and each grass tile is 44 pixels wide.
# We are using a list to represent the background because we want the background to stay constant, rather than constantly changing.
        
def button(x, x2, y, y2, color, outlinecolor, text, textcolor, fontname, fontsize, nextpage): 
    # We are creating a function called button, to reduce the number of lines we use to create each button used in-game and in the menus.
    # This function has 12 parameters; the x and y coordinates, and the x2 and y2 coordinates. The background color of the button, the outline color of the button,
    # the text within the button, the color of the text within the button, the font name of the text, the font size of the text, and the game state the button will change to when clicked. 
    global page # We are making the variable page global, because we want whatever happens in this function to change the game state, which is referenced outside of the function.
    width = math.fabs(x2 - x) # Creating a variable called width. It is the absolute value of the difference between x2 and x.
    height = math.fabs(y2 - y) # Creating a variable called height. It is the absolute value of the difference between y2 and y.
    pygame.draw.rect(screen, color, [x, y, width, height]) # Drawing a rectangle using our parameters x, y, width and height.
    font = pygame.font.SysFont(fontname, fontsize, False, False) # Creating the font for the button based on the parameters fontname and fontsize.
    buttonText = font.render(text, True, textcolor) # Creating a text image based on the parameters of the desired button text, and the text color.
    screen.blit(buttonText, [x + (width / 2) - height , y + (height / 10)]) # Blitting that text onto the screen, using the x and y coordinates. We are adding a fraction of the variables width and height to the variables to ensure that the text is centered on the button.
    if (mouse_x > x and mouse_y > y) and (mouse_x < x2 and mouse_y < y2): # If the x coordinate of the mouse pointer is less than the parameter x, and the y coordinate of the mouse pointer is less than the parameter y, and the x coordinate of the mouse pointer is less than the parameter x2 and the y coordinate of the mouse pointer is less than the parameter y2. 
    # This is the collision detection between the mouse pointer and the button.
        pygame.draw.rect(screen, outlinecolor, [x, y, width, height], 3)
        # Draw the outline of the button, using the parameters outline color, postitioning it at parameters x and y and using the variables width and heihgt to prefectly surround the background of the button.
        if buttons[0] == True: # If the user is left clicking, 
            page = nextpage # Set the variable for game state (page) to the parameter nextpage.

def title(x, y, width, height, color, outlinecolor, text, textcolor, fontname, fontsize):
    # We are creating a function called title, to reduce the number of lines we use every time we want to create text with a rectangle behind it.
    # It has 10 parameters, x and y, width, height, color, outlinecolor, text, textcolor, fontname, and fontsize.
    pygame.draw.rect(screen, color, [x, y, width, height]) # Draw a rectangle using the parameters color for the color, x and y for the position, and width and height for the width and height.
    pygame.draw.rect(screen, outlinecolor, [x, y, width, height], 3) # Create a 3 pixel outline with the color of the parameter outlinecolor with the exact positioning as the last rect.
    font = pygame.font.SysFont(fontname, fontsize, False, False) # Create a font using the parameters fontname and fontsize.
    titleText = font.render(text, True, textcolor) # Create a variable for the text image, using the parameters text and textcolor.
    screen.blit(titleText, [x + (width / 2) - height , y + (height / 10)]) # Blit that text image onto the screen, at coordinates x and y, with half of width added to the x coordinate and one tenth of height added to the y coordinate so it is centered.
    
def togglebutton(x, x2, y, y2, color, outlinecolor, text, textcolor, fontname, fontsize, list, listitem, id):
    # We are creating a function called toggle button to reduce the number of lines we use for each button.
    # The difference between this function and the button function is that this one is focused on changing the item of a list,
    # and the button function is focused on setting the gamestate to a desired number.
    # This function has 13 parameters. You can decide the position, width, height, text, and the customisable colors. 
    # You can decide what list you want to modify and what you want to modify it to.
    width = math.fabs(x2 - x) # Creating a variable called width. It is the absolute value of the difference between x2 and x. 
    height = math.fabs(y2 - y) # Creating a variable called height. It is the absolute value of the difference between y2 and y.
    pygame.draw.rect(screen, color, [x, y, width, height]) # Drawing the base of the button using parameters color, x, y, width, and height.
    font = pygame.font.SysFont(fontname, fontsize, False, False) # Create the font for the button using the parameter fontname, and fontsize.
    buttonText = font.render(text, True, textcolor) # Create a text image using the parameters text, and textcolor.
    screen.blit(buttonText, [x + (width / 2) - height , y + (height / 10)]) # Blit that text image onto the screen, at coordinates x and y, with half of width added to the x coordinate and one tenth of height added to the y coordinate so it is centered.
    if (mouse_x > x and mouse_y > y) and (mouse_x < x2 and mouse_y < y2): # If the x coordinate of the mouse pointer is less than the parameter x, and the y coordinate of the mouse pointer is less than the parameter y, and the x coordinate of the mouse pointer is less than the parameter x2 and the y coordinate of the mouse pointer is less than the parameter y2. 
    # This is the collision detection between the mouse pointer and the button.
        pygame.draw.rect(screen, outlinecolor, [x, y, width, height], 3) # Draw an outline of 3 px around the button to show that it is being hovered on and can be clicked.
        if buttons[0] == True: # If the left mouse button is being clicked, 
            list[listitem] = id # Using the parameter listitem, find the parameter lists listitemth item, and set it to the desired value, the parameter id.
    if list[listitem] == id: # If the listitemth item of the parameter list is equal to the desired value (id),
        pygame.draw.rect(screen, outlinecolor, [x, y, width, height], 3) # Draw an outline of 3 px around the button to show that it has been selected. 

inGameTileId = [] # Create a list for the ids of each grass tile in game.
inGameBgX = [] # Create a list for the x coordinate of those tiles.
inGameBgY = [] # Create a list for the y coordinate of those tiles.
inGameResources = [] # Create a list for the id, as well as the coordinates of the in game resources.
# The reason that the same list was not used for the tiles was because there were issues making the tiles show up on screen, and it was difficult to debug with such long lists since there are so many tiles.

for i in range(-1500, 1500, 44): # Starting at -1500 and ending on or past 1500, increment the variable i by 44 each time.
    inGameBgX.append(i) # Add i to the end of the list of the x coordinates of the grass tiles.
for i in range(-1500, 1500, 44): # Starting at -1500 and ending on or past 1500, increment the variable i by 44 each time.
    inGameBgY.append(i) # Add i to the end of the list of the y coordinates of the grass tiles.
# The reason I chose for it to start at -1500 and end at 1500 for both loops is because I want the ground to be 3000 by 3000 px. It increments by 44 each time on both loops because the dimensions of the grass tiles are 44 x 44 px.
for i in range(len(inGameBgX) * len(inGameBgY)): # Starting at 0 and ending on or past the product of the length of the list of the x coordinates of the grass tiles and the length of the of the y coordinates of the grass tiles, increment i by 1.
    inGameTileId.append(random.randrange(0, 5)) # Add a random number ranging from 0 to 4 to the end of the list for the id of the grass tiles.
    # The reason that this is done is because there are 5 different tile ids, and 0 to 4 has 5 different numbers.
for i in range(2): # Starting at 0 and ending on or past 2, increment i by 1 each time.
    for ii in range(10): # Starting at 0 and ending on or past 10, increment, ii by 1 each time.
        inGameResources.append(i) # Add i to the end of the list for the information on the in game resources. 
        inGameResources.append(random.randrange(-1200, 1200)) # Add a random number from -1200 to 1199 to the end of the list for the information on the in game resources. (This represents the x coordinate of the resource.)
        inGameResources.append(random.randrange(-1200, 1200)) # Add a random number from -1200 to 1199 to the end of the list for the information on the in game resources. (This represents the y coordinate of the resource.)
        # The reason that the range is -1200 to 1200 is because the world starts at -1500 and ends at 1500, so I dont want any in game resources to appear along the margins of the world.
# What these two for loops accomplish is adding the id, and the coordinates of in game resources that will show up on the screen!
# The loops make it so that 10 of each resource appear on screen.

for ii in range(5): # Starting at 0 and ending on or past 5, increment, ii by 1 each time.
    inGameResources.append(2) # Add 2 to the end of the list for the information on the in game resources. 
    inGameResources.append(random.randrange(-1200, 1200)) # Add a random number from -1200 to 1199 to the end of the list for the information on the in game resources. (This represents the x coordinate of the resource.)
    inGameResources.append(random.randrange(-1200, 1200)) # Add a random number from -1200 to 1199 to the end of the list for the information on the in game resources. (This represents the y coordinate of the resource.)
# This loop adds a separate resource to the list, and this resource is cotton.

def inGameBgRender(): # This function is used to organise these lines of code from the others. 
    # This code creates the background scrolling effect you see in game. 
    for i in range(len(inGameBgX)): # Starting at 0 and ending on or past the length of the list representing the x coordinates of the grass tiles, increment i by 1 each time.
        for ii in range(len(inGameBgY)): # Starting at 0 and ending on or past the length of the list representing the y coordinates of the grass tiles, increment ii by 1 each time.
            screen.blit(grass[inGameTileId[ii * i]], [inGameBgX[ii] - playerX, inGameBgY[i] - playerY]) # Blit the product of i and ii of the list containing the ids of the grass tiles of the list containing the images of the grass tiles.
            # Blit this image at x = the iith element of the list representing the x coordinates of the grass tiles subtracted by the x position of the player, y = the ith element of the list representing the y coordinates of the grass tiles subtracted by the y position of the player
            # The reason we are subtracting the coordinates of the player from the coordinates of the tiles is because we want the tiles that show up on screen to be only tiles that are near the player.
            # We are multiplying i and ii in inGameTileId because the amount of ids are the product of the amount of x and y coordinates.
            
inventorySlot = 0 # Create a variable that represents the selected inventory slot.
inventoryItems = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Create a list that represents the id of items in your inventory.
inventoryQty = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Create a list that represents the quantity of items in your inventory.

def inventoryTroubleshoot():
    # This is a function to troubleshoot the inventory. What it accomplishes is if there is no quantity, it removes the item id from the list of item in your inventory.
    for i in range(9): # Starting at 0 and ending on or past 9, 
        if inventoryQty[i] <= 0: # if the ith element of the quantity of items in your inventory is less than or equal to 0,
            inventoryItems[i] = 0 # set the ith element of the list of item ids in your inventory to 0.

def inventoryUpdate():
    # This is a function used to organise the code used to update the users inventory. 
    for i in range(9): # Starting at 0 and ending on or past 9, increment i by 1.
        if i == inventorySlot: # If i is equal to the selected inventory slot,
            pygame.draw.rect(screen, LIGHTRED, [i * 95 + 85, 700, 75, 75]) # draw a red rectangle at x = i mulitplied by 95 plus 85, y = 700, and with a width of 75 and a height of 75.
            # The reason that it is i * 95 is because each tile is supposed to be shown in a different spot, each further to the right that the one before.
            pygame.draw.rect(screen, BLACK, [i * 95 + 85, 700, 75, 75], 3) # Draw an outline 3 px thick at the same location.           
        else: # Otherwise,
            pygame.draw.rect(screen, LIGHTYELLOW, [i * 95 + 85, 700, 75, 75]) # draw a yellow rectangle at the same location as the red,
            pygame.draw.rect(screen, BLACK, [i * 95 + 85, 700, 75, 75], 3) # with the same outline.
        if inventoryQty[i] >= 1: # If there is more than or equal to one item in the ith slot,
            screen.blit(items[inventoryItems[i]], [i * 95 + 90, 710]) # Blit that item at the ith slot. 
            if inventoryQty[i] > 1: # If there is more than one item in the ith slot, 
                font = pygame.font.SysFont("Calibri", 25, False, False)
                qtyImg = font.render(str(inventoryQty[i]), True, BLACK)
                screen.blit(qtyImg, [i * 95 + 90, 705])
                # Show the amount of that item in a number that is in a text image blitted at the location of the ith cell.
            
def inventoryAdd(item, qty):
    # This function is used to easily add anitem to the players inventory.
    if item in inventoryItems: # If the desired item is in the list of inventory items,
        # I used this link to help me with "in" https://www.geeksforgeeks.org/check-if-element-exists-in-list-in-python/
        inventoryQty[inventoryItems.index(item)] += qty # add the quantity of that desired item to the slot previously containing the desired item.
    elif 0 in inventoryItems: # Otherwise, if there is an empty slot in the list of inventory items, 
        inventoryItems[inventoryItems.index(0)] = item # Set the empty slot id to teh desired item,
        inventoryQty[inventoryQty.index(0)] += qty # set the quantity of that item to the desired quantity.
        
def resourceRender():
    # This function is used to organise and separate the code that renders resources and makes the player able to harvest them from the rest of the code.
    global click, mining, efficiency
    # Globalizing the variables in this function since they are going to be used outside the function. 
    for i in range(int(len(inGameResources) / 3)): # Starting at 0, and ending on or past the length of the list representing in game resources divided by 3 (since each resource requires 3 values to show up on the screen: id, x, and y.),
        screen.blit(resources[inGameResources[i * 3]], [inGameResources[i * 3 + 1] - playerX, inGameResources[i * 3 + 2] - playerY]) 
        # Show the resources on the screen. 
        # The reason that it is using the i * 3th element of in game resources as its image file is because the list repeats in a pattern of id, x coord, and y coord, to blit resources with less lines. 
        # Similarly, inGameResources[i * 3 + 1] represents the x coord, and inGameResources[i * 3 + 2] represents the y coord.
        # This was explained before with the grass tiles, but it is subtracted by the player coordinates because we want the resources to show up relative to the position of the player. 
    for i in range(int(len(inGameResources) / 3)): # Starting at 0, and ending on or past the length of the list representing in game resources divided by 3,
        if pregamechoices[4] == True: # If the choice to activate in game hitboxes is true,
            pygame.draw.rect(screen, LIGHTRED, [inGameResources[i * 3 + 1] - playerX, inGameResources[i * 3 + 2] - playerY, 70, 70], 4)
            # draw a 70 x 70 4px red rectangle outline around the ith resource at its position on the screen (explained before).
        if math.fabs(mouse_x - math.fabs(inGameResources[i * 3 + 1] - playerX)) < 70 and math.fabs(mouse_y - math.fabs(inGameResources[i * 3 + 2] - playerY)) < 70 and click == True:
            # If the mouse pointer is less than 70 px away from a resource, and the left mouse button is clicked,
            # The reason that it subtracts the x position of the mouse from the coordinates of the resource is because we want to find the distance of the mouse relative to the coordinates of the resource on the screen. 
            efficiency = 1 # set the efficiency to 1.
            if inventoryItems[inventorySlot] == 12: # If the user is holding an iron pick, 
                efficiency = 3 # set the efficiency to 3.
            elif inventoryItems[inventorySlot] == 7:
                efficiency = 2
            mining += efficiency # Increment the mining variable by efficiency. 
            if mining >= 10: # If the mining variable has reached its max (10), 
                mining = 0 # set the mining variable to 0.
                if inGameResources[i * 3] != 2: # If the mined resource is not cotton, 
                    inventoryAdd(inGameResources[i * 3] + 1, 1) # add the resource to the player inventory with a qty of 1.
                else: # Otherwise, 
                    inventoryAdd(5, 1) # add cotton to the players inventory with a qty of 1.
            click = False # Set the variable controlling whether there was a click with the left mouse button to false.
        elif pregamechoices[4] == True: # If hitboxes are on,
            pygame.draw.rect(screen, LIGHTGREEN, [inGameResources[i * 3 + 1] - playerX, inGameResources[i * 3 + 2] - playerY, 100, 100], 4)
            # draw a 70 x 70 4px green rectangle outline around the ith resource at its position on the screen (explained before).

minesX = []
minesY = []
minesFUEL = []
minesIRON = []
minesGEM = []
# Create lists for the data that the mines will hold.

def minesRender(): 
    # This is a function to simplify the rendering of mines on the screen.
    global click # Globalization of the click variable as it will be used outside the function.
    for i in range(len(minesX)): # Starting at 0 and ending on or past the length of the list representing the X position of the mines, increment i by 1.
        minesFUEL[i] -= 0.5 # Subtract 0.5 fuel from the ith mine.
        if minesFUEL[i] > 0: # If the fuel of the ith mine is more than 0, 
            if random.randrange(0, 600) == 1: # if a random number from 0 to 599 is 1, 
                minesIRON[i] += random.randrange(0, 3) # add a random number of iron ranging from 0 to 2 to the players inventory.
            if random.randrange(0, 1000) == 1: # if a random number from 0 to 1000 is 1, 
                minesGEM[i] += 1 # add 1 gem to the players inventory. 
        if click == True and math.fabs(mouse_x - math.fabs(minesX[i] - playerX)) < 70 and math.fabs(mouse_y - math.fabs(minesY[i] - playerY)) < 70:
            # If the user is clicking less than 70px away from the mine, (math explained earlier)
            for ii in range(minesIRON[i]): # Starting at 0 and ending at the value of the amount of iron in the ith mine,
                inventoryAdd(3, 1) # add 1 iron to the players inventory.
            for ii in range(minesGEM[i]): # Starting at 0 and ending at the value of the amount of gems in the ith mine,
                inventoryAdd(10, 1) # add 1 gem to the players inventory.
            minesGEM[i] = 0 
            minesIRON[i] = 0
            # Set the amount of gems and iron in the ith mine to 0
            click = False # Set the variable controlling whether there was a click with the left mouse button to false.
        elif minesFUEL[i] <= 0: # If the ith mine runs out of fuel, 
            del minesX[i]
            del minesY[i]
            del minesFUEL[i]
            del minesIRON[i] 
            del minesGEM[i] 
            # delete the data from all of the lists of the ith mine.
        bar(minesFUEL[i], RED, 2000, minesX[i] - playerX, minesY[i] - playerY - 60, 65, 15, "Fuel")
        # Create two bars positioned above the mine displaying the level of the mine and the amount of fuel it has.
        screen.blit(mine, [minesX[i] - playerX, minesY[i] - playerY]) 
        # Show the ith mine on screen relative to the players position. 

def bar(variable, color, max, x, y, width, height, text = ""): 
    # This is a function creating a bar that can be controlled by a variable.
    pygame.draw.rect(screen, WHITE, [x, y, width, height])
    pygame.draw.rect(screen, color, [x, y, variable / max * width, height])
    pygame.draw.rect(screen, BLACK, [x, y, width, height], 3)
    font = pygame.font.SysFont("Calibri", 15, False, False)
    barText = font.render(text, True, BLACK)
    screen.blit(barText, [x + width + 10, y])

spawning = False
# A variable that controls the spawning of zombies.
zombieX = []
zombieY = []
zombieHP = []
zombieMAXHP = []
# Creating lists for the data the zombies need to load in.
hitcooldown = 5 # Creating the variable hitcooldown, that will control the cool down you have on zombies.
strength = 0 # Strength is the variable that will affect how much damage you do to the zombies.
cooldown = 0 # This is the cooldown rate in hitcooldown that will change as you switch weapons.

def zombieUpdate():
    global strength, cooldown, hitcooldown, click, health
    # Globalizing mulitple variables, as they will be used outside of the function.
    if inventoryItems[inventorySlot] == 6: # If the item held is a wooden club,
        strength = 1.5 # it will have a strength of 1.5, 
        cooldown = 1.25 # and a cooldown rate of 1.25.
    elif inventoryItems[inventorySlot] == 8: # If the item held is a stone spear,
        strength = 2.5 # it will have a strength of 2.5, 
        cooldown = 2 # and a cooldown rate of 2.
    elif inventoryItems[inventorySlot] == 11: # If the item held is an iron sword,
        strength = 2 # it will have a strength of 2, 
        cooldown = 1 # and a cooldown rate of 1.
    else: # Otherwise, if you are not holding a weapon, 
        strength = 0.5 # it will have a strength of 0.5, 
        cooldown = 0.5 # and a cooldown rate of 0.5.
    for i in range(len(zombieHP) - 1): # Starting at 0, and ending on or past the amount of zombies, increment i by 1.
        # The reason I am subtracting it by one is because if the amount of zombies is four, the length of the list is also four, 
        # making the list index out of range, since you would be indexing item four, which does not exist.
        if playerX + 500 > zombieX[i] and playerY + 400 > zombieY[i]: 
            # If the players x and y coordinates are both greater than the x and y of the ith zombie, 
            zombieX[i] += random.randrange(3, 5)
            zombieY[i] += random.randrange(3, 5)
            # move the ith zombie towards the player.
        elif playerX + 500 < zombieX[i] and playerY + 400 > zombieY[i]: 
            # If the players x coordinate is less than the x position of the ith zombie, and the players y coordinate is greater than the y position of the ith zombie,
            zombieX[i] -= random.randrange(3, 5)
            zombieY[i] += random.randrange(3, 5)
            # move the ith zombie towards the player.
        elif playerX + 500 > zombieX[i] and playerY + 400 < zombieY[i]:
            # If the players x coordinate is greater than the x position of the ith zombie, and the players y coordinate is less than the y position of the ith zombie,
            zombieX[i] += random.randrange(3, 5)
            zombieY[i] -= random.randrange(3, 5) 
            # move the ith zombie towards the player.
        elif playerX + 500 < zombieX[i] and playerY + 400 < zombieY[i]:
            # If the players x and y coordinates are both less than the x and y of the ith zombie, 
            zombieX[i] -= random.randrange(3, 5)
            zombieY[i] -= random.randrange(3, 5)
            # move the ith zombie towards the player.
        x = zombieX[i]
        y = zombieY[i]
        # Set the variables x and y to the ith item of the lists zombieX and zombieY for ease of access.
        screen.blit(zombie, [x - playerX, y - playerY])
        # Blit the zombie relative to the position of the player.
        if math.fabs(mouse_x - math.fabs(zombieX[i] - playerX)) < 70 and math.fabs(mouse_y - math.fabs(zombieY[i] - playerY)) < 70 and hitcooldown == 5 and click == True:
            zombieHP[i] -= strength
            hitcooldown = 0
            click = False
        elif math.fabs(zombieX[i] - (playerX + 500)) <= 50 and math.fabs(zombieY[i] - (playerY + 400)) <= 50:
            health -= 0.1
        bar(zombieHP[i], RED, zombieMAXHP[i], zombieX[i] - playerX, zombieY[i] - playerY - 35, 75, 15, "Health")
        if zombieHP[i] <= 0:
            del zombieX[i]
            del zombieY[i]
            del zombieHP[i]
            del zombieMAXHP[i]
    
def zombieInit(x, y, hp, maxhp):
    # This is a function that initializes zombies and adds desired values to their lists
    zombieX.append(x)
    zombieY.append(y)
    zombieHP.append(hp)
    zombieMAXHP.append(maxhp)    
    
recipes = ["Wooden Club", "Stone Pick", "Stone Spear", "Iron Sword", "Iron Pickaxe", "Wooden Planks", "Mine", "Bed", "Sticks"]
recipeShowing = [False, False, False, False, False, False, False, False, False]
recipeMaterialNeeds = ["W", "TS", "TS", "TI", "TI", "W", "SWT", "WC", "W"]
recipeQtyNeeds = ["2", "23", "31", "12", "23", "3", "336", "33", "2"]
# Defining the needs for recipes.
itemNames = ["wood", "stone", "iron", "sticks", "cotton"]
itemLetters = ["W", "S", "I", "T", "C"]
# Defining item short forms, as well as item names.

def craft(item, result, qty):
    # This is a function to simplify crafting.
    global click # Globalization of the variable click, as it will be used outside of the function.
    if click == True: # If the user has clicked, 
        done = False # set done (local var) to false.
        click = False # Set the click to false.
    else: # Otherwise,  
        done = True # set done to true.
    # This senses if the mouse has been clicked or not, and whether the following code should run. 
    itemNeedsMaterial = recipeMaterialNeeds[item]
    itemNeedsQty = recipeQtyNeeds[item] 
    recipeItemID = []
    recipeItemQty = []
    # Create lists for the needs of the recipe, based on the parameter item. 
    for letter in itemNeedsMaterial: # Go through each item in the material needs string, 
        recipeItemID.append(itemLetters.index(letter) + 1) # and add one id to the end of the list of all of the needed item ids for the recipe.
    for letter in itemNeedsQty: # Go through each item in the item quantity string, 
        recipeItemQty.append(int(letter)) # and add that number as an integer to the end of the list of all of the needed quantities for the recipe.
    for letter in recipeItemID: # Go through each item in the needed item ids list, 
        if done == False: # if done is false, 
            if not letter in inventoryItems: # if the items in the players inventory do not meet the recipe requirements, 
                done = True # Set done to true, ending the code. 
            elif not recipeItemQty[recipeItemID.index(letter)] <= inventoryQty[inventoryItems.index(letter)]:
                # if the quantities in the players inventory do not meet the recipe requirements,
                done = True # Set done to true, ending the code. 
    if done == False: # If done is false, 
        for letter in recipeItemID: # Go through each item in the needed item ids list, 
            inventoryQty[inventoryItems.index(letter)] -= recipeItemQty[recipeItemID.index(letter)] # and remove the needed recipe quantity from the players inventory.
        inventoryTroubleshoot() # troubleshoot the inventory to make sure there are no item ids with a quantity less than 1,
        inventoryAdd(result, qty) # and add the desired result item to the players inventory with the desired quantity. 

bedsX = []
bedsY = []
# Creating lists that will later define the coordinates of beds in the game. 

def bedsRender():
    # This is a function to organise the rendering of the beds in the game.
    for i in range(len(bedsX)): # Starting at 0, and ending on or after the amount of beds, increment i by 1. 
        screen.blit(bed, [bedsX[i] - playerX, bedsY[i] - playerY]) # Blit the bed image at the ith beds x and y coordinates, relative to the position of the player.
        if math.fabs(playerX - bedsX[i]) < 70 and math.fabs(playerY - bedsY[i]) < 70 and qpressed == True and timestate == "Night":
            # If the player is 70 pixels away from the bed and the key Q is pressed, and it is night time, 
            time = daylength + 1
            # reset the day by setting the time to the daylength + 1. 
            # This will trigger an if statement in the while loop that sets the time to day and resets the timer. 
            
page = 0 # Creates a variable that represents the current game state. 
time = 0 # Creates a variable that represents time in ms. 
days = 0 # Creates a variable that represents the amount of days that have gone by.
timestate = "Day" # Creates a variable that represents the time of day. This sets it to Day.
click = False # Creates a variable that represents whether a left mouse button click has occured. 
buttons = pygame.mouse.get_pressed() # Gets the mouse buttons that are currently pressed.          
clock = pygame.time.Clock()  
done = False # Start the while loop by setting done to false.
qpressed = False # Creates a variable that defines whether the key Q is pressed or not.
while not done: # While the game is not over,
    for event in pygame.event.get(): # Get all of the possible pygame events.
        if event.type == pygame.QUIT: # If the user quit, 
            done = True # end the while loop by setting done to true.
        if event.type == pygame.MOUSEBUTTONDOWN: # If a mouse button is down,
            buttons = pygame.mouse.get_pressed() # get the mouse buttons that are currently pressed,       
            click = True # Set click to true
        if event.type == pygame.MOUSEBUTTONUP: # If a mouse button is released,
            buttons = pygame.mouse.get_pressed() # get the mouse buttons that are currently pressed,        
            click = False # Set click to false
        if page == 3: # If you are in game, 
            if event.type == pygame.KEYDOWN: # if you are pressing any key on your keyboard,
                if event.key == pygame.K_w: # if that key is W,
                    keys[0] = True # set the 0th item of the list representing whether the keys WSAD are pressed to true.
                if event.key == pygame.K_s: # if that key is S,
                    keys[1] = True # set the 1st item of the list representing whether the keys WSAD are pressed to true.
                if event.key == pygame.K_a: # if that key is A,
                    keys[2] = True # set the 2nd item of the list representing whether the keys WSAD are pressed to true.
                if event.key == pygame.K_d: # if that key is D,
                    keys[3] = True # set the 3rd item of the list representing whether the keys WSAD are pressed to true.
                if event.key == pygame.K_1: # if that key is 1,
                    inventorySlot = 0 # set the variable representing the selected inventory slot to 0.
                if event.key == pygame.K_2: # if that key is 2,
                    inventorySlot = 1 # set the variable representing the selected inventory slot to 1.
                if event.key == pygame.K_3: # if that key is 3,
                    inventorySlot = 2 # set the variable representing the selected inventory slot to 2.
                if event.key == pygame.K_4: # if that key is 4,
                    inventorySlot = 3 # set the variable representing the selected inventory slot to 3.
                if event.key == pygame.K_5: # if that key is 5,
                    inventorySlot = 4 # set the variable representing the selected inventory slot to 4.
                if event.key == pygame.K_6: # if that key is 6,
                    inventorySlot = 5 # set the variable representing the selected inventory slot to 5.
                if event.key == pygame.K_7: # if that key is 7,
                    inventorySlot = 6 # set the variable representing the selected inventory slot to 6.
                if event.key == pygame.K_8: # if that key is 8,
                    inventorySlot = 7 # set the variable representing the selected inventory slot to 7.
                if event.key == pygame.K_9: # if that key is 9,
                    inventorySlot = 8 # set the variable representing the selected inventory slot to 8.
                if event.key == pygame.K_e: # if that key is E,
                    if inventoryItems[inventorySlot] == 9 and inventoryQty[inventorySlot] > 0: # if the inventorySlotth element of the list of the ids of inventory items is equal to 9, (if a mine is being held),
                        # and if the inventorySlotth element of the list of the quantity of inventory items is greater than 0 (if there is more than 0 mines),
                        minesX.append(playerX + 500) 
                        minesY.append(playerY + 400)
                        # add the coordinates of the mine to the end of the list of mine coordinates. 
                        # The reason 500 is being added to the x coordinate of the player is because the percieved x coordinate of the player is actually at the top left corner of the screen at all times,
                        # so we have to move the screen by half of its width to the right and half of its height down to get the player coordinates right in the middle, which is where the mine is being placed.
                        minesFUEL.append(2000) # Add 2000 to the end of the list representing the fuel level of the mines.
                        minesIRON.append(0) # Add 0 to the end of the list representing the amount of iron collected by the mines.
                        minesGEM.append(0) # Add 0 to the end of the list representing the amount of gems collected by the mines.
                        inventoryQty[inventorySlot] -= 1 # Subtract 1 from the inventorySlotth item of the list representing the quantity of the items in the players inventory. (Subtract one mine from the users inventory.) 
                    if inventoryItems[inventorySlot] == 9: # Otherwise, if the player is holding a mine but has less than one mine.
                        inventoryQty[inventorySlot] = 0
                        inventoryItems[inventorySlot] = 0
                        # Reset the values, since the user has no mine. 
                        # This is to troubleshoot a glitch.
                    if inventoryItems[inventorySlot] == 14 and inventoryQty[inventorySlot] > 0: # if the inventorySlotth element of the list of the ids of inventory items is equal to 14, (if the user is holding a bed), and if 
                        # the inventorySlotth element of the list of the quantity of inventory items is greater than 0 (if there is more than 0 beds),  
                        inventoryQty[inventorySlot] -= 1 # Subtract one mine from the users inventory
                        bedsX.append(playerX + 500)
                        bedsY.append(playerY + 400) 
                        # Add the coordinates of the player to the list representing the coordinates of the beds.
                    if inventoryItems[inventorySlot] == 14: # Otherwise, if the user is only holding a bed, but has less than one bed,
                        inventoryQty[inventorySlot] = 0
                        inventoryItems[inventorySlot] = 0 
                        # Reset the values, since the user has no bed. 
                        # This is to troubleshoot a glitch.                        
                elif event.key == pygame.K_q: # if that key is Q,
                    qpressed = True # set the variable representing whether the key Q is pressed to true.
            if event.type == pygame.KEYUP: # if you are releasing any key on your keyboard,
                if event.key == pygame.K_w: # if that key is W,
                    keys[0] = False # set the 0th item of the list representing whether the keys WSAD are pressed to false. 
                if event.key == pygame.K_s: # if that key is S,
                    keys[1] = False # set the 1st item of the list representing whether the keys WSAD are pressed to false. 
                if event.key == pygame.K_a: # if that key is A,
                    keys[2] = False # set the 2nd item of the list representing whether the keys WSAD are pressed to false. 
                if event.key == pygame.K_d: # if that key is D,
                    keys[3] = False # set the 3rd item of the list representing whether the keys WSAD are pressed to false. 
                if event.key == pygame.K_q: # if that key is Q,
                    qpressed = False # set the variable representing whether the key Q is pressed to false.              
    pos = pygame.mouse.get_pos() # Get the coordinates of the mouse pointer as a list.
    mouse_x = pos[0] 
    mouse_y = pos[1]
    # Separate that list into two variables that individually represent the x and y coords of the mouse pointer.
    pygame.mixer.Sound.play(music)
    if page != 3: # If the player is not in game,
        i = 0 # set i to 0. 
        for col in range(0, 800, 44): # Starting at 0 and ending on or past 800, increment col by 44.
            for row in range(0, 1000, 44): # Starting at 0 and ending on or past 1000, increment row by 44.
                screen.blit(background[i], [row, col]) # Blit the ith element of the background grass tile list onto the screen at x = row, y = col.
                i += 1 # Increment i by 1. 
        # Essentially what this does is it shows the background previously generated numerically in a list and puts it onto the screen.
    if page == 0: # If the player is in the main menu,
        adventuretitle = custom_font.render("Adventure", True, BLUE)
        screen.blit(adventuretitle, [320, 150])
        # Blitting the title with the custom font.
        button(425, 575, 300, 360, LIGHTYELLOW, BLACK, "Play", BLACK, "Calibri", 40, 1)
        button(425, 575, 400, 460, LIGHTYELLOW, BLACK, "Settings", BLACK, "Calibri", 40, 2)
        button(425, 575, 500, 560, LIGHTYELLOW, BLACK, "How to play", BLACK, "Calibri", 25, 4)
        title(325, 600, 360, 50, LIGHTGREEN, BLACK, "Gem highscore: " + gemscore, BLACK, "Calibri", 20)
        # Show the title, high score, and the different menu options.
    elif page == 1: # If the player is in the pregame menu,
        title(425, 50, 165, 65, WHITE, BLACK, "Pregame", BLACK, "Calibri", 40)
        title(200, 200, 120, 45, WHITE, BLACK, "Difficulty", BLACK, "Calibri", 28)
        togglebutton(200, 320, 250, 310, LIGHTGREEN, BLACK, "Easy", BLACK, "Calibri", 28, pregamechoices, 0, 1)
        togglebutton(370, 490, 250, 310, LIGHTYELLOW, BLACK, "Medium", BLACK, "Calibri", 28, pregamechoices, 0, 2)
        togglebutton(540, 660, 250, 310, LIGHTRED, BLACK, "Hard", BLACK, "Calibri", 28, pregamechoices, 0, 3)
        title(200, 370, 150, 45, WHITE, BLACK, "Timer on?", BLACK, "Calibri", 28)
        togglebutton(200, 320, 430, 480, LIGHTGREEN, BLACK, "Yes", BLACK, "Calibri", 28, pregamechoices, 1, True)
        togglebutton(370, 490, 430, 480, LIGHTRED, BLACK, "No", BLACK, "Calibri", 28, pregamechoices, 1, False)        
        title(200, 540, 150, 45, WHITE, BLACK, "Day length", BLACK, "Calibri", 28)
        togglebutton(200, 320, 590, 640, LIGHTGREEN, BLACK, "7 min", BLACK, "Calibri", 28, pregamechoices, 2, 1)
        togglebutton(370, 490, 590, 640, LIGHTYELLOW, BLACK, "5 min", BLACK, "Calibri", 28, pregamechoices, 2, 2)
        togglebutton(540, 660, 590, 640, LIGHTRED, BLACK, "4 min", BLACK, "Calibri", 28, pregamechoices, 2, 3)        
        button(35, 150, 700, 745, LIGHTRED, BLACK, "Back", BLACK, "Calibri", 28, 0)   
        button(835, 950, 700, 745, LIGHTGREEN, BLACK, "Next", BLACK, "Calibri", 28, 3)
        # Show the pregame options.
        if pregamechoices[2] == 1: # If you chose for your day to be 7 mins long, 
            daylength = 420000 # set the day length to 7 mins in ms.
        elif pregamechoices[2] == 2: # If you chose for your day to be 5 mins long, 
            daylength = 300000 # set the day length to 5 mins in ms.
        else: # Otherwise, 
            daylength = 240000 # set the day length to 4 mins in ms.       
    elif page == 2: # If the player is in the settings menu,
        title(425, 50, 150, 65, WHITE, BLACK, "Settings", BLACK, "Calibri", 40)
        button(35, 150, 700, 745, LIGHTRED, BLACK, "Back", BLACK, "Calibri", 28, 0)
        title(200, 370, 210, 45, WHITE, BLACK, "Hitboxes on?", BLACK, "Calibri", 28)
        togglebutton(200, 320, 430, 480, LIGHTGREEN, BLACK, "Yes", BLACK, "Calibri", 28, pregamechoices, 4, True)
        togglebutton(370, 490, 430, 480, LIGHTRED, BLACK, "No", BLACK, "Calibri", 28, pregamechoices, 4, False)                
    elif page == 3: # If the player is in the ingame menu,
        if health < 0: # If the players health is less than 0, 
            page = 5 # go to the end screen.
        time += clock.get_rawtime() # Add the exact time in ms that went by in the last tick to the variable representing time in ms.
        inGameBgRender() # Render the in game background, the grass tiles.
        minesRender() # Render the mines that have been placed down.
        bedsRender() # Render the beds that have been placed down.
        hitcooldown += cooldown # Add the constant variable cooldown to the variable representing total hit cooldown.  
        if hitcooldown > 5: # If the variable representing total hit cool down is greater than 5,
            hitcooldown = 5 # set it to 5.
        bar(hitcooldown, BLUE, 5, 480, 265, 75, 15, "Hit cooldown") 
        # Create a bar positioned at x = 480, y = 265, with a width of 75 and a height of 15. The text beside it will be "Hit cooldown". The bar color will be blue, and controlled by the variable representing the total hit cool down. Its max value will be 5.
        if mining > 0: # If the variable representing the cooldown for mining is more than 0, 
            mining -= 0.05 # subtract 0.05 from it.
        bar(mining, GREEN, 10, 480, 315, 75, 15, "Mining") 
        # Create a bar positioned at x = 480, y = 315, with a width of 75 and a height of 15. The text beside it will be "Mining". The bar color will be green, and controlled by the variable representing the total mining cool down. Its max value will be 10.
        bar(health, RED, 10, 480, 290, 75, 15, "Health")
        # Create a bar positioned at x = 480, y = 290, with a width of 75 and a height of 15. The text beside it will be "Health". The bar color will be red, and controlled by the variable representing the health of the player. Its max value will be 10.
        if time >= daylength: # If the time is greater than or equal to the day length, 
            time = 0 # set the time to 0. 
            days += 1 # Change the variable representing the number of days that have gone by by 1.
            timestate = "Day" # Set the variable representing whether it is day or night to "Day". 
            spawning = False # Set the variable representing zombie spawning to False.   
        elif time >= daylength - 120000 and spawning == False: # Otherwise, if the time is greater than the daylength in ms subtracted by 2 minutes in ms, and the variable representing zombie spawning is False,
            timestate = "Night" # Set the variable representing whether it is day or night to Night".
            for i in range((pregamechoices[0] * 2) + days * 2): # Starting at 0 and ending on or past the product of the game difficulty as an integer and 5, added to the product of the amount of days gone by mulitplied by 3, increment i by 1.
                zombieInit(random.randrange(0, 3000) - 1500, random.randrange(0, 3000) - 1500, 10, 10)
                # Initialize the zombies, and set their x and y coordinates to a random number from -1500 to 1499 for both coords. 
            spawning = True 
            # Set the variable representing zombie spwaning to true.
        if len(zombieHP) > 0: # If the amount of zombies is more than 0,
            zombieUpdate() # update the zombie positions.
        screen.blit(playerrotation, [475, 350])
        # Blit the rotation of the player on the screen.
        resourceRender() # Render the resources.
        inventoryUpdate() # Update the inventory.
        togglebutton(710, 860, 60, 100, LIGHTYELLOW, BLACK, "Crafting", BLACK, "Calibri", 30, pregamechoices, 5, True)
        # Create the button for crafting.
        title(80, 150, 100, 50, LIGHTYELLOW, BLACK, "Days: " + str(days), BLACK, "Calibri", 30)
        title(80, 250, 205, 50, LIGHTYELLOW, BLACK, "Time of day: " + timestate, BLACK, "Calibri", 22)
        # Create the indicator for the amount of days that went by and the time of day.
        if pregamechoices[5] == True: # If the crafting menu is open,
            pygame.draw.rect(screen, LIGHTGREEN, [40, 40, 920, 740])
            pygame.draw.rect(screen, BLACK, [40, 40, 920, 740], 10)
            # Draw a background for the menu.
            togglebutton(90, 240, 60, 100, LIGHTRED, BLACK, "Back", BLACK, "Calibri", 30, pregamechoices, 5, False)
            # Create a button allowing you to go back.
            for i in range(5): # Starting at 0 and ending on or past 5, increment i by 1.
                title(90, 205 + i * 65, 230, 40, LIGHTYELLOW, BLACK, recipes[i], BLACK, "Calibri", 20)
                togglebutton(330, 435, 205 + i * 65, 245 + i * 65, LIGHTRED, BLACK, "Craft", BLACK, "Calibri", 30, recipeShowing, i, True)
                # Show the ith recipe title, along with the craft button.
                # The reason that the y position is 205 + i * 65 is because we want the menu to start at y = 205, then each time the loop repeats, it shows the next menu item 65 px down.
            for i in range(4): # Starting at 0 and ending on or past 4, increment i by 1.
                title(460, 205 + i * 65, 230, 40, LIGHTYELLOW, BLACK, recipes[i + 5], BLACK, "Calibri", 20)
                togglebutton(700, 815, 205 + i * 65, 245 + i * 65, LIGHTRED, BLACK, "Craft", BLACK, "Calibri", 30, recipeShowing, i + 5, True) 
                # Show the ith recipe title, along with the craft button.
                # The reason that the y position is 205 + i * 65 is because we want the menu to start at y = 205, then each time the loop repeats, it shows the next menu item 65 px down.                
            for i in range(len(recipes)): # Starting at 0, and ending on or after the length of the list of recipes, increment i by 1.
                if recipeShowing[i] == True: # If the ith recipe is clicked, 
                    if i == 0: # If i is 0,
                        craft(i, 6, 1) # craft a wooden club.
                    elif i == 1: # If i is 1,
                        craft(i, 7, 1) # craft a stone pick.
                    elif i == 2: # If i is 2,
                        craft(i, 8, 1) # craft a stone spear.
                    elif i == 3: # If i is 3,
                        craft(i, 11, 1) # craft an iron sword.
                    elif i == 4: # If i is 4,
                        craft(i, 12, 1) # craft an iron pick.
                    elif i == 5: # If i is 5,
                        craft(i, 13, 1) # craft wood planks.
                    elif i == 6: # If i is 6,
                        craft(i, 9, 1) # craft a mine.
                    elif i == 7: # If i is 7,
                        craft(i, 14, 1) # craft a bed.                   
                    elif i == 8: # If i is 8,
                        craft(i, 4, 3) # craft 3 sticks.
                    inventoryTroubleshoot()
                    recipeShowing[i] = False
        else: # Otherwise, 
            if keys[0] == True: # If W is being pressed, 
                playerY -= 7 # move the player up by 7 px.
                playerrotation = pygame.transform.rotate(player, 0)
                # Rotate the player to make it point 0 degrees.
            elif keys[1] == True: # If S is being pressed, 
                playerY += 7 # move the player down by 7 px.
                playerrotation = pygame.transform.rotate(player, 180)
                # Rotate the player to make it point 180 degrees.
            elif keys[2] == True: # If A is being pressed, 
                playerX -= 7 # move the player right by 7 px.
                playerrotation = pygame.transform.rotate(player, 90) 
                # Rotate the player to make it point 90 degrees.
            elif keys[3] == True: # If D is being pressed, 
                playerX += 7 # move the player left by 7 px.
                playerrotation = pygame.transform.rotate(player, 270)
                # Rotate the player to make it point 270 degrees.
            if pregamechoices[1] == True:
                title(80, 60, 230, 50, LIGHTYELLOW, BLACK, str(time / 1000) + " secs", BLACK, "Calibri", 35) 
    elif page == 4: # If the player is in the how to play menu,
        pygame.draw.rect(screen, LIGHTGREEN, [240, 40, 560, 700])     
        title(400, 50, 220, 65, WHITE, BLACK, "How to play", BLACK, "Calibri", 35)
        title(270, 150, 220, 65, LIGHTGREEN, LIGHTGREEN, "Use WASD to move around!", BLACK, "Calibri", 18)
        title(270, 250, 220, 65, LIGHTGREEN, LIGHTGREEN, "Use E to place mines!", BLACK, "Calibri", 18)
        title(270, 350, 220, 65, LIGHTGREEN, LIGHTGREEN, "Use left click to attack zombies and harvest resources!", BLACK, "Calibri", 18)
        title(270, 450, 220, 65, LIGHTGREEN, LIGHTGREEN, "Use Q to fuel mines and to sleep in beds!", BLACK, "Calibri", 18)
        title(270, 550, 220, 65, LIGHTGREEN, LIGHTGREEN, "Use R to upgrade mines!", BLACK, "Calibri", 18)
        title(270, 650, 220, 65, LIGHTGREEN, LIGHTGREEN, "Get as many gems as possible.", BLACK, "Calibri", 18)
        button(35, 150, 700, 745, LIGHTRED, BLACK, "Back", BLACK, "Calibri", 28, 0)
        # Show all of the instructions on how to play, along with a back button. 
    else: # Otherwise,
        pygame.draw.rect(screen, BLACK, [0, 0, 1000, 800]) # Make the whole screen black.  
        title(400, 300, 220, 65, BLACK, RED, "You Died!", RED, "Calibri", 35) # Display "You Died!" in red text on the screen.
        g = open("score.txt", "w") # open the text file containing the high score of the player.
        if 10 in inventoryItems: # If there are gems in the players inventory, 
            if inventoryQty[inventoryItems.index(10)] > int(gemscore): # if the quantity of those gems exceed the quantity of the gems in the highscore, 
                g.write(str(inventoryQty[inventoryItems.index(10)])) # replace the current file with the amount of gems gained this game.
        g.close() # Close the file.
        done = True # Set done to true, ending the while loop.
    pygame.display.flip() # Make all drawings show up from memory to the screen.
    clock.tick(60) # Make the game run on 60 fps.
pygame.quit() # Quit pygame. This happens when done = True and the while loop is over.