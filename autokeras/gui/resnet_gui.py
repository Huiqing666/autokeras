from tkinter import *


class resnet_gui:
    def __init__(self):
        root = Tk()
        theGui = gui(root)
        root.geometry("500x500")  # You want the size of the app to be 500x500
        root.resizable(0, 0)  # Don't allow resizing in the x or y direction
        root.title('Gui for resnet')
        root.mainloop()
        self.var = theGui.var
        print(self.var)


class gui:
    def __init__(self, master):
        self.master = master
        Label(self.master, text='Set your parameters of resnet').pack()
        frame1 = Frame(self.master)
        frame1.pack()

        self.btn1 = StringVar()
        self.btn2 = StringVar()

        Label(frame1, text='Number of Layers').grid(row=1, column=0)
        subframe1 = Frame(frame1)
        subframe1.grid(row=1, column=1)
        radio1_1 = Radiobutton(subframe1, text='18', value=18, variable=self.btn1).pack(side=LEFT)
        radio1_2 = Radiobutton(subframe1, text='34', value=34, variable=self.btn1).pack(side=LEFT)
        radio1_3 = Radiobutton(subframe1, text='50', value=50, variable=self.btn1).pack(side=LEFT)
        radio1_4 = Radiobutton(subframe1, text='101', value=101, variable=self.btn1).pack(side=LEFT)
        radio1_5 = Radiobutton(subframe1, text='152', value=152, variable=self.btn1).pack(side=LEFT)

        Label(frame1, text='Size of filters').grid(row=2, column=0)
        subframe2 = Frame(frame1)
        subframe2.grid(row=2, column=1)
        radio2_1 = Radiobutton(subframe2, text='2*2', value=2, variable=self.btn2).pack(side=LEFT)
        radio2_2 = Radiobutton(subframe2, text='3*3', value=3, variable=self.btn2).pack(side=LEFT)
        radio2_3 = Radiobutton(subframe2, text='4*4', value=4, variable=self.btn2).pack(side=LEFT)

        Label(frame1, text='Learning rate').grid(row=3, column=0)
        self.rateEntry = Entry(frame1)
        self.rateEntry.grid(row=3, column=1)

        frame3 = Frame(self.master)
        frame3.pack()
        button = Button(frame3, text='Run network', width=10)
        button.bind('<Button-1>', self.get_variable)
        button.pack()

        frame4 = Frame(self.master)
        frame4.pack()
        Label(frame4, text='show the network architecture').pack(side=LEFT)

        self.quitBtn = Button(self.master, text="Quit", command=self.master.quit).pack()
        # get parameters of resnet

    def get_variable(self, event):
        self.var = []
        self.var.append(int(self.btn1.get()))
        self.var.append(int(self.btn2.get()))
        self.var.append(float(self.rateEntry.get()))
        # res_range = int(rangeEntry.get())

        print("Reading inputs from gui: ...")

        # print(var)


