from tkinter import *


class resnet_gui:
    def __init__(self):
        root = Tk()
        theGui = gui(root)
        root.geometry("600x400")  # You want the size of the app to be 500x500
        root.resizable(0, 0)  # Don't allow resizing in the x or y direction
        root.title('Gui for resnet')
        root.mainloop()


class gui:
    def __init__(self, master):
        self.master = master

        self.var = []

        label = Label(self.master, text='Set your parameters of resnet', font=("Arial", 18))
        # label.config(font=("Arial", 20))
        label.pack()
        frame1 = Frame(self.master)
        frame1.pack()
        self.btn2 = IntVar()

        Label(frame1, text='Block Design', font=("", 12)).grid(row=2, column=0)
        subframe2 = Frame(frame1)
        subframe2.grid(row=2, column=1)
        radio2_1 = Radiobutton(subframe2, text='Basic', value=0, variable=self.btn2, font=("", 12)).pack(side=LEFT)
        radio2_2 = Radiobutton(subframe2, text='Bottleneck', value=1, variable=self.btn2, font=("", 12)).pack(side=LEFT)

        frame2 = Frame(self.master)
        frame2.pack()
        Label(frame1, text='Repetitions of Conv Block', font=("", 12)).grid(row=3, column=0, rowspan=50)
        subframe1 = Frame(frame2)

        default_r = StringVar()
        default_r.set('2')
        self.conv2_x = Entry(subframe1, textvariable=default_r)
        self.conv2_x.grid(row=3, column=1, columnspan=20)
        self.conv3_x = Entry(subframe1, textvariable=default_r)
        self.conv3_x.grid(row=4, column=1, columnspan=20)

        self.conv4_x = Entry(subframe1, textvariable=default_r)
        self.conv4_x.grid(row=5, column=1, columnspan=20)

        self.conv5_x = Entry(subframe1, textvariable=default_r)
        self.conv5_x.grid(row=6, column=1, columnspan=20)

        subframe1.grid(row=3, column=0)
        frame3 = Frame(self.master)
        frame3.pack()
        button = Button(frame3, text='Run network', width=10, font=("", 12))
        button.bind('<Button-1>', self.get_variable)
        button.pack()

        self.quitBtn = Button(frame3, text="Quit", command=self.master.quit, font=("", 12)).pack()
        # get parameters of resnet

    def get_variable(self, event):
        self.var.append(int(self.conv2_x.get()))
        self.var.append(int(self.conv3_x.get()))
        self.var.append(int(self.conv4_x.get()))
        self.var.append(int(self.conv5_x.get()))
        self.var.append(int(self.btn2.get()))

        print(self.var)


