# https://www.acmicpc.net/problem/12851

"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

예제 입력 1
5 17

예제 출력 1
4
2
"""

import sys; input=sys.stdin.readline
from collections import deque

# 수빈 N, 동생 K
N, K = map(int, input().split())

# 찾는 값을 인덱스로, 인덱스의 값을 찾아본 횟수로 하는 distance
MAX = 100000; distance = [0 for _ in range(MAX + 1)]

cnt = 0

# 수빈의 값으로 시작
q = deque([N])
while  q:
    x = q.popleft()

    # 찾으면 개수 + 1
    if x == K:
        cnt += 1
        continue

    # 3개씩 탐색, 너비우선탐색
    for next_x in (x - 1, x + 1, x * 2): # 걷기(x+1, x-1) / 순간이동(2x)
        if  0 <= next_x <= MAX and (distance[next_x] == distance[x] + 1 or distance[next_x] == 0):
            distance[next_x] = distance[x] + 1
            q.append(next_x)

print(distance[K])
print(cnt)