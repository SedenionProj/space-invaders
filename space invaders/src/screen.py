import os

width, height = os.get_terminal_size()

image = [[' ' for _ in range(width)] for _ in range(height)]
height -= 2


def installPKG():
    # installe le module keyboard
    print('Installing keybord module...')
    os.pip.main(['install', "keyboard"])


def autoresize():
    # met automatiquement l'écran en 240/62
    os.system('mode con: cols=240 lines=62')
    resize()


def resize():
    # active le recadrage de l'écran
    global image
    global width
    global height
    width, height = os.get_terminal_size()
    image = [[' ' for _ in range(width)] for _ in range(height)]
    height -= 1
    os.system('cls')


def placerPixel(x, y, char):
    # place un pixel sur l'écran
    x1 = round(x)
    y1 = round(y)
    if 0 <= x1 <= width - 1 and 0 <= y1 <= height - 1:
        image[y1][x1] = char


def afficher(*info):
    # affiche l'image à l'écran
    info = "".join(info)
    info += ' ' * (width - len(info))
    strImage = ''
    for y in range(height):
        for x in range(width):
            strImage += image[y][x]
    print(info + strImage, end='')


def supprimer():
    # réinitialise l'image
    for y in range(height):
        for x in range(width):
            image[y][x] = ' '
