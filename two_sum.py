'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
from collections import defaultdict

nums = [2,7,9,0,15]
target = 9
# nums = [3,3]
# target = 6
nums = [2,3,4]
target = 6
# nums = [3,3]
# target = 6

def two_sum(nums : list,target : int)->tuple:
    
    
    '''
    1. Naive approach 
    
    '''
    
    
    
    '''
    2. De-coupled approach 
    '''
    
    # nums_bar=defaultdict(list)
    # for i in range(len(nums)):
    #     nums_bar[nums[i]].append(i)
    
    
    # for i in range(len(nums)):
    #     if target-nums[i] in nums_bar:
    #         if target-nums[i]==nums[i]:
    #             if len(nums_bar[nums[i]])>1:
    #                 return nums_bar[nums[i]][:2]
    #             else:
    #                 pass
    #         elif target-nums[i]!=nums[i]:
    #             return [nums_bar[nums[i]][0],nums_bar[target-nums[i]][0]]
    #         else:
    #             assert False
    
    
    '''
    3. Online version of the above-approach
    '''
    
    # nums_bar ={}
    # for i in range(len(nums)):
    #     if target-nums[i] in nums_bar:
    #         return [nums_bar[target-nums[i]],i]
    #     else:
    #         nums_bar[nums[i]]=i
    
    
    '''
    
    Assumes nums is sorted :
    
    '''
    
    left=0
    right=len(nums)-1
    
    while left<right:
        if nums[left]+nums[right]<target:
            left+=1
        elif nums[left]+nums[right]>target:
            right-=1
        elif nums[left]+nums[right]==target:
            return [left,right]
        else:
            assert False
    return [None,None]
    
                
            
    


if __name__ == '__main__':
    print(two_sum(sorted(nums),target))

