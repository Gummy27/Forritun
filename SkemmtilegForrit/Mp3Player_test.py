from tkinter import *
from os import listdir
from pygame import mixer
from time import sleep

win = Tk()

class MusicPlayer():
    def __init__(self):
        self.isPlaying = False

    def spila(self, oldPath, newPath):

        mixer.init()
        print(oldPath+"/"+newPath)
        mixer.music.load(oldPath+"/"+newPath)
        mixer.music.play()
        self.isPlaying = True

    def toggleMusic(self):
        if self.isPlaying:
            mixer.music.pause()
            self.isPlaying = False
        else:
            mixer.music.unpause()
            self.isPlaying = True

class Navigator():
    def __init__(self, path):
        self.frameList = Frame(win)
        self.frameList.grid(row=0)
        self.mediaPath = path

        for y, x in enumerate(listdir(self.mediaPath)):
            print(x)
            takki = Button(self.frameList, text=x, command=lambda x=x: pathGenerator(self.mediaPath, x))
            takki.pack()

    def update(self, newMediaPath):
        self.mediaPath = newMediaPath
        self.frameList.destroy()
        self.frameList = Frame(win)
        self.frameList.grid(row=0)

        if listdir(self.mediaPath)[0][-4:] != ".mp3":
            for y, x in enumerate(listdir(self.mediaPath)):
                print(x)
                takki = Button(self.frameList, text=x, command=lambda x=x: pathGenerator(self.mediaPath, x))
                takki.pack()

        else:
            for y, x in enumerate(listdir(self.mediaPath)):
                print("Here!")
                takki = Button(self.frameList, text=x, command=lambda x=x: spilari.spila(self.mediaPath, x))
                takki.pack()


def pathGenerator(mediaPath="", newPath="", back=True):
    if back:
        mediaPath += "/"+newPath
        gluggi.update(mediaPath)

    elif gluggi.mediaPath != "C:/Users/Brimi/Music":
        mediaPath = gluggi.mediaPath
        mediaPath = mediaPath[::-1].split("/", 1)[1][::-1]
        gluggi.update(mediaPath)

spilari = MusicPlayer()

# -------- Control buttons ----------
# Control frame
frameControls = Frame(win)
frameControls.grid(row=1)

# Play button
play = Button(frameControls, text="Play/Pause", command=spilari.toggleMusic)
play.grid(row=0, column=0, sticky=E)

# Quit button
quitButton = Button(frameControls, text="Quit", command=win.quit)
quitButton.grid(row=0, column=1, sticky=W)

# Back button
backButton = Button(frameControls, text="Back", command=lambda : pathGenerator(back=False))
backButton.grid(row=0, column=2)

gluggi = Navigator(input("Hvar er tonlístar mappan? : "))

win.mainloop()
