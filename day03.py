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
            
    
def main():
    try:
        number = int(input("Input number : "))
        class_name = boot_camp()
        rst = class_name.prime_number(number)
        if rst == 1:
            print(f'{number} is prime number')
        elif rst == 0 :
            print(f'{number} is "not" prime number')

        
    except: 
        print("error")

if __name__ == "__main__":
    main()

