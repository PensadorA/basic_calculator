import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculadora Básica')
        self.geometry('350x500')
        self.frame_display()
        self.frame_button()
        self.acc = None

    def frame_display(self):
        style = ttk.Style(self)
        style.configure('frame1.TFrame', background='#2C3E50')
        frame_display_var = ttk.Frame(self, style='frame1.TFrame')
        frame_display_var.place(relheight=0.3, relwidth=1)

        label_dispaly = ttk.Label(frame_display_var, text='6796545465464646464646_')
        label_dispaly.place(width=310, height=100, relx=0.05, rely=0.2)


    def frame_button(self):
        style = ttk.Style(self)
        style.configure('frame2.TFrame', background='#566573')
        frame_display_var = ttk.Frame(self, style='frame2.TFrame')
        frame_display_var.place(rely=0.3, relheight=0.7, relwidth=1)

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12))

        button7 = ttk.Button(frame_display_var, text='7', style='my.TButton')
        button7.place(relx= 0.25, rely=0.1, height=50, width=50)

        button8 = ttk.Button(frame_display_var, text='8', width=3, style='my.TButton')
        button8.place(relx=0.4, rely=0.1, height=50, width=50)

        button9 = ttk.Button(frame_display_var, text='9', width=3, style='my.TButton')
        button9.place(relx=0.55, rely=0.1, height=50, width=50)

        button4 = ttk.Button(frame_display_var, text='4', style='my.TButton')
        button4.place(relx=0.25, rely=0.25, height=50, width=50)

        button5 = ttk.Button(frame_display_var, text='5', width=3, style='my.TButton')
        button5.place(relx=0.4, rely=0.25, height=50, width=50)

        button6 = ttk.Button(frame_display_var, text='6', width=3, style='my.TButton')
        button6.place(relx=0.55, rely=0.25, height=50, width=50)

        button1 = ttk.Button(frame_display_var, text='1', style='my.TButton')
        button1.place(relx=0.25, rely=0.4, height=50, width=50)

        button2 = ttk.Button(frame_display_var, text='2', width=3, style='my.TButton')
        button2.place(relx=0.4, rely=0.4, height=50, width=50)

        button3 = ttk.Button(frame_display_var, text='3', width=3, style='my.TButton')
        button3.place(relx=0.55, rely=0.4, height=50, width=50)

if __name__ == "__main__":
    app = App()
    app.mainloop()
