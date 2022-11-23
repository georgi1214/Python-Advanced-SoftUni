from collections import deque
import math


expression=deque([])

strExp=input()
strExp=strExp.split(" ")
for k in range(0,len(strExp)):
    expression.append(strExp[k])


currExp=deque([])
while True:
    operation=""
    element=expression.popleft()
    if element == "*" or element == "+" or element == "-" or element == "/":
        operation = element
    else:
        currExp.append(element)
    if operation!="":
        sum="0"; initNumberReceived=False
        while len(currExp)!=0:
            if sum=="0" and initNumberReceived==False:
                sum=currExp.popleft()
                initNumberReceived=True
            else:
                sum=eval(sum+operation+currExp.popleft())
                sum=str(math.floor(float(sum)))
        expression.appendleft(str(sum))
        if len(expression)==1:
            break
res=expression.pop(); res=math.floor(float(res))
print(res)