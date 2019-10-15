# mediaPath = "C:/Users/Brimi/Music/Metallica"
# mediaPath = mediaPath[::-1].split("/", 1)[1][::-1]
# print(mediaPath)

from pygame import mixer

mixer.init()
mixer.music.load("/home/gudmundur/Music/Metallica_Ride-The-LIghtning/03 For Whom The Bell Tolls.mp3")
mixer.music.play()

while True:
    pass