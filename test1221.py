# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:44:13 2021

@author: KITCOOP
test1221.py
"""
'''
1.  화면에서 한개의 문자를 입력받아  대문자인 경우는 소문자로, 소문자인 경우는 대문자로 
     숫자인 경우는 20을 더한 값을  출력하기
[예시]
한개의 문자를 입력하세요 : A
A 문자의 소문자는  a

한개의 문자를 입력하세요 : a
a 문자의 대문자는  A

한개의 문자를 입력하세요 : 1
1 + 20 = 21
'''

a = input("한개의 문자를 입력하세요 : ")
if a.isdigit():
    print("%d + 20 = %d" %(int(a),int(a)+20))
else:
    if a.isupper() :
        print("%s 문자의 소문자는 %s" %(a,a.lower()))
    else:
        print("%s 문자의 대문자는 %s" %(a,a.upper()))


'''
2 (1)+(1+2)+(1+2+3)+(1+2+3+4)... (1+2+3+...10)=220 출력하기
'''

total=0
for i in range(1,11):
    print("(",end="")
    for j in range(1,i+1):
        print(j,end="")
        if(j!=i):
            print("+",end="")
        total+=j
    print(")",end="")
    print("=" if i==10 else "+", end="") #조건연산자
print(total)


'''
3. 화면에서 자연수를 입력받아 각각의 자리수의 합을 구하기.

 [결과]
 자연수를 입력하세요 : 12345
 12345 자리수의 합: 15
'''
#1
nlist=[]
num=input("자연수를 입력하세요 : ")
for i in range(len(num)):
    nlist.append(int(num[i]))
print(num,"자리수의 합: ",sum(nlist))
    
#2
num=input("자연수를 입력하세요 : ")
nums=[int(i) for i in num]
print(num,"자리수의 합: ",sum(nums))



'''
4. aa,bb 리스트를 생성하고, 
  aa 리스트는 0부터 짝수 100개를 저장하고
  bb 리스트는 aa 배열의 역순으로 값을 저장하기.
  aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기
'''  
#1 
aa=[x*2 for x in range(100)]
bb=aa[::-1]

print(aa[0:10])
print(bb[::-1][0:10])

#2
print(aa[:10])
print(bb[99:89:-1])

   
'''
5. 다음 모레시계모양을 출력하기

모래시계의 높이를 홀수로 입력하세요 : 7
*******  별 7(7-0*2)개 공백 0개
 *****   별 5(7-1*2)개 공백 1개
  ***    별 3(7-2*2)개 공백 2개
  -------------------------------
   *     별 1(0*2+1)개 공백 3개(0,4-1)
  ***    별 3(1*2+1)개 공백 2개(4-2)
 *****   별 5(2*2+1)개 공백 1개(4-3)
*******  별 7개(3*2+1) 공백 0개(4-4)
 '''    
height = int(input("모래시계의 높이를 홀수로 입력하세요 : "))
h = height//2
for i in range(0,h):
    print(" "*i+"*"*(height-(i*2)))
for i in range(0,(h+1)):
    print(" "*((h+1)-(i+1)),end="")
    print("*"*(i*2+1))


'''
6. 피보나치 수열 출력하기
   피보나치 수열은 0,1로 시작하고
   앞의 두수를 더하여 새로운 수를 만들어 주는 수열을 의미한다.
   피보나치 수열의 갯수를 입력받아 피보나치 수열을 갯수만큼 저장한
   리스트를 생성하는 함수 fibo 함수를 작성하기

0,1,1,2,3,5,8,13,21,34,55,89....
[결과]
피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :10
fibo( 10 )=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]   
'''
  

def fibo(n=3):
    fibolist = [0,1]
    n1=0
    n2=1
    n3=n1+n2
    fibolist.append(n3)
    for i in range(3,n):
        n1 = n2
        n2 = n3
        n3 = n1+n2
        fibolist.append(n3)
    return fibolist

n = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :"))
print("fibo(",n,")=",end="")
print(fibo(n))


