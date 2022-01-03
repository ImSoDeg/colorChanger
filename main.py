import time

import pygame
from PIL import Image

import File

global position

filepath = File.getFile()


pygame.init()


# Programme qui remplace les pixel d'une couleur a pour une couleur b
def changeColor(pix, newpix):
    img = Image.open(filepath)
    raw = Image.new('RGB', img.size)
    a, b = img.size



    for j in range(a):
        for i in range(b):
            couleurActuel = img.getpixel((j, i))
            if couleurActuel == pix:
                raw.putpixel((j, i), newpix)
            else:
                raw.putpixel((j, i), couleurActuel)
    raw.show()


# Renvois la taille de l'image en paramètre
def getSize(file):
    img = Image.open(file)
    return img.size


# Renvois la couleur du pixel pointé en format RGB
def getColor(pos: tuple, file: str):
    img = Image.open(file)
    lastColor = img.getpixel(pos)

    return lastColor


# Permet de sélectionner la nouvelle couleur
def newColor():
    palette = Image.open("palette.jpg")
    images = pygame.display.set_mode(getSize("palette.jpg"))
    pygame.display.set_caption("Test")
    backgrounds = pygame.image.load("palette.jpg")
    image.blit(backgrounds, (0, 0))
    pygame.display.flip()
    pass


running = True
pygame.display.init()
image = pygame.display.set_mode(getSize(filepath))
pygame.display.set_caption("Test")
background = pygame.image.load(filepath)

image.blit(background, (0, 0))


while running:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                position = pygame.mouse.get_pos()
                color = getColor(position, filepath)
                newColor()
                time.sleep(1)
                for events in pygame.event.get():
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        posNewCol = pygame.mouse.get_pos()
                        print(position, posNewCol)
                        newColor = getColor(posNewCol, "palette.jpg")

                        changeColor(color, newColor)
                        running = False
                        pygame.quit()
                        break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
