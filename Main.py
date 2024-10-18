import pgzrun
import random
import time

WIDTH=600
HEIGHT=383


ship=Actor("ship.png")
SpaceRock=Actor("spacerocksprite.png")

ship.pos=100,300
SpaceRock.x = 200
SpaceRock.y = 100

score = 0
game_over=False

def draw():


    screen.blit("spacebackground",(0,0))
    ship.draw()
    SpaceRock.draw()
    screen.draw.text(msg, (100,300)) 
    screen.draw.text(f"Score: {score}", topleft=(10, 10), color="white")

    if game_over:
        screen.draw.text("GG!", center=(WIDTH // 2, HEIGHT // 2), color="red", fontsize=50)
        screen.draw.text("Click to Restart", center=(WIDTH // 2, HEIGHT // 2 + 50), color="white")
    else:
        screen.draw.text(msg, center=(WIDTH // 2, HEIGHT - 30), color="white")

def update():
    global score, game_over
    if keyboard.up:
        ship.y-=5
    if keyboard.down:
        ship.y+=5
    if keyboard.left:
        ship.x-=5
    if keyboard.right:
        ship.x+=5   
    if ship.colliderect(SpaceRock):
        score += 1
        SpaceRock.x=random.randint(50, WIDTH - 50)
        SpaceRock.y=random.randint(50, HEIGHT - 50)
        msg = "WORK FASTER"
    else:
        if score == 20:
            game_over=True

def on_mouse_down():
    global score, game_over
    if game_over:
        score = 0
        game_over = False
        SpaceRock.x = 325
        SpaceRock.y = 250
        ship.pos=300,192

        
pgzrun.go()