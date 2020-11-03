class Node: 
    # Smiður, frumstillir d og núllstillir bendana prv og nxt
    def __init__(self, d):
        self.data = d
        self.prv = None
        self.nxt = None

    # Endurkvæmt fall sem bætir aftast á listann.   
    def append(self, d):
        # Þinn kóði hér
        if(self.nxt == None):
            self.nxt = Node(d)
            self.nxt.prv = self.nxt

        else:
            self.nxt.append(d)

    # Endurkvæmt fall sem prentar listann.
    def printList(self):
        print(self.data, end=" ")

        if(self.nxt != None):
            self.nxt.printList()
        
        # Þinn kóði hér
                 
    # Endurkvæmt fall sem athuga hvort stak d er í listanum.
    def find(self, d):
        if(self.data == d):
            return "True"
        else:
            if(self.nxt == None):
                return "False"
            else:
                return self.nxt.find(d)

        # Þinn kóði hér

    # Endurkvæmt fall sem eyðir staki d úr listanum.
    def delete(self, d):
        if(self.data == d):
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv

            del self

            return "Deletion complete."
        else:
            if(self.nxt == None):
                return "Deletion incomplete."
            else:
                return self.nxt.delete(d)
        # Þinn kóði hér

class DLL:
    # Smiður, núllstillir Haus listans
    def __init__(self):
        pass
        self.head = None

    # Bætir við fremst á listann, hnúturinn verður Head -> förum ekki í Node klasann.
    def push(self,d):
        newNode = Node(d)

        newNode.nxt = self.head
        self.head.prv = newNode

        self.head = newNode
        self.printList()
        # Þinn kóði hér
    
    # Bætir við aftast á listann -> kallar á endurkvæmnt fall í Node.
    def append(self, d):
        if(self.head):
            self.head.append(d)
        else:
            self.head = Node(d)

        self.printList()
        # Þinn kóði hér

    # Prentar listann allan á skjá -> kallar á endurkvæmt fall í Node.
    def printList(self):
        self.head.printList()
        print()
        # Þinn kóði hér
    
    # Finnur stak d í ef til -> kallar á endurkvæmnt fall í Node.
    def find(self, d):
        return self.head.find(d)
        # Þinn kóði hér

    # Eyðir staki d úr lista ef til -> kallar á endurkvæmnt fall í Node.
    def delete(self, d):
        return self.head.delete(d)
        # Þinn kóði hér

# Keyrslurútína
dbl = DLL()
dbl.append(5)           # 5
dbl.append(7)           # 5 7    
dbl.push(1)             # 1 5 7 
dbl.push(0)             # 0 1 5 7 
dbl.append(10)          # 0 1 5 7 10
# dbl.printList()         
print()
print(dbl.delete(5))   # 0 1 7 10
dbl.printList() 
print()
print(dbl.find(5))      # False
print(dbl.find(7))      # True