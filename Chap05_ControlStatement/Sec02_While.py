# -*- coding:utf-8 -*-
"""
2) while문

while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...

“열 번 찍어 안 넘어 가는 나무 없다” 라는 속담을 파이썬에 적용시켜 보면 다음과 같이 될 것이다.

>>> treeHit = 0
>>> while treeHit < 10:
. . .     treeHit = treeHit +1
. . .     print("나무를 %d번 찍었습니다." % treeHit)
. . .     if treeHit == 10:
. . .         print("나무 넘어갑니다.")
. . .
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.

""""""

	무한루프(Loop)

while 1:    
    <수행할 문장1>     
    <수행할 문장2>
    ...

""""""
>>> prompt = '''
. . . 1. Add
. . . 2. Del
. . . 3. List
. . . 4. Quit
. . .
. . . Enter number: '''
>>> number = 0
>>> while number != 4:
. . .     print(prompt)
. . .     number = int(input())
. . .

1. Add
2. Del
3. List
4. Quit

Enter number:
"""
prompt = """
1. Add
2. Del
3. Lis
4. Quit

Enter number: """

number = 0;	# 초기화하지 않고 사용하면 에러가 남

while number != 4:
	print(prompt)
	number = int(input()) # input() : 사용자의 입력을 받음
print()
"""

	while문 빠져 나가기(break)

예) break의 사용

>>> coffee = 10
>>> money = 300
>>> while money:
...     print("돈을 받았으니 커피를 줍니다.")
...     coffee = coffee -1
...     print("남은 커피의 양은 %d 입니다." % coffee)
...     if not coffee:
...         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
...         break
...

# coffee.py
"""
coffee = 10
while 1:
	money = int(input("돈을 넣어 주세요: "))
	if money == 300:
		print("커피를 줍니다.")
		coffee = coffee -1
	elif money > 300:
		print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
		coffee = coffee -1
	else:
		print("돈을 다시 돌려주고 커피를 주지 않습니다.")
		print("남은 커피의 양은 %d개 입니다." % coffee)
	if not coffee: # not
		print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
		break
"""

	while문 조건문으로 돌아가기(continue)

예) continue의 사용

>>> a = 0
>>> while a < 10:
...     a = a+1
...     if a % 2 == 0: continue
...     print(a)
...
1
3
5
7
9
"""
a = 0
while a<10:
	a = a + 1
	if a%2 == 0: continue
	print(a)