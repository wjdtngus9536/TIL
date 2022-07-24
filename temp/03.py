n = int(input())
# 1) while
s = 0
i = 0
while i <= n:
	s+=i
	i+=1
print('by wihle :',s)

# 2) for
s = 0
for i in range(n+1):
	s+=i

print('by for :', s)