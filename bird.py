import pygame
 
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5 
        self.flap_strength = -8
        self.width = 34
        self.height = 24
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
 
    def flap(self):
        self.velocity = self.flap_strength
 
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.y = self.y
 
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)
 
    def get_rect(self):
        return self.rect
 
