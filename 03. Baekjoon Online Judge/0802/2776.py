# import sys
# T = int(sys.stdin.readline())
# for i in range(T):
#     N = sys.stdin.readline()
#     note1 = list(map(int, sys.stdin.readline().split()))
#     M = int(sys.stdin.readline())
#     note2 = list(map(int, sys.stdin.readline().split()))
#     for i in note2:
#         if i in note1:
#             print(1)
#         else:
#             print(0)

I=input
exec("I();s={*I().split()};I();[print(+(e in s))for e in I().split()];"*int(I()))