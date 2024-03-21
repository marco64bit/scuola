

class Node():
    
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data
        


root = Node(data=4)
root.left = Node(data=2, left=Node(data=1), right=Node(data=3))
root.right = Node(data=6, left=Node(data=5), right=Node(data=7))

def search(node, value):
    if(value < node.data):
        if not node.left:
            return None
        return search(node.left, value)
    elif(value > node.data):
        if not node.right:
            return None
        return search(node.right, value)
    else:
        return node.data
        
print("search 3", search(root, 3))
print("search 1", search(root, 1))
print("search 9", search(root, 9))

    