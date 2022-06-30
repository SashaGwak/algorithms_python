# 합 8393번
# n 이 주어졌을때 1부터 n까지의 합을 구하는 프로그램 작성하시오.
n = int(input())
i = 1
sum = 0

while n > 0:
    sum += n
    n -= i
    
print(sum)