import sys
input = sys.stdin.readline

n,m = map(int,input().split())
num_list = list(map(int,input().split()))
pre_sum = [0]

for num in num_list:
    pre_sum.append(pre_sum[-1] + num)
# print(pre_sum)
cnt = 0
for i in range(1,n+1):
    for j in range(i):
        if m == pre_sum[i] - pre_sum[j]:
            cnt +=1
print(cnt)