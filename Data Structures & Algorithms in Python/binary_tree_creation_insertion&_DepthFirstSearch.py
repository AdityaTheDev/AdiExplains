class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    
    queue = []
    queue.append(root)
    
    while queue:
        temp = queue.pop(0)
        
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    
    return root

# A function to do inorder tree traversal
        
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)        
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')
        
        
# Let us create the following Binary Tree
#      1
#    /   \
#   2     3
#  / \   / 
# 4   5 6   

r= Node(1)
r = insert(r, 2)
r = insert(r, 3)
r = insert(r, 4)
r = insert(r, 5)
r = insert(r, 6)

# Print in-order traversal of the Binary Tree
print("Inorder traversal of the Binary Tree:")
inorder(r)
print()
print("preorder traversal of the Binary Tree:")
preorder(r)
print()
print("postorder traversal of the Binary Tree:")
postorder(r)

