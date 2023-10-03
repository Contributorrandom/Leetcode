'''
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''



    

n = 2 
n = 3

    
    
    
    
CONST={
    -1:0,
    0:1
}

def climbStairs( n: int) -> int:
    if n in CONST: 
        return CONST[n]
    CONST[n]=climbStairs(n-1)+climbStairs(n-2)
    return CONST[n]

if __name__ == '__main__':
    print(climbStairs(5))