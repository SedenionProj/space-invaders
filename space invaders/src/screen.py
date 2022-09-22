import os

width, height = os.get_terminal_size()

image = [[' ' for _ in range(width)] for _ in range(height)]
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