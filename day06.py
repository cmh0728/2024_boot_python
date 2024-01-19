# ----------------------------------------------------------------------------- #
# day 06 

# global : 전역변수화 시키는 것. >> 메모리를 쓸데없이 많이 차지할 수도 있어서 유의해서 사용.


# # 재귀함수 

# def factorial_recursion(n):
#     if n == 1:
#         return n
#     else : 
#         return n*factorial_recursion(n-1)
    
# def fiboncahi(n):
#     if n == 1 or n == 2:
#         return 1
#     else : 
#         return fiboncahi(n-1) + fiboncahi(n-2)
    
# number = int(input())
# print(factorial_recursion(number))
# print(fiboncahi(number))

# ----------------------------------------------------------------------------- #
# 예외 처리

# import random

# my_nums = [random.randint(1,100) for i in range(5)] #random은 난수관련 모듈, randit메서드는 start 이상 stop 이하 범위의 정수 난수 생성
# print(my_nums)

# try:
#     pick = int(input(f"Input index (0~ {len(my_nums)-1})"))
#     print(my_nums[pick])
# # except :          >>> index 이외에도 다른 에러가 있을 수 있기 때문에
# #     print("Index_error :Out of range")

# except IndexError as err : 
#     print(f"Index_Error : Out of range\n{err}")
# except ValueError : 
#     print("Value Error : Input only number ~ ")
# except Exception : # >> 위의 두개를 제외한 모든 예외를 처리하는 구문
#     print("other error occurs")

# ----------------------------------------------------------------------------- #

# object and class

# class poketmon():
#     def __init__(self): #>>init단은 객체마다 딱 한번씩만 돌음 , 꼭 필요하지는 않음.
#         pass

#     def func1(self, name): #관례적으로 self를 사용, 객체가 자기 자신을 호출하기 때문에
#         self.name = name
#         print(f"{name} 포켓몬스터 생성")

#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) 공격!")
# def main():
#     seung_hyeon = poketmon()
#     # seung_hyeon.name = "승현"
#     seung_hyeon.func1("승현")
#     hyeon_gu = poketmon()
#     hyeon_gu.func1("형구")
#     siu = poketmon()
#     siu.func1("시우")

#     siu.attack(seung_hyeon)
#     # print(seung_hyeon.name)
#     # print(hyeon_gu.name)

# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------------------- #
# 상속 클래스 
# example 1 : 난수발생 모듈을 이용해서 랜덤한 데미지로, 다른 객체를 공격하고, 판단하는 코드 작성
# import random 
# class Pokemon:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.power = random.randint(1,10) # 공격력을 난수로 발생

#     def attack(self, target):
#         print(f"{self.name}이(가) {target.name}을(를) {self.power}의 데미지로 {self.type} 공격했다.")
#         if self.power > 5 : 
#             print(f"{target.name}에게 공격 효과는 굉장했다!!.")
#         else : 
#             print(f"{target.name}에게 공격 효과가 미미한듯 하다..")


# class Pikachu(Pokemon): 
#     pass


# class Squirtle(Pokemon):
#     pass

# class Charizard(Pokemon): 
#     pass
# p1 = Pikachu('피카츄', '전기')
# p2 = Squirtle('꼬부기', '물')


# p3 = Charizard('차라드', '불')
# # print(p3.name)
# p3.attack(p1)

# # print(p1.name)
# p1.attack(p2)

# ----------------------------------------------------------------------------- #

# example 2

# import random

# class Pokemon:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.power = random.randint(1, 10)

#     def attack(self, target):
#         print(f"{self.name}의 {self.type} 포켓몬이 {target.name}의 {target.type} 포켓몬을 공격하여 {self.power}의 데미지를 입혔습니다.")

# pokemon_types = ['불', '물', '전기', '풀', '얼음', '독', '페어리', '고스트', '악', '땅', '바위', '벌레', '노말', '행크', '피카츄', '스텔스', '드래곤', '무적']

# people_list = ["승현","민혁","흑구","시우","제언","의제","승민","후원","성현","백구","형구 "]

# # 각 사람에게 무작위로 포켓몬 할당
# pokemon_list = [Pokemon(name, random.choice(pokemon_types)) for name in people_list]

# # 리스트에서 무작위로 두 명 선택
# person1 = random.choice(pokemon_list)
# pokemon_list.remove(person1)  # 이미 선택된 사람은 리스트에서 제거
# person2 = random.choice(pokemon_list)

# # 두 사람의 포켓몬이 서로 공격
# person1.attack(person2)
# person2.attack(person1)

# ----------------------------------------------------------------------------- #
class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 날아갑니다."
class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 바닷속을 헤엄칩니다"

class Poketmon:
    def __init__(self,name):
        self.name = name
    
    def attack(self):
        return "공격" # >> return이 없으면 NOne을 반환하기 때문에 , 이런식으로 해주는게 방지할 수 있음    
    
    def get_name(self):
        print("inside getter")
        return self.name
    
    def set_name(self,new_name):
        self.name = new_name
class Charizard(Poketmon, FlyingMixin):
   pass
     

class Gyarados(Poketmon , SwimmingMixin):
    pass
g1 = Gyarados('갸라도스')
c1 = Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# print(c1.attack())

# g1.name = "잉어킹"
# print(g1.swim())

print(g1.get_name())
g1.set_name("잉어킹")
print(g1.get_name())
# ----------------------------------------------------------------------------- #

# 시험 >> 중간중간 commit을 해야됨. 시험범위 : 다음주 오전까지 배운 내용(모듈). , 월요일 오후 시험.(22일)
# 과제 : 포켓몬 게임 만들기 1. 기획(등장인물, 캐릭터, 공격, 기능, 공격순서, 진화 등등 ), 2.창열어서 텍스트 기반으로,, 3. save파일 등등  

# ----------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------- #
