import pygame
import random
 
SCREEN_HEIGHT = 600
GAP = 150          # vertical space between top and bottom pipe
PIPE_WIDTH = 60
PIPE_SPEED = 3     # how many pixels the pipe moves left per frame
 
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = PIPE_WIDTH
        self.gap = GAP

        # top pipe height is random so each pair is different
        self.top_height = random.randint(50, SCREEN_HEIGHT - GAP - 50)
        self.bottom_y = self.top_height + self.gap  # bottom pipe starts after the gap
        self.passed = False  # flips to True once the bird clears it (used for scoring)

        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, SCREEN_HEIGHT - self.bottom_y)
 
    def update(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x
 
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 128, 0), self.top_rect) # top pipe
        pygame.draw.rect(screen, (0, 128, 0), self.bottom_rect) # bottom pipe
 
    def get_rects(self):
        return (self.top_rect, self.bottom_rect)
 
    def is_off_screen(self):
        return self.x + self.width < 0
