from sys import*

first_number = int(input('First number : '))
second_number = int(input('Second number : '))

quotient = first_number // second_number
remainder = first_number % second_number

print(f'몫은 {quotient} 나머지는 {remainder}입니다.')

#divmod함수를 이용해서 몫과 나머지를 구할 수 있다. 

print(f'몫은 {divmod(first_number,second_number)[0]} 나머지는 {divmod(first_number,second_number)[1]}입니다.')
