import time
import os
import keyboard

longueur, largeur = os.get_terminal_size()
image = [[' ' for _ in range(longueur)] for _ in range(largeur)]
dernier = time.time()
speed = 1

def placerPixel(x,y,char):
    x1=round(x)
    y1=round(y)
    if 0<=x1<=longueur-1 and 0<=y1<=largeur-1:
        image[y1][x1]=char

def afficher():
    strImage=' '*longueur
    for y in range(largeur):
        for x in range(longueur):
            strImage+=image[y][x]
    print(strImage,end='')

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
    tex =  ["  #  ",
            "# # #",
            "#####"]

class Bullet(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)
        self.shot = False
    tex =  ["#",
            "#"]

class Mob(Entity):
    pass
    
p1 = Ship(longueur//2,largeur*3/4)
b1 = Bullet(p1.x,p1.y)

while True:
    actuelle = time.time()
    dt=actuelle-dernier
    dernier = actuelle
    supprimer()
    
    if keyboard.is_pressed("up arrow"):
        b1.velY=-10
        b1.shot = True
    elif b1.shot:
        pass
    else:
        b1.x = p1.x

    if keyboard.is_pressed("left arrow"):
        p1.velX-=speed
    elif keyboard.is_pressed("right arrow"):
        p1.velX+=speed
    else:
        if p1.velX>0:
            p1.velX -= speed
        if p1.velX<0:
            p1.velX += speed
    p1.update(dt)
    p1.draw()
    b1.update(dt)
    b1.draw()
    
    #placerPixel(p1.x,p1.y,'#')

    afficher()