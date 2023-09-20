'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_LL(val_list : list)->'ListNode':
    HEAD=None
    tail=None
    i=0
    while i<len(val_list):
        try:
            tail.next=ListNode(val_list[i])
            tail=tail.next
            i+=1
        except AttributeError:
            HEAD=ListNode(val_list[i])
            tail=HEAD
            i+=1
    head=HEAD
    reconstructed_list=[]
    while head!=None:
        reconstructed_list.append(head.val)
        head=head.next
    try:    
        assert val_list.__eq__(reconstructed_list)
    except AssertionError:
        print("Some issue")
    return HEAD    

def mergeTwoSortedLists(list1 : list, list2 : list)->list:
    final=[]
    i,j=0,0
    f_1=lambda x,y: (x,0) if x<y else (y,1)
    f_2=lambda i,j,list1,list2: (i,list1) if j==len(list2) else (j,list2)
    while i< len(list1) and j<len(list2):
        min_val,index=f_1(list1[i],list2[j])
        final.append(min_val)
        if index==0:
            i+=1
        else:
            j+=1
    if i==len(list1) and j==len(list2):
        return final
    i,list1=f_2(i,j,list1,list2)
    while i<len(list1):
        final.append(list1[i])
        i+=1
    return final
    
        
    
    
    
    
    
    return

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    
    1. Naive way:
    
    '''
    # HEAD=None
    # tail=None
    # head_1=list1
    # head_2=list2
    # argmin=lambda x,y: (x,0) if x.val<y.val else (y,1)
    # f=lambda head_1,head_2: head_2 if head_1 is None  else head_1
    # while head_1!=None and head_2!=None:
    #     min_node,i=argmin(head_1,head_2)
    #     try:
    #         tail.next=min_node
    #         tail=min_node
    #     except AttributeError:
    #         tail=min_node
    #         HEAD=min_node
    #     if i==0:
    #         head_1=head_1.next
    #     else:
    #         head_2=head_2.next
    # if head_1==None and head_2==None:
    #     return HEAD
    # f=lambda head_1,head_2: head_2 if head_1 is None  else head_1
    # head_1=f(head_1,head_2)
    # try:
    #     tail.next=head_1
    # except AttributeError:
    #     tail=HEAD=head_1

    # return HEAD
    
    # '''
    # 2. Beautiful piece of code - Play Shot like Rohit Sharma
    # '''
    
    HEAD=tail=ListNode()
    while list1 and list2:
        if list1.val>list2.val:
            tail.next = list2
            list2,tail=list2.next,tail.next
        else:
            tail.next=list1
            list1,tail=list1.next,tail.next
    if list1 or list2:
        tail.next= list1 if list1 else list2

    return HEAD.next
  
    
list1 = [1,2,4]
list2 = [1,3,4] 
# list1 = []
# list2 = [] 
# list1 = []
# list2 = [0]     
        
list_1,list_2=get_LL(list1),get_LL(list2)


if __name__ == '__main__':
    head_1=mergeTwoLists(list_1,list_2)
    list_LL=[]
    while head_1!=None:
        list_LL.append(head_1.val)
        head_1=head_1.next
    list_list=mergeTwoSortedLists(list1,list2)
    try:
        assert list_list.__eq__(list_LL)
    except AssertionError:
        print("Some issues")