

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value 
        if value < self.value:
            if not self.value:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left else False
        else:
            return self.right.contains(target) if self.right else False
    