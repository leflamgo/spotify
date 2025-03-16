import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
import time
import threading



def play_music(mp3File):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3File)
    pygame.mixer.music.play()

def wait_for_input():
    input()
    pygame.mixer.music.stop()

musicthread = threading.Thread(target=play_music, args=("Come Over(1).mp3", "hot.mp3", "apple.mp3",  ))
input_thread = threading.Thread(target=wait_for_input)

musicthread.start()
input_thread.start()


music_player = tkr.Tk()
music_player.title("Music Player")
music_player.geometry("500x400")

directory = askdirectory()
if not directory:
    print("No directory selected")
    exit()

os.chdir(directory)

song_list = [song for song in os.listdir() if song.endswith(".mp3")]
if not song_list:
    print("No songs found in the directory")
    exit()

playlist = tkr.Listbox(music_player, font = "Serif 12 bold" ,
                       fg = "navy" , bg = "green", selectmode= tkr.SINGLE)

for song in song_list:
    playlist.insert(tkr.END, song)


pygame.init()
pygame.mixer.init()

def play():
    try:
        selected_song = playlist.get(tkr.ACTIVE)
        full_path = os.path.join(directory, selected_song)
        pygame.mixer.music.load(full_path)
        var.set(selected_song)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error: {e}")

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def pause1():
    pygame.mixer.music.pause()

def pause2():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = play, bg = "navy" , fg = "green")
Button2 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = pause, bg = "navy" , fg = "green")
Button3 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = unpause, bg = "navy" , fg = "green")
Button4 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = stop, bg = "navy" , fg = "green")
Button5 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = stop, bg = "navy" , fg = "green")
Button6 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = stop, bg = "navy" , fg = "green")
Button7 = tkr.Button(music_player, width = 5, height = 3,
                     font = "Serif 12 bold", text = "PLAY",
                     command = stop, bg = "navy" , fg = "green")

var = tkr.StringVar()
song_title = tkr.Label(music_player, font = "Serif 12 bold", textvariable = var)

song_title.pack()
Button1.pack(fill = "x")
Button2.pack(fill = "x")
Button3.pack(fill = "x")
Button4.pack(fill = "x")
Button5.pack(fill = "x")
Button6.pack(fill = "x")
Button7.pack(fill = "x")
playlist.pack(fill = "both" , expand = "yes")


music_player.mainloop()





