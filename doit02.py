# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:23:10 2021

@author: SMKIM

Do it 점투파 : 02장 자료형 - 나혼자코딩, 연습문제
"""
###숫자형###
print("14를 3으로 나누었을 때 몫:",14//3,", 나머지:",14%3)

###문자열###
len('!!!python!!!')
f'{"python":!^12}'
"{0:!^12}".format("python")

###리스트###
A=[1,2,5,2,1,3,4,5]
print(A[1:3],"리스트 만드는 법은 A[1:3] 이다." )

###튜플###
print((1,2,3),"이라는 튜플에 값 4를 추가하려면 (1,2,3)+(4,) 해주면 ",(1,2,3)+(4,),"이 된다.")

###딕셔너리###
dic={'name':'홍길동','birth':'1128','age':'30'}
print(dic)

###변수###
a=[1,2,3]
b=[1,2,3]
print("a is b의 결과는",a is b)

###연습문제###
# Q1. 홍길동의 평균 점수 구하기
hkd={'국어':80,'수학':75,'영어':55}
avg=sum(list(hkd.values())) / len(hkd)

# Q2. 자연수 13이 홀수인지 짝수인지 판별하기
num = 13
print('odd' if num % 2 == 1 else 'even')

# Q3. 주민번호를 출생연도와 뒷번호 나누어서 출력하기
pin="881120-1068234"
print("yyyymmdd :","19"+pin[:6])
print("num :",pin[7:])

# Q4. 주민번호 뒷번호로 성별 알아내기
pin="881120-1068234"
gender=pin[7]
print('남자' if (gender=='1' or gender=='3') else '여자')

# Q5. a:b:c:d 문자열 a#b#c#d로 바꿔서 출력하기
a="a:b:c:d"
b=a.replace(":", "#")
print(b)

# Q6. [1,3,5,4,2] 리스트 [5,4,3,2,1]로 만들기
li = [1,3,5,4,2]
li.sort()
li.reverse()
print(li)

# Q7. ['Life','is','too','short'] 리스트를 문자열로 만들기
li = ['Life','is','too','short']
s = ' '.join(li)
print(s)

# Q8. (1,2,3) 튜플에 값이 4인 요소 추가하기
tu=(1,2,3)+(4,)
print(tu)

# 09. 오류가 발생하는 경우 고르기
a=dict()

a['name']='python' # {'name':'python'}
a[('a',)]='python' # {'name':'python', ('a',):'python'}
a[[1]]='python' # 오류발생, key값으로 리스트는 올 수 없다. 변하는 값을 사용 할 수 없다.
a[250]='python' # {'name':'python', ('a',):'python', 250:'python'}
print(a)

# 10. 딕셔너리 a에서 'B'에 해당하는 값 추출하기
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11. a 리스트에서 중복 숫자 제거해 보기
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

# 12. a=b=[1,2,3]으로 변수 선언 후 a 요소 값을 변경하면 b까지 바뀌는 이유는?
a = b = [1,2,3]
a[1]=4
print(b)

id(a) == id(b) # 변수가 가리키고 있는 객체의 주소 값이 동일하기 때문이다.
