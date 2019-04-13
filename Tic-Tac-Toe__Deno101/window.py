import tkinter as tk
from PIL import ImageTk, Image

# Declaration of all global vars to be used/modified by any function
txt = ''
turn = 'X'
btn = {}
whiteimg = ''
xplays = set([])
oplays = set([])
iswinner = False
plays = 0

# Class responsible for checking in there is a winner
class Processing:
    def check_winner(self):
        global iswinner, xplays, oplays, txt, turn

        # interchanging vars to compensate change in class Frame2up
        inhouseturn = "X" if turn == "O" else "O"
        data = xplays if inhouseturn == 'X' else oplays

        if not len(data) >= 3:
            return
        # all the winning senario's
        wincond = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

        for x in wincond:
            if x <= data:
                iswinner = True
                txt.config(text="%s wins" % inhouseturn)

                # disabling all the buttons after win
                for s in btn:
                    btn[s].__state__ = False
                break


class App:
    # global class var to hold all frame objects
    frames = {}

    def __init__(self):
        # defining the main container window
        self.root = tk.Tk()
        self.root.geometry('250x250')
        self.root.title('XOXO Game')

        # declaring a super container frame to hold all child frames
        superFrame = tk.Frame(self.root, bg='green')

        # the loop reduces redundant code for similar frames
        # also helps in managing produced frames
        for F in (Frame1, Frame2,):
            dumy = F(parent=superFrame, controller=self)

            # grid is used since grid helps implement card-layout since grid objects can occupy the same grid
            dumy.grid(row=0, column=0, sticky='nsew')
            dumy.grid_columnconfigure(0, weight=1)
            dumy.grid_rowconfigure(0, weight=1)

            # storing the frames in a dict with a key of 'name'
            self.frames[F.__name__] = dumy

        superFrame.pack(expand=True)
        self.up()
        self.root.mainloop()

    # function to raise 'bring into view' a the frame arg 'target'
    def up(self, target='Frame1'):
        x = self.frames[target]
        x.tkraise()


# returns object of type frame contents--{a single button to open the play window}
# args parent = frame or window to place this frame = object containing methods to change window
class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        btn = tk.Button(self, text='Play', command=lambda: controller.up('Frame2'))
        btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


# returns object of type frame like [Frame1] contents--{the playing deck}
class Frame2up(Processing):
    global btn

    # function to init the frame with widgets
    def main(self, parent, controller):
        global whiteimg

        # define the  x, o and white img
        self.ximg = ImageTk.PhotoImage(Image.open('x.jpg'))
        self.oimg = ImageTk.PhotoImage(Image.open('o.jpg'))
        self.uimg = ImageTk.PhotoImage(Image.open('n.jpg'))
        whiteimg = self.uimg
        self.con = tk.Frame(parent, bg='black')
        i = 1
        rowg = 0
        colg = 0

        # populate the playing grid avoiding redunduncy
        for x in range(0, 9, 1):
            x = tk.Label(self.con, image=self.uimg)
            x.grid(row=rowg, column=colg, padx=2, pady=2)
            x.__name__ = i

            # crutial to enabling and disabling click
            x.__state__ = True

            # binds a label to a mouse click event <Button-1>
            x.bind("<Button-1>", self.clickevent)

            # populating btn dict
            btn[x.__name__] = x

            i += 1
            if colg == 2:
                colg = 0
                rowg += 1
                continue
            colg += 1
        self.con.pack()
        return self.con

    # function that handles click-events takes args 'event' all the info about the click
    def clickevent(self, event):
        global turn, txt, xplays, oplays, iswinner, plays

        # disable btn after click
        if event.widget.__state__:
            event.widget.__state__ = False
        else:
            return

        # toggles the current player and the img. it also populates the global plays record
        if turn == 'X' and not iswinner:
            plays += 1
            # populate the global play set
            xplays.add(event.widget.__name__)
            turn = 'O'
            img = self.ximg
            txt.config(text="'%s' turn" % turn)
        elif turn == 'O' and not iswinner:
            plays += 1
            oplays.add(event.widget.__name__)
            turn = 'X'
            img = self.oimg
            txt.config(text="'%s' turn" % turn)

        if plays == 9:
            txt.config(text="Draw try again!")

        event.widget.config(image=img)
        self.check_winner()


# frame object contents--{reset btn, the info lable}
class Frame2down:
    def main(self, parent, controller):
        global txt
        self.con = tk.Frame(parent)
        reset = tk.Button(self.con, text='reset', command=lambda: self.reset())
        reset.grid(row=0, column=0, columnspan=4, pady=10)
        self.con.pack()
        txt = tk.Label(self.con, text="'X' turn")
        txt.grid(row=1, column=0, columnspan=4, padx=10)
        return self.con

    # resetting the deck, global play records, nd label
    def reset(self):
        global btn, whiteimg, txt, turn, xplays, oplays, iswinner,plays

        for x in btn:
            xplays = set([])
            oplays = set([])
            plays = 0
            btn[x].config(image=whiteimg)
            iswinner = False
            for s in btn:
                btn[s].__state__ = True
            txt.config(text="'X' turn")
            turn = "X"


# container frame for both frame2 frames
class Frame2(Frame2up, Frame2down, tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Frame2up().main(self, controller)
        Frame2down().main(self, controller)


# Application start
if __name__ == '__main__':
    App()

# THE END

