'''
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    CONST=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        '''
        1. Recursive traversal
        
        '''
        # if root:
        #     return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        # return []
        '''
        Updating a common list 
        
        '''

        def traverse(node :'TreeNode'):
            if node:
                if node.left:
                    traverse(node.left)
                Solution.CONST.append(node.val)
                if node.right:
                    traverse(node.right)
        traverse(root)
        return Solution.CONST

if __name__ == '__main__':
    A,B,C,D,E,F=TreeNode(0),TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5)
    A.left,A.right,B.right,C.right,C.left=B,C,D,E,F
    S=Solution()
    print(S.inorderTraversal(A))
            