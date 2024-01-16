import sys
# input = sys.stdin.readline

class boot_camp:
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
        option = int(input("select option 1)'check prime number' 2)prime number between two number : "))
        if option == 1:
            number = int(input("Input number : "))
            class_name = boot_camp()
            rst = class_name.prime_number(number)
            if rst == 1: #1반환하면 소수
                print(f'{number} is prime number')
            elif rst == 0 : #아니면 소수x
                print(f'{number} is "not" prime number')
        elif option == 2:
            first_number = int(input("first number : "))
            second_number = int(input("second number : "))
            class_name = boot_camp()
            rst_array = class_name.prime_numbers_list(first_number,second_number)
            print("The prime numbers : ",end=' ')
            print('"',end=' ')
            for i in range(len(rst_array)):
                print(rst_array[i],end=' ')
            print('"',end='')
    except: 
        print("error")

if __name__ == "__main__":
    main()

