import pygame  # O módulo não está instalada por padrão porém, o Pycharm dá a opção de instalar

pygame.init()  # iniciar o pygame
pygame.mixer.music.load(
    'desafio021.mp3')  # carrega o arquivo MP3 lembrando que o arquivo deve estar entre aspas e na mesma pasta onde o projeto é salvo.
pygame.mixer.music.play()  # Aqui a música irá tocar
pygame.event.wait()  # Encerra o programa.
#não está tocando a música
