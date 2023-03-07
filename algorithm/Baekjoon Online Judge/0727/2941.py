s = input()
croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
i = 0
while i < len(s):
    if s[i:i+2] in croa:
        i += 1
        cnt += 1
    elif s[i:i+3] == 'dz=':
        i += 2
        cnt += 1
    else:
        cnt += 1
    i+=1

print(cnt)