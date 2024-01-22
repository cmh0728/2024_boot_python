import pygame
import sys
from pygame.locals import * 
import random

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
        self.total_movement = 0  # 플레이어의 총 이동 거리를 추적하고, 전투상황 발생

        #player의 포켓몬 >> 피카츄 
        self.pikachu = Pokemon("Pikachu", ["Electric"], 100, 20)

        #이름 타입, 체력, 공격력 ( 뒤 두개 옵션은 일단은 동일하게 세팅 )
        self.bulbasaur = Pokemon("Bulbasaur", ["Grass", "Poison"], 100, 20)
        self.charmander = Pokemon("Charmander", ["Fire"], 100, 20)
        self.squirtle = Pokemon("Squirtle", ["Water"], 100, 20)
        self.caterpie = Pokemon("Caterpie", ["Bug", "Grass"], 100, 20)
     


        self.pokemons = [self.bulbasaur, self.charmander, self.squirtle, self.caterpie]
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
    
    def battle_option(self,prev_screen):
        self.screen.fill("white")  # 배경 색
        self.battle_start_origin = pygame.image.load('battle_start.png')
        self.battle_start = pygame.transform.scale(self.battle_start_origin, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(self.battle_start, (0, 0))
        basic_battle_screen = self.screen.copy()
        
        #text line
        self.draw_text("Press '1' key to fight               Press '2' key to run away", 45, self.screen.get_width() / 2, self.screen.get_height() * 8.3 / 9)

        pygame.display.flip()

        self.waiting = True
        while self.waiting:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_2]:  #탈출옵션
                    # 이전 화면을 복원
                    self.screen.blit(self.prev_screen, (0, 0))
                    pygame.display.flip()
                    self.waiting = False  #대기 루프 탈출 trigger
                    return prev_screen
                if keys[pygame.K_1]: # 전투옵션
                    self.random_number = random.randint(1, 5)
                    self.battle_figth_option(self.random_number)
                    # print(random_number)
                    # print(self.pokemons[1])

    def battle_figth_option(self,random_number):
        self.screen.fill("white")  # 배경 색
        self.battle_start_origin = pygame.image.load('battle_start.png')
        self.battle_start = pygame.transform.scale(self.battle_start_origin, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(self.battle_start, (0, 0))
        basic_battle_screen = self.screen.copy()
        
        #text line

        pygame.display.flip()

        self.waiting = True
        while self.waiting:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_F2]:  #탈출옵션
                    pass
                if keys[pygame.K_F1]: # 전투옵션
                    pass

        
    def run_game(self):
        self.first_page()
        self.grass_image_origin = pygame.image.load('background_image.png')
        self.player_image = pygame.image.load('player.png')
        

        # player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        player_pos = pygame.Vector2(self.screen.get_width() / 2 - 25, self.screen.get_height() / 2-25)

        while self.running: 

            #탈출조건 : x누르기
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black") # 배경 색

            # pygame.draw.circle(self.screen, "white", player_pos, 10) # 플레이어 색
            self.grass_image = pygame.transform.scale(self.grass_image_origin, (self.screen.get_width(), self.screen.get_height()))

            self.screen.blit(self.grass_image, (0, 0))
            self.screen.blit(self.player_image, player_pos)

            #방향키로 플레이어(가운데 점) 조종
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 300 * self.dt
                self.total_movement += 300 * self.dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * self.dt
                self.total_movement += 300 * self.dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * self.dt
                self.total_movement += 300 * self.dt
            if keys[pygame.K_d]:
                player_pos.x += 300 * self.dt
                self.total_movement += 300 * self.dt
            # if keys[pygame.K_TAB]: #>> test
            #     self.game_over()
            # flip() the display to put your work on self.screen
            pygame.display.flip()

            # 프레임 조정
            self.dt = self.clock.tick(60) / 1000

            # 무작위 전투 발생조건(픽셀)
            if self.total_movement >= random.randint(100, 500):  # 픽셀미터 단위 난수 추첨
                # print("전투 시작!")
                # 전투 시작 전의 화면을 저장합니다.
                self.prev_screen = self.screen.copy()
                self.battle_option(self.prev_screen)
                self.total_movement = 0  # 전투 후 이동 거리를 초기화합니다.

        pygame.quit()




def main():
    game_class = pocketmon_game()
    game_class.run_game() # 게임실행

if __name__ == "__main__":
    main()
    