# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

nums1 = [0]
m = 0
nums2 = [1]
n = 1

def seperate(nums1 :list[int],nums2 :list[int],m :int=0)->tuple :
    j=0
    min_len=min(m,len(nums2))
    while j< min_len and nums1[m-1-j]>nums2[j]:
        nums2[j], nums1[m-1-j]=nums1[m-1-j],nums2[j]
        j+=1
    return nums1, nums2

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    nums1,num2=seperate(nums1, nums2,m)
    nums1[:m]=sorted(nums1[:m])
    nums1[m:]=sorted(num2)
    print(nums1)
    return 


def merge_with_rslt(nums1 : list[int], nums2 : list[int])->list[int]:
    rslt=[0]*(len(nums1)+len(nums2))
    (nums1,nums2)=(nums1,nums2) if nums1[-1]>nums2[-1] else (nums2,nums1)
    i,j=0,0
    while j<len(nums1):
        if i<len(nums2) and nums1[j]>nums2[i]:
            rslt[i+j]=nums2[i]
            i+=1
        else:
            rslt[i+j]=nums1[j]
            j+=1
    return rslt
            



if __name__ == '__main__':
    nums1=[1,3,5,7]
    nums2=[2,4,6]
    nums2=[1,2,3,4]
    nums1=[6,7,8]
    print(merge_with_rslt(nums1,nums2))
    