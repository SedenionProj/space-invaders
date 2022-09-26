import time
import src.screen as screen
import src.main as main

dernier = time.time()
fps=0
msg = ""

if __name__ == "__main__":
    while True:
        actuelle = time.time()
        dt=actuelle-dernier
        dernier = actuelle


        screen.supprimer()

        if main.running == 0:
            main.intro(dt)
        if main.running == 1:
            main.menu(dt)
        if main.running == 2:
            main.gameLoop(dt)
        if main.running == 3:
            main.deathScreen(dt)

        if dt != 0:
            fps = 1/dt

        msg = "info :"+ "fps : "+str(round(fps))+' w : '+str(screen.width)+' h : '+str(screen.height+1)
        screen.afficher(msg)