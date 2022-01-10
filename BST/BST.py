def main():
    list = [10,7,20,5,8,11,2,6,9,16,1,3,5,13,12,14,15]
    bstNode = Node()
    
    for num in list:
        bstNode.insert(num)
    print(bstNode.printTree([]))

    bstNode.insert(2)
    print(bstNode.printTree([]))

    print(bstNode.exist(35))

    bstNode.delete(0)
    print(bstNode.printTree([]))

    print(bstNode.getmax())
    print(maxDepth(bstNode))

# O(N^2)
def maxDepth(root):
    # Check if tree is empty
    if root == None:
        return 0 
    
    # Begin searching through both sides of our tree and at the same time we add a count to leftDepth and rightDepth variables.
    # Then, at the end we return the highest value of the two variables.
    leftDepth  = maxDepth(root.left) 
    rightDepth = maxDepth(root.right) 

    if leftDepth > rightDepth:
        return leftDepth + 1 
    else:
        return rightDepth + 1 

class Node:
    # Node constructor
    def __init__(self, val=None):
        self.left  = None
        self.right = None
        self.val   = val

    # O(N)
    def insert(self, val):
        # First we check for empty tree
        if not self.val:
            self.val = val
            return

        # If val already exists in the Tree we can simply return
        if self.val == val:
            return

        # If val is less the the value of our current node
        if val < self.val:
            # If there already exist a left node, we recursively call insert for that left node
            if self.left:
                self.left.insert(val)
                return
            # If no left node exist, we create the node with our val
            self.left = Node(val)
            return

        # Checking if the val is greater than our current node is redundant 
        # we simply check if a right node exists, and follow the same process
        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)

    # O(N)
    def exist(self, val):      
        # First we check if our value is the same as the current Node  
        if val == self.val:
            return True

        # We verify if our value is less than our Node and if a left Node exist to search from
        # if there is no Node to check we return false if not we check that left Node
        if val < self.val:
            if self.left == None:
                return False
            self.left.exist(val)
        
        # If the val is greater than our current Node we check if a right Node exist
        # if it does exist we must return our previous recursive call and check with the right Node
        # by doing this we make sure that we don't get stuck with a empty Node check which will return False
        if self.right == None:
            return False
        return self.right.exist(val)

    # O(N)
    def delete(self, val):
        if self.exist(val):
            # First we check if there is a Node and if our val is less o more than our current Node
            if self == None:
                return self
            if val < self.val:
                self.left = self.left.delete(val)
                return self
            if val > self.val:
                self.right = self.right.delete(val)
                return self
            
            # If we pass to this point it means we found our value in the tree, now we check if our Node
            # has and child Nodes
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right

            # min_larger_node: This variable describes the Node that will take the position of the new current Node.
            min_larger_node = self.right
            while min_larger_node.left:
                min_larger_node = min_larger_node.left # We are finding the new Node that will take the current
                                                       # Nodes position, it must be greater than the current Node
                                                       # but less than all other greater Nodes, hence the name.
            self.val = min_larger_node.val
            self.right = self.right.delete(min_larger_node.val)
            return self   
        else:
            return 0 

    # O(N^2)
    def printTree(self, vals):
        # We go through the left nodes of the tree, until we reach the last left node
        if self.left is not None:
            self.left.printTree(vals) 
        # Then recursively we add those values ​​to our list
        if self.val is not None:
            vals.append(self.val) 
        # At the same time we are verifying if there is a node on the right, 
        # if so, we repeat the process of the left and right node and add the values ​​to the list.
        if self.right is not None:
            self.right.printTree(vals)
        return vals

    # O(N)
    def getmax(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
        
main()