# not은 True, False를 반환하게 한다. --> 논리연산자이기 때문에, 판단을 한다. 
# *n을 이용하면 튜플과 같은 것도 넣을 수 있다.


#generator 를 이용해보기


# rst = sum(range(1,101))
# print(rst)

#decorater, inner function,,,

# day05 과제
#p.242 9.16 연습문제
 
#9.1 

# def good():
#     my_list = ["Harry","Ron","Hermione"]
#     return my_list

# print(good())

# #9.2  제너레이터 이용 , for 문으로 반환된 세번째 홀수를 찾아서 출력한다.
# def get_odds():
#     odds = []
#     for i in range(10):
#         if i%2 !=0:
#             odds.append(i)
#     return odds

# print(get_odds()[2]) >>제너레이터를 이용하지 않은거같은데..

# 제너레이터 예시
# def my_range(first , last , step=1):
#     number = first
#     while number < last : 
#         yield number
#         number += step

# print(my_range)
# ranger = my_range(1,5)
# for x in ranger:
#     print(x)

#9.2 another answer


# def get_odds(first=0, last=9, step=1): # >> 홀수 제너레이터 반환
#     number = first 
#     while number < last:
#         if number %2 != 0:
#             yield number
#         else : 
#             pass
#         number += step

# odds_ranger = get_odds()
# count = 1
# for i in odds_ranger:
#     if count == 3:
#         print(i)
#         break
#     else : 
#         count+=1

# #9.3 어떤 함수가 호출되면, start를 , 끝나면 end를 출력하는 test 데커레이터를 정의

# def test(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# # 데커레이터를 사용할 함수 정의
# @test
# def my_function():
#     # print('함수 내용')
#     return

# # 함수 호출
# my_function()
