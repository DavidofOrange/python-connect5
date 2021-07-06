import pygame
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('menu.png')
#pygame.display.set_icon(background)

red = (255, 0, 0)
green = (0, 255, 0)
WHITE = (0, 0, 0)

# Menu music
mixer.music.load('chilly.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

def button(screen, position, text, size=50, color="yellow", bg="darkblue"):
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, color)
    x, y, w , h = text_render.get_rect()
    x, y = position
    # line(surface, color, (startingpoint), (endingpoint), thickness)
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w + 1, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w + 2, h))
    return screen.blit(text_render, (x, y))

def start():
    import round2 as round
    round

def ai_game():
    import connectAI
    connectAI

def menu():
    """ This is the menu that waits you to click the s key to start """
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Args: button(surface, (width, height), text)
    # added size, color and bg in version 2
    b3 = button(screen, (400, 300), "AI 4", size=50, color="WHITE", bg="black")
    b1 = button(screen, (500, 300), "Quit", size=50, color="WHITE", bg="black")
    b2 = button(screen, (600, 300), "Start", size=50, color="WHITE", bg="black")
  

    while True:
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    ai_game()


        pygame.display.update()
    pygame.quit()

menu()