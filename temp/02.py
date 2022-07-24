'''
문자열 word의 길이를 출력하는 코드를 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.
len() 함수 사용 금지
'''
# input
word = 'happy!'

# 1) while문
i=0
while word[i:]:i+=1 
print(i)

# 2) for문(문자열 그대로)
i=0
for letter in word:i += 1
print(i)

# 3) for문(index)
for i, letter in enumerate(word):pass
print(i+1)