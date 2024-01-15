import sys
input = sys.stdin.readline

class bk_joon : 
    def __init__(self):
        pass

    def add_func(self,a,b):
        rst = a+b
        return rst

def main():
    try:
        a,b = map(int,input().split())
        func = bk_joon()
        rst = func.add_func(a,b)
        print(rst)
    except: print('error')


if __name__ == "__main__":
    main()
