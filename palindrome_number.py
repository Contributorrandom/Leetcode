'''

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

'''

x = 121
# x = -121
# x = 10


def isPalindrome(x: int) -> bool:
    
    '''
    1. String -two parameter

    '''
    
    x_bar=list(str(x))
    # left=0
    # right=len(x_bar)-1
    # while left<right:
    #     if x_bar[left]==x_bar[right]:
    #         left+=1
    #         right-=1
    #     else:
    #         break
    # if left>=right:
    #     return True
    # return False

    '''
    2. String -one parameter

    '''
    # i=0
    # while i<=(len(x_bar)-1)//2:
    #     if x_bar[i]==x_bar[-i-1]:
    #         i+=1
    #     else:
    #         break
    # if i>(len(x_bar)-1)//2:
    #     return True
    # return False
    
    '''
    3. Integer - Approach 
    '''
    y=x
    if x<0:
        return False
    rev=0
    while x>0:
        rem=x%10
        x=x//10
        rev=10*rev+rem
    if rev==y:
        return True
    return False


    
    
    

if __name__=='__main__':
    # A=[1,3,4,5,6]
    print(isPalindrome(x=-121))
    # print(A[0],A[0-1])