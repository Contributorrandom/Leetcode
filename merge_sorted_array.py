'''
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1


'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


def get_pos(nums1 :list[int],target :int) ->int:
    left,right=0,len(nums1)
    
    def condition(k : int) -> bool:
        nonlocal nums1,target
        try:
            return nums1[k]>target
        except IndexError:
            return True
    
    while left < right:
        mid=left+(right-left)//2
        if condition(mid):
            right = mid
        else:
            left=mid+1
    return left

def seperate(nums1 :list[int],nums2 :list[int],m :int=0)->tuple :
    j=0
    min_len=min(m,len(nums2))
    while j< min_len and nums1[m-1-j]>nums2[j]:
        nums2[j], nums1[m-1-j]=nums1[m-1-j],nums2[j]
        j+=1
    return nums1, nums2


    

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    
    '''
    1. Naive approach
    '''
    
    # i=0
    # while i<n:
    #     target_pos=get_pos(nums1[:m],nums2[i])
    #     j=m
    #     while j>target_pos:
    #         nums1[j]=nums1[j-1]
    #         j-=1
    #     nums1[target_pos]=nums2[i]
    #     m+=1
    #     i+=1
    '''
    2. Using builtin function
    
    ''' 
    # nums1,num2=seperate(nums1, nums2,m)
    # nums1[:m]=sorted(nums1[:m])
    # nums1[m:]=sorted(num2)
    # print(nums1)
    # return  

    '''
    3. Elegant method - effortless shot
    
    
    '''
    
    i,j,last_index=m-1,n-1,m+n-1
    while j>-1:
        if i>-1 and nums1[i]>=nums2[j]:
            nums1[last_index]=nums1[i]
            i-=1
        else:
            nums1[last_index]=nums2[j]
            j-=1
        last_index-=1
    return nums1
        

if __name__ == '__main__':
    print(merge(nums1,m,nums2,n))
    
    
        