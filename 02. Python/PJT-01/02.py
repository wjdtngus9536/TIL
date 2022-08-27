with open('./data/fruits.txt', 'r',encoding="utf-8") as d:
    text=d.read()
    fruit=text.split("\n")
    #fruit=text
    f_list=[]
    cnt=0
    #print(lines)
    for i in fruit:
        if i.endswith("berry") or i.endswith(" berry"):
            cnt+=1
            if i in f_list:
                continue
            else:
                f_list.append(i)
    #print(len(f_list))
    with open('./02.txt', 'w',encoding="utf-8") as a:
        a.write(str(len(f_list))+"\n")
        for x in range(len(f_list)):
            a.write(f_list[x]+"\n")