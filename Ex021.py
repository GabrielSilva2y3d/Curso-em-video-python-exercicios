import pygame 
print('MP3 player')
pygame.init()
music = pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=-1)
pygame.event.wait()

