# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        mylist = []
        myP = []   
        ptr = root
        while ptr !=None:
            myP.append(ptr)
            mylist.append(ptr.val)
            ptrLeft = ptr.left
            
            while ptrLeft != None:
                myP.append(ptrLeft)
                mylist.append(ptrLeft.val)
                if ptrLeft.left == None:
                    break
                else:
                    ptrLeft = ptrLeft.left
            
            if ptrLeft!= None:
                if ptrLeft.right != None:
                    ptr = ptrLeft.right
                    myP.pop()
                else:
                    ptr =(myP.pop()).right
                    while ptr == None and len(myP) !=0:
                        ptr =(myP.pop()).right
            else:
                ptr =(myP.pop()).right
                while ptr == None and len(myP) !=0:
                    ptr =(myP.pop()).right
               
        return mylist