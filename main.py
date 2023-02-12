
import pygame
from sys import exit
from pygame.constants import QUIT
pygame.init()  # Start pygame, initiating
# There is Display surface (the game window, anything displayed goes here) and
# regular surface (essentially a single image (something imported, rendered text or a plain color) Display surface
# creation

screen = pygame.display.set_mode((800, 400))  # Display Surface should be one, width = 800, height=400
pygame.display.set_caption('Roman Empire')  # Setting up name of the game
clock = pygame.time.Clock()  # Clock object helping us with time and to control parameters
sky_surface = pygame.image.load('UltimatePygameIntro/graphics/sky.png')
ground_surface = pygame.image.load('UltimatePygameIntro/graphics/ground.png')

# test_surface = pygame.Surface((100, 200))  # Creating regular surface with width and height
# test_surface.fill('red')  # Command fill adding color to the surface, we use arguments predefined by python
# test_surface.fill((50, 50, 50)) - other way of adding color, it will be added on the top left

while True:  # Creating loop for elements on display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # opposite to pygame.init()
            exit()
    screen.blit(ground_surface, (0, 300))
    screen.blit(sky_surface, (0, 0))
    # We attach our test surface to our display surface by using this blit command
    # BLock Image Transfer, choosing surface which we want to position on the coordinate which are in brackets
    # It means that we placed our test_surface in the top left corner (0,0) coordinates if there would be (200,100) than
    # 200 - по осі х і 100 по осі y, тобто це відстань від осі координат
    pygame.display.update() # draw all our elements, update everything
    clock.tick(60)  # This while True loop should not run faster than 60 times per seconds
