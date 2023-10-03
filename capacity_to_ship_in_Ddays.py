
# capacity=6
# weights=[2,2,2,2]

# weights = [1,2,3,4,5,6,7,8,9,10]
# Days = 5

# weights = [3,2,2,4,1,4]
# Days = 3

weights = [1,2,3,1,1]
Days = 4


def condition(capacity : int ,weights : list[int],Days : int):
    remain_days=Days
    i=current=0
    while i<len(weights):
        if remain_days:
            if capacity >=current+weights[i]:
                current+=weights[i]
                i+=1
            else:
                current=0
                remain_days-=1
        else:
            return False
    return True

def shipWithinDays(weights: list[int], days: int) -> int:
    left,right=min(weights),sum(weights)
    while left < right:
        mid=left+(right-left)//2
        if condition(mid,weights,days):
            right=mid
        else:
            left=mid+1
    return left

if __name__ == "__main__":
    print(shipWithinDays(weights,Days))
    