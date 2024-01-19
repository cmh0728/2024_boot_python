import pygame
import sys
from pygame.locals import * 



class pocketmon():
    def __init__(self):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720)) # 화면 크기 설정
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("pocketmon game") #창 이름 설정
        self.running = True
        self.dt = 0
    
    def run_game(self):
        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the self.screen with a color to wipe away anything from last frame
            self.screen.fill("purple")

            pygame.draw.circle(self.screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * self.dt

            # flip() the display to put your work on self.screen
            pygame.display.flip()

            # limits FPS to 60
            # self.dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()

def main():
    game_class = pocketmon()
    game_class.run_game()

if __name__ == "__main__":
    main()
    