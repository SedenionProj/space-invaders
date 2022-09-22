import time
import keyboard
import entities
import screen


dernier = time.time()
speed = 1


p1 = entities.Ship(screen.width//2,screen.height*3//4)
b1 = entities.Bullet(p1.x+4,p1.y)
mobs = [entities.Mob1(15*i+screen.width//2,screen.height//10) for i in range(-5,5)]
mobs = mobs+[entities.Mob2(15*i+screen.width//2,mobs[0].y+10) for i in range(-5,5)]
mobs = mobs+[entities.Mob3(15*i+screen.width//2,mobs[0].y+20) for i in range(-5,5)]
fps=0
if __name__ == "__main__":
    while True:
        actuelle = time.time()
        dt=actuelle-dernier
        dernier = actuelle
        screen.supprimer()
        
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

        screen.afficher(str(round(fps)))