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

for i in range(N):

    nIter += 1
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    SCREEN.fill((0, 0, 0))
    for x in range(N):
        pygame.draw.rect(SCREEN, (255, 255, 255), pygame.rect.Rect(x, HEIGHT, 1, -rectangles[x]))
    pygame.display.flip()

    leastIndex = i
    for j in range(i+1, N):
        if rectangles[leastIndex] > rectangles[j]:
            leastIndex = j
    rectangles[i], rectangles[leastIndex] = rectangles[leastIndex], rectangles[i]

print(*rectangles)
print('nIter:', nIter)
pygame.quit()
