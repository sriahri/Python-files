from tkinter import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, window):
        window.geometry('320x100')
        window.title('Music Player')
        window.resizable(0, 0)
        load = Button(window, text="Load", width=10, font=('Times', 10), command=self.load)
        play = Button(window, text="Play", width=10, font=('Times', 10), command=self.play)
        pause = Button(window, text="Pause", width=10, font=('Times', 10), command=self.pause)
        stop = Button(window, text="Stop", width=10, font=('Times', 10), command=self.stop)
        load.place(x=0, y=20)
        play.place(x=110, y=20)
        pause.place(x=220, y=20)
        stop.place(x=110, y=60)
        self.music_file = False
        self.is_playing = False

    def load(self):
        self.music_file = filedialog.askopenfilename()

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        if not self.is_playing:
            mixer.music.pause()
            self.is_playing = True
        else:
            mixer.music.unpause()
            self.is_playing = False

    def stop(self):
        if self.music_file:
            mixer.music.stop()


if __name__ == '__main__':
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
