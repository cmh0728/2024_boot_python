# 1/15 예습 
# 반복문으로 3번을 누르기 전까지는 계속 프로그램이 돌아가며 
# 화씨, 섭씨 온도를 변환해주고, 3을 누르면 프로그램 종료

# 화씨 섭씨 변환공식
# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F
import sys
# input = sys.stdin.readline

while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
    elif menu == '2':
        celsius = float(input('Input Celcius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
    else : 
        print("프로그램이 종료되었습니다.")
        break
        

