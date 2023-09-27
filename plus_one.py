'''

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


'''


# digits = [1,2,3]
# digits = [4,3,2,1]
digits = [9]


def plusOne(digits: list[int]) -> list[int]:
    
    '''
    1 . Iterative
    '''
    i=len(digits)-1
    carry=1
    while i>-1:
        if digits[i]==9:
            if carry:
                digits[i]=0
                i-=1
                carry=1
        else:
            digits[i]+=1
            return digits
    
    if carry:
        digits.insert(0,1)
    # return digits
    
    

if __name__ == '__main__':
    # print(str())
    # print(int(str(digits)))
    print(list(range(len(digits)-1,-1,-1)))