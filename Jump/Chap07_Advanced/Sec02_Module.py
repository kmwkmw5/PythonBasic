# -*- coding:utf-8 -*-
"""
2) 모듈

	모듈.함수 처럼 사용하고 싶을 때
	
import 모듈이름


	모듈의 특정 함수를 모듈이름 없이 사용하고 싶을 때
	
from 모듈이름 import 모듈함수(,로 여러 개 선언 가능)
from 모듈이름 import *

""""""

		if __name__ == "__main__": 의 의미
		
	이번에는 mod1.py 파일에 다음과 같이 추가하여 보자.
	
	# mod1.py 
	def sum(a, b): 
	    return a+b
	
	def safe_sum(a, b): 
	    if type(a) != type(b): 
	        print("더할수 있는 것이 아닙니다.")
	        return 
	    else: 
	        result = sum(a, b) 
	    return result
	
	
	print(safe_sum('a', 1))
	print(safe_sum(1, 4))
	print(sum(10, 10.4))

sum, safe_sum의 함수만 사용하고 싶은 것이었는데 import하면 위의 세 줄이 실행된다.
이를 방지하기 위해서 아래와 같이 사용

	if __name__ == "__main__": 
	    print(safe_sum('a', 1))
	    print(safe_sum(1, 4))
	    print(sum(10, 10.4))
	    

""""""

	sys.path

"""
import sys
print(sys.path)
sys.path.append('/var/www')
print(sys.path)
"""

	reload

>>> import mod2 
>>> print(mod2.PI)
3.141592
대화형 인터프리터를 아직 닫지 말고 에디터로 mod2.py의 PI 부분을 다음 처럼 수정하자.

PI = 3.14
PI를 좀더 간단한 값(3.14)으로 바꾸었다. 다음에 대화형 인터프리터 모드로 돌아가서 다음과 같이 해보자.

>>> import imp
>>> imp.reload(mod2) 
>>> print(mod2.PI)
3.14
reload를 하면 바뀐 값이 적용되지만 import는 이전의 값을 유지하고 있음을 알게 될 것이다.
하지만 위에서 mod2.py파일을 수정한 다음 대화형 인터프리터를 닫고 다시 대화형 인터프
리터를 실행한 후 import mod2를 하면 변경된 사항이 적용되는 것은 당연한 일이다.
"""
import mod2
import imp
imp.reload(mod2)