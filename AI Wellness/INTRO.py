import time
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer

# Initialize pygame mixer
mixer.init()

# Create root window
root = Tk()
root.geometry("1000x500")
root.title("Iron Snap")

# Optional: Load and play a sound file (uncomment below and replace 'snap.mp3' with your file)
# mixer.music.load("snap.mp3")
# mixer.music.play()

# Function to play gif
def play_gif():
    root.lift()
    root.attributes("-topmost", True)

    # Load GIF
    gif = Image.open("ironsnap2.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)

    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.resize((1000, 500), Image.ANTIALIAS)
        frame_image = ImageTk.PhotoImage(frame)
        frames.append(frame_image)

    # Display each frame in sequence
    for frame in frames:
        lbl.config(image=frame)
        root.update()
        time.sleep(0.05)

    root.destroy()

# Run the GIF player
root.after(0, play_gif)
root.mainloop()
