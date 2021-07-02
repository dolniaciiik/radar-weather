from tkinter import *
from PIL import Image as im

radar = im.open('radar.png')

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text='download images', command=self.download)
        self.button.pack(side=LEFT)

        self.button = Button(frame, text='show images', command=self.show_im)
        self.button.pack(side=LEFT)

        self.w = Label(frame, image=photo)
        self.w.pack()

    def download(self):
        print('func works')

    def show_im(self):
        print('showing files')

if __name__=='__main__':
    main = Tk()
    app = App(main)
    main.mainloop()
