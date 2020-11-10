class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    def debug(self):
        print(self.value, end=": ")

        if(self.left != None):
            print(self.left.value, end=", ")
        else:
            print("None", end=", ")
        if(self.right != None):
            print(self.right.value, end=", ")
        else:
            print("None", end=", ")
        print()

        if(self.left != None):
            self.left.debug()
        if(self.right != None):
            self.right.debug()


    def insert(self,d):
        if(self.value > d.value):
            if(self.left == None):
                self.left = d
                return
            else:
                self.left.insert(d)
        else:
            if(self.right == None):
                self.right = d
                return
            else:
                self.right.insert(d)
        # þinn kóði hér

    def find(self,d):
        if(self.left != None):
            if(self.left.value == d):
                return "True"
            elif(self.left.find(d) == "True"):
                return "True"

        if(self.right != None):
            if(self.right.value == d):
                return "True"
            elif(self.right.find(d) == "True"):
                return "True"

        # þinn kóði hér

    def preOrderPrint(self):
        if(self.left != None):
            print(self.left.value, end=", ")
            self.left.preOrderPrint()
            
        if(self.right != None):
            print(self.right.value, end=", ")
            self.right.preOrderPrint()
        # þinn kóði hér

    def postOrderPrint(self):
        if(self.left != None):
            self.left.postOrderPrint()
            print(self.left.value, end=", ")

        if(self.right != None):
            self.right.postOrderPrint()
            print(self.right.value, end=", ")
        # þinn kóði hér
 

    def delete(self,d): 
        pass
        # þinn kóði hér

    def findDeleteItems(self, d):
        if(self.left != None):
            if(self.left.value == d):
                return self, self.left
            else:
                outcome = self.left.findDeleteItems(d)
                if(outcome):
                    return outcome

        if(self.right != None):
            if(self.right.value == d):
                return self, self.right
            else:
                outcome = self.right.findDeleteItems(d)
                if(outcome):
                    return outcome



class Tree:
    def __init__(self):
        self.root = None
    
    def debug(self):
        self.root.debug()

    def insert(self,d):
        if(self.root == None):
            self.root = Node(d)
        else:
            self.root.insert(Node(d))
        # þinn kóði hér

    def find(self,d):
        if(self.root.value != d):
            return(self.root.find(d))
        else:
            return("True")
        # þinn kóði hér

    def preOrderPrint(self):
        print(self.root.value, end=", ")
        self.root.preOrderPrint()
        print()
        # þinn kóði hér

    def postOrderPrint(self):
        self.root.postOrderPrint()
        print(self.root.value, end=", ")
        print()
        # þinn kóði hér

    def delete(self,d):
        parent, deleteItem = self.findDeleteItems(d)
        print(parent.value, deleteItem.value)
        if(deleteItem):
            if(deleteItem.left and deleteItem.right):
                print("Case 3")
            elif(deleteItem.left or deleteItem.right):
                print("Case 2")
            else:
                if(parent.value > deleteItem.value):
                    parent.left = None
                else:
                    parent.right = None
                print("Case 1")
        else:
            print("No")
        # þinn kóði hér

    def findDeleteItems(self, d):
        if(self.root.value != d):
            return(self.root.findDeleteItems(d))
        else:
            return(self.root)

    def 

t = Tree()
t.insert(20)
t.insert(10)

t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
t.insert(2)

# t.debug()

t.preOrderPrint()
t.postOrderPrint()
print()
t.delete(2)
t.preOrderPrint()
print()
print(t.find(1))
print(t.find(35))
print(t.find(20))
