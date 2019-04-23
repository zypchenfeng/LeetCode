def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) == 0:
        return False
    elif len(preorder) == 1:
        return preorder
    else:
        root_id = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[root_id])
        root.left = buildTree(preorder, inorder[0:root_id])
        root.right = buildTree(preorder, inorder[root_id+1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]