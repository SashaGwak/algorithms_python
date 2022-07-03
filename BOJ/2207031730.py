# 기찍 2742번
# 입력
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
# 출력 
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
N = int(input())

# 풀이 1
# i = 1
# while N > 0:
#     print(N)
#     N -= i 

# 풀이 2 
for i in range(N, 0 , -1):
    print(i)


