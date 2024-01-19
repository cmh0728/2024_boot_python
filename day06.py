#global : 전역변수화 시키는 것. >> 메모리를 쓸데없이 많이 차지할 수도 있어서 유의해서 사용.


# 재귀함수 

def factorial_recursion(n):
    if n == 1:
        return n
    else : 
        return n*factorial_recursion(n-1)
    
def fiboncahi(n):
    if n == 1 or n == 2:
        return 1
    else : 
        return fiboncahi(n-1) + fiboncahi(n-2)
    
number = int(input())
print(factorial_recursion(number))
print(fiboncahi(number))