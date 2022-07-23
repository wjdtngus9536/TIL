with open('data/fruits.txt', 'r',encoding="utf-8") as d:
    lines=d.readlines()
lines=[line.rstrip('\n') for line in lines]
#print(len(lines))    
with open('01.txt', 'w',encoding="utf-8") as a:
    a.write(str(len(lines))+"\n")