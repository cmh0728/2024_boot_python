import sys
input = sys.stdin.readline

N , M = map(int,input().split())
#자연수 n과 m이 주어졌을때, 1부터 n까지 자연수중에서 중복없이 m개를 고른 수열

global num_list

def backtracking(i,M):
    num_list = [i]*N
    if M == 1:
        cnt = 1
        for j in num_list:
            if j != i : 
                print(cnt,end=' ')
                num_list[cnt-1] = 1
                break
            else : 
                cnt += 1

    else :
        backtracking(i,M-1)

for i in range(1,N+1):
    # num_list = [i]*N
    backtracking(i,M) #
    print()