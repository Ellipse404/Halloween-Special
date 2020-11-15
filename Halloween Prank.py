import pygame as pg
from time import sleep
pg.init()
window = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.mixer.init()
# music1
pg.mixer.music.load('hhgsfog.mp3')
pg.mixer.music.play()
sleep(5)
#music2
pg.mixer.music.load('sono_moo.mp3')
pg.mixer.music.play()
sleep(5)
#music3
pg.mixer.music.load('ghostepsen.mp3')
pg.mixer.music.play()
sleep(5)
#music4
pg.mixer.music.load('falling.mp3')
pg.mixer.music.play()
#sleep(1)
#show
img = pg.image.load("maingh.jpg")
window.blit(img, (0,0))
pg.display.update()
sleep(3)
window.close()
