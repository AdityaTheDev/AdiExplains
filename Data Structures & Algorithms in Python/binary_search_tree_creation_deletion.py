class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    #Insert a new node with the given key
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    #Delete a node with the given key
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        #Traverse the tree to find the node to delete
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            #Node with only one child or no child
            if root.left is None:
                temp=root.right
                del root
                return temp
                #return root.right
            
            elif root.right is None:
                temp=root.left
                del root
                return temp
                #return root.left

            #Node with two children: Get the inorder successor
            min_larger_node = self._find_min(root.right)
            root.key = min_larger_node.key
            root.right = self._delete_recursive(root.right, min_larger_node.key)

        return root

    #Helper function to find the minimum key in the subtree
    def _find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    #Inorder traversal of the tree (for testing)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)



bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder traversal after insertion:", bst.inorder_traversal())

bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder_traversal())

bst.delete(30)
print("Inorder traversal after deleting 30:", bst.inorder_traversal())

bst.delete(50)
print("Inorder traversal after deleting 50:", bst.inorder_traversal())
