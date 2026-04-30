import pygame
from game import Game
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60  # frames per second, controls how fast the game runs
 
def main():
    pygame.init()  # start up all pygame modules (display, sound, etc.)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create the window
    pygame.display.set_caption("Flappy Bird")  # title shown at the top of the window
    clock = pygame.time.Clock()  # used to control the frame rate
 
    game = Game(screen)  # create our Game object and pass the screen to it
 
    running = True
    while running:  # main game loop, runs once per frame
 
        # --- handle events (keyboard, mouse, window close) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # user clicked the X button
                running = False
            game.handle_event(event)  # pass the event to the game (e.g. flap)
 
        # --- update game state (move bird, pipes, check collisions) ---
        game.update()
 
        # --- draw everything to the screen ---
        game.draw()
 
        pygame.display.flip()  # push everything we drew to the actual screen
        clock.tick(FPS)  # wait long enough to maintain our target FPS
 
    pygame.quit()  # cleanly shut down pygame when the loop ends
 
if __name__ == "__main__":
    main()  # only run if this file is executed directly (not imported)
