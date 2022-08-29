import heapq,sys
sys.stdin = open('./20220802/input.txt')

numbers = []
N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(numbers, x)
for i in range(N):
    print(heapq.heappop(numbers))
