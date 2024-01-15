import sys


# 다양한 입출력 방법

base_number = int(input("Input base number : "))
exponent_number = int(input("Input exponent number : "))

# f-string
print(f'base_number : {base_number}, exponent_number : {exponent_number}, result : {base_number**exponent_number}')

# format function
# print('밑은 {}, 지수는 {}, 결과값은 {}'.format(*args: base_number, exponent_number, pow(base_number,exponent_number)))

#c like(c와 유사한 방법)
print('밑은 %d, 지수는 %d, 결과 값은 %d' %(base_number, exponent_number, pow(base_number,exponent_number)))