#chap08_dict 260p
#1
import re # regular expression
s = 'Python is a programming language that lets you work more quickly and integrate your systems more effectively. You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.'
s2 = re.sub('[^a-zA-Z]', ' ', s)
print(s2)
ws = s2.split()

# 방법1 if문을 이용한 방법
count = {}
for w in ws:
	if w in count:
		count[w] += 1
	else:
		count[w] = 1
print(count)

# 방법2 get() 메소드를 이용
count = {}
for w in ws:
	count[w] = count.get(w, 0) + 1
	#count[w] = count.setdefault(w, 0) + 1
print(count)

# 방법3 collection 모듈의 Counter 클래스 이용
from collections import Counter
c = Counter(ws)
print(c) # Counter는 dict의 하위 클래스
print(c['and'])
print(c.most_common(3))