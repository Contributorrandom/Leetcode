
nums=[8,8]
target=7

def min_len_sub_array(nums : list[int], target : int)-> int:
    
    '''
    
    1. Naive -O(n^2)
    
    '''
    
    # i=0
    # minimum=10000
    # while i<len(nums):
    #     sum=0
    #     j=i
    #     while j<len(nums):
    #         sum=sum + nums[j]
    #         if sum==target:
    #             minimum=min(minimum,j-i+1)
    #             break
    #         j+=1
    #     i+=1
    # return minimum
    
    '''
    
    1. Sliding window -O(n)
    
    '''
    
    i,j=0,0
    sum=0
    minimum=10000
    while j<len(nums):
        sum+=nums[j]
        while sum>=target and i<=j:
            if sum==target:
                minimum=min(minimum,j-i+1)
            sum-=nums[i]
            i+=1
        j+=1
    if minimum==10000:
        return -1
    return minimum
            
            
    
    



if __name__ == '__main__':
    print(min_len_sub_array(nums,target))
            
            
        