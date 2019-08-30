import csv

class Invoice:
    #creates a new Invoice with the specified values
    def __init__(self, partNumber,partDescription,quantity,pricePerItem):
        self.partNumber = partNumber
        self.partDescription = partDescription
        self.quantity = quantity
        self.pricePerItem = pricePerItem

    #Calculate InvoiceAmount
    def getInvoiceAmount(self):
        return self.quantity * self.pricePerItem

    def printInvoice(self):
        print('Partnumber: {}\nPart Description: {}\nQuantity: {}\nPrice Per Item: {}'.format(self.partNumber,self.partDescription,self.quantity,self.pricePerItem))

def readFile():
    reikningar = []
    try:
        with open('invoice.csv', 'r', encoding='utf-8') as csv_file:
            for account in csv.reader(csv_file, delimiter=';'):
                try:
                    reikningar.append(Invoice(int(account[0]), account[1], int(account[2]), int(account[3])))
                except:
                    print('Villa við innsetningu breytna!')
    except IOError:
        print('Ekki tókst að opna skránna!')

    finally:
        global invoiceList
        invoiceList = reikningar
        
def writeFile():
    try:
        with open('invoice.csv', 'w', encoding='utf-8') as csv_file:
            for acc in invoiceList:
                csv_file.write(';'.join(list(map(str, vars(acc).values())))+'\n')
    except:
        print('Ekki tókst að opna skránna!')

def addInvoice():
    partNumber = int(input("Part number: "))
    partDescription = input("Part description: ")
    quantity = int(input("Quantity: "))
    pricePerItem = int(input("Price of the item: "))

    newAccount = Invoice(partNumber, partDescription, quantity, pricePerItem)
    invoiceList.append(newAccount)

def printInvoice():
    for acc in invoiceList:
        print(f'{acc.partDescription}: {acc.getInvoiceAmount()}')

def delInvoice():
    nr = int(input("Hvað er númerið á hlutnum sem þú vilt eyða? : "))
    for index, part in enumerate(invoiceList):
        if part.partNumber == nr:
            del invoiceList[index]
            break

def updateInvoice():
    nr = int(input("Hvað er númerið á hlutnum sem þú vilt uppfæra? : "))
    for index, part in enumerate(invoiceList):
        if part.partNumber == nr:
            part.pricePerItem = int(input("Hvað kostar varan mikið? : "))
            break

readFile()

#addInvoice()
# printInvoice()
delInvoice()
# updateInvoice()

writeFile()