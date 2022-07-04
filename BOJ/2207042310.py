# A + B -7(11021번)
# 입력 
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다./kr/mac-jpg/
import sys
T = int(input())
result = []

for i in range(0, T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a + b)

for j in range(0, T):
    print("Case #{}: {}".format(j + 1, result[j]))
