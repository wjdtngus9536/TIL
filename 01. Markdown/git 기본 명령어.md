# 2. git 기본 명령어



## 2-1. git init

현재 디렉토리에 .git 폴더를 만들어서 깃이 버전 관리를 할 수 있게 함



## 2-2. git add <파일명>

인덱스의 내용과 비교했을 때 로컬에서 변동된 사항을 인덱스에 반영 시키는 명령어.

<파일명> 대신 . 기호를 사용하면 로컬의 혀내 디렉토리에서 add 명령의 대상이 되는 파일들 전부를 인덱스에 반영한다.



## 2-3. git commit -m <메세지>

인덱스의 내용을 바탕으로 새로운 **버전**(commit 파일)을 생성하는 명령어.

특정 시점에 존재하는 파일들의 정보에 대한 스냅샷을 찍어서 하나의 버전으로서 저장해두겠다는 의미.

<메세지>에는 해당 버전에 대한 설명 등을 기록할 수 있다.

 

## 2.4. git status

- ### a.txt 파일을 만든 직후

```bash
$ git status
# 지금 당장은 설명 넘어가고
On branch master

# Working Directory에 저장된 파일들?
Untracked files:
# git add 사용해봐..
# 포함시키기 위해서 / 커밋이 될 것
  (use "git add <file>..." to include in what will be committed)
        a.txt
# Staging Area가 비어있고, Add 되지 않은 파일이 존재한다.
nothing added to commit but untracked files present (use "git add" to track)
```

- ### b.txt 파일을 만들고 add한 이후

```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt
```





## git log







