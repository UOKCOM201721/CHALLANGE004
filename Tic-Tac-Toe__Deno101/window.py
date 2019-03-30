import tkinter as tk
from PIL import ImageTk, Image

class App:
    frames = {}

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x250')
        self.root.title('XOXO Game')
        superFrame = tk.Frame(self.root)
        for F in (Frame1, Frame2,):
            dumy = F(parent=superFrame, controller=self)
            dumy.grid(row=0, column=0, sticky='nsew')
            dumy.grid_columnconfigure(0, weight=1)
            dumy.grid_rowconfigure(0, weight=1)
            self.frames[F.__name__] = dumy
        superFrame.pack(expand=True)
        self.up()
        self.root.mainloop()

    def up(self, target='Frame1'):
        x = self.frames[target]
        x.tkraise()


class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='red')
        btn = tk.Button(self, text='Play', command=lambda: controller.up('Frame2'))
        btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class Frame2(tk.Frame):

    def __init__(self, parent, controller):
        self.ximg = ImageTk.PhotoImage(Image.open('x.jpg'))
        tk.Frame.__init__(self, parent, bg='green')
        d = tk.Button(self, text='ddd', image=self.ximg)
        d.pack()


App()
