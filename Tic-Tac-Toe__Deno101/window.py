import tkinter as tk
from PIL import ImageTk, Image

txt = ''
turn = 'X'
btn = {}
whiteimg = ''
xplays = set([])
oplays = set([])
iswinner = False


class Processing:
    def check_winner(self):
        global iswinner, xplays, oplays, txt, turn
        inhouseturn = "X" if turn == "O" else "O"
        data = xplays if inhouseturn == 'X' else oplays
        if not len(data) >= 3:
            return
        wincond = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        for x in wincond:
            if x <= data:
                iswinner = True
                txt.config(text="%s wins" % inhouseturn)
                for s in btn:
                    btn[s].__state__ = False
                break


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


class Frame2up(Processing):
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
            x.__name__ = i
            x.__state__ = True
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
        global turn, txt, xplays, oplays, iswinner

        if event.widget.__state__:
            event.widget.__state__ = False
        else:
            return
        if turn == 'X' and not iswinner:
            xplays.add(event.widget.__name__)
            turn = 'O'
            img = self.ximg
            txt.config(text="'%s' turn" % turn)
        elif turn == 'O' and not iswinner:
            oplays.add(event.widget.__name__)
            turn = 'X'
            img = self.oimg
            txt.config(text="'%s' turn" % turn)
        event.widget.config(image=img)
        self.check_winner()

class Frame2down:
    def main(self, parent, controller):
        global txt
        self.con = tk.Frame(parent)
        reset = tk.Button(self.con, text='reset', command=lambda: self.reset())
        reset.grid(row=0, column=0, columnspan=2, pady=10)
        self.con.pack()
        txt = tk.Label(self.con, text="'X' turn")
        txt.grid(row=1, column=0, columnspan=3, padx=10)
        return self.con


    def reset(self):
        global btn, whiteimg, txt, turn, xplays, oplays, iswinner

        for x in btn:
            xplays = set([])
            oplays = set([])
            btn[x].config(image=whiteimg)
            iswinner = False
            for s in btn:
                btn[s].__state__ = True
            txt.config(text="'X' turn")
            turn = "X"


class Frame2(Frame2up, Frame2down, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame2up().main(self, controller)
        Frame2down().main(self, controller)


App()

