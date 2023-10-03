
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def supplement(p :Optional['TreeNode'],q : Optional['TreeNode']) ->bool:
        if isinstance(p,type(q)) is False:
            return False
        if p and q:
            if p.val==q.val:
                return Solution.supplement(p.left,q.right) and Solution.supplement(p.right,q.left)
            else:
                return False
        if p==None and q==None:
            return True
    @staticmethod
    def left_order( node : Optional[TreeNode])->list:
        if node:
            return Solution.left_order(node.left)+[node.val]+Solution.left_order(node.right) if any([x!=None for x in [node.left,node.right]]) else [node.val]
        return [None] 
    @staticmethod
    def right_order( node : Optional[TreeNode])->list:
        if node:
            return Solution.right_order(node.right)+[node.val]+Solution.right_order(node.left) if any([x!=None for x in [node.left,node.right]]) else [node.val]
        return [None]
    
     
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.right_order(root.right)==Solution.left_order(root.left) if root else True
    
            
if __name__ == '__main__':
    A,B,C,D,E,F,G=TreeNode(1),TreeNode(2),TreeNode(2),TreeNode(2),None,TreeNode(2),None
    A.left,A.right,B.left,B.right,C.left,C.right=B,C,D,E,F,G
    S=Solution()
    print(S.left_order(A.left))
    print(S.right_order(A.right))
    # print(S.isSymmetric(A))
         