'''

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


'''
nums = [3,2,2,3]
val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums: list[int], val: int) -> int:
    '''
    1. Two pointer approach.
    
    '''
    # i,j=0,0
    # while j<len(nums):
    #     if nums[j]==val:
    #         j+=1
    #     else:
    #         nums[j],nums[i]=nums[i],nums[j]
    #         i+=1
    #         j+=1
    # return i
    
    '''
    2. Using builtin function
    
    '''
    # count=0
    # while val in nums:
    #     nums.remove(val)
    #     count+=1
    # return len(nums)

    while True:
        try:
            nums.remove(val)
        except ValueError:
            return len(nums)
    

        
    

if __name__=='__main__':
    print(removeElement(nums,val))
    