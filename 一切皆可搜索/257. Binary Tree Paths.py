# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans=[]
        def dfs(node,s):
            if (s!=""):
                s=s+"->"
            s+=node.val
            if(node.left==None and node.right==None):
                ans.append(s)
            if(node.left!=None):
                dfs(node.left, s)
            if (node.right != None):
                dfs(node.right, s)
        dfs(root,"")
        return ans

