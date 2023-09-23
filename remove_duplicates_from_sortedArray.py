'''
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''


import sys
import copy

# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4,4]

def removeDuplicates(nums: list[int]) -> int:
    
    '''
    1. Naive approach -O(n^2)
    
    '''
    
    prev=None
    i=0
    while i<len(nums):
        if prev==nums[i]:
            nums.pop(i)
        else:
            prev=nums[i]
            i+=1
    return len(nums)

def better_approach(nums):
    '''
    1. A Better approach- O(n*log(n))
    
    '''
    prev=None
    i=0
    k=0
    while i<len(nums):
        if prev==nums[i]:
            nums[i] ="d"
        else:
            prev=nums[i]
            k+=1
        i+=1
    nums=[x for x in nums if x!="d"]
    return k

def Linear_time(nums):
    prev=None
    i,j=0,0
    while j<len(nums):
        if prev==nums[j]:
            prev=nums[j]
        else:
            prev=nums[j]
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return i
            
    




if __name__=='__main__':
    a=10
    b=12
    print(a,b)
    a=a+b
    b=a-b
    a=a-b
    print(a,b)