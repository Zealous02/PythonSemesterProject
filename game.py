import pygame
from bird import Bird
from pipe import Pipe
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIPE_SPAWN_INTERVAL = 90  # spawn a new pipe every 90 frames (1.5 seconds at 60fps)
 
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.bird = Bird(80, SCREEN_HEIGHT // 2)  # start bird in the middle-left
        self.pipes = []       # list of active Pipe objects
        self.score = 0
        self.frame_count = 0  # counts up each frame, used to time pipe spawning
        self.state = "playing"  # switches to "game_over" on collision
        self.font = pygame.font.SysFont(None, 40)
 
    def handle_event(self, event):
        # if state is "playing" and spacebar/mouse pressed: call self.bird.flap()
        # if state is "game_over" and a key is pressed: reset the game
        pass
 
    def update(self):
        # only update if state is "playing"
        # 1. call self.bird.update()
        # 2. increment frame_count, spawn a pipe every PIPE_SPAWN_INTERVAL frames
        # 3. update and clean up off-screen pipes
        # 4. check collisions and update score
        pass
 
    def _spawn_pipe(self):
        # create a Pipe starting just off the right edge of the screen
        pass
 
    def _check_collisions(self):
        # get bird rect, loop through pipes and check colliderect() against both rects
        # also check if bird.y < 0 or bird.y > SCREEN_HEIGHT
        # if any hit: set self.state = "game_over"
        pass
 
    def _update_score(self):
        # loop through pipes, if pipe.passed is False and bird.x > pipe.x + pipe.width:
        #   set pipe.passed = True and increment self.score
        pass
 
    def draw(self):
        # fill background with a sky color
        # draw all pipes, then the bird, then the score text
        pass
 
    def _draw_game_over(self):
        #Overlay a game-over message with the final score.
        pass
