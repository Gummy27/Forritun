from random import randint, shuffle
from time import sleep

class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

    # Þetta fall notaði ég til að debuga kóðann. Ég ætlaði að eyða því hann hugsaði að þú myndir vilja nota það.
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

    def preOrderPrint(self):
        if(self.left != None):
            print(self.left.value, end=", ")
            self.left.preOrderPrint()
            
        if(self.right != None):
            print(self.right.value, end=", ")
            self.right.preOrderPrint()

    def postOrderPrint(self):
        if(self.left != None):
            self.left.postOrderPrint()
            print(self.left.value, end=", ")

        if(self.right != None):
            self.right.postOrderPrint()
            print(self.right.value, end=", ")

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

    def findMinItems(self):
        if(self.left == None):
            return self
        else:
            return self.left.findMinItems()

class Tree:
    def __init__(self):
        self.root = None
    
    def debug(self):
        if(self.root):
            self.root.debug()

    def insert(self,d):
        if(self.root == None):
            self.root = Node(d)
        else:
            self.root.insert(Node(d))

    def find(self,d):
        if(self.root):
            if(self.root.value != d):
                return(self.root.find(d))
            else:
                return("True")

    def preOrderPrint(self):
        if(self.root):
            print(self.root.value, end=", ")
            self.root.preOrderPrint()
            print()

    def postOrderPrint(self):
        if(self.root):
            self.root.postOrderPrint()
            print(self.root.value, end=", ")
            print()

    def delete(self,d):
        if(self.root and self.find(d)):
            if(self.root.value == d):
                if(self.root.right):
                    # print("Root case 3")
                    minItem = self.root.right.findMinItems()
                        
                    temp = minItem.value
                    minItem.value = self.root.value
                    self.root.value = temp
                    
                    self.delete(minItem.value)

                elif(self.root.left):
                    # print("Root case 2")

                    self.root.value = self.root.left.value
                    newLeft, newRight = self.root.left.left, self.root.left.right

                    self.root.left = newLeft
                    self.root.right = newRight

                else:
                    # print("Root Case 1")
                    self.root = None
            else:
                parent, deleteItem = self.findDeleteItems(d)
                if(deleteItem):
                    if(deleteItem.right):
                        # print(deleteItem.right.value, "Case 3")
                        minItem = deleteItem.right.findMinItems()
                        
                        temp = minItem.value
                        minItem.value = deleteItem.value
                        deleteItem.value = temp
                        
                        self.delete(minItem.value)

                    elif(deleteItem.left):
                        # print(deleteItem.left.value, "Case 2")

                        deleteItem.value = deleteItem.left.value
                        newLeft, newRight = deleteItem.left.left, deleteItem.left.right

                        deleteItem.left = newLeft
                        deleteItem.right = newRight


                    else:
                        # print(deleteItem.value, "Case 1")
                        if(parent.left):
                            if(parent.left.value == deleteItem.value):
                                parent.left = None

                        if(parent.right):
                            if(parent.right.value == deleteItem.value):
                                parent.right = None
        else:
            print("This value does not exist in this list!")

    def findDeleteItems(self, d):
        if(self.root.value != d):
            return(self.root.findDeleteItems(d))
        else:
            return(self.root)
    

t = Tree()
'''
t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
t.insert(2)
'''

leaves = []
for x in range(100):
    newRandom = randint(1, 500)
    if(newRandom not in leaves):
        leaves.append(newRandom)
        t.insert(newRandom)

print("Here are the leaves:", leaves)
t.debug()
print("-----------")
shuffle(leaves)

for x in leaves:
    t.delete(x)
    print(x, end=": ")
    t.preOrderPrint()

t.debug()
print()

t.preOrderPrint()
t.postOrderPrint()

t.debug()
print()

t.preOrderPrint()
print()

print()
t.debug()

# print(t.find(1))
# print(t.find(35))
# print(t.find(20))

print("If this is at the bottom then the code is working!")
t.preOrderPrint()