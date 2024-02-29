import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import time
page=Tk()

mixer.init()

mus_file=[]
count=0
def listMusic():
    pass

def addMusic():
    musicValue=filedialog.askdirectory()
    if musicValue:
        os.chdir(musicValue)
        songs=os.listdir(musicValue)
        
        for song in songs:
            if song.endswith(".mp3"):
                mus_file.append(song)
                listbox.insert(END,song)
def playMusic():
    global count 
    musicName=mus_file[0] #chking...
    musicName=listbox.get(ACTIVE)
    mixer.music.load(mus_file[count],musicName)
    mixer.music.load(musicName)
    mixer.music.play()

def stopMusic():
    mixer.music.pause()

def nextMusic():
        global count
        count+=1
        mixer.music.load(mus_file[count])
        mixer.music.play()
#Back M   
def backMusic():
    global count
    count-=1
    mixer.music.load(mus_file[count])
    mixer.music.play()

def unPauseMusic():
    mixer.music.unpause()
# close page
def close():
    page.quit()

def s():
    mixer.music.fadeout(time)
# Frame_Music=Frame(page)
# Frame_Music.grid(row=10,columnspan=10)

#list box music
# Scroll=Scrollbar(Frame_Music)
# Playlist=Listbox(Frame_Music,width=15,height=15,yscrollcommand=Scroll.set)
# Scroll.config(command=Playlist.yview)
# Scroll.pack(side=RIGHT,fill=Y)
# Playlist.pack()
listbox=Listbox(page,width=20,height=18,)
listbox.place(x=100)

btn_play=Button(page,text="دست نزن جیزه ",bg="red",command=s).place(x=10,y=10)
# Button player
btn_play=Button(page,text="play music",bg="red",command=playMusic).place(x=10,y=50)
# Button add music
btn_play=Button(page,text="add music",bg="green",command=addMusic).place(x=10,y=90)
#Button next music
btn_play=Button(page,text="next music",bg="pink",command=nextMusic).place(x=10,y=130)
btn_play=Button(page,text="back music",bg="pink",command=backMusic).place(x=10,y=170)
#Button stop
btn_play=Button(page,text="stop music",bg="yellow",command=stopMusic).place(x=10,y=210)
btn_play=Button(page,text="un music",bg="yellow",command=unPauseMusic).place(x=10,y=250)
btn_play=Button(page,text="exit",bg="yellow",command=close).place(x=10,y=290)



page.geometry('700x700')
page.mainloop()