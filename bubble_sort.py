import pygame
import random

random.seed(3.14)
pygame.init()

DIMENSIONS = (WIDTH, HEIGHT) = (800, 600)
SCREEN = pygame.display.set_mode(DIMENSIONS)
CLOCK = pygame.time.Clock()

N = WIDTH
rectangles = [random.randrange(1, HEIGHT) for _ in range(N)]

nIter = 0
sorting = True
while sorting:

    nIter += 1
    CLOCK.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sorting = False 

    SCREEN.fill((0, 0, 0))
    for i in range(N):
        pygame.draw.rect(SCREEN, (255, 255, 255), pygame.rect.Rect(i, HEIGHT, 1, -rectangles[i]))
    pygame.display.flip()

    nSwaps = 0

    for i in range(N-1):
        if rectangles[i] > rectangles[i+1]:
            rectangles[i], rectangles[i+1] = rectangles[i+1], rectangles[i]
            nSwaps += 1

    if nSwaps == 0:
        sorting = False


print(*rectangles)
print('nIter:', nIter)
pygame.quit()
