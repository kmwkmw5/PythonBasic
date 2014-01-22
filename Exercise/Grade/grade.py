# -*- coding:utf-8 -*-
class ScoresParamsError(Exception):
	def __init__(self, scoreNum, subjectNum):
		self.message = '''
%d개의 과목 점수를 입력하였습니다.
입력해야할 과목 수는 %d개 입니다.
''' % (scoreNum, subjectNum)
	def __str__(self):
		return repr(self.message)

class InvalidScoreError(Exception):
	def __init__(self, score):
		self.message = '''
점수 %d를 입력하였습니다.
점수는 0~100 사이의 값으로 입력해야 합니다.
''' % score
	def __str__(self):
		return repr(self.message)

class Score:
	def __init__(self, *scores):
		# scores가 만약 한 개의 리스트의 형태로 입력되었다면
		if isinstance(scores[0], list):
			scores = scores[0]
		# 각 점수를 0으로 초기화
		self.subject = { 'korean': 0, 'english': 0, 'math': 0 }
		self.subjectNum = len(self.subject)
		# 과목 수에 맞지 않는 인수 개수를 입력받았을 때 예외 처리
		try:
			scoresNum = len(scores)
			if scoresNum != self.subjectNum:
				raise ScoresParamsError(scoresNum, self.subjectNum)
		except ScoresParamsError as e:
			print(e.message)
			exit()
		# 0~100 점 이외의 값을 입력했을 때 예외 처리
		try:
			for score in scores:
				if score < 0 or score > 100: raise InvalidScoreError(score)
		except InvalidScoreError as e:
			print(e.message)
			exit()
		# scores를 subject에 입력
		self.subject['korean'] = scores[0]
		self.subject['english'] = scores[1]
		self.subject['math'] = scores[2]
	
	def getKorean(self):
		return self.subject['korean']
	def getEnglish(self):
		return self.subject['english']
	def getMath(self):
		return self.subject['math']
	
	def getSum(self):
		sumOfSubject = 0
		for score in self.subject.values():
			sumOfSubject += score
		return sumOfSubject
	def getAverage(self):
		return self.getSum() / self.subjectNum
	def getGrade(self):
		avg = self.getAverage()
		if avg >= 80:
			return 'A'
		elif avg >= 60:
			return 'B'
		elif avg >= 40:
			return 'C'
		elif avg >= 20:
			return 'D'
		else:
			return 'F'
		
class Student:
	def __init__(self, id, name, score):
		self.id = id
		self.name = name
		self.setScore(score)
	def getId(self):
		return self.id
	def getName(self):
		return self.name
	def getScore(self):
		return self.score
	def setScore(self, score):
		if not isinstance(score, Score):
			print('점수 정보를 잘못 입력하였습니다.')
			exit()
		self.score = score
		
class Class:
	def __init__(self):
		self.students = {}
	def addStudent(self, *students):
		for student in students:
			if not isinstance(student, Student):
				print('학생 정보를 잘못 입력하였습니다.')
				exit()
			self.students[student.getId()] = student
	def getStudent(self, id):
		try:
			return self.students[id]
		except KeyError as e:
			print("%s번 학생은 존재하지 않습니다." % e)
			exit()
	def printAllStudentsGrade(self):
		for student in self.students.values():
			print('%3d번 학생 %s은 총점 %3d점, 평균 %3d점으로 %s등급입니다.'
				% (student.getId(), student.getName(), student.getScore().getSum(),
				student.getScore().getAverage(), student.getScore().getGrade()))
		
if __name__ == '__main__':
	# pyClass 학급 생성
	pyClass = Class()
	
	# py_student 파일로부터 학생 정보를 읽어옴
	try:
		fPyClass = open('py_student', 'r')
	except IOError:
		print('학생 정보를 py_student 입력해 주세요.')
		exit()
		
	# 학생 정보를 읽어 pyClass 학급에 등록
	try:
		lines = fPyClass.readlines()
		for line in lines:
			line = line.replace('\n', '')
			info = line.split(',')
			# 임시 student 딕셔너리 생성
			dic_student = {}
			(dic_student['id'], dic_student['name']) = int(info.pop(0)), info.pop(0)
			#dic_student['score'] = [int(score) for score in info]
			#dic_student['score'] = list(map(int, info))
			dic_student['score'] = list(map(lambda s: int(s), info))
			# 학생 추가
			student = Student(dic_student['id'], dic_student['name'], Score(dic_student['score']))
			pyClass.addStudent(student)
	except ValueError:
		print('입력 방법: 번호(int),이름(string),성적1(int),성적2(int),성적3(int)')
		exit()
	finally:
		fPyClass.close()
	'''
	pyClass.addStudent(
		Student(1, '학생일', Score(55, 66, 80)),
		Student(2, '학생이', Score(10, 5, 6)),
		Student(3, '학생삼', Score(80, 88, 100)),
		Student(4, '학생사', Score(100, 45, 88)),
		Student(5, '학생오', Score(42, 55, 33)),
		Student(6, '학생육', Score(11, 22, 33)),
		Student(7, '학생칠', Score(12, 84, 35)),
		Student(8, '학생팔', Score(45, 44, 33)),
		Student(9, '학생구', Score(70, 60, 55)),
		Student(10, '학생십', Score(66, 75, 43)))
	'''
	#print(pyClass.getStudent(10).getScore().getGrade())
	# pyClass 학급의 모든 학생 점수 정보 출력
	pyClass.printAllStudentsGrade()