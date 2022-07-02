# 블랙잭 2798번
# 입력
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 출력 
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
import sys
import itertools

# N, M 값 받기
N, M = map(int, input().split())

# 카드 숫자 저장되는 리스트 생성
card_list = []
card_input = map(int, sys.stdin.readline().split())
for i in card_input:
    card_list.append(i)

# 카드 3장을 더해 나올 수 있는 모든 경우의 수 리스트 생성(M 보다 큰 수 제외)
combi_sum = [sum(combi) for combi in itertools.combinations(card_list, 3) if sum(combi) <= M] 

# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
print(max(combi_sum))