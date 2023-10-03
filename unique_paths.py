'''

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down


'''

# m = 3
# n = 7

m = 3
n = 2

CONST={
    
}

FACT_CONST={
    
}

def factorial(x : int)->int:
    if x==1:
        return 1
    if x in FACT_CONST:
        return FACT_CONST[x]
    return x*factorial(x-1)

def uniquePaths(m: int, n: int) -> int:
    '''
    1. Recursion + memoization O(m*n) -time, O(m*n) -space
    
    '''
    # if (m,n)==(1,1):
    #     return 1
    # if m<1 or n<1:
    #     return 0
    # if (m,n) in CONST:
    #     return CONST[(m,n)]
    # CONST[(m,n)]=uniquePaths(m-1,n)+uniquePaths(m,n-1)
    # return CONST[(m,n)]

    '''
    2. As a pure maths problem
    
    '''
    return factorial(m+n-2)//factorial(m-1)*factorial(n-1)
    
if __name__ == '__main__':
    print(uniquePaths(m,n))