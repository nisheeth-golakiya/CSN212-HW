import numpy as np
import time

def quickhull(A,N):
    A.sort()
    Top=[[]]
    Bot=[[]]
    Xmax=A[N-1]
    Xmin=A[0]
    M=slope(Xmin,Xmax)
    if M==False:
        return
    for i in range(1,N-1):
        if A[i]==A[i+1]:
            A.remove(A[i])
        if M<slope(Xmin,A[i]):
            Top.append(A[i])
        elif slope(Xmin,A[i])==False:
            if A[i][1]>Xmin[1]:
                Top.append(A[i])
            else:
                Bot.append(A[i])
        elif M>slope(Xmin,A[i]):
            Bot.append(A[i])
    Top.remove(Top[0])
    Bot.remove(Bot[0])
    print(Xmin)
    findhull_T(Top,Xmin,Xmax)
    findhull_B(Bot,Xmin,Xmax)
    print(Xmax)
    
# For top half    
def findhull_T(A,v1,v2):
    if len(A)==1:
        print(A[0])
        return A[0]
    if len(A)==0:
        return
    C=Ymax(A)
    M1=slope(v2,C)
    M2=slope(v1,C)
    L=[[]]
    R=[[]]
    for i in range(len(A)):
        if A[i][0]*M1<A[i][1]:
            if A[i][0]<C[0]:
                R.append(A[i])
        if A[i][0]*M2<A[i][1]:
            if A[i][0]<C[0]:
                L.append(A[i])
    L.remove(L[0])
    R.remove(R[0])
    findhull_T(L,v1,C)
    findhull_T(R,v2,C)
    print(C)
    return C
    
# For bottom half    
def findhull_B(A,v1,v2):
    if len(A)==1:
        print(A[0])
        return A[0]
    if len(A)==0:
        return
    C=Ymin(A)
    M1=slope(v2,C)
    M2=slope(v1,C)
    L=[[]]
    R=[[]]
    for i in range(len(A)):
        if A[i][0]*M1>A[i][1]:
            if A[i][0]>C[0]:
                R.append(A[i])
        if A[i][0]*M2>A[i][1]:
            if A[i][0]<C[0]:
                L.append(A[i])
    L.remove(L[0])
    R.remove(R[0])
    findhull_B(L,v1,C)
    findhull_B(R,v2,C)
    print(C)
    return C

def slope(a,b):
    if b[0]==a[0]:
        return False
    return float(b[1]-a[1]/b[0]-a[0])
    
def Ymax(A):
    C=A[0]
    for i in range(len(A)):
        if C[1]<A[i][1]:
            C=A[i]
    return C
    
def Ymin(A):
    C=A[0]
    for i in range(len(A)):
        if C[1]>A[i][1]:
            C=A[i]
    return C

if __name__=="__main__":
    A=[[np.random.randint(0,300),np.random.randint(0,300)] for i in range(20)]
    start = time.clock()
    c = quickhull(A,5)
    end = time.clock()
    print "Time consumed:",end - start
