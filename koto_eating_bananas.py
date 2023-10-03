'''

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

'''
from math import ceil

piles = [3,6,7,11]
h = 8

# piles = [30,11,23,4,20]
# h = 5

# piles = [30,11,23,4,20]
# h = 6

def condition(k : int,piles :list[int],h : int):
    return sum([ ceil(x/k) for x in piles])<=h




def minEatingSpeed( piles: list[int], h: int) -> int:
    left,right=1,max(piles)
    while left < right:
        mid=left+(right-left)//2
        if condition(mid,piles,h):
            right=mid
        else:
            left=mid+1
    return left

if __name__ == '__main__':
    # print(condition(23,piles,h))
    print(minEatingSpeed(piles,h))