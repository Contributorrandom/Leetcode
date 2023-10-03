'''
Input: p = [1,2,3], q = [1,2,3]
Output: true

'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        1. Recursive approach. O(# nodes)
        
        '''
        # if isinstance(p,type(q)) is False:
        #     return False
        # if p and q:
        #     return (p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # if p==None and q==None:
        #     return True
        
        '''
        2. Using stack
        
        '''
        
        CONST_STACK=[(p,q)]
        while len(CONST_STACK):
            p,q=CONST_STACK.pop()
            if isinstance(p,type(q)) is False:
                return False
            if p and q :
                if p.val==q.val:
                    CONST_STACK.append((p.left,q.left))
                    CONST_STACK.append((p.right,q.right))
                else:
                    return False
        return True
                
        

if __name__=='__main__':
    A,B,C,D,E,F=TreeNode(0),TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5)
    A.left,A.right,B.right,C.right,C.left=B,C,D,E,F
    S=Solution()
    print(S.isSameTree(A,A))