# -*- coding:utf-8 -*-
"""
1) 숫자형 (Number)
숫자형이란 숫자 형태로 이루어진 자료형으로 우리가 이미 아는 것들이다. 우리가 흔히 사용해 왔던 것들을 생각해 보자.
123과 같은 정수, 12.34 같은 실수, 공대생이라면 필수적으로 알아야 할 복소수(1 + 2j) 같은 것들도 있고,
드물게 쓰이긴 하지만 8진수나 16진수 같은 것들도 있다.

이런 숫자들을 파이썬에서는 어떻게 사용하는 지 알아보자.
""""""
    항목    사용 예
    정수    123, -345, 0
    실수    123.45, -1234.5, 3.4e10
    복소수    1 + 2j, -3j
    8진수    0o34, 0o25
    16진수    0x2A, 0xFF
""""""
위의 표는 숫자들이 파이썬에서 어떻게 사용되는지를 간략하게 보여준다.

정수형(Integer)

정수형이란 말 그대로 정수를 뜻하는 숫자를 말한다. 아래의 a는 각각의 숫자를 대입한 변수이다.
다음 예는 양의 정수와 음의 정수, 숫자 0을 변수 a에 대입하는 예제이다.

>>> a = 123
>>> a = -178
>>> a = 0

소수점 포함된 것(Floating-point)

아래의 첫 번째 예와 두 번째 예는 우리가 늘 사용하는 방식이다. 그리고 세 번째와 네 번째 방법은 컴퓨터식 지수 표현법이다.
지수 표현법으로 파이썬에서는 4.24e10 또는 4.24E10처럼 표현한다. (e, E둘중 어느 것을 사용해도 무방하다.)

>>> a = 1.2
>>> a = -3.45
>>> a = 4.24E10
>>> a = 4.24e-10
위 예에서 4.24E10은 4.24 곱하기 10의 10승, 4.24e-10은 4.24 곱하기 10의 마이너스 10승을 의미한다.
""""""
    8진수(Octal)
    
    8진수를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 + 알파벳 o 또는 대문자 O)으로 시작하면 된다.
    
    >>> a = 0o177
""""""
    16진수(Hexadecimal)
    
    16진수를 만들기 위해서는 숫자가 0x로 시작하면 된다.
    
    >>> a = 0x8ff
    >>> b = 0xABC
    8진수나 16진수는 잘 사용하지 않는 형태의 숫자 자료형이다.
"""
print(0o177)
print(0O177)
print(0x8ff)
print(0X8ff)
print("")
"""
    복소수 (Complex number)

    보통 우리는 중고등학교 시절에 'j' 대신 'i'를 사용했을 것이다. 파이썬은 'i' 대신 'j'를 사용한다.
    'j'를 써도 되고 'J'를 써도 된다.
    
    >>> a = 1+2j
    >>> b = 3-4J
    복소수를 활용하는 예들을 몇가지 보도록 하자. 복소수에는 복소수가 자체적으로 가지고 있는 내장함수가 있다.
    그것들을 이용하면 좀더 다양한 방법으로 복소수를 사용할 수 있게 된다.
    
    다음의 복소수 예들을 보자.
    복소수.real은 복소수의 실수 부분을 돌려준다.
    
    >>> a = 1+2j
    >>> a.real
    1.0
    복소수.imag는 복소수의 허수 부분을 돌려준다.
    
    >>> a = 1+2j
    >>> a.imag
    2.0
    복소수.conjugate()는 복소수의 켤레 복소수를 돌려준다.
    
    >>> a = 1+2j
    >>> a.conjugate()
    (1-2j)
    abs(복소수)는 복소수의 절대값을 돌려준다. (1+2j의 절대값은 루트 1^2 + 2^2 이다.)
    
    >>> a = 1+2j
    >>> abs(a)
    2.2360679774997898
"""
a = 1 + 2j
b = 3 - 4j
print(a.real)
print(b.imag)
print(a.conjugate())
print(abs(a))
print(a+b)
print("")
"""
숫자 연산
프로그래밍을 한번도 해 본적이 없는 독자라도 사칙연산(+, -, *, /)은 알고 있을 것이다.
파이썬에서도 역시 계산기와 마찬가지로 아래의 연산자를 이용하여 사칙연산을 수행한다.

>>> a = 3
>>> b = 4
>>> a + b
7
>>> a * b
12
>>> a / b
0.75
""""""
    다음에 알아야 될 연산자로 ** 라는 연산자가 있다. 이것은 x ** y처럼 사용되었을 때 x의 y승 값을 돌려 준다.
    다음의 예를 통해 알아보자.
    
    >>> a = 3
    >>> b = 4
    >>> a ** b
    81
"""
print(3**4)
"""
프로그래밍을 접해 본 적이 없는 독자라면 %연산자는 본 적이 없을 것이다. %는 나머지 값을 반환하는 연산자이다.
7을 3으로 나누면 나머지는 1이 될 것이고 3을 7로 나누면 나머지는 3이 될 것이다. 다음의 예로 확인해 보자.

>>> 7 % 3
1
>>> 3 % 7
3
"""