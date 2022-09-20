import time
import os
import keyboard

width, height = os.get_terminal_size()
image = [[' ' for _ in range(width)] for _ in range(height)]
dernier = time.time()
speed = 1
height-=2

def placerPixel(x,y,char):
    x1=round(x)
    y1=round(y)
    if 0<=x1<=width-1 and 0<=y1<=height-1:
        image[y1][x1]=char

def afficher(*info):
    info="".join(info)
    info+=' '*(width-len(info))
    strImage=''
    for y in range(height):
        for x in range(width):
            strImage+=image[y][x]
    print(info+strImage,end='')

def supprimer():
    for y in range(height):
        for x in range(width):
            image[y][x]=' '

class Entity:
    tex =  ["#"]
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
    def update(self,dt):
        self.x+=self.velX*dt
        self.y+=self.velY*dt

    def draw(self):
        for y in range(len(self.__class__.tex)):
            for x in range(len(self.__class__.tex[0])):
                placerPixel(x+self.x,y+self.y,self.__class__.tex[y][x])
        
class Ship(Entity):
    tex =  ["    ^    ",
            " |  #  | ",
            "<##---##>",
            "   ###   "]

class Bullet(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.shot = False
    tex =  ["#",
            "#"]
    def reset(self,x,y):
        self.x = x+4
        self.y = y
        self.shot = False
        self.velY = 0

class Mob(Entity):
    tex =  ["#"]
    def update(self, dt):
        return super().update(dt)
    def collision(self,x,y):
        if self.x-0.5<x<self.x+len(self.__class__.tex[0]) and self.y<y<self.y+len(self.__class__.tex):
            return True
        return False

class Mob1(Mob):
    tex =  ["   #   #   ",
            " ## ### ## ",
            "###########",
            "# ##   ## #",
            "   ## ##   "]   
class Mob2(Mob):
    tex =  ["     #     ",
            "   #####   ",
            " ## ### ## ",
            "###########",
            " #       # "]
class Mob3(Mob):
    tex =  ["     #     ",
            " ######### ",
            "##  ###  ##",
            "##### #####",
            "  #  #  #  "]

p1 = Ship(width//2,height*3//4)
b1 = Bullet(p1.x+4,p1.y)
mobs = [Mob1(15*i+width//2,height//10) for i in range(-5,5)]
mobs = mobs+[Mob2(15*i+width//2,mobs[0].y+10) for i in range(-5,5)]
mobs = mobs+[Mob3(15*i+width//2,mobs[0].y+20) for i in range(-5,5)]
fps=0

while True:
    actuelle = time.time()
    dt=actuelle-dernier
    dernier = actuelle
    supprimer()
    
    if keyboard.is_pressed("up arrow"):
        b1.velY=-30
        b1.shot = True
    elif b1.shot:
        pass
    else:
        b1.x = p1.x+4

    if keyboard.is_pressed("left arrow"):
        p1.velX-=speed
    elif keyboard.is_pressed("right arrow"):
        p1.velX+=speed
    else:
        if p1.velX>0:
            p1.velX -= speed
        if p1.velX<0:
            p1.velX += speed

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

    if dt != 0:
        fps = 1/dt

    afficher(str(round(fps)))