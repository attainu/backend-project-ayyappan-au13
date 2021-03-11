import sys
#array length
arr_length = list(map(int, input().split()))
#array1 from user input
A = list(map(int, input().split()))
#array2 from user input
B = list(map(int, input().split()))
#length of array1
M = len(A) 
#length of array2
N = len(B) 
result = sys.maxsize 
A.sort() 
B.sort() 
a = 0
b = 0
while (a < M and b < N): 
    
    if (abs(A[a] - B[b]) < result): 
        result = abs(A[a] - B[b]) 

    elif (A[a] < B[b]): 
        a = a + 1

    else: 
        b = b + 1

print(result) 
