# Tilvik af node heldur utan um gildið og næstu gildi, hægra og vinstra megin í tréinu.
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

    # Þetta fall tekur inn node og situr það í tréið með endurkvæmni.
    def insert(self,d):
        # Tjékkað er hvort nodein á að fara hægra eða vinstra megin.
        if(self.value > d.value): # Vinstra
            # Gáð er hvort að vinstra parturinn er laus. Ef svo er þá er nóðunni komið fyrir þar.
            if(self.left == None):
                self.left = d
                return # Þetta fall skilar ekki neinu.
            else:
                # Haldið er áfram með endurkvæmni.
                self.left.insert(d)
        else: # Hægri
            # Gáð er hvort að hægri parturinn er laus. Ef svo er þá er nóðunni komið fyrir þar.
            if(self.right == None): 
                self.right = d
                return
            else:
                # Haldið er áfram með endurkvæmni.
                self.right.insert(d)

    # Þetta fall leitar að nóðu með gildi sem samsvara d. Fallið skilar "True" eða "False".
    def find(self,d):
        # Gáð er hvort að nóðann sé fundinn með gildið d.
        if(self.value == d):
            return "True"
        else:
            # Gáð er hvort að gildið sé minni en d
            if(self.value < d):
                # Gáð er hvort að hægra greinin sé aktív. 
                if(self.right):
                    # Haldið er áfram með leitina.
                    return self.right.find(d)
                # Ef svo ekki þá er gildið ekki til í listanum.
                else:
                    # Fallið skilar "False" ef að nóðan er tóm. 
                    return "False"
            else:
                if(self.left):
                    return self.left.find(d)
                else:
                    return "False"

    # Fallið prentar út listanum í preorder.
    def preOrderPrint(self):
        # Gáð er hvort að vinstri greinin sé til.
        if(self.left != None):
            # Gildið er prentað út með , í endann. 
            print(self.left.value, end=", ")
            # Haldið er áfram vinstri greinina.
            self.left.preOrderPrint()
        
        # Gáð er hvort að hægri greinin sé til.
        if(self.right != None):
            # Gildið er prentað út með , í endann.
            print(self.right.value, end=", ")
            # Haldið er áfram hægri greina.
            self.right.preOrderPrint()

    # Fallið prentar út listanum í postorder
    def postOrderPrint(self):
        # Fallið er í raun alveg eins nema print skipuninn kemur á eftir
        # endurkvæmninni.
        if(self.left != None):
            self.left.postOrderPrint()
            print(self.left.value, end=", ")

        if(self.right != None):
            self.right.postOrderPrint()
            print(self.right.value, end=", ")

    # Þetta fall er notað til að finna nóðuna sem á að eyða.
    # Fallið skilar bæði nóðunni og foreldrinu.
    def findDeleteItems(self, parent, d):
        # Fyrst er gáð hvort við séum komnir á gildið sem leitað er að.
        if(self.value == d):
            # Bæði foreldrið og nóðan er skiluð. Foreldrið er notað til að þurrka 
            # annaðhvort hægri eða vinstri greinina.
            return parent, self
        # Annnars er haldið áfram með endurkvæmnina. Ekki er gert ráð fyrir því að 
        # fallið finni ekki gildið þar sem .find fall er keyrt fyrir.
        else:
            # Gáð er hvort að gildið sé stærra eða minna en gildið á self
            if(self.value < d):
                # Endurkvæmnin er haldinn áfram
                return self.right.findDeleteItems(self, d)
            else:
                return self.left.findDeleteItems(self, d)
    
    # Þetta fall er notað til að finna minnstu nóðuna í listanum. 
    def findMinItems(self, parent):
        # Gáð er hvort að minnsta stakið sé fundið.
        if(self.left == None):
            return parent, self # Nóðann er skiluð
        # Haldið er áfram dýpra inn í tréið.
        else:
            return self.left.findMinItems(self)

class Tree:
    def __init__(self):
        self.root = None
    
    # Þetta er fallið sem ég nota til að tjékka á strúktúr trésins.
    def debug(self):
        if(self.root):
            self.root.debug()

    # Þetta fall kallar á insert fall rótarinnar til að byrja endurkvæmni.
    def insert(self,d):
        # Fyrst er gáð hvort að rótinn sé til. Ef svo er ekki þá er nýja gildið sett í rótina.
        if(self.root == None):
            self.root = Node(d)
        else:
            # Fallið skilgreinur Node(d) og hendur tilvikinu í insert fall rótarinnar.
            self.root.insert(Node(d))

    # Þetta fall kallar á find fall rótarinnar.
    def find(self,d):
        # Gáð er hvort að rótin sé til yfir höfuð
        if(self.root):
            # Gáð er hvort að rótin samsvari gildinu.
            if(self.root.value != d):
                return(self.root.find(d))
            else:
                return("True")
        else:
            print("Tréið er tómt!")

    # Þetta fall kallar á preorder fall rótarinnar.
    def preOrderPrint(self):
        # Gáð er hvort að tréið sé tómt eða ekki.
        if(self.root):
            # Rótin er prentuð fyrst.
            print(self.root.value, end=", ")
            self.root.preOrderPrint()
            print()
        else:
            print("Tréið er tómt!")

    # Þetta fall kallar á postorder fall rótarinnar.
    def postOrderPrint(self):
        # Gáð er hvort að tréið sé tómt eða ekki.
        if(self.root):
            self.root.postOrderPrint()
            print(self.root.value, end=", ")
            print()
        else:
            print("Tréið er tómt.")


    # Þetta fall tekur inn gildi og eyðir því úr tréinu.
    def delete(self,d):
        # Gáð er fyrst hvort að rótin sé til og að gildið sé í tréinu.
        if(self.root and self.find(d) == "True"):
            # Þurfti að gera aðeins öðruvísi aðgerðir við rótina svo gerði það bara sér.
            if(self.root.value == d):
                print("The root deletion is now active!")
                # Root case 3 - Ef hægri greinin er aktív
                if(self.root.right):
                    # Fyrst er fundinn minnsta gildið í greininni og foreldrið.
                    parentDelete, minItem = self.root.right.findMinItems(self.root)

                    # Hvor megin foreldrisins nóðan var er varðveitist í bool breytu.
                    right = parentDelete.value < minItem.value

                    # Tímabundinn breyta er skilgreind í smá tíma og verðu notuð aðeins einu sinni.
                    temp = minItem.value

                    # minItem og rótar gildin eru skipt.
                    minItem.value = self.root.value
                    self.root.value = temp
                    
                    # Gáð er hvor megin á að eyða.
                    if(right):
                        parentDelete.right = None
                    else:
                        parentDelete.left = None

                # Root case 2 - Ef aðeins vinstra greinin er aktív
                elif(self.root.left):
                    # Rótin fær á sig nýtt gildi.
                    self.root.value = self.root.left.value
                    newLeft, newRight = self.root.left.left, self.root.left.right

                    # Greinarnar eru lagfærðar. Rótin tekur greinarnar frá eyddu nóðunni.
                    self.root.left = newLeft
                    self.root.right = newRight

                # Root case 1 - Ef hvorug greinin er aktív
                else:
                    # Rótin er bara tóm.
                    self.root = None
            else:
                parent, deleteItem = self.findDeleteItems(d)
                if(deleteItem):
                    # Case 3 - Ef aðeins hægri greinin er aktív
                    if(deleteItem.right):
                        # Fyrst er minnsta gildi hægri greinarinnar fundinn. Foreldrið er líka tekið inn.
                        parentDelete, minItem = deleteItem.right.findMinItems(deleteItem)
                        # Hvor megin foreldrisins nóðan var er geymd varðveitist í bool breytu.
                        right = parentDelete.value < minItem.value

                        # Tímabundinn breyta er skilgreind í smá tíma og verðu notuð aðeins einu sinni.
                        temp = minItem.value

                        # Minitem og eyddanóðan skipta á gildum.
                        minItem.value = deleteItem.value
                        deleteItem.value = temp
                        
                        # Gáð er hvor megin á að eyða.
                        if(right):
                            parentDelete.right = None
                        else:
                            parentDelete.left = None
                        # self.delete(minItem.value)

                    # Case 2 - Ef aðeins vinstri greinin er aktív
                    elif(deleteItem.left):
                        # Eydda nóðan fær á sig nýtt gildi.
                        deleteItem.value = deleteItem.left.value
                        newLeft, newRight = deleteItem.left.left, deleteItem.left.right

                        # Greinarnar eru lagfærðar. nóðan tekur greinarnar frá eyddu nóðunni.
                        deleteItem.left = newLeft
                        deleteItem.right = newRight

                    # Case 3 - Ef hvorug greinin er aktív
                    else:
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
            return(self.root.findDeleteItems(self.root, d))
        else:
            return(self.root, self.root)
    


t = Tree()

t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)

t.preOrderPrint()
t.postOrderPrint()
print()
print("Deletion phase:")
print("---------------")
t.delete(20)

print()
t.preOrderPrint()
print("---------------")
print()
print(t.find(1))
print(t.find(35))
print(t.find(25))
