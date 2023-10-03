nums=[2,3,1,2,-4,-3]

# def min_sum_sub_array(nums : list[int])->int:
#     if len(nums) == 0:
#         return 10000
#     return min(nums[-1],nums[-1]+min_sum_sub_array(nums[:-1]))


def min_sum_sub_array(nums : list[int]):
    CONST={}
    def fun(k : int )->int:
        if k in CONST:
            return CONST[k]
        if k<0:
            return 10000
        nonlocal nums
        CONST[k]=min(nums[k],nums[k]+fun(k-1))
        return CONST[k]
    
    i,maximum=0,-100000
    sum=-10000
    while i<len(nums):
        sum=max(nums[i],nums[i]+sum)
        maximum=max(maximum,sum)
        i+=1
    return maximum

    


if __name__ == '__main__':
    print(min_sum_sub_array(nums))
    # pass