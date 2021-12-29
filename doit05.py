# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 12:37:05 2021

@author: SMKIM

Do it 점투파 : 05장 파이썬 클래스, 모듈, 패키지, 예외처리, 내장함수, 라이브러 - 나혼자코딩, 연습문제
"""
###연습문제###
# Q1. Calculator클래스 상속받아서 minus메서드 추가하기
class Calculator:
    def __init__(self):
        self.value = 0      
    
    def add(self, val):
        self.value += val
        
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 3출력

# Q2. Calculator클래스 상속받아서 객체변수 value가 100이상 못 갖게 제한두기
class Calculator:
    def __init__(self):
        self.value = 0      
    
    def add(self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

        
cal = MaxLimitCalculator()
print(cal.value)
cal.add(20)
print(cal.value)
cal.add(85)
print(cal.value)

# Q3. 결과 예측하기
all([1,2,abs(-3)-3])
print("[1,2,0] 0이 들어있어서 결과는 False")

chr(ord('a')) == 'a'
print("'a'의 아스키코드값을 다시 문자로 변환해서 'a' 결과는 True")

# Q4. filter(), lambda를 사용하여 리스트의 음수 제거하기
list(filter(lambda x: x>0, [1,-2,3,-5,8,-3]))

# Q5. 0xea 16진수 10진수로 변경하기
int('0xea',16)

# Q6. map, lambda를 사용하여 리스트 요솟값 전부 3 곱해주기
list(map(lambda a:a*3,[1,2,3,4]))

# Q7. 리스트의 최대값, 최소값의 합구하기
a = [-8,2,7,5,-3,5,0,1]
max(a)+min(a)

# Q8. 17/3의 결과를 소숫점 4자리까지만 반올림하기
round(17/3,4)

# Q9. sys모듈로 매개변수를 주고 다 더하는 myargv.py 작성하기
f = open("myargv.py",'w',encoding='UTF-8')
data="""
#sys1.py
import sys

args=sys.argv[1:]
result=0
for i in args:
    result += int(i)
print(result)
"""
f.write(data)
f.close()

# Q10. os모듈로 디렉터리 이동, dir명령실행, 실행결과 출력하기
import os
os.chdir("C:\\webtest\\6.python\\doit") #이동
workspace=os.getcwd() #현재작업폴더 경로 저장
li_dir=os.listdir(workspace) #현재작업폴더 파일,폴더 리스트로 반환
for s in li_dir: 
    print(s)

# Q11. glob모듈로 디렉터리의 파일 중 확장자가 py인 파일만 출력하기
import glob
glob.glob("C:\\webtest\\6.python\\doit\\*.py")

# Q12. time 모듈 사용해서 현재 날짜와 시간 출력하기
import time
time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))

# Q13. random모듈사용하여 1~45까지의 자연수 중 중복되지 않은 숫자 6개 출력
import random
lotto=set()
while len(lotto) < 6:
    lotto.add(random.randint(1,45))
list(lotto)

