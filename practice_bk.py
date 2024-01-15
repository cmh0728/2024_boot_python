import sys
input = sys.stdin.readline

class boot_camp:
    def __init__(self):
        pass

    def factorial(self,num):
        if num <=0:
            return 0
        elif num ==1 :
            return 1
        else : 
            return self.factorial(num-1) + self.factorial(num-2)
        
                
    
def main():
    try:
        num = int(input())
        func = boot_camp()
        rst = func.factorial(num)
        print(rst)
    except: 
        print("error")

if __name__ == "__main__":
    main()

