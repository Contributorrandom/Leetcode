'''
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1


'''

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1

# bloomDay = [7,7,7,7,12,7,7]
# m = 2
# k = 3

bloomDay = [1,10,3,10,2]
m = 3
k = 2

def condition(day : int,bloomDay : list[int], m : int, k :int) -> bool :
    i,count,pre_count=0,0,0
    while i<len(bloomDay):
        pre_count=pre_count+1 if bloomDay[i]<=day else 0
        if pre_count==k:
            count,pre_count=count+1,0
            if count==m: return True
        i+=1
    return False

def minDays(bloomDay: list[int], m: int, k: int) -> int:
    if m*k>len(bloomDay): return -1
    left,right=min(bloomDay),max(bloomDay)
    while left<right:
        mid=left+(right-left)//2
        if condition(mid,bloomDay,m,k):
            right=mid
        else:
            left=mid+1
    return left

if __name__ == '__main__':
    # print(condition(3,bloomDay,m,k))
    print(minDays(bloomDay,m,k))
    