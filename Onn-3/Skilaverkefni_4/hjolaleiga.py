from tkinter import *
import csv

class Skjar():
    def __init__(self):
        with open('hjol.csv', 'r', newline='', encoding='utf-8') as file:
            ihusi, ileigu = csv.reader(file, delimiter='\n')
            self.ihusi = list(csv.reader(ihusi, delimiter=','))[0]
            self.ileigu = list(csv.reader(ileigu, delimiter=','))[0]

        self.win = Tk()
        self.frame = Frame()

        self.valmynd()

    def valmynd(self):
        self.clear()

        selectionFrame = Frame(self.win)
        selectionFrame.pack()

        rentBike = Button(selectionFrame, text='Rent a bike', command=self.chooseBike)
        rentBike.pack(fill=X)

        returnBike = Button(selectionFrame, text='Return a bike', command=self.returnBike)
        returnBike.pack(fill=X)

        exitProgram = Button(selectionFrame, text='Exit', command=self.close_window)
        exitProgram.pack(fill=X)

        self.frame = selectionFrame

    # ---- Panta hjól föll ----

    def clear(self):
        self.frame.destroy()

    def chooseBike(self):
        self.clear()

        chBikesFrame = Frame(self.win)
        chBikesFrame.pack()

        nafn = ''
        for index, hjol in enumerate(self.ihusi):
            if nafn != hjol:
                takki = Button(chBikesFrame, text=hjol, command=lambda hjol=index: self.basis(hjol))
                takki.pack(fill=X)
                nafn = hjol

        self.frame = chBikesFrame

    def basis(self, hjol):
        self.clear()

        basisFrame = Frame(self.win)
        basisFrame.pack()

        hourlyButton = Button(basisFrame, text='Request a bike on an hourly basis.', command=lambda basis='h', hjol=hjol : self.orderSuccessful(basis, hjol))
        hourlyButton.pack(fill=X)

        dailyButton = Button(basisFrame, text='Request a bike on a daily basis.', command=lambda basis='d', hjol=hjol : self.orderSuccessful(basis, hjol))
        dailyButton.pack(fill=X)

        weeklyButton = Button(basisFrame, text='Request a bike on a weekly basis.', command=lambda basis='w', hjol=hjol : self.orderSuccessful(basis, hjol))
        weeklyButton.pack(fill=X)

        self.frame = basisFrame

    def orderSuccessful(self, basis, hjol):
        self.clear()

        orderFrame = Frame(self.win)
        orderFrame.pack()

        words = {
            'h':'an hourly',
            'd':'a daily',
            'w':'a weekly'
        }

        message = Label(orderFrame, text=f'You have successfully ordered a {self.ihusi[hjol]} on {words[basis]} basis')
        message.pack()

        self.ileigu.append(self.ihusi.pop(hjol)+'-'+basis)

        returnButton = Button(orderFrame, text='Back', command=self.valmynd)
        returnButton.pack()

        self.frame = orderFrame

    # ---- Skila hjóli föll ----

    def returnBike(self):
        self.clear()

        rtBikesFrame = Frame(self.win)
        rtBikesFrame.pack()

        basis = {
            'h': 'an hourly',
            'd': 'a daily',
            'w': 'a weekly'
        }

        for index, hjol in enumerate(self.ileigu):
            nafn, letter = hjol.split('-')
            takki = Button(rtBikesFrame, text=f'{nafn} that was rented on {basis[letter]} basis', command=lambda hjol=index : self.returnSuccessful(hjol))
            takki.pack(fill=X)

        self.frame = rtBikesFrame

    def returnSuccessful(self, hjol):
        self.clear()

        rtsFrame = Frame(self.win)
        rtsFrame.pack()

        message = Label(rtsFrame, text=f'You have successfuly returned the {self.ileigu[hjol].split("-")[0]}')
        message.pack()

        self.ihusi.append(self.ileigu.pop(hjol).split('-')[0])
        print(self.ihusi)

        returnButton = Button(rtsFrame, text='Back', command=self.valmynd)
        returnButton.pack()

        self.frame = rtsFrame

#    def successful
    def close_window(self):
        self.win.destroy()

        with open('hjol.csv', 'w', newline='', encoding='utf-8') as file:
            file.write(','.join(self.ihusi)+'\n')
            file.write(','.join(self.ileigu)+'\n')





skjar = Skjar()

skjar.win.mainloop()