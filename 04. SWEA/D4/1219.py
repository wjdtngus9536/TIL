import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
   t, V = map(int, input().split())
   lst = list(map(int, input().split()))
   arr = {}
   for i in range(0, V*2, 2):
       v = lst[i]
       e= lst[i+1]
       arr[v] = arr.get(v, [])+ [e]
   stack = []
   stack.append(0)
   visit = [0] * 100
   while stack:
       x = stack.pop()
       visit[x] = 1
       if x in arr.keys():
           for w in arr[x]:
               if not visit[w]:
                   stack.append(w)
   print('#%d %d'%(t, visit[-1]))