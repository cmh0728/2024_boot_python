#global : 전역변수화 시키는 것. >> 메모리를 쓸데없이 많이 차지할 수도 있어서 유의해서 사용.


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
# 예외 

import random

my_nums = [random.randint(1,100) for i in range(5)] #random은 난수관련 모듈, randit메서드는 start 이상 stop 이하 범위의 정수 난수 생성
print(my_nums)

try:
    pick = int(input(f"Input index (0~ {len(my_nums)-1})"))
    print(my_nums[pick])
# except :          >>> index 이외에도 다른 에러가 있을 수 있기 때문에
#     print("Index_error :Out of range")

except IndexError as err : 
    print(f"Index_Error : Out of range\n{err}")
except ValueError : 
    print("Value Error : Input only number ~ ")
except Exception : # >> 위의 두개를 제외한 모든 예외를 처리하는 구문
    print("other error occurs")




# ----------------------------------------------------------------------------- #











# ----------------------------------------------------------------------------- #








# ----------------------------------------------------------------------------- #

