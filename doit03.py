# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:00:04 2021

@author: SMKIM

Do it 점투파 : 03장 제어문 - 나혼자코딩, 연습문제
"""

###if문###
# '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'
pocket=['paper','cellphone','money']
if 'card' not in pocket:
    print('걸어가라')
else:
    print("버스타라")
    
print("걸어가라" if 'card' not in pocket else "버스타라")

###while문###
# 1~10까지의 숫자중 3의 배수 빼고 출력하기
n=0
while n < 10:
    n+=1
    if n % 3 == 0: continue
    print(n)
    
###for문###
# 1~100까지 숫자 더하기
hap=0
for i in range(1,101):
    hap+=i
print(hap)

###연습문제###
# Q1. 결과값 예측하기
a="Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print("결과값은 shirt")

# Q2. 1~1000까지의 자연수 중 3의 배수의 합 while문으로 구하기
result=0
i=1
while i <= 1000:
    if i % 3 == 0: 
        result += i 
    i += 1
print(result)

# Q3. while문으로 별찍기
i = 0
while True:
     i += 1
     if i > 5: break
     print("*" * i)

# Q4. for문으로 1~100까지의 숫자 출력
for i in range(1,101):
    print(i)
    
# Q5. A학급의 중간고사 점수 리스트를 for문으로 평균점수 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total =0
for score in A:
    total += score
average = total / len(A)
print(average)

# Q6. 숫자 리스트에서 홀수에만 2를 곱하여 저장하는 코드 컴프리헨션으로 표현하기
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)























