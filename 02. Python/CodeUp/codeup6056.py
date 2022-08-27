from operator import xor

a,b = map(int, input().split())
print(bool(a) ^ bool(b))