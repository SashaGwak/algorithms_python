# A+B -4(10951)
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.
import sys

while True:
    try:
    # 변수에 int형이 들어가면 print를 출력한다
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except: 
    # try에 대한 에러가 발생한 경우 
        break

# try_except 구문 
# 파이썬에서 구문 오류가 발생할 때 해결할 수 있는 코드
# try 쪽에 에러가 발생한 가능성이 있는 코드를 작성하고 
# except 쪽에 예외 발생시 실행할 코드를 지정한다(예외 실제 발생시 실행됨)