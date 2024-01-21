import pygame
import sys
from pygame.locals import * 

class Pokemon:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack

    def attack(self, other):
        other.health -= self.attack

class pocketmon_game():
    def __init__(self):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720)) # 화면 크기 설정
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("pocketmon game") #창 이름 설정
        self.running = True #게임 triger설정
        self.dt = 0
        self.waiting = True

        self.bulbasaur = Pokemon("이상해씨", ["풀", "독"], 100, 20)
        self.charmander = Pokemon("파이리", ["불꽃"], 100, 20)
        self.squirtle = Pokemon("꼬부기", ["물"], 100, 20)
        self.caterpie = Pokemon("캐터피", ["벌레", "풀"], 100, 20)
        self.pidgey = Pokemon("구구", ["노말"], 100, 20)
        self.rattata = Pokemon("꼬렛", ["노말"], 100, 20)
        self.pikachu = Pokemon("피카츄", ["전기"], 100, 20)
        self.oddish = Pokemon("모다피", ["풀"], 100, 20)
        self.chikorita = Pokemon("치코리타", ["풀"], 100, 20)
        self.drowzee = Pokemon("마자용", ["에스퍼"], 100, 20)

        self.pokemons = [self.bulbasaur, self.charmander, self.squirtle, self.caterpie, self.pidgey, self.rattata, self.pikachu, self.oddish, self.chikorita, self.drowzee]


    def first_page(self):
        self.screen.fill("black")  # 배경 색
        self.start_image = pygame.image.load('start_poketmon.jpg')
        self.start_image = pygame.transform.scale(self.start_image, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(self.start_image, (0, 0))
        # self.draw_text("Welcome to the Pocketmon game!", 80, self.screen.get_width() / 2, self.screen.get_height() / 4)
        self.draw_text("Press 'F2' key to know 'How to play '           Press 'F1' key to start the game", 45, self.screen.get_width() / 2, self.screen.get_height() * 8 / 9)
        # self.draw_text("Press 'F1' key to start the game", 35, self.screen.get_width() / 2, self.screen.get_height() / 2)

        pygame.display.flip()

        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F1]:  # F1 key 누르면 시작
                    self.waiting = False  #대기 루프 탈출 trigger
                if keys[pygame.K_F2]:
                    self.How_to_play_game()

    def How_to_play_game(self): #게임에 대한 설명
        self.screen.fill("white")
        self.draw_text("Use 'W','A','D','S' keys to move player",50, self.screen.get_width() / 2, self.screen.get_height() / 4)
        self.draw_text("Choose multiple options to fight!",50,self.screen.get_width()/2, self.screen.get_height()*2/4)
        # 부가 게임 설명 필요
        
        self.draw_text("Press 'F1' key to start the game", 35, self.screen.get_width() / 2, self.screen.get_height() *3/4)

        
        pygame.display.flip()

        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F1]:  # F1 key 누르면 시작
                    self.waiting = False  #대기 루프 탈출 trigger

    def draw_text(self,text,size,x,y):
        font = pygame.font.Font(None, size)
        text_surface=font.render(text, True,(0,0,0)) #글자 검정색으로 설정.
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface, text_rect)

    def game_over(self):
        self.draw_text("GAME OVER",  48, self.screen.get_width()/ 2, self.screen.get_height() / 2)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
    
    def run_game(self):
        self.first_page()
        player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

        while self.running: 
            #탈출조건 : x누르기
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black") # 배경 색

            pygame.draw.circle(self.screen, "white", player_pos, 10) # 플레이어 색

            #방향키로 플레이어(가운데 점) 조종
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 300 * self.dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * self.dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * self.dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * self.dt
            # if keys[pygame.K_TAB]: #>>나중에 설정
            #     self.game_over()
            # flip() the display to put your work on self.screen
            pygame.display.flip()

            # 프레임 조정
            # self.dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(60) / 1000

        pygame.quit()




def main():
    game_class = pocketmon_game()
    game_class.run_game() # 게임실행

if __name__ == "__main__":
    main()
    