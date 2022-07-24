n = int(input())
# 1) while
m = 1
i = 1
while i <= n:
	m*=i
	i+=1
print('by wihle :',m)

# 2) for
m = 1
for i in range(n):
	m*=i+1

print('by for :', m)