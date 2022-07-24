from asyncio.windows_events import INFINITE


numbers = [-10, -100, -30] # -10 
max = -INFINITE
for i in numbers:
    if i > max:
        max = i

print('max =', max)