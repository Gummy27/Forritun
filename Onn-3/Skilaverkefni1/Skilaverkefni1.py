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
        with open('invoice.csv', 'r') as csv_file:
            for account in csv.reader(csv_file, delimiter=';'):
                try:
                    reikningar.append(Invoice(int(account[0]), account[1], int(account[2]), int(account[3])))
                except:
                    print('Villa við innsetningu breytna!')
    except:
        print('Ekki tókst að opna skránna!')

    finally:
        return reikningar

def writeFile(accList):
    try:
        with open('invoice.csv', 'w') as csv_file:
            for acc in accList:
                csv_file.write(';'.join(list(map(str, vars(acc).values())))+'\n')
    except:
        print('Ekki tókst að opna skránna!')

def addInvoice():
    global invoiceList
    partNumber = input("Part number: ")
    partDescription = input("Part description: ")
    quantity = input("Quantity: ")
    pricePerItem = input("Price of the item: ")

    newAccount = Invoice(partNumber, partDescription, quantity, pricePerItem)
    invoiceList.append(newAccount)

def printInvoice(accList):
    for acc in accList:
        print(f'{acc.partDescription}: {acc.getInvoiceAmount()}')

invoiceList = readFile()
addInvoice()
writeFile(invoiceList)
printInvoice(invoiceList)
