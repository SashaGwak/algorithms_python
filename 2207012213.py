import sys

T = int(input())
sum = []

for i in range(0, T):
    # 반복문으로 여러줄을 입력받아야 할 때 input 사용하면 시관초과 발생할 수있음! 
    a, b = map(int, sys.stdin.readline().split())
    sum.append(a + b)

for i in sum:
    print(i)