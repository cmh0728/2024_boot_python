# 튜플 자료형과 리스트 자료형의 큰 차이점 
#1. 튜플은 요소를 변경하거나 삭제할 수 없다. 리스트는 가능 >>실제로는 리스트를 훨씬 많이 사용 
#2. 인덱싱이나 슬라이싱은 가능. 반드시 ','를 사용해야 튜플 자료형이다. 
#파이썬은 객체를 리스트나 튜플 형태로 다양한 값을 담아서 반환할 수 있음. >>장점 
# 뮤터블 : 변경이 가능한 객체 , 이뮤터블 : 변경이 불가능한 객체 
# 뮤터블(mutable)
# - 변경이 가능한 객체
# - 생성 후 자유롭게 값을 변경, 추가, 삭제 등이 가능하다.
# - list, set, dictionary 등
# - 변수의 값을 변경하면 객체 자체를 업데이트 한다. (값 변경 -> 할당된 메모리에 전달)
# - call by reference(참조에 의한 호출)
#  
# 이뮤터블(immutable)
# - 변경이 불가능한 객체
# - 생성 후 값 변경, 추가, 삭제 등이 불가능하다.
# - 숫자, string, tuple 등
# - 변수의 값을 변경하면 다른 객체를 생성하고 그 객체에 대한 참조로 업데이트 된다.
#   (값 변경 -> 새로운 메모리에 전달)
# - call by value(값에 의한 호출)
    
# 과제 p205의 8.10까지 문제해결(10개)

# # 8.1
# import sys
# input = sys.stdin.readline


# e2f = dict([("dog","chien"),("cat","chat"),("walrus","morse")])
# print(e2f)

# #8.2
# import sys
# input = sys.stdin.readline

# e2f = dict([("dog","chien"),("cat","chat"),("walrus","morse")])
# # print(e2f)
# print(e2f["walrus"])

# #8.3
# import sys
# input = sys.stdin.readline
# e2f = dict([("dog","chien"),("cat","chat"),("walrus","morse")])
# f2e = {}
# # print(e2f)
# for key,value in e2f.items():
#     # print(key,value)
#     f2e[value] = key
# print(f2e)


# #8.4
# import sys
# input = sys.stdin.readline
# e2f = dict([("dog","chien"),("cat","chat"),("walrus","morse")])
# f2e = {}
# # print(e2f)
# for key,value in e2f.items():
#     # print(key,value)"
#     f2e[value] = key
# # print(f2e)
# print(f2e["chien"])

# #8.5
# e2f = dict([("dog","chien"),("cat","chat"),("walrus","morse")])
# print(e2f.keys())

# #8.6 >> 이차원 딕셔너리 만들기 
# life = dict()

# my_dict2 = dict([("cats","Henri"),("octopi","Grumpy"),("emus","Lucy")])
# life["animals"] = my_dict2
# life["plants"] = {}
# life["other"] = {}

# print(life)

# #8.7
# life = dict()

# my_dict2 = dict([("cats","Henri"),("octopi","Grumpy"),("emus","Lucy")])
# life["animals"] = my_dict2
# life["plants"] = {}
# life["other"] = {}

# print(life.keys())
# #8.8

# life = dict()

# my_dict2 = dict([("cats","Henri"),("octopi","Grumpy"),("emus","Lucy")])
# life["animals"] = my_dict2
# life["plants"] = {}
# life["other"] = {}

# print(life["animals"].keys())

# #8.9
# life = dict()

# my_dict2 = dict([("cats","Henri"),("octopi","Grumpy"),("emus","Lucy")])
# life["animals"] = my_dict2
# life["plants"] = {}
# life["other"] = {}

# print(life["animals"]["cats"])


# #8.10
# squares = {k : k**2 for k in range(10)}
# print(squares)

#컴프리헨션 예시 
# name = ['YB', 'SW', 'EJ', 'HJ']
# age = [32, 31, 28, 28]

# #딕셔너리 생성(name : age)
# name_dic = dict(zip(name,age))

# #나이가 28살인 사람만 딕셔너리로 생성하는 컴프리헨션
# dict1 = {k : v for k, v in name_dic.items() if v == 28}

# #이름이 YB인사람만 딕셔너리로
# dict2 = {k : v for k, v in name_dic.items() if k =="YB"}

# #key와 value를 서로 바꾸기
# dict3 = {v : k for k, v in name_dic.items()}


# 출처: https://ybworld.tistory.com/96 [투손플레이스:티스토리]