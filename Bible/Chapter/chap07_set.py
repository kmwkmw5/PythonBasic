#===============================================================================
# 제 7 장 집합
#===============================================================================

#===============================================================================
# 7.1 set 객체의 생성
#===============================================================================

a = set()	# {}로 하면 딕셔너리가 되버림
b = {1, 2, 3}
print(a)
#set()	# 공집합인 경우
print(b)
#{1, 2, 3}
print(type(a))
#<class 'set'>
print(type(a) == type(b))
#True
b = a.copy()

# 반복 가능한 객체로부터의 생성
print(set((1,2,3)))
#{1, 2, 3}
print(set('abcd'))
#{'d', 'b', 'c', 'a'}			# 순서 무작위? 계속바뀜
print(set([1,2,3]))
#{1, 2, 3}
print(set((1,2,3,1,2,3,1,2,3)))	# 중복 없음
#{1, 2, 3}
print(set({'one':1, 'two':2}))	# 키를 반환
#{'one', 'two'}

# QUIZ
quiz = "Python is a programming language that lets you work more quickly and integrate our systems"
quiz_set = set(quiz)
quiz_set.discard(' ')
quiz_sorted = sorted(quiz_set, key = str.lower)
for alpha in quiz_sorted:
	print(alpha, end='')
print('')

#===============================================================================
# 7.2 set 객체의 연산
#===============================================================================

# 원소 추가
a = {1, 2, 3}
a.add(4)
a.update([4,5,6])	# 합집합
print(a)
#{1, 2, 3, 4, 5, 6}
a.update({4,5,6}, {7,8,9})
print(a)
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
b = a.copy()

# 원소 제거
a.clear()			# 전체 원소를 제거
print(a)
#set()
a = {1,2,3,4,5,6,7,8,9}
a.discard(3)
a.discard(3)		# 없으면 그냥 통과
print(a)
#{1, 2, 4, 5, 6, 7, 8, 9}
a.remove(4)
#a.remove(4)		# 없으면 예외가 발생(KeyError: 4)
print(a)
#{1, 2, 5, 6, 7, 8, 9}
print(a.pop())
#1
print(a.pop())
#2
print(a)
#{5, 6, 7, 8, 9}

# 집합 연산
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
C = {4, 10}

print(A.union(B))			# 합집합 A|B
#{1,2,3,4,5,6,7,8,9}
print(A.intersection(B))	# 교집합 A&B
#{4,5,6}
print(A.intersection(B, C))
#{4}
print(A.difference(B))		# 차집합 A-B
#{1,2,3}
print(A.symmetric_difference(B)) # 대칭차집합 A^B
#{1,2,3,7,8,9}
# 연산 결과가 첫 인수의 집합에 반영되기를 바란다면 뒤에 update를 붙인다.
# update(), intersection_update(), difference_update(), symmetric_difference_update()
# |=, &=, -=, ^=

# 포함 관계
A = {1,2,3,7,8,9}
print(2 in A)
#True
print(2 not in A)
#False
A = {1,2,3,4,5}
B = {1,2,3}
print(A.issuperset(B))	# A⊃B
#True
print(B.issubset(A))	# B⊂A
#True
print(A.isdisjoint(B))	# 교집합이 공집합인가?
#False

# 순서가 없는 자료형이므로 인덱싱, 슬라이싱, 정렬 불가능
# 하지만 for 문 접근 가능
for element in A:
	print(element, end=' ')
print('')
#1 2 3 4 5

#===============================================================================
# 7.3 frozenset 객체의 생성과 연산
#===============================================================================

print(frozenset([1,2,3,4,5]))

#===============================================================================
# 7.4 집합 내장(List Comprehension)
#===============================================================================

print({v*v for v in [1,2,3,4]})
#{16,1,4,9}
print({v for v in 'python' if v not in 'aeiou'})
#{'p', 'y', 't', 'n', 'h'}