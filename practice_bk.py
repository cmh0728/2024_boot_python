import sys
input = sys.stdin.readline

class boot_camp:
    def __init__(self):
        pass

    def  prime_number(self):
        return 0
                
    
def main():
    try:
        number = int(input())

    except: 
        print("error")

if __name__ == "__main__":
    main()

# 1 1 2 3 5 8 13 fibonachi    
    
def fibonachi_1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonachi_1(n-1) + fibonachi_1(n-2)

def fibonachi_2(n):
    dp=[0]*(n+1)
    dp[1] =1
    dp[2] =1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]