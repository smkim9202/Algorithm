# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:10:44 2021

@author: SMKIM

Do it 점투파 : 06장 - 파이썬 프로그래밍
"""
# 06-1.구구단 프로그램
def GuGu():
    dan = int(input("몇 단을 출력할까요? "))
    for i in range(1,10):
        print(dan,"x",i,"=",dan * i)   
GuGu()

# 06-2. 1000미만의 자연수 중 3의배수와 5의 배수 합하기

hap = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        hap += i  
print(hap)

# 06-3. 게시판 페이징처리하기
def getTotalPage(t,n): # t : 총게시물건수, # n : 한페이지에서 보여줄 건수
    if t==0:
        return "게시물이 없습니다."
    if t % n == 0:
        return t //n
    else:   
        return t // n + 1

# 06-4. 간단한 메모장 만들기
f = open("memo.py",'w',encoding=('UTF-8'))
data = """
# C:/webtest/6.python/doit/memo.py
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt','a')
    f.write(memo+'\\n')
    f.close()
    
elif option == '-v':
    f = open('memo.txt','r')
    memo = f.read()
    f.close()
    print(memo)
else:
    print("실행 옵션은 : '-a'(추가해서 쓰기) '-v'(읽기)만 가능합니다.")
"""
f.write(data)
f.close()

# 06-5. 메모장d안에 있는 tap을 공백 space4개로 바꿔주기
f = open("tepto4.py",'w',encoding=('UTF-8'))
data = """
# C:/webtest/6.python/doit/tebto4.py
import sys

src=sys.argv[1]
dst=sys.argv[2]

f1=open(src)
tab_content=f1.read()
f1.close()

space_content=tab_content.replace("\\t"," "*4)
f2=open(dst,'w')
f2.write(space_content)
f2.close()
"""
f.write(data)
f.close()

# 06-6. 하위 디렉터리에서 파이썬파일만 출력하기
import os

def searchPy(dirname):
    try:
        for path, direct, files in os.walk(dirname):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.py':
                    print(path, filename)
    except PermissionError:
        pass
            
searchPy("C:\\webtest\\6.python\\doit")

