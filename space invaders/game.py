from math import sin
from random import randint
import time
import keyboard
import src.entities as entities
import src.screen as screen

running = 0
dernier = time.time()
speed = 5


p1 = entities.Ship(screen.width//2,screen.height*3//4)
b1 = entities.Bullet(p1.x+4,p1.y)
mobs = [entities.Mob1(15*i+screen.width//2,screen.height//10) for i in range(-5,5)]
mobs = mobs+[entities.Mob2(15*i+screen.width//2,mobs[0].y+10) for i in range(-5,5)]
mobs = mobs+[entities.Mob3(15*i+screen.width//2,mobs[0].y+20) for i in range(-5,5)]
text = entities.texte(10,10)

fps=0

def gameLoop(dt):
    
    if keyboard.is_pressed("up arrow"):
        b1.velY=-30
        b1.shot = True
    elif b1.shot:
        pass
    else:
        b1.x = p1.x+4

    if keyboard.is_pressed("left arrow"):
        if p1.velX > -entities.Ship.maxSpeed:
            p1.velX-=speed
    elif keyboard.is_pressed("right arrow"):
        if p1.velX < entities.Ship.maxSpeed:
            p1.velX+=speed
    else:
        p1.velX*=0.99

    if b1.y < 0:
        b1.reset(p1.x,p1.y)

    p1.update(dt)
    p1.draw()
    b1.update(dt)
    b1.draw()
    
    for mob in mobs:
        if mob.collision(b1.x,b1.y):
            b1.reset(p1.x,p1.y)
            mobs.remove(mob)
        else:
            mob.draw()



r=0
r1=0
r2=0
def intro(dt):
    global running
    global r
    global r1
    global r2
    r+=dt*10
    if r**2 > screen.width-100:
        r1+=dt*100
    if screen.height-int(r1)==0:
        running = 1        
    for y in range(screen.height-int(r1)):
        for x in range(screen.width):
            if (x-screen.width//2)**2+4*(y-screen.height//2)**2<r**5:
                    screen.placerPixel(x,y,'.')
            if (x-screen.width//2)**2+4*(y-screen.height//2)**2<r**4:
                    screen.placerPixel(x,y,'█')
id_play = 1
id_menu = 2
def menu(dt):
    global id_play
    global id_menu
    global running
    if keyboard.is_pressed("up arrow"):
        id_play = 3
        id_menu = 2
    elif keyboard.is_pressed("down arrow"):
        id_play = 1
        id_menu = 4
    if keyboard.is_pressed("enter"):
        if id_play == 3:
            running = 2
        if id_menu == 4:
            text.set("texte",100,40)
    for _ in range(10):
        screen.placerPixel(randint(0,screen.width),randint(0,screen.height),".")
    
    text.draw(0,10,10)
    text.draw(id_play,10,text.y+10)
    text.draw(id_menu,10,text.y+10)
    
    

if __name__ == "__main__":
    while True:
        actuelle = time.time()
        dt=actuelle-dernier
        dernier = actuelle

        screen.supprimer()

        if running == 0:
            intro(dt)
        if running == 1:
            menu(dt)
        if running == 2:
            gameLoop(dt)

        if dt != 0:
            fps = 1/dt

        screen.afficher("fps :",str(round(fps)))