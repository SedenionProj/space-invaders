import keyboard
from random import randint
import src.entities as entities
import src.screen as screen

speed = 5
running = 0

p1 = entities.Ship(screen.width//2,screen.height-5)
b1 = entities.Bullet(p1.x+4,p1.y)
mobs = []

text = entities.texte(10,10)
vel_mob = 1
score = 0
level = 0

def gameLoop(dt):
    global vel_mob
    global score
    global level
    global mobs
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
        p1.velX*=0.95

    if b1.y < 0:
        b1.reset(p1.x,p1.y)

    p1.update(dt)
    p1.draw()
    b1.update(dt)
    b1.draw()
    text.set(str(score),0,1)
    text.set(str(level),0,2)

    if len(mobs)==0:
        level+=1
        mobs = mobs+[entities.Mob1(15*i+screen.width//2,5) for i in range(-5,5)]
        mobs = mobs+[entities.Mob2(15*i+screen.width//2,mobs[0].y+10) for i in range(-5,5)]
        mobs = mobs+[entities.Mob3(15*i+screen.width//2,mobs[0].y+20) for i in range(-5,5)]
        p1.x=screen.width//2
        p1.y=screen.height-5;

    for mob in mobs:
        mob.x+=dt*5*vel_mob*score/10
        if mob.collision(b1.x,b1.y):
            b1.reset(p1.x,p1.y)
            mobs.remove(mob)
            if type(mob)==entities.Mob1:
                score+=3
            if type(mob)==entities.Mob2:
                score+=2
            if type(mob)==entities.Mob3:
                score+=1
        else:
            mob.draw()
        if mob.x>screen.width-9 or mob.x<=0:
            for mob1 in mobs:
                mob1.y += 2
            vel_mob *= -1
            mob.x += vel_mob


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
r=0
r1=0
r2=0

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