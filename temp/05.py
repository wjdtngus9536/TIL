from asyncio.windows_events import INFINITE


numbers = [4, 10, 20]
s=0
cnt=0
for i in numbers:
    s += i
    cnt += 1

print(format(s/cnt, ".2f"))