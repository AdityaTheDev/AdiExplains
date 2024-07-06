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
        
def search(root, key):
    if root is None:
        return False
    
    queue = []
    queue.append(root)
    
    while queue:
        temp = queue.pop(0)
        
        if temp.val == key:
            return True
        
        if temp.left:
            queue.append(temp.left)
        
        if temp.right:
            queue.append(temp.right)
    
    return False       
        
 
def delete_deepest(root, d_node):
    queue = []
    queue.append(root)
    
    while queue:
        temp = queue.pop(0)
        
        if temp == d_node:
            temp = None
            return
        
        if temp.right:
            if temp.right == d_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)
        
        if temp.left:
            if temp.left == d_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)

def delete(root, key):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.val == key:
            return None
        else:
            return root
    
    key_node = None
    queue = []
    queue.append(root)
    
    while queue:
        temp = queue.pop(0)
        
        if temp.val == key:
            key_node = temp
        
        if temp.left:
            queue.append(temp.left)
        
        if temp.right:
            queue.append(temp.right)
    
    if key_node:
        x = temp.val
        delete_deepest(root, temp)
        key_node.val = x
    
    return root 

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
delete(r,1)
print("preorder traversal of the Binary Tree:")
preorder(r)
print()
print("postorder traversal of the Binary Tree:")
postorder(r)

print(search(r,6))

