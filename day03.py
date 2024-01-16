#1. 과제 
# 섭씨 화씨 4번메뉴가 구간소수구하기 , 3번메뉴가 소수 판정프로그램, 종료는 알아서 
# 교재에 있는 143
# 연습문제 6.5

# 화씨 섭씨 변환공식
# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F
import sys
# input = sys.stdin.readline

class subject_program():
    def __init__(self):
        pass

    def  prime_number(self,n):

        if n == 1:
            return 0
        else :
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return 0
            else : 
                return 1
    
    def prime_numbers_list(self,a,b):
        arr = []
        for i in range(a,b+1):
            rst = self.prime_number(i)
            if rst == 0 : #소수가 아닐때 
                continue
            elif rst == 1 : #소수일때 
                arr.append(i)
        return arr
    
def main():
    try:
        while True:
            menu = input("'menu'를 선택하세요 --> 1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit  3)check prime number 4)prime number between two number :  q) Quit program : ")
            if menu == '1':
                fahrenheit = float(input('Input Fahrenheit : '))
                print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
            
            elif menu == '2':
                celsius = float(input('Input Celcius : '))
                print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
            
            elif menu == '3':
                number = int(input("Input number : "))
                class_name = subject_program()
                rst = class_name.prime_number(number)
                if rst == 1: #1반환하면 소수
                    print(f'"{number}" is prime number')
                elif rst == 0 : #아니면 소수x
                    print(f'"{number}" is "not" prime number')
                
                print()

            elif menu == '4':
                first_number = int(input("first number : "))
                second_number = int(input("second number : "))
                class_name = subject_program()
                rst_array = class_name.prime_numbers_list(first_number,second_number)
                print("The prime numbers are : ",end=' ')
                for i in range(len(rst_array)):
                    print(f'"{rst_array[i]}"',end=' ')
                print()


            elif menu == "q" : 
                print("프로그램이 종료되었습니다.")
                break
    except : 
        print("error!!")

if __name__ == "__main__":
    main()

      