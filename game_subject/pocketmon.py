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
        self.player_health = 3
        self.wild_poketmon_pos = pygame.Vector2(self.screen.get_width() / 2 + 230, self.screen.get_height() / 2-350)



        #player의 포켓몬 >> 피카츄 
        self.pikachu = ["pikachu","Electric",100,20]

        #이름 타입, 체력, 공격력 ( 뒤 두개 옵션은 일단은 동일하게 세팅 )
        bulbasaur = ["Bulbasaur", "Grass",  100, 20]
        charmander = ["Charmander", "Fire", 100, 20]
        squirtle = ["Squirtle", "Water", 100, 20]
        muche = ["muche", "espor", 10000, 200]
        #포켓몬 추가 란
        self.wild_pokemons = [bulbasaur, charmander, squirtle, muche]
        self.len_of_poketmon = len(self.wild_pokemons)



    def first_page(self):
        self.screen.fill("black")  # 배경 색
        self.start_image = pygame.image.load('start_poketmon.jpg')
        self.start_image = pygame.transform.scale(self.start_image, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(self.start_image, (0, 0))
        # self.draw_text("Welcome to the Pocketmon game!", 80, self.screen.get_width() / 2, self.screen.get_height() / 4)
        self.draw_text("Press 'F1' key to start the game                Press 'F2' key to know 'How to play '", 45, self.screen.get_width() / 2, self.screen.get_height() * 8 / 9)
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

    def game_over(self): #player hp == 0 -- > game over
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
                if keys[pygame.K_2]:  #탈출옵션(2번 선택)
                    # 이전 화면을 복원
                    self.screen.blit(self.prev_screen, (0, 0))
                    pygame.display.flip()
                    self.waiting = False  #대기 루프 탈출 trigger
                    return prev_screen
                if keys[pygame.K_1]: # 전투옵션(1번을 선택ㅈ)
                    self.random_number = random.randint(1, self.len_of_poketmon*2 -1) #포켓몬 수 인덱스로 제한
                    self.battle_figth_option(self.random_number,prev_screen) #이전 이동화면으로 
                    # print(random_number)
                    # print(self.pokemons[1])

    def battle_figth_option(self,random_number,prev_screen):
        self.screen.fill("white")  # 배경 색
        self.battle_start_origin = pygame.image.load('battle_start.png')
        self.fight_prev_screen = self.screen.copy() #첫 배틀 화면을 copy
        self.battle_start = pygame.transform.scale(self.battle_start_origin, (self.screen.get_width(), self.screen.get_height()))

        self.screen.blit(self.battle_start, (0, 0))
        

        self.draw_text("cannot fight yet", 45, self.screen.get_width() / 2, self.screen.get_height() * 7.5 / 9)
        self.draw_text("Press 'ESC' key to move previous screen", 45, self.screen.get_width() / 2, self.screen.get_height() * 8.3 / 9)


        print(random_number)

        # random_number = 2
        if random_number == 1:
            
            print(f"poketmon is {self.wild_pokemons[0][0]}")
            self.bulbassur_origin = pygame.image.load('bulbassur.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)


        elif random_number == 2:
            print(f"poketmon is {self.wild_pokemons[1][0]}")
            self.bulbassur_origin = pygame.image.load('charmander.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)

        elif random_number == 3:
            print(f"poketmon is {self.wild_pokemons[2][0]}")
            self.bulbassur_origin = pygame.image.load('squirtle.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)

        if random_number == 4:
            print(f"poketmon is {self.wild_pokemons[0][0]}")
            self.bulbassur_origin = pygame.image.load('bulbassur.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)


        elif random_number == 5:
            print(f"poketmon is {self.wild_pokemons[1][0]}")
            self.bulbassur_origin = pygame.image.load('charmander.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)

        elif random_number == 6:
            print(f"poketmon is {self.wild_pokemons[2][0]}")
            self.bulbassur_origin = pygame.image.load('squirtle.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)

        elif random_number == 7: # muche >> gameover
            print(f"poketmon is {self.wild_pokemons[3][0]}")
            self.bulbassur_origin = pygame.image.load('muche.png')
            self.bulbassur_image = pygame.transform.scale(self.bulbassur_origin, (self.screen.get_width()/3, self.screen.get_height()/3))

            self.screen.blit(self.bulbassur_image, self.wild_poketmon_pos)


        #간단한 배틀 화면 구현 및 전투 로직 구현, 불 > 풀 , 전기 = 불, 물> 불, 전기 > 물 , 물 = 풀 등의 로직으로 전투 구현, 
        #hp = 0 -- > 플레이어 hp -1 
        #text line
    

        pygame.display.flip()

        self.waiting = True
        while self.waiting:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_2]:  #탈출옵션
                    pass
                if keys[pygame.K_1]: # 전투옵션
                    # print(self.pikachu)
                    # print(self.len_of_poketmon)
                    # print(self.wild_pokemons)
                    pass
                if keys[pygame.K_ESCAPE]: 
                    self.screen.blit(self.prev_screen, (0, 0))
                    pygame.display.flip()
                    self.waiting = False


        
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
            if self.player_health >= 1 : 
                if self.total_movement >= random.randint(100, 500):  # 픽셀미터 단위 난수 추첨
                    # print("전투 시작!")
                    # 전투 시작 전의 화면을 저장합니다.
                    self.prev_screen = self.screen.copy()
                    self.battle_option(self.prev_screen)
                    self.total_movement = 0  # 전투 후 이동 거리를 초기화합니다.
            else : self.game_over()
        pygame.quit()




def main():
    game_class = pocketmon_game()
    game_class.run_game() # 게임실행

if __name__ == "__main__":
    main()
    