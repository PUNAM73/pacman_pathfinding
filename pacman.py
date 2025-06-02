# # # # # # import pygame
# # # # # # import sys
# # # # # # from astar import astar


# # # # # # black = (0,0,0)
# # # # # # white = (255,255,255)
# # # # # # blue = (0,0,255)
# # # # # # green = (0,255,0)
# # # # # # red = (255,0,0)
# # # # # # purple = (255,0,255)
# # # # # # yellow   = ( 255, 255,   0)

# # # # # # Trollicon=pygame.image.load('images/Trollman.png')
# # # # # # pygame.display.set_icon(Trollicon)

# # # # # # #Add music
# # # # # # pygame.mixer.init()
# # # # # # pygame.mixer.music.load('pacman.mp3')
# # # # # # pygame.mixer.music.play(-1, 0.0)

# # # # # # # This class represents the bar at the bottom that the player controls
# # # # # # class Wall(pygame.sprite.Sprite):
# # # # # #     # Constructor function
# # # # # #     def __init__(self,x,y,width,height, color):
# # # # # #         # Call the parent's constructor
# # # # # #         pygame.sprite.Sprite.__init__(self)
  
# # # # # #         # Make a blue wall, of the size specified in the parameters
# # # # # #         self.image = pygame.Surface([width, height])
# # # # # #         self.image.fill(color)
  
# # # # # #         # Make our top-left corner the passed-in location.
# # # # # #         self.rect = self.image.get_rect()
# # # # # #         self.rect.top = y
# # # # # #         self.rect.left = x

# # # # # # # This creates all the walls in room 1
# # # # # # def setupRoomOne(all_sprites_list):
# # # # # #     # Make the walls. (x_pos, y_pos, width, height)
# # # # # #     wall_list=pygame.sprite.RenderPlain()
     
# # # # # #     # This is a list of walls. Each is in the form [x, y, width, height]
# # # # # #     walls = [ [0,0,6,600],[0,0,600,6],[0,600,606,6],[600,0,6,606],[300,0,6,66],[60,60,186,6],[360,60,186,6],[60,120,66,6],[60,120,6,126],
# # # # # #               [180,120,246,6],[300,120,6,66],[480,120,66,6],[540,120,6,126],[120,180,126,6],[120,180,6,126],[360,180,126,6],[480,180,6,126],
# # # # # #               [180,240,6,126],[180,360,246,6],[420,240,6,126],[240,240,42,6],[324,240,42,6],[240,240,6,66],[240,300,126,6],[360,240,6,66],
# # # # # #               [0,300,66,6],[540,300,66,6],[60,360,66,6],[60,360,6,186],[480,360,66,6],[540,360,6,186],[120,420,366,6],[120,420,6,66],
# # # # # #               [480,420,6,66],[180,480,246,6],[300,480,6,66],[120,540,126,6],[360,540,126,6]]
     
# # # # # #     # Loop through the list. Create the wall, add it to the list
# # # # # #     for item in walls:
# # # # # #         wall=Wall(item[0],item[1],item[2],item[3],blue)
# # # # # #         wall_list.add(wall)
# # # # # #         all_sprites_list.add(wall)
         
# # # # # #     # return our new list
# # # # # #     return wall_list

# # # # # # def setupGate(all_sprites_list):
# # # # # #       gate = pygame.sprite.RenderPlain()
# # # # # #       gate.add(Wall(282,242,42,2,white))
# # # # # #       all_sprites_list.add(gate)
# # # # # #       return gate

# # # # # # # This class represents the ball        
# # # # # # # It derives from the "Sprite" class in Pygame
# # # # # # class Block(pygame.sprite.Sprite):
     
# # # # # #     # Constructor. Pass in the color of the block, 
# # # # # #     # and its x and y position
# # # # # #     def __init__(self, color, width, height):
# # # # # #         # Call the parent class (Sprite) constructor
# # # # # #         pygame.sprite.Sprite.__init__(self) 
 
# # # # # #         # Create an image of the block, and fill it with a color.
# # # # # #         # This could also be an image loaded from the disk.
# # # # # #         self.image = pygame.Surface([width, height])
# # # # # #         self.image.fill(white)
# # # # # #         self.image.set_colorkey(white)
# # # # # #         pygame.draw.ellipse(self.image,color,[0,0,width,height])
 
# # # # # #         # Fetch the rectangle object that has the dimensions of the image
# # # # # #         # image.
# # # # # #         # Update the position of this object by setting the values 
# # # # # #         # of rect.x and rect.y
# # # # # #         self.rect = self.image.get_rect() 

# # # # # # # This class represents the bar at the bottom that the player controls
# # # # # # class Player(pygame.sprite.Sprite):
  
# # # # # #     # Set speed vector
# # # # # #     change_x=0
# # # # # #     change_y=0
  
# # # # # #     # Constructor function
# # # # # #     def __init__(self,x,y, filename):
# # # # # #         # Call the parent's constructor
# # # # # #         pygame.sprite.Sprite.__init__(self)
   
# # # # # #         # Set height, width
# # # # # #         self.image = pygame.image.load(filename).convert()
  
# # # # # #         # Make our top-left corner the passed-in location.
# # # # # #         self.rect = self.image.get_rect()
# # # # # #         self.rect.top = y
# # # # # #         self.rect.left = x
# # # # # #         self.prev_x = x
# # # # # #         self.prev_y = y

# # # # # #     # Clear the speed of the player
# # # # # #     def prevdirection(self):
# # # # # #         self.prev_x = self.change_x
# # # # # #         self.prev_y = self.change_y

# # # # # #     # Change the speed of the player
# # # # # #     def changespeed(self,x,y):
# # # # # #         self.change_x+=x
# # # # # #         self.change_y+=y
          
# # # # # #     # Find a new position for the player
# # # # # #     def update(self,walls,gate):
# # # # # #         # Get the old position, in case we need to go back to it
        
# # # # # #         old_x=self.rect.left
# # # # # #         new_x=old_x+self.change_x
# # # # # #         prev_x=old_x+self.prev_x
# # # # # #         self.rect.left = new_x
        
# # # # # #         old_y=self.rect.top
# # # # # #         new_y=old_y+self.change_y
# # # # # #         prev_y=old_y+self.prev_y

# # # # # #         # Did this update cause us to hit a wall?
# # # # # #         x_collide = pygame.sprite.spritecollide(self, walls, False)
# # # # # #         if x_collide:
# # # # # #             # Whoops, hit a wall. Go back to the old position
# # # # # #             self.rect.left=old_x
            
# # # # # #         else:

# # # # # #             self.rect.top = new_y

# # # # # #             # Did this update cause us to hit a wall?
# # # # # #             y_collide = pygame.sprite.spritecollide(self, walls, False)
# # # # # #             if y_collide:
# # # # # #                 # Whoops, hit a wall. Go back to the old position
# # # # # #                 self.rect.top=old_y

# # # # # #         if gate != False:
# # # # # #           gate_hit = pygame.sprite.spritecollide(self, gate, False)
# # # # # #           if gate_hit:
# # # # # #             self.rect.left=old_x
# # # # # #             self.rect.top=old_y

# # # # # # #Inheritime Player klassist
# # # # # # class Ghost(Player):
# # # # # #     # Change the speed of the ghost
# # # # # #     def changespeed(self,list,ghost,turn,steps,l):
# # # # # #       try:
# # # # # #         z=list[turn][2]
# # # # # #         if steps < z:
# # # # # #           self.change_x=list[turn][0]
# # # # # #           self.change_y=list[turn][1]
# # # # # #           steps+=1
# # # # # #         else:
# # # # # #           if turn < l:
# # # # # #             turn+=1
# # # # # #           elif ghost == "clyde":
# # # # # #             turn = 2
# # # # # #           else:
# # # # # #             turn = 0
# # # # # #           self.change_x=list[turn][0]
# # # # # #           self.change_y=list[turn][1]
# # # # # #           steps = 0
# # # # # #         return [turn,steps]
# # # # # #       except IndexError:
# # # # # #          return [0,0]

# # # # # # Pinky_directions = [[0,-30,4],[15,0,9],[0,15,11],[-15,0,23],[0,15,7],[15,0,3],[0,-15,3],[15,0,19],[0,15,3],[15,0,3],[0,15,3],
# # # # # #                     [15,0,3],[0,-15,15],[-15,0,7],[0,15,3],[-15,0,19],[0,-15,11],[15,0,9]]

# # # # # # Blinky_directions = [[0,-15,4],[15,0,9],[0,15,11],[15,0,3],[0,15,7],[-15,0,11],[0,15,3],[15,0,15],[0,-15,15],[15,0,3],[0,-15,11],
# # # # # #                      [-15,0,3],[0,-15,11],[-15,0,3],[0,-15,3],[-15,0,7],[0,-15,3],[15,0,15],[0,15,15],[-15,0,3],[0,15,3],[-15,0,3],
# # # # # #                      [0,-15,7],[-15,0,3],[0,15,7],[-15,0,11],[0,-15,7],[15,0,5]]

# # # # # # Inky_directions = [[30,0,2],[0,-15,4],[15,0,10],[0,15,7],[15,0,3],[0,-15,3],[15,0,3],[0,-15,15],[-15,0,15],[0,15,3],[15,0,15],[0,15,11],
# # # # # #                     [-15,0,3],[0,-15,7],[-15,0,11],[0,15,3],[-15,0,11],[0,15,7],[-15,0,3],[0,-15,3],[-15,0,3],[0,-15,15],[15,0,15],
# # # # # #                     [0,15,3],[-15,0,15],[0,15,11],[15,0,3],[0,-15,11],[15,0,11],[0,15,3],[15,0,1],]

# # # # # # Clyde_directions = [[-30,0,2],[0,-15,4],[15,0,5],[0,15,7],[-15,0,11],[0,-15,7],[-15,0,3],[0,15,7],[-15,0,7],[0,15,15],[15,0,15],[0,-15,3],
# # # # # #                     [-15,0,11],[0,-15,7],[15,0,3],[0,-15,11],[15,0,9],]

# # # # # # pl = len(Pinky_directions)-1
# # # # # # bl = len(Blinky_directions)-1
# # # # # # il = len(Inky_directions)-1
# # # # # # cl = len(Clyde_directions)-1

# # # # # # # Call this function so the Pygame library can initialize itself
# # # # # # pygame.init()
  
# # # # # # # Create an 606x606 sized screen
# # # # # # screen = pygame.display.set_mode([606, 606])

# # # # # # # This is a list of 'sprites.' Each block in the program is
# # # # # # # added to this list. The list is managed by a class called 'RenderPlain.'


# # # # # # # Set the title of the window
# # # # # # pygame.display.set_caption('Pacman')

# # # # # # # Create a surface we can draw on
# # # # # # background = pygame.Surface(screen.get_size())

# # # # # # # Used for converting color maps and such
# # # # # # background = background.convert()
  
# # # # # # # Fill the screen with a black background
# # # # # # background.fill(black)
# # # # # # clock = pygame.time.Clock()

# # # # # # pygame.font.init()
# # # # # # font = pygame.font.Font("freesansbold.ttf", 24)

# # # # # # #default locations for Pacman and monstas
# # # # # # w = 303-16 #Width
# # # # # # p_h = (7*60)+19 #Pacman height
# # # # # # m_h = (4*60)+19 #Monster height
# # # # # # b_h = (3*60)+19 #Binky height
# # # # # # i_w = 303-16-32 #Inky width
# # # # # # c_w = 303+(32-16) #Clyde width

# # # # # # def startGame():

# # # # # #   all_sprites_list = pygame.sprite.RenderPlain()

# # # # # #   block_list = pygame.sprite.RenderPlain()

# # # # # #   monsta_list = pygame.sprite.RenderPlain()

# # # # # #   pacman_collide = pygame.sprite.RenderPlain()

# # # # # #   wall_list = setupRoomOne(all_sprites_list)

# # # # # #   gate = setupGate(all_sprites_list)

# # # # # #   p_turn = 0
# # # # # #   p_steps = 0

# # # # # #   b_turn = 0
# # # # # #   b_steps = 0

# # # # # #   i_turn = 0
# # # # # #   i_steps = 0

# # # # # #   c_turn = 0
# # # # # #   c_steps = 0

# # # # # #   # Create the player paddle object
# # # # # #   Pacman = Player( w, p_h, "images/Trollman.png" )
# # # # # #   all_sprites_list.add(Pacman)
# # # # # #   pacman_collide.add(Pacman)
   
# # # # # #   Blinky=Ghost( w, b_h, "images/Blinky.png" )
# # # # # #   monsta_list.add(Blinky)
# # # # # #   all_sprites_list.add(Blinky)

# # # # # #   Pinky=Ghost( w, m_h, "images/Pinky.png" )
# # # # # #   monsta_list.add(Pinky)
# # # # # #   all_sprites_list.add(Pinky)
   
# # # # # #   Inky=Ghost( i_w, m_h, "images/Inky.png" )
# # # # # #   monsta_list.add(Inky)
# # # # # #   all_sprites_list.add(Inky)
   
# # # # # #   Clyde=Ghost( c_w, m_h, "images/Clyde.png" )
# # # # # #   monsta_list.add(Clyde)
# # # # # #   all_sprites_list.add(Clyde)

# # # # # #   # Draw the grid
# # # # # #   for row in range(19):
# # # # # #       for column in range(19):
# # # # # #           if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
# # # # # #               continue
# # # # # #           else:
# # # # # #             block = Block(yellow, 4, 4)

# # # # # #             # Set a random location for the block
# # # # # #             block.rect.x = (30*column+6)+26
# # # # # #             block.rect.y = (30*row+6)+26

# # # # # #             b_collide = pygame.sprite.spritecollide(block, wall_list, False)
# # # # # #             p_collide = pygame.sprite.spritecollide(block, pacman_collide, False)
# # # # # #             if b_collide:
# # # # # #               continue
# # # # # #             elif p_collide:
# # # # # #               continue
# # # # # #             else:
# # # # # #               # Add the block to the list of objects
# # # # # #               block_list.add(block)
# # # # # #               all_sprites_list.add(block)

# # # # # #   bll = len(block_list)

# # # # # #   score = 0

# # # # # #   done = False

# # # # # #   i = 0

# # # # # #   while done == False:
# # # # # #       # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
# # # # # #       for event in pygame.event.get():
# # # # # #           if event.type == pygame.QUIT:
# # # # # #               done=True

# # # # # #           if event.type == pygame.KEYDOWN:
# # # # # #               if event.key == pygame.K_LEFT:
# # # # # #                   Pacman.changespeed(-30,0)
# # # # # #               if event.key == pygame.K_RIGHT:
# # # # # #                   Pacman.changespeed(30,0)
# # # # # #               if event.key == pygame.K_UP:
# # # # # #                   Pacman.changespeed(0,-30)
# # # # # #               if event.key == pygame.K_DOWN:
# # # # # #                   Pacman.changespeed(0,30)

# # # # # #           if event.type == pygame.KEYUP:
# # # # # #               if event.key == pygame.K_LEFT:
# # # # # #                   Pacman.changespeed(30,0)
# # # # # #               if event.key == pygame.K_RIGHT:
# # # # # #                   Pacman.changespeed(-30,0)
# # # # # #               if event.key == pygame.K_UP:
# # # # # #                   Pacman.changespeed(0,30)
# # # # # #               if event.key == pygame.K_DOWN:
# # # # # #                   Pacman.changespeed(0,-30)
          
# # # # # #       # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
   
# # # # # #       # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
# # # # # #       Pacman.update(wall_list,gate)

# # # # # #       returned = Pinky.changespeed(Pinky_directions,False,p_turn,p_steps,pl)
# # # # # #       p_turn = returned[0]
# # # # # #       p_steps = returned[1]
# # # # # #       Pinky.changespeed(Pinky_directions,False,p_turn,p_steps,pl)
# # # # # #       Pinky.update(wall_list,False)

# # # # # #       returned = Blinky.changespeed(Blinky_directions,False,b_turn,b_steps,bl)
# # # # # #       b_turn = returned[0]
# # # # # #       b_steps = returned[1]
# # # # # #       Blinky.changespeed(Blinky_directions,False,b_turn,b_steps,bl)
# # # # # #       Blinky.update(wall_list,False)

# # # # # #       returned = Inky.changespeed(Inky_directions,False,i_turn,i_steps,il)
# # # # # #       i_turn = returned[0]
# # # # # #       i_steps = returned[1]
# # # # # #       Inky.changespeed(Inky_directions,False,i_turn,i_steps,il)
# # # # # #       Inky.update(wall_list,False)

# # # # # #       returned = Clyde.changespeed(Clyde_directions,"clyde",c_turn,c_steps,cl)
# # # # # #       c_turn = returned[0]
# # # # # #       c_steps = returned[1]
# # # # # #       Clyde.changespeed(Clyde_directions,"clyde",c_turn,c_steps,cl)
# # # # # #       Clyde.update(wall_list,False)

# # # # # #       # See if the Pacman block has collided with anything.
# # # # # #       blocks_hit_list = pygame.sprite.spritecollide(Pacman, block_list, True)
       
# # # # # #       # Check the list of collisions.
# # # # # #       if len(blocks_hit_list) > 0:
# # # # # #           score +=len(blocks_hit_list)
      
# # # # # #       # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
   
# # # # # #       # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
# # # # # #       screen.fill(black)
        
# # # # # #       wall_list.draw(screen)
# # # # # #       gate.draw(screen)
# # # # # #       all_sprites_list.draw(screen)
# # # # # #       monsta_list.draw(screen)

# # # # # #       text=font.render("Score: "+str(score)+"/"+str(bll), True, red)
# # # # # #       screen.blit(text, [10, 10])

# # # # # #       if score == bll:
# # # # # #         doNext("Congratulations, you won!",145,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)

# # # # # #       monsta_hit_list = pygame.sprite.spritecollide(Pacman, monsta_list, False)

# # # # # #       if monsta_hit_list:
# # # # # #         doNext("Game Over",235,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate)

# # # # # #       # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
      
# # # # # #       pygame.display.flip()
    
# # # # # #       clock.tick(10)

# # # # # # def doNext(message,left,all_sprites_list,block_list,monsta_list,pacman_collide,wall_list,gate):
# # # # # #   while True:
# # # # # #       # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
# # # # # #       for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #           pygame.quit()
# # # # # #         if event.type == pygame.KEYDOWN:
# # # # # #           if event.key == pygame.K_ESCAPE:
# # # # # #             pygame.quit()
# # # # # #           if event.key == pygame.K_RETURN:
# # # # # #             del all_sprites_list
# # # # # #             del block_list
# # # # # #             del monsta_list
# # # # # #             del pacman_collide
# # # # # #             del wall_list
# # # # # #             del gate
# # # # # #             startGame()

# # # # # #       #Grey background
# # # # # #       w = pygame.Surface((400,200))  # the size of your rect
# # # # # #       w.set_alpha(10)                # alpha level
# # # # # #       w.fill((128,128,128))           # this fills the entire surface
# # # # # #       screen.blit(w, (100,200))    # (0,0) are the top-left coordinates

# # # # # #       #Won or lost
# # # # # #       text1=font.render(message, True, white)
# # # # # #       screen.blit(text1, [left, 233])

# # # # # #       text2=font.render("To play again, press ENTER.", True, white)
# # # # # #       screen.blit(text2, [135, 303])
# # # # # #       text3=font.render("To quit, press ESCAPE.", True, white)
# # # # # #       screen.blit(text3, [165, 333])

# # # # # #       pygame.display.flip()

# # # # # #       clock.tick(10)

# # # # # # startGame()

# # # # # # pygame.quit()

# # # # # # print("Game is starting...")




# # # # import pygame
# # # # import sys
# # # # # You mentioned "from astar import astar"
# # # # # I'll assume astar(start, goal, grid) returns a list of (row, col) tuples for path
# # # # from astar import astar  # Ensure this is your A* implementation returning path as list of cells

# # # # black = (0, 0, 0)
# # # # white = (255, 255, 255)
# # # # blue = (0, 0, 255)

# # # # GRID_SIZE = 15  # Each tile is 15x15 px
# # # # ROWS, COLS = 606 // GRID_SIZE, 606 // GRID_SIZE

# # # # pygame.init()
# # # # pygame.mixer.init()

# # # # Trollicon = pygame.image.load('images/Trollman.png')
# # # # pygame.display.set_icon(Trollicon)
# # # # pygame.mixer.music.load('pacman.mp3')
# # # # pygame.mixer.music.play(-1, 0.0)

# # # # class Wall(pygame.sprite.Sprite):
# # # #     def __init__(self, x, y, width, height, color):
# # # #         super().__init__()
# # # #         self.image = pygame.Surface([width, height])
# # # #         self.image.fill(color)
# # # #         self.rect = self.image.get_rect(topleft=(x, y))

# # # # def setupRoomOne(all_sprites_list):
# # # #     wall_list = pygame.sprite.RenderPlain()
# # # #     walls = [
# # # #         [0, 0, 6, 600], [0, 0, 600, 6], [0, 600, 606, 6], [600, 0, 6, 606],
# # # #         [300, 0, 6, 66], [60, 60, 186, 6], [360, 60, 186, 6], [60, 120, 66, 6],
# # # #         [60, 120, 6, 126], [180, 120, 246, 6], [300, 120, 6, 66], [480, 120, 66, 6],
# # # #         [540, 120, 6, 126], [120, 180, 126, 6], [120, 180, 6, 126], [360, 180, 126, 6],
# # # #         [480, 180, 6, 126], [180, 240, 6, 126], [180, 360, 246, 6], [420, 240, 6, 126],
# # # #         [240, 240, 42, 6], [324, 240, 42, 6], [240, 240, 6, 66], [240, 300, 126, 6],
# # # #         [360, 240, 6, 66], [0, 300, 66, 6], [540, 300, 66, 6], [60, 360, 66, 6],
# # # #         [60, 360, 6, 186], [480, 360, 66, 6], [540, 360, 6, 186], [120, 420, 366, 6],
# # # #         [120, 420, 6, 66], [480, 420, 6, 66], [180, 480, 246, 6], [300, 480, 6, 66],
# # # #         [120, 540, 126, 6], [360, 540, 126, 6]
# # # #     ]
# # # #     for item in walls:
# # # #         wall = Wall(*item, blue)
# # # #         wall_list.add(wall)
# # # #         all_sprites_list.add(wall)
# # # #     return wall_list

# # # # def generate_grid(wall_list):
# # # #     grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
# # # #     for wall in wall_list:
# # # #         x = wall.rect.x // GRID_SIZE
# # # #         y = wall.rect.y // GRID_SIZE
# # # #         w = wall.rect.width // GRID_SIZE
# # # #         h = wall.rect.height // GRID_SIZE
# # # #         for dx in range(w):
# # # #             for dy in range(h):
# # # #                 grid[y + dy][x + dx] = 1
# # # #     return grid

# # # # def setupGate(all_sprites_list):
# # # #     gate = pygame.sprite.RenderPlain()
# # # #     gate.add(Wall(282, 242, 42, 2, white))
# # # #     all_sprites_list.add(gate)
# # # #     return gate

# # # # class Player(pygame.sprite.Sprite):
# # # #     def __init__(self, x, y, filename):
# # # #         super().__init__()
# # # #         self.image = pygame.image.load(filename).convert()
# # # #         self.rect = self.image.get_rect(topleft=(x, y))
# # # #         self.change_x = 0
# # # #         self.change_y = 0

# # # #     def changespeed(self, x, y):
# # # #         self.change_x += x
# # # #         self.change_y += y

# # # #     def update(self, walls, gate):
# # # #         old_x = self.rect.left
# # # #         old_y = self.rect.top

# # # #         new_x = old_x + self.change_x
# # # #         new_y = old_y + self.change_y

# # # #         self.rect.left = new_x
# # # #         if pygame.sprite.spritecollideany(self, walls):
# # # #             self.rect.left = old_x
# # # #         else:
# # # #             self.rect.top = new_y
# # # #             if pygame.sprite.spritecollideany(self, walls):
# # # #                 self.rect.top = old_y

# # # #         if gate:
# # # #             if pygame.sprite.spritecollideany(self, gate):
# # # #                 self.rect.left = old_x
# # # #                 self.rect.top = old_y

# # # #     def get_grid_position(self):
# # # #         return (self.rect.top // GRID_SIZE, self.rect.left // GRID_SIZE)


# # # # class Ghost(Player):
# # # #     def get_grid_position(self):
# # # #         return (self.rect.top // GRID_SIZE, self.rect.left // GRID_SIZE)

# # # # def manhattan_heuristic(a, b):
# # # #     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# # # # def doNext(ghost, walls, gate, pacman, grid):
# # # #     ghost_grid_pos = ghost.get_grid_position()
# # # #     pacman_grid_pos = pacman.get_grid_position()

# # # #     path = astar(ghost_grid_pos, pacman_grid_pos, grid, manhattan_heuristic)

# # # #     if path and len(path) > 1:
# # # #         next_cell = path[1]
# # # #         next_x = next_cell[1] * GRID_SIZE
# # # #         next_y = next_cell[0] * GRID_SIZE
# # # #         dx = next_x - ghost.rect.left
# # # #         dy = next_y - ghost.rect.top

# # # #         ghost.change_x = max(-15, min(15, dx))
# # # #         ghost.change_y = max(-15, min(15, dy))

# # # #     ghost.update(walls, gate)


# # # # # Main setup
# # # # def main():
# # # #     screen = pygame.display.set_mode([606, 606])
# # # #     pygame.display.set_caption('Pacman')

# # # #     all_sprites_list = pygame.sprite.RenderPlain()
# # # #     wall_list = setupRoomOne(all_sprites_list)
# # # #     gate = setupGate(all_sprites_list)
# # # #     grid = generate_grid(wall_list)

# # # #     w = 303 - 16  # starting x pos for Pacman and ghosts
# # # #     p_h = (7 * 60) + 19
# # # #     b_h = (3 * 60) + 19
# # # #     i_w = 303 - 16
# # # #     i_h = (3 * 60) + 19
# # # #     c_w = 303 - 16
# # # #     c_h = (7 * 60) + 19

# # # #     pacman = Player(w, p_h, 'images/Pacman.png')
# # # #     blinky = Ghost(w, b_h, 'images/Blinky.png')
# # # #     pinky = Ghost(w, p_h, 'images/Pinky.png')
# # # #     inky = Ghost(i_w, i_h, 'images/Inky.png')
# # # #     clyde = Ghost(c_w, c_h, 'images/Clyde.png')

# # # #     all_sprites_list.add(pacman, blinky, pinky, inky, clyde)

# # # #     clock = pygame.time.Clock()

# # # #     done = False
# # # #     while not done:
# # # #         for event in pygame.event.get():
# # # #             if event.type == pygame.QUIT:
# # # #                 done = True
# # # #             elif event.type == pygame.KEYDOWN:
# # # #                 if event.key == pygame.K_LEFT:
# # # #                     pacman.changespeed(-15, 0)
# # # #                 elif event.key == pygame.K_RIGHT:
# # # #                     pacman.changespeed(15, 0)
# # # #                 elif event.key == pygame.K_UP:
# # # #                     pacman.changespeed(0, -15)
# # # #                 elif event.key == pygame.K_DOWN:
# # # #                     pacman.changespeed(0, 15)
# # # #             elif event.type == pygame.KEYUP:
# # # #                 if event.key == pygame.K_LEFT:
# # # #                     pacman.changespeed(15, 0)
# # # #                 elif event.key == pygame.K_RIGHT:
# # # #                     pacman.changespeed(-15, 0)
# # # #                 elif event.key == pygame.K_UP:
# # # #                     pacman.changespeed(0, 15)
# # # #                 elif event.key == pygame.K_DOWN:
# # # #                     pacman.changespeed(0, -15)

# # # #         screen.fill(black)

# # # #         # Move ghosts towards pacman using A*
# # # #         doNext(pinky, wall_list, gate, pacman, grid)
# # # #         doNext(blinky, wall_list, gate, pacman, grid)
# # # #         doNext(inky, wall_list, gate, pacman, grid)
# # # #         doNext(clyde, wall_list, gate, pacman, grid)

# # # #         # Update Pacman
# # # #         pacman.update(wall_list, gate)

# # # #         all_sprites_list.draw(screen)

# # # #         pygame.display.flip()
# # # #         clock.tick(10)  # fps - adjust speed

# # # #     pygame.quit()
# # # #     sys.exit()

# # # # if __name__ == '__main__':
# # # #     main()

# # # import pygame
# # # import sys
# # # from astar import a_star_search
# # # import random

# # # GRID_SIZE = 20
# # # ROWS = 20
# # # COLS = 20
# # # WIDTH = COLS * GRID_SIZE
# # # HEIGHT = ROWS * GRID_SIZE

# # # WHITE = (255, 255, 255)
# # # BLACK = (0, 0, 0)
# # # YELLOW = (255, 255, 0)
# # # BLUE = (0, 0, 255)

# # # pygame.init()
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # pygame.display.set_caption("Autonomous Pac-Man")
# # # clock = pygame.time.Clock()

# # # # Grid: 0 = empty, 1 = wall, 2 = dot
# # # grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# # # # Add random walls
# # # for _ in range(100):
# # #     r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
# # #     grid[r][c] = 1

# # # # Add dots
# # # for _ in range(50):
# # #     r, c = random.randint(0, ROWS-1), random.randint(0, COLS-1)
# # #     if grid[r][c] == 0:
# # #         grid[r][c] = 2

# # # # Pac-Man starting position
# # # pacman_pos = [1, 1]

# # # def draw_grid():
# # #     for r in range(ROWS):
# # #         for c in range(COLS):
# # #             rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# # #             if grid[r][c] == 1:
# # #                 pygame.draw.rect(screen, BLUE, rect)
# # #             elif grid[r][c] == 2:
# # #                 pygame.draw.circle(screen, WHITE, rect.center, 3)
# # #             pygame.draw.rect(screen, BLACK, rect, 1)

# # # def draw_pacman():
# # #     rect = pygame.Rect(pacman_pos[1] * GRID_SIZE, pacman_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# # #     pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE // 2 - 2)

# # # def find_nearest_dot(start):
# # #     from collections import deque
# # #     visited = set()
# # #     queue = deque([start])
# # #     while queue:
# # #         current = queue.popleft()
# # #         if grid[current[0]][current[1]] == 2:
# # #             return current
# # #         for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
# # #             neighbor = (current[0]+dx, current[1]+dy)
# # #             if (0 <= neighbor[0] < ROWS and
# # #                 0 <= neighbor[1] < COLS and
# # #                 neighbor not in visited and
# # #                 grid[neighbor[0]][neighbor[1]] != 1):
# # #                 visited.add(neighbor)
# # #                 queue.append(neighbor)
# # #     return None

# # # path = []

# # # def main():
# # #     global path, pacman_pos

# # #     while True:
# # #         screen.fill(BLACK)
# # #         draw_grid()
# # #         draw_pacman()

# # #         for event in pygame.event.get():
# # #             if event.type == pygame.QUIT:
# # #                 pygame.quit()
# # #                 sys.exit()

# # #         if not path:
# # #             target = find_nearest_dot(tuple(pacman_pos))
# # #             if target:
# # #                 path = a_star_search(tuple(pacman_pos), target, grid)

# # #         if path:
# # #             next_pos = path.pop(0)
# # #             pacman_pos = list(next_pos)
# # #             if grid[pacman_pos[0]][pacman_pos[1]] == 2:
# # #                 grid[pacman_pos[0]][pacman_pos[1]] = 0

# # #         pygame.display.flip()
# # #         clock.tick(5)  # slower for clarity

# # # if __name__ == '__main__':
# # #     main()

# # import pygame
# # import sys
# # from astar import a_star_search
# # from collections import deque

# # # Constants
# # GRID_SIZE = 20
# # ROWS = 20
# # COLS = 20
# # WIDTH = COLS * GRID_SIZE
# # HEIGHT = ROWS * GRID_SIZE

# # # Colors
# # WHITE = (255, 255, 255)
# # BLACK = (0, 0, 0)
# # YELLOW = (255, 255, 0)
# # BLUE = (0, 0, 255)
# # RED = (255, 0, 0)

# # # Initialize Pygame
# # pygame.init()
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Autonomous Pac-Man with Ghost")
# # clock = pygame.time.Clock()

# # # Grid: 0 = empty, 1 = wall, 2 = dot
# # grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# # # Add some fixed walls
# # for r in range(5, 15):
# #     grid[r][10] = 1  # vertical wall in column 10

# # # Add some fixed food dots
# # food_coords = [(2, 2), (3, 7), (5, 5), (10, 3), (15, 15), (18, 1)]
# # for r, c in food_coords:
# #     grid[r][c] = 2

# # # Initial positions
# # pacman_pos = [1, 1]
# # ghost_pos = [ROWS - 2, COLS - 2]

# # def draw_grid():
# #     for r in range(ROWS):
# #         for c in range(COLS):
# #             rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# #             if grid[r][c] == 1:
# #                 pygame.draw.rect(screen, BLUE, rect)
# #             elif grid[r][c] == 2:
# #                 pygame.draw.circle(screen, WHITE, rect.center, 3)
# #             pygame.draw.rect(screen, BLACK, rect, 1)

# # def draw_pacman():
# #     rect = pygame.Rect(pacman_pos[1] * GRID_SIZE, pacman_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# #     pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE // 2 - 2)

# # def draw_ghost():
# #     rect = pygame.Rect(ghost_pos[1] * GRID_SIZE, ghost_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# #     pygame.draw.circle(screen, RED, rect.center, GRID_SIZE // 2 - 2)

# # def find_nearest_dot(start):
# #     visited = set()
# #     queue = deque([start])
# #     while queue:
# #         current = queue.popleft()
# #         if grid[current[0]][current[1]] == 2:
# #             return current
# #         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
# #             neighbor = (current[0] + dx, current[1] + dy)
# #             if (0 <= neighbor[0] < ROWS and
# #                     0 <= neighbor[1] < COLS and
# #                     neighbor not in visited and
# #                     grid[neighbor[0]][neighbor[1]] != 1):
# #                 visited.add(neighbor)
# #                 queue.append(neighbor)
# #     return None

# # pacman_path = []
# # ghost_path = []

# # def main():
# #     global pacman_path, ghost_path, pacman_pos, ghost_pos

# #     while True:
# #         screen.fill(BLACK)
# #         draw_grid()
# #         draw_pacman()
# #         draw_ghost()

# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 pygame.quit()
# #                 sys.exit()

# #         # Pac-Man logic
# #         if not pacman_path:
# #             target = find_nearest_dot(tuple(pacman_pos))
# #             print("Target:", target)
# #             if target:
# #                 pacman_path = a_star_search(tuple(pacman_pos), target, grid)
# #                 print("Path to target:", pacman_path)

# #         if pacman_path:
# #             next_pos = pacman_path.pop(0)
# #             pacman_pos = list(next_pos)
# #             if grid[pacman_pos[0]][pacman_pos[1]] == 2:
# #                 grid[pacman_pos[0]][pacman_pos[1]] = 0

# #         # Ghost logic
# #         if not ghost_path or ghost_path[-1] != tuple(pacman_pos):
# #             ghost_path = a_star_search(tuple(ghost_pos), tuple(pacman_pos), grid)

# #         if ghost_path:
# #             next_pos = ghost_path.pop(0)
# #             ghost_pos = list(next_pos)

# #         # Collision check
# #         if pacman_pos == ghost_pos:
# #             print("Pac-Man caught by Ghost!")
# #             pygame.quit()
# #             sys.exit()

# #         pygame.display.flip()
# #         clock.tick(5)

# # if __name__ == '__main__':
# #     main()

# import pygame
# import sys
# from astar import a_star_search
# import random

# # Constants
# GRID_SIZE = 20
# ROWS = 20
# COLS = 20
# WIDTH = COLS * GRID_SIZE
# HEIGHT = ROWS * GRID_SIZE

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# YELLOW = (255, 255, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)

# # Initialize Pygame
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Autonomous Pac-Man with Ghost")
# clock = pygame.time.Clock()

# # Initial positions
# pacman_start = [1, 1]
# ghost_start = [ROWS - 2, COLS - 2]

# def draw_grid(grid):
#     for r in range(ROWS):
#         for c in range(COLS):
#             rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
#             if grid[r][c] == 1:
#                 pygame.draw.rect(screen, BLUE, rect)
#             elif grid[r][c] == 2:
#                 pygame.draw.circle(screen, WHITE, rect.center, 3)
#             pygame.draw.rect(screen, BLACK, rect, 1)

# def draw_pacman(pos):
#     rect = pygame.Rect(pos[1] * GRID_SIZE, pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
#     pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE // 2 - 2)

# def draw_ghost(pos):
#     rect = pygame.Rect(pos[1] * GRID_SIZE, pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
#     pygame.draw.circle(screen, RED, rect.center, GRID_SIZE // 2 - 2)

# def find_nearest_dot(grid, start):
#     from collections import deque
#     visited = set()
#     queue = deque([start])
#     while queue:
#         current = queue.popleft()
#         if grid[current[0]][current[1]] == 2:
#             return current
#         for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
#             neighbor = (current[0] + dx, current[1] + dy)
#             if (0 <= neighbor[0] < ROWS and
#                 0 <= neighbor[1] < COLS and
#                 neighbor not in visited and
#                 grid[neighbor[0]][neighbor[1]] != 1):
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#     return None

# def main():
#     pacman_pos = list(pacman_start)
#     ghost_pos = list(ghost_start)
#     pacman_path = []
#     ghost_path = []

#     # Create grid fresh on each run
#     grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

#     # Add random walls (more walls)
#     for _ in range(150):
#         r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
#         if (r, c) != tuple(pacman_pos) and (r, c) != tuple(ghost_pos):
#             grid[r][c] = 1

#     # Add random dots (more food)
#     for _ in range(100):
#         r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
#         if grid[r][c] == 0 and (r, c) != tuple(pacman_pos) and (r, c) != tuple(ghost_pos):
#             grid[r][c] = 2

#     while True:
#         screen.fill(BLACK)
#         draw_grid(grid)
#         draw_pacman(pacman_pos)
#         draw_ghost(ghost_pos)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Pac-Man logic
#         if not pacman_path:
#             target = find_nearest_dot(grid, tuple(pacman_pos))
#             # print("Target:", target)
#             if target:
#                 pacman_path = a_star_search(tuple(pacman_pos), target, grid)

#         if pacman_path:
#             next_pos = pacman_path.pop(0)
#             pacman_pos = list(next_pos)
#             if grid[pacman_pos[0]][pacman_pos[1]] == 2:
#                 grid[pacman_pos[0]][pacman_pos[1]] = 0

#         # Ghost logic (chase Pac-Man)
#         if not ghost_path or ghost_path[-1] != tuple(pacman_pos):
#             ghost_path = a_star_search(tuple(ghost_pos), tuple(pacman_pos), grid)

#         if ghost_path:
#             next_pos = ghost_path.pop(0)
#             ghost_pos = list(next_pos)

#         # Collision check
#         if pacman_pos == ghost_pos:
#             print("Pac-Man caught by Ghost!")
#             pygame.quit()
#             sys.exit()

#         pygame.display.flip()
#         clock.tick(7)  # Slightly faster for fun

# if __name__ == '__main__':
#     main()
import pygame
import sys
from collections import deque
import heapq

# Constants
GRID_SIZE = 20
ROWS = 20
COLS = 20
WIDTH = COLS * GRID_SIZE
HEIGHT = ROWS * GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man A* Autonomous")
clock = pygame.time.Clock()

# Maze grid: 0=empty, 1=wall, 2=food
grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,0,0,0,1,0,0,2,0,0,1,0,0,0,1,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,1,2,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,2,0,0,0,0,0,0,0,0,2,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,2,1,0,0,0,0,0,2,0,0,0,0,1,0,0,0,1,2,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,2,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1],
    [1,2,0,0,0,1,0,1,2,0,0,0,0,0,0,1,0,0,2,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,2,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,2,0,0,0,2,0,0,0,0,2,1,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,2,1,0,0,0,0,0,2,0,0,0,0,1,0,0,0,1,2,1],
    [1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Positions
pacman_pos = [1, 1]
ghost_pos = [18, 18]

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * GRID_SIZE, r * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if grid[r][c] == 1:
                pygame.draw.rect(screen, BLUE, rect)
            elif grid[r][c] == 2:
                pygame.draw.circle(screen, WHITE, rect.center, 3)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_pacman():
    rect = pygame.Rect(pacman_pos[1] * GRID_SIZE, pacman_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.circle(screen, YELLOW, rect.center, GRID_SIZE // 2 - 2)

def draw_ghost():
    rect = pygame.Rect(ghost_pos[1] * GRID_SIZE, ghost_pos[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.circle(screen, RED, rect.center, GRID_SIZE // 2 - 2)

def find_nearest_dot(start):
    visited = set([start])
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if grid[current[0]][current[1]] == 2:
            return current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] != 1:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return None

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star_search(start, goal, grid):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f, g, node, path)

    closed_set = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current == goal:
            # exclude starting pos for movement to next steps
            return path[1:]

        if current in closed_set:
            continue
        closed_set.add(current)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                if grid[neighbor[0]][neighbor[1]] != 1 and neighbor not in closed_set:
                    new_g = g + 1
                    new_f = new_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return []  # no path found

def main():
    global pacman_pos, ghost_pos
    pacman_path = []
    ghost_path = []

    while True:
        screen.fill(BLACK)
        draw_grid()
        draw_pacman()
        draw_ghost()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Pac-Man logic
        if not pacman_path:
            target = find_nearest_dot(tuple(pacman_pos))
            if target:
                if target == tuple(pacman_pos):
                    grid[pacman_pos[0]][pacman_pos[1]] = 0
                    print(f"Pac-Man ate food at {pacman_pos} (no movement needed)")
                else:
                    pacman_path = a_star_search(tuple(pacman_pos), target, grid)
                    print("Pac-Man path:", pacman_path)

        # Pac-Man: move along path
        if pacman_path:
            next_pos = pacman_path.pop(0)
            pacman_pos = list(next_pos)

            if grid[pacman_pos[0]][pacman_pos[1]] == 2:
                grid[pacman_pos[0]][pacman_pos[1]] = 0
                print(f"Pac-Man ate food at {pacman_pos}")

        # Check collision (end game) after Pac-Man moves
        if pacman_pos == ghost_pos:
            print("Ghost caught Pac-Man! Game Over.")
            pygame.quit()
            sys.exit()

        # Ghost logic (chase Pac-Man)
        if not ghost_path:
            ghost_path = a_star_search(tuple(ghost_pos), tuple(pacman_pos), grid)
            print("Ghost path:", ghost_path)

        if ghost_path:
            next_ghost_pos = ghost_path.pop(0)
            ghost_pos = list(next_ghost_pos)

        # Check collision (end game) after both have moved
        if pacman_pos == ghost_pos:
            print("Ghost caught Pac-Man! Game Over.")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        clock.tick(5)  # Slow down for visibility


print(f"Pac-Man position: {pacman_pos}, Ghost position: {ghost_pos}")

if __name__ == "__main__":
    main()

