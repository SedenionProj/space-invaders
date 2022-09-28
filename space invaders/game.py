import time
import src.screen as screen
import src.main as main

dernier = time.time()
fps = 0
msg = ""

if __name__ == "__main__":
    while True:
        # boucle principale du programme
        actuelle = time.time()
        # calcule la différence de temps entre deux images pour avoir un
        # mouvement constant
        dt = actuelle - dernier
        dernier = actuelle

        screen.supprimer()

        if main.running == 0:  # fenêtres
            main.intro(dt)
        if main.running == 1:
            main.menu(dt)
        if main.running == 2:
            main.gameLoop(dt)
        if main.running == 3:
            main.deathScreen(dt)

        if dt != 0:
            fps = 1 / dt

        msg = "(info)" + ' w: ' + str(screen.width) + 'px h: ' + str(screen.height +
        1) + "px, fps : " + str(round(fps)) # informations sur le programme
        screen.afficher(msg)
