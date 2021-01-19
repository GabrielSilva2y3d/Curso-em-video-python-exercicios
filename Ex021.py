print('isso não funciona!')
print('pygame.error: Failed loading libmpg123-0.dll:')

import pygame 
from pygame import mixer
print('MP3 player')
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('undertale.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
while(pygame.mixer.music.get_busy()): 
    pass
pygame.event.wait()


