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
        if event.type == pygame.KEYDOWN:
            if self.state == "playing" and event.key == pygame.K_SPACE:
                self.bird.flap()
            elif self.state == "game_over" and event.key == pygame.K_SPACE:
                self.__init__(self.screen)
 
    def update(self):
        if self.state != "playing":
            return
        
        self.bird.update()

        self.frame_count += 1 # timer to spawn new pipes
        if self.frame_count % PIPE_SPAWN_INTERVAL == 0:
            self._spawn_pipe()

        # moves all pipes    
        for pipe in self.pipes:
            pipe.update()

        # holds pipes not on screen
        self.pipes = [p for p in self.pipes if not p.off_screen()]

        self._check_collisions()
        self._update_score()
 
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
        self.screen.fill((135, 206, 235))  # sky blue

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.bird.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        if self.state == "game_over":
            self._draw_game_over()
 
    def _draw_game_over(self):
        text = self.font.render(f"Game Over! Score: {self.score}", True, (255, 0, 0))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        hint = self.font.render("Press SPACE or LEFT MOUSE CLICK to restart", True, (255, 255, 255))
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
