import time
import src.screen as screen
import src.main as main

dernier = time.time()
fps=0

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

        if dt != 0:
            fps = 1/dt

        screen.afficher("fps :",str(round(fps)))