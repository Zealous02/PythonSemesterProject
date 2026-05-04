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
        self.highscore = 0
        self.frame_count = 0  # counts up each frame, used to time pipe spawning
        self.state = "playing"  # switches to "game_over" on collision
        self.font = pygame.font.SysFont(None, 40)
 
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == "playing" and event.key == pygame.K_SPACE:
                self.bird.flap()
            elif self.state == "game_over" and event.key == pygame.K_SPACE:
                old_highscore = self.highscore
                self.__init__(self.screen)
                self.highscore = old_highscore
 
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
        self.pipes = [p for p in self.pipes if not p.is_off_screen()]

        self._check_collisions()
        self._update_score()
 
    def _spawn_pipe(self):
        self.pipes.append(Pipe(SCREEN_WIDTH)) # makes a new pipe
 
    def _check_collisions(self): 
        bird_rect = self.bird.get_rect() # bird's rect
        
        for pipe in self.pipes: # iterating through all pipes to check for collision
            if bird_rect.colliderect(pipe.top_rect) or bird_rect.colliderect(pipe.bottom_rect): # 
                self.state = "game_over"
        
        if self.bird.y < 0 or self.bird.y > SCREEN_HEIGHT: # checks if we hit the top or bottom of the screen
            if self.score > self.highscore:
                self.highscore = self.score
            self.state = "game_over" 

 
    def _update_score(self):
        for pipe in self.pipes:
            if pipe.passed == False and self.bird.x > pipe.x + pipe.width:
                pipe.passed = True
                self.score += 1
 
    def draw(self):
        self.screen.fill((135, 206, 235))  # sky blue

        for pipe in self.pipes:
            pipe.draw(self.screen)

        self.bird.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        highscore_text = self.font.render(f"Highscore: {self.highscore}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(highscore_text, (225, 10))

        if self.state == "game_over":
            self._draw_game_over()
 
    def _draw_game_over(self):
        text = self.font.render(f"Game Over! Score: {self.score}", True, (255, 0, 0))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2))
        hint = self.font.render("Press SPACE or LEFT MOUSE CLICK to restart", True, (255, 255, 255))
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        high_text = self.font.render(f"Best: {self.highscore}", True, (255, 255, 0))
        self.screen.blit(high_text, (SCREEN_WIDTH // 2 - high_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
