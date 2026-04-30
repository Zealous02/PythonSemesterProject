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
 
    def update(self):
        # Move pipe to the left each frame.
        # subtract PIPE_SPEED from self.x
        pass
 
    def draw(self, screen):
        # top pipe:    rect from (self.x, 0) with height = self.top_height
        # bottom pipe: rect from (self.x, self.bottom_y) down to bottom of screen
        pass
 
    def get_rects(self):
        # Return (top_rect, bottom_rect) for collision detection.
        # return a tuple of two pygame.Rect objects
        pass
 
    def is_off_screen(self):
        # Return True if the pipe has moved past the left edge.
        # check if self.x + self.width < 0
        pass
