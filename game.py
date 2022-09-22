import space_invaders

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
                space_invaders.placerPixel(x+self.x,y+self.y,self.__class__.tex[y][x])
        
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