# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:47:27 2021

@author: SMKIM

Do it 점투파 : 04장 프로그램의 입출력 - 나혼자코딩, 연습문제
"""
###연습문제###
# Q1. 입력한 자연수 홀수인지 판별해주는 함수(is_odd) 작성
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수 작성
def avg_numbers(* args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

# Q3. 두개의 숫자 입력받고, 더해서 돌려주는 프로그램 
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

total = num1 + num2
print("두 수의 합은 %d 입니다." %total)

# Q4. 출력 결과가 다른 것 고르기
print("you""need""python") #youneedpython
print("you"+"need"+"python") #youneedpython
print("you","need","python") #you need python
print("".join(["you","need","python"])) #youneedpython

# Q5. "Life is too short"문자열 "test.txt" 파일로 출력 후 다시 그 파일 읽기
f1 = open("test.txt",'w')
f1.write("Life is too short\n")
f1.close()

f2= open("test.txt",'r')
print(f2.read())
f2.close()

# Q6. 기존에 있는 test.txt파일에 사용자가 추가로 입력한 값을 써서 출력하는 프로그램 
user_input = input("저장할 내용을 입력하세요 : ")
f = open("test.txt",'a')
f.write(user_input)
f.write("\n")
f.close()

# Q7. test.txt 파일에서 java라는 문자열 python으로 바꿔서 저장하기
f = open('test.txt','r')
body = f.read()
f.close()

body = body.replace("java", "python")

f = open('test.txt','w')
f.write(body)
f.close()

