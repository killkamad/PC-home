import pygame
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

display_width=1000
display_height=900


gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("My Mario")
clock=pygame.time.Clock()


mario_left=pygame.image.load("mario_left.png")
mario_right=pygame.image.load("mario_right.png")
bullet_left=pygame.image.load("bullet_left.png")
bullet_right=pygame.image.load("bullet_right.png")
brickFragileImg = pygame.image.load("bricks_fragile.png")
brickImg = pygame.image.load("bricks.png")
coinImg = pygame.image.load("coin.png")
back = pygame.image.load('back.png')             #background
back = pygame.transform.scale(back,(1000,900))   #size of background
sound_coin = pygame.mixer.Sound("coin.wav")
sound_jump = pygame.mixer.Sound("jump.wav")
sound_coin.set_volume(0.05)
sound_jump.set_volume(0.05)


pygame.mixer.music.load('bgmusic.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

level = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,7,7,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,7,0,7,1],
    [1,0,0,0,0,0,7,0,0,7,0,0,0,0,0,0,0,0,2,2,2,2,1,1,0,2,7,0,0,0,0,0,0,0,0,0,0,7,7,0,0,0,7,0,0,0,0,0,1],
    [1,0,0,0,0,7,0,0,0,0,7,0,0,2,2,0,0,0,0,0,7,0,0,0,7,0,0,0,0,7,0,0,0,0,1,0,0,0,0,7,0,0,2,0,0,0,0,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,2,2,2,2,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    ]
    

crashed = False
x = 200
y = 100
gravity = 1
dy = 0
dx =0
die=False
white=(255,255,255)
in_air = True
look=0
offset= -100
kol=0
bullets=[]
for row in range(len(level)) :
    for col in range(len(level[row])):
        if level[row][col] == 7:
                kol +=1
    
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                new_bullet = {"x":x,"y":y}
                if look == 0:
                    new_bullet["dx"] = 5
                else:
                    new_bullet["dx"] = -5
                    bullets.append(new_bullet)    
                    
                
            if event.key == pygame.K_LEFT:
                dx = -5
                look = 1
            if event.key == pygame.K_RIGHT:
                 dx = 5
                 look =0
            if event.key == pygame.K_UP:
                if not in_air:
                    dy = -20
                    in_air = True
                    sound_jump.play()
            if event.key == pygame.K_DOWN:
                moving = "down"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                  dx = 0
            if event.key == pygame.K_RIGHT:
                    dx = 0
        print(event)
            
    for row in range(len(level)) :
        for col in range(len(level[row])):
            if level[row][col] == 1 or level [row][col] == 2:
                brick_x = col*48
                brick_y = row*48
                    
                if brick_x-48 <=x<=brick_x + 48 and brick_y-48 <= y +48 <= brick_y+48:
                    if y-dy+48<=brick_y and y+48>=brick_y:
                        y = brick_y -48
                        y = brick_y -48 -dy
                        in_air = False
                            
        #logic:
            
    dy += gravity
    if dy > 12 :
        dy = 20
    if y >900:
        die = True
    y += dy
    while die ==True:
        gameDisplay.fill((255,255,255))
        font = pygame.font.Font(None,150)
        text = font.render("Game over",True,(255,0,0))
        gameDisplay.blit(text,[250,250])
        pygame.display.update()

    
          
    #logic2:

    if dx < 0:
        dx -= 1
    if dx < -10:
        dx = -10
    if dx > 0:
        dx += 1
    if dx > 10 :
        dx = 13
    x += dx

    if x + offset > display_width * 5/10 :
        offset = display_width* 5/10 - x
            
    if x + offset < display_width * 5/10 :
        offset = display_width * 5/10 -x 
         #check if we touch a coin:
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 6:
                wall_x = col * 48
                wall_y = row * 48
                touch = False
                if wall_x <= x <=  wall_x +48 and wall_y <= y <= wall_y + 48:
                    touch = True
                if wall_x <= x + 48<= wall_x +48 and wall_y <= y <= wall_y + 48:
                    touch = True
                if wall_x <= x <=  wall_x +48 and wall_y <= y + 48<= wall_y + 48:
                    touch = True
                if wall_x <= x + 48 <=  wall_x +48 and wall_y <= y + 48 <= wall_y + 48:
                    touch = True    
                if touch:
                    level[row][col] = 0
                    sound_coin.play()
                    kol-=1
    for p in bullets : 
        if p["x"] > 1000:
            bullets.remove(p)


    for bullet in bullets:
        bullet["x"] += bullet["dx"]
        for row in range(len(level)):
            for col in range(len(level[row])):
                if level[row][col] == 1 or level[row][col] == 2:  
                    wall_x = col*48
                    wall_y = row*48
                    touch= False

                    if wall_x <= bullet["x"] <= wall_x + 48 and wall_y <= bullet["y"] <= wall_y + 48:
                        touch = True
                    if wall_x <= bullet["x"] + 48 <= wall_x + 48 and wall_y <= bullet["y"] <= wall_y + 48:
                        touch = True
                    if wall_x <= bullet["x"] <= wall_x + 48 and wall_y <= bullet["y"] + 48 <= wall_y + 48:
                        touch = True
                    if wall_x <= bullet["x"] + 48 <= wall_x + 48 and wall_y <= bullet["y"] + 48 <= wall_y + 48:
                        touch = True
                    if touch:
                        level[row][col] -=1
                        if bullet in bullets:
                            bullets.remove(bullet)
 
                    
    #drawing here
    gameDisplay.fill((255,255,255))
    gameDisplay.blit(back,(0,0))
        #gameDisplay.blit(,(0,0))
    for row in range(len(level)):
        for col in range(len(level[row])):
            if level[row][col] == 2:
                gameDisplay.blit(brickFragileImg,(col*48+offset,row*48))
            if level[row][col] == 1:
                gameDisplay.blit(brickImg,(col*48+offset,row*48))
            if level[row][col] == 7:
                gameDisplay.blit(coinImg, (col*48+offset,row*48))
            if level[row][col] == 3:
                gameDisplay.blit(cloudImg,(col*48 ,row*48))
            
                    
                            
    if look == 0:
        gameDisplay.blit(mario_right,(x+offset,y))
    else:
        gameDisplay.blit(mario_left,(x+offset,y))

    for bullet in bullets:
        if bullet["dx"] > 0:
            gameDisplay.blit(bullet_right,
                         (bullet["x"]+offset,bullet["y"]))

        else:
            gameDisplay.blit(bullet_left,
                             (bullet["x"] + offset,bullet["y"]))
                
    if kol==0:
        if in_air==False:
            gameDisplay.fill((255,255,255))
            font = pygame.font.Font(None,150)
            text = font.render("YOU WIN",True,(255,0,0))
            gameDisplay.blit(text,[250,250])
  


    pygame.display.update()
    clock.tick(30)
pygame.quit()    


