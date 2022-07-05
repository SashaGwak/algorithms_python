# A + B - 8(11022번)
# 입력 
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
import sys

T = int(input())
a_list = []
b_list = []
sum_list = []
count = 1 

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    a_list.append(a)
    b_list.append(b)
    sum_list.append(a + b)

for j in range(0, T):
    print("Case #{}: {} + {} = {}".format(count, a_list[j], b_list[j], sum_list[j]))
    count += 1 