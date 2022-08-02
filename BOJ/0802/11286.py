import heapq, sys
sys.stdin = open('./20220802/input.txt')

heap = []

N = int(sys.stdin.readline( ))
for i in range(N):
    n = int(sys.stdin.readline())
    if n:
        heapq.heappush(heap, (abs(n), n))       # 
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)