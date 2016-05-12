import pygame,sys
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)

#initialise pygame and window
pygame.init()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

#for random movement
foo = [.75,-.75]     

#class block
class Block(pygame.sprite.Sprite):
    def __init__(self,colour):
        super().__init__()
        self.col = colour
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, colour, [0, 0, 10, 10])
    def update(self):
            self.rect.x += random.choice(foo)
            self.rect.y += random.choice(foo)
            if self.rect.x == 0:
                self.rect.x = random.randrange(screen_width,screen_width+10)
            if self.rect.y == 0:
                self.rect.y = random.randrange(screen_height,screen_height+10)

#class player        
class Player(Block):
    def update(self):
        
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x-=1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x+=1
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y-=1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y+=1



all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()


for i in range(10):
    # This represents a block
    block = Block(WHITE)
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(10):
    # This represents a block
    block = Block(GREEN)
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    
player = Player(RED)
player.rect.x = screen_width/2
player.rect.y = screen_height/2
#p = 1
all_sprites_list.add(player)


done  = False

def button(msg,first_colour, text_colour, x,y,w,h,text_size):
        pygame.draw.rect(screen, first_colour,(x,y,w,h))
        myfont = pygame.font.SysFont("freesansbold", text_size)
        label = myfont.render(msg, 1, text_colour)
        screen.blit(label, (x+5,y+5))
    
def butt(msg,first_colour, second_colour,text_colour, x,y,w,h):
##    game_loop()
    while True:
        ev1 = pygame.event.poll()
        if ev1.type == pygame.QUIT:
            pygame.quit()
            quit()
##        smallText = pygame.font.SysFont("comicsansms",20)
##        textSurf, textRect = text_objects(msg, smallText)
##        textRect.center = ( (x+(w/2)), (y+(h/2)) )
##        screen.blit(textSurf, textRect)
##        pygame.draw.rect(screen, (0,255,0),(100,100,100,50))
##        myfont = pygame.font.SysFont("monospace", 30)
##        label = myfont.render(msg, 1, (255,255,0))
##        screen.blit(label, (105,105))
        
        #pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, second_colour,(x,y,w,h))
            
            if click[0] == 1:
                game_loop()
                    
        else:
            pygame.draw.rect(screen, first_colour,(x,y,w,h))
        button(msg,first_colour, text_colour, x,y,w,h,50)
        
        pygame.display.update()
def game_over(count):    

##    pygame.draw.rect(screen, (0,255,0),(100,100,100,50))
##    myfont = pygame.font.SysFont("monospace", 30)
##    label = myfont.render(str(count), 1, (255,255,0))
##    screen.blit(label, (105,105))
    
#    pygame.display.flip()
    screen.fill(WHITE)
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
##        pygame.draw.rect(screen, (0,255,0),(100,100,100,50))
##        myfont = pygame.font.SysFont("monospace", 30)
##        label = myfont.render("aaa", 1, (255,255,0))
##        screen.blit(label, (105,105))
        score = "SCORE = "+str(count)
        button(score,(255,255,255),(255,0,0),90,100,240,150,40)
        button("Play",(0,255,0),(0,0,0),50,250,100,60,40)
        button("Quit",(0,255,0),(0,0,0),250,250,100,60,40)
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 50 < mouse[0] < 150 and 250 < mouse[1] < 310:
            if click[0] == 1:
                game_loop()
##                ball = pygame.image.load("gameover.png")
##                ballrect = ball.get_rect()
##                #screen.fill(BLACK)
##                screen.blit(ball, ballrect)
##                pygame.display.flip()
##                pygame.time.delay(2000)
        if 250 < mouse[0] < 350 and 250 < mouse[1] < 310:
            if click[0] == 1:
                pygame.quit()
                quit()
        clock.tick(40)
    #pygame.display.flip()
def game_loop():
    num_white = 10
    num_green = 15
    count = 0
    p = 1
    while True:    
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
          break

        all_sprites_list.update()
        screen.fill(BLACK)
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
        
        for block in blocks_hit_list:
            a = player.rect.x
            b = player.rect.y

            #block == white
            if block.col == WHITE:
                count+=1
                num_white-=1
                if num_white == 0:
                    game_over(count)
                    break                
                p = p + 1
                player.image = pygame.Surface([10*p, 10*p])
                player.image.fill(BLACK)
                player.image.set_colorkey(BLACK)
                player.rect = player.image.get_rect()
                player.rect.x = a
                player.rect.y = b
                pygame.draw.ellipse(player.image, RED, [0, 0, 10*p, 10*p])

            #block == green
            if block.col == GREEN:
                #count-=1
                p = p - 1
                if p == 0:
                    game_over(count)
                    break
                player.image = pygame.Surface([10*p, 10*p])
                player.image.fill(BLACK)
                player.image.set_colorkey(BLACK)
                player.rect = player.image.get_rect()
                print("aaaaaaaaa")            
                player.rect.x = a
                player.rect.y = b
                pygame.draw.ellipse(player.image, RED, [0, 0, 10*p, 10*p])
                
        clock.tick(120)
        
        all_sprites_list.draw(screen) 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    pygame.quit()
     
def game_intro():
    while True:
        ev2 = pygame.event.poll()
        if ev2.type == pygame.QUIT:
          pygame.quit()
          break
        pygame.draw.rect(screen, (0,0,0),(0,0,50,50))
        myfont = pygame.font.SysFont("comicsansbold", 100)
        label = myfont.render("ROTUND", 1, (255,0,0))
        screen.blit(label, (50,100))
        butt("Play",(0,255,0),(0,100,0),(0,0,0),150,250,100,50)
        pygame.display.update()
        clock.tick(15)
game_intro()
#game_loop()
        
