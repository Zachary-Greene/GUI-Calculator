# importing all the necessary libraries
from tkinter import *
import tkinter as tk
import sys

# defining and the answer to call back
answer = []


# creating the Window object
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.myText_Box = None
        self.master = master
        self.init_window()

    # define init_window
    def init_window(self):
        def retrieve_input():  # define retrieve_input for evaluation
            global var  # input var into the function
            x = text.get("1.0", 'end-2c')  # define x as the equation within the textbox
            text.delete(1.0, END)  # clear the textbox
            y = eval(x)  # define y as the answer
            text.insert(END, y)  # write the answer to the textbox after clearing the equation

        # defining the functions for the numbers and inserting the corresponding digit
        def zero():
            text.insert(END, '0')

        def one():
            text.insert(END, '1')

        def two():
            text.insert(END, '2')

        def three():
            text.insert(END, '3')

        def four():
            text.insert(END, '4')

        def five():
            text.insert(END, '5')

        def six():
            text.insert(END, '6')

        def seven():
            text.insert(END, '7')

        def eight():
            text.insert(END, '8')

        def nine():
            text.insert(END, '9')

        def point():
            text.insert(END, '.')

        # defining the functions for the other buttons and their corresponding symbols
        def add():
            text.insert(END, '+')

        def minus():
            text.insert(END, '-')

        def times():
            text.insert(END, '*')

        def divide():
            text.insert(END, '÷')

        def equals():
            text.insert(END, '=')
            retrieve_input()

        # def x10():
        #     text.insert(END, 'x10^x')

        # defining the functions for removing the last digit and clear the box
        def delete():
            text.delete('end-2c', END)

        def clear():
            text.delete(1.0, END)

        self.master.title('Calculator')  # setting the title
        self.pack(fill=BOTH, expand=1)
        text = tk.Text(root, height=3, width=27)  # setting the width and height of the textbox
        text.config(state='normal')  # setting the box as editable
        text.place(x=0, y=0)  # placinng the textbox at the top
        quitButton = Button(self, text='QUIT', height=2, width=4, command=self.client_exit)  # creating the quit button
        no0 = Button(root, text='0', height=2, width=4, command=zero)  # creating the 0 button
        no1 = Button(root, text='1', height=2, width=4, command=one)  # creating the 1 button
        no2 = Button(root, text='2', height=2, width=4, command=two)  # creating the 2 button
        no3 = Button(root, text='3', height=2, width=4, command=three)  # creating the 3 button
        no4 = Button(root, text='4', height=2, width=4, command=four)  # creating the 4 button
        no5 = Button(root, text='5', height=2, width=4, command=five)  # creating the 5 button
        no6 = Button(root, text='6', height=2, width=4, command=six)  # creating the 6 button
        no7 = Button(root, text='7', height=2, width=4, command=seven)  # creating the 7 button
        no8 = Button(root, text='8', height=2, width=4, command=eight)  # creating the 8 button
        no9 = Button(root, text='9', height=2, width=4, command=nine)  # creating the 9 button
        addBtn = Button(root, text='+', height=2, width=4, command=add)  # creating the addition button
        minusBtn = Button(root, text='-', height=2, width=4, command=minus)  # creating the subtraction button
        timesBtn = Button(root, text='x', height=2, width=4, command=times)  # creating the times button
        divideBtn = Button(root, text='÷', height=2, width=4, command=divide)  # creating the division button
        pointBtn = Button(root, text='.', height=2, width=4, command=point)  # creating the point button
        equalsBtn = Button(root, text='=', height=2, width=4, command=equals)  # creating the equals button
        # x10Btn = Button(root, text='x10^x', height=2, width=4, command=x10) #creating the times 10 by a power button
        delBtn = Button(root, text='DEl', height=2, width=4, command=delete)  # creating the delete button
        acBtn = Button(root, text='AC', height=2, width=4, command=clear)  # creating the clear button

        # placing the buttons
        no0.place(x=0, y=210)
        no1.place(x=0, y=160)
        no2.place(x=45, y=160)
        no3.place(x=90, y=160)
        no4.place(x=0, y=110)
        no5.place(x=45, y=110)
        no6.place(x=90, y=110)
        no7.place(x=0, y=60)
        no8.place(x=45, y=60)
        no9.place(x=90, y=60)
        addBtn.place(x=135, y=160)
        minusBtn.place(x=180, y=160)
        timesBtn.place(x=135, y=110)
        divideBtn.place(x=180, y=110)
        pointBtn.place(x=45, y=210)
        equalsBtn.place(x=135, y=210)
        # x10Btn.place(x=90, y=210)
        delBtn.place(x=135, y=60)
        acBtn.place(x=180, y=60)
        quitButton.place(x=180, y=210)

    # defining the quit function
    def client_exit(self):
        sys.exit()


root = Tk()  # defining root
entry = tk.Entry(root)  # defining entry
root.geometry('218x250')  # defining the window dimensions
app = Window(root)  # defining app
root.mainloop()  # initializing the main loop
