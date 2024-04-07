import numpy as np

def main():
    A = np.array([8,2,5,3])
    for i in range(1,len(A), 1):
        j=i
        print(j, end=" ")
        while (j>0) and (A[j]<A[j-1]):
            
            np.swap(A[j],A[j-1])
        print(A)
main()