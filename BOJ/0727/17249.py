taebo = input()

l, r = 0, 0
left = True
for i in taebo:
    if i == '@' and left:
        l += 1
    elif i == '@':
        r += 1
    if i not in '@=':
        left = False
print(l,r)