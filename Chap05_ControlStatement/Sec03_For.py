"""
3) for문

for 변수 in 리스트(또는 터플, 문자열):
    <수행할 문장1>
    <수행할 문장2>
    ...

# marks1.py
"""
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: # mark 자체가 element
	number = number +1 
	if mark >= 60: # mark
		print("%d번 학생은 합격입니다." % number)
	else: 
		print("%d번 학생은 불합격입니다." % number)
print()
"""

	for와 continue

# marks2.py 
"""
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
	number = number +1 
	if mark < 60: continue 
	print("%d번 학생 축하합니다. 합격입니다. " % number)
print()
"""

		for와 range함수
	
	for문은 range라는 숫자 리스트를 자동으로 만들어 주는 함수와 함께 사용되는 경우가 많다.
	다음은 range함수의 간단한 사용법이다.
	
	>>> a = range(10) 
	>>> a 
	range(0, 10)
	위에서 보는 것과 같이 range(10)은 0부터 9까지의 숫자 range객체를 만들어 준다.
""""""
	시작 번호와 끝 번호를 지정하려면 다음과 같이 해야 한다.
	끝 번호는 포함되지 않는다.
	
	>>> a = range(1, 11) 
	>>> a 
	range(1, 11)
"""
a = range(10)		# 0~9
print(a)
b = range(1, 11)	# 1~10
print(b)
"""
	위처럼 시작 숫자를 정해 줄 수도 있다.
	
	for와 range를 이용하면 1부터 10까지 더하는 것을 다음과 같이 쉽게 구현할 수 있다.
	
	예 ) 1부터 10까지의 합
	
	>>> sum = 0 
	>>> for i in range(1, 11): 
	. . .     sum = sum + i 
	. . . 
	>>> print(sum)
	55
	range(1, 11)은 숫자 1부터 11까지의 숫자를 데이터로 갖는 자료형이다.
	따라서 위의 예에서 i변수에 리스트의 숫자들이 하나씩 차례로 대입되면서
	sum = sum + i라는 문장을 수행하게 되어 sum은 최종적으로 55가 되게 된다.
"""
sum = 0
for i in range(1, 11):	# 1~10까지의 합
	sum = sum + i
print(sum)
print()
"""
또한 우리가 앞서 살펴 보았던 60점 이상이면 합격인 예제도 range함수를 이용해서 적용시킬 수도 있다. 다음을 보자.

#marks3.py
"""
marks = [90, 25, 67, 45, 80]

for number in range(len(marks)): # 0~marks의 길이(5) : 0~4
	if marks[number] < 60: continue 
	print("%d번 학생 축하합니다. 합격입니다." % (number+1))
print()
# len()이라는 함수가 처음 나왔는데 len함수는 리스트의 요소 개수를 돌려주는 함수이다.
"""

		다양한 for문의 사용

	>>> a = [(1,2), (3,4), (5,6)] 
	>>> for (first, last) in a: 
	. . .     print(first + last)
	. . . 
	3 
	7 
	11
"""
a = [(1,2), (3,4), (5,6)]
for (x, y) in a: # [x, y] 무관
	print(x + y)

b = [[1,2], [3,4], [5,6]]
for [x, y] in b: # (x, y) 무관
	print(x + y)

print()
"""

	for와 range를 이용한 구구단

for와 range함수를 이용하면 단 4줄만으로 구구단을 출력해 볼 수가 있다.

>>> for i in range(2,10): 
...     for j in range(1, 10): 
...         print(i*j, end=" ") 
...     print('') 
... 
2 4 6 8 10 12 14 16 18 
3 6 9 12 15 18 21 24 27 
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54 
7 14 21 28 35 42 49 56 63 
8 16 24 32 40 48 56 64 72 
9 18 27 36 45 54 63 72 81
"""
for i in range(1,10):
	for j in range(2,10):
		print("%d * %d = %d" % (j, i, i*j), end="\t")    # print("", end="")
	print()
"""
위에서 print(i*j, end=" "), 처럼 end 파라미터를 넣어준 이유는
해당 결과값을 출력할 때 다음 줄로 넘어가지 않고 그 줄에 계속해서 출력하기 위한 것이다.
"""