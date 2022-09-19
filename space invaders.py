import time
import os
import keyboard

longueur, largeur = os.get_terminal_size()
image = [[' ' for _ in range(longueur)] for _ in range(largeur)]
dernier = time.time()
speed = 1
largeur-=2

def placerPixel(x,y,char):
    x1=round(x)
    y1=round(y)
    if 0<=x1<=longueur-1 and 0<=y1<=largeur-1:
        image[y1][x1]=char

def afficher(*info):
    info="".join(info)
    info+=' '*(longueur-len(info))
    strImage=''
    for y in range(largeur):
        for x in range(longueur):
            strImage+=image[y][x]
    print(info+strImage,end='')

def supprimer():
    for y in range(largeur):
        for x in range(longueur):
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
    tex =  ["   #   #   ",
            " ## ### ## ",
            "###########",
            "# ##   ## #",
            "   ## ##   "]
    def update(self, dt):
        return super().update(dt)
    def collision(self,x,y):
        if self.x<x<self.x+len(self.__class__.tex[0]) and self.y<y<self.y+len(self.__class__.tex):
            return True
        return False

p1 = Ship(longueur//2,largeur*3//4)
b1 = Bullet(p1.x+4,p1.y)
m1 = Mob(longueur//2,10)
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

    if m1.collision(b1.x,b1.y):
        b1.reset(p1.x,p1.y)
        m1.delete()


    p1.update(dt)
    p1.draw()
    b1.update(dt)
    b1.draw()
    try:
        m1.update(dt)
        m1.draw()
    except:
        pass
    
    #placerPixel(p1.x,p1.y,'#')

    if dt != 0:
        fps = 1/dt

    afficher(str(round(fps)))