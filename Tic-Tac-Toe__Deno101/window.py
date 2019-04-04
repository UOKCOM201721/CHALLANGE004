import tkinter as tk
from PIL import ImageTk, Image

txt = ''
turn = 'X'
btn = {}
whiteimg = ''


class Processing:
    pass


class App:
    frames = {}

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('250x250')
        self.root.title('XOXO Game')
        superFrame = tk.Frame(self.root, bg='green')
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
        tk.Frame.__init__(self, parent)
        btn = tk.Button(self, text='Play', command=lambda: controller.up('Frame2'))
        btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class Frame2up:
    global btn

    def main(self, parent, controller):
        global whiteimg
        self.ximg = ImageTk.PhotoImage(Image.open('x.jpg'))
        self.oimg = ImageTk.PhotoImage(Image.open('o.jpg'))
        self.uimg = ImageTk.PhotoImage(Image.open('n.jpg'))
        whiteimg = self.uimg
        self.con = tk.Frame(parent, bg='black')
        i = 1
        rowg = 0
        colg = 0

        for x in range(0, 9, 1):
            x = tk.Label(self.con, image=self.uimg)
            x.grid(row=rowg, column=colg, padx=2, pady=2)
            x.__name__ = 'Btn-%s' % str(i)
            x.bind("<Button-1>", self.clickevent)
            btn[x.__name__] = x
            i += 1
            if colg == 2:
                colg = 0
                rowg += 1
                continue
            colg += 1
        self.con.pack()
        return self.con

    def clickevent(self, event):
        global turn, txt
        if turn == 'X'"":
            turn = 'O'
            img = self.ximg
        elif turn == 'O':
            turn = 'X'
            img = self.oimg
        event.widget.config(image=img)
        txt.config(text="'%s' turn" % turn)


class Frame2down:
    def main(self, parent, controller):
        global txt
        self.con = tk.Frame(parent)
        reset = tk.Button(self.con, text='reset', command=lambda: self.reset())
        reset.grid(row=0, column=0, columnspan=2, pady=10)
        self.con.pack()
        txt = tk.Label(self.con, text='')
        txt.grid(row=1, column=0, columnspan=3, padx=10)
        return self.con

    def reset(self):
        global btn, whiteimg, txt, turn

        for x in btn:
            btn[x].config(image=whiteimg)
            txt.config(text="'X' turn")
            turn = "X"



class Frame2(Frame2up, Frame2down, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        f1 = Frame2up().main(self, controller)
        f2 = Frame2down().main(self, controller)


App()

