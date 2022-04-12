class TreeNode:
    def __init__(self, data, left, right) -> None:
        self.data = data
        self.left = left
        self.right = right

def construct(arr, low, high):
    if low > high:
        return None
    mid = low + (high - low) // 2
    rootValue = arr[mid]
    leftNode = construct(arr, low, mid - 1)
    rightNode = construct(arr, mid + 1, high)
    newNode = TreeNode(rootValue, leftNode, rightNode)

    return newNode

def inorder(root):
    if root == None:
        return
    print(root.data)
    inorder(root.left)
    inorder(root.right)

def findMax(root):
    if root == None:
        return -1
    if root.right != None:
        return findMax(root.right)
    else:
        return root.data

def findMin(root):
    if root == None:
        return -1
    if root.left != None:
        return findMin(root.left)
    else:
        return root.data

def insert(root, data):
    if root == None:
        return TreeNode(data, None, None)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    root = construct(arr, 0, len(arr) - 1)
    inorder(root)
    print("Max =", findMax(root))
    print("Min =", findMin(root))