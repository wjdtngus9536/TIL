with open('./3회차/정수현/00.txt', 'w',encoding="utf-8") as f:
    print("회차와 이름을 입력하시오:",end="")
    n,m=input().split()
    f.write(f"{int(n)}회차 {m}\nHello, Python!\n")
    for i in range(5):
        f.write(f"{i+1}일차 파이썬 공부중\n") 