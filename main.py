import tkinter as tk
from tkinter import ttk
from calculator import *


class App(tk.Tk):
    def __init__(self):
        self.acc = ''
        self.acc1 = ''
        self.operador = None
        self.result = ''
        self.status: bool = False
        super().__init__()
        self.title('Calculadora Básica')
        self.geometry('350x500')
        self.frame_display()
        self.frame_button()



    def frame_display(self, value =''):
        style = ttk.Style(self)
        style.configure('frame1.TFrame', background='#2C3E50')

        style1 = ttk.Style(self)
        style1.configure('display.TLabel', font=('Helvetica', 15))
        frame_display_var = ttk.Frame(self, style='frame1.TFrame')
        frame_display_var.place(relheight=0.3, relwidth=1)

        label_dispaly = ttk.Label(frame_display_var, text=value, style='display.TLabel')
        label_dispaly.place(width=310, height=100, relx=0.05, rely=0.2)


    def frame_button(self):
        style = ttk.Style(self)
        style.configure('frame2.TFrame', background='#566573')
        frame_display_var = ttk.Frame(self, style='frame2.TFrame')
        frame_display_var.place(rely=0.3, relheight=0.7, relwidth=1)

        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12))

        button7 = ttk.Button(frame_display_var, text='7', style='my.TButton',
                             command= lambda :self.function_btt(7)
                             )
        button7.place(relx= 0.25, rely=0.1, height=50, width=50)

        button8 = ttk.Button(frame_display_var, text='8', width=3, style='my.TButton',
                             command=lambda: self.function_btt(8)
                             )
        button8.place(relx=0.4, rely=0.1, height=50, width=50)

        button9 = ttk.Button(frame_display_var, text='9', width=3, style='my.TButton',
                             command=lambda: self.function_btt(9)
                             )
        button9.place(relx=0.55, rely=0.1, height=50, width=50)

        button4 = ttk.Button(frame_display_var, text='4', style='my.TButton',
                             command=lambda: self.function_btt(4)
                             )
        button4.place(relx=0.25, rely=0.25, height=50, width=50)

        button5 = ttk.Button(frame_display_var, text='5', width=3, style='my.TButton',
                             command=lambda: self.function_btt(5)
                             )
        button5.place(relx=0.4, rely=0.25, height=50, width=50)

        button6 = ttk.Button(frame_display_var, text='6', width=3, style='my.TButton',
                             command=lambda: self.function_btt(6)
                             )
        button6.place(relx=0.55, rely=0.25, height=50, width=50)

        button1 = ttk.Button(frame_display_var, text='1', style='my.TButton',
                             command=lambda: self.function_btt(1)
                             )
        button1.place(relx=0.25, rely=0.4, height=50, width=50)

        button2 = ttk.Button(frame_display_var, text='2', width=3, style='my.TButton',
                             command=lambda: self.function_btt(2)
                             )
        button2.place(relx=0.4, rely=0.4, height=50, width=50)

        button3 = ttk.Button(frame_display_var, text='3', width=3, style='my.TButton',
                             command=lambda: self.function_btt(3)
                             )
        button3.place(relx=0.55, rely=0.4, height=50, width=50)

        button_equal = ttk.Button(frame_display_var, text='=', width=3, style='my.TButton',
                             command=self.operation_equal
                             )
        button_equal.place(relx=0.70, rely=0.4, height=50, width=50)

        button_more = ttk.Button(frame_display_var, text='+', width=3, style='my.TButton',
                             command=lambda: self.operation_soma()
                             )
        button_more.place(relx=0.70, rely=0.25, height=50, width=50)

        button_sub = ttk.Button(frame_display_var, text='-', width=3, style='my.TButton',
                             command=lambda: self.operation_sub()
                             )
        button_sub.place(relx=0.70, rely=0.1, height=50, width=50)

        button_mux = ttk.Button(frame_display_var, text='x', width=3, style='my.TButton',
                                command=lambda: self.operation_mux()
                                )
        button_mux.place(relx=0.70, rely=0.55, height=50, width=50)

        button_div = ttk.Button(frame_display_var, text='/', width=3, style='my.TButton',
                                command=lambda: self.operation_div()
                                )
        button_div.place(relx=0.55, rely=0.55, height=50, width=50)

        button_clear = ttk.Button(frame_display_var, text='C', width=3, style='my.TButton',
                                command=lambda: self.operation_clear()
                                )
        button_clear.place(relx=0.4, rely=0.55, height=50, width=50)

    def function_btt(self, value):
        if not self.status:
            self.acc = self.acc + str(value)
            self.frame_display(self.acc)
        else:
            self.acc1 = self.acc1 + str(value)
            self.frame_display(self.acc1)


    def operation_soma(self):

        if self.status:
            aaa = Operation.soma(int(self.acc), int(self.acc1))
            self.operador = '+'
            self.acc = aaa
            self.acc1 = ''
            self.frame_display(self.acc)
        else:
            self.status = True
            self.operador = '+'

    def operation_sub(self):

        if self.status:
            aaa = Operation.subtracao(int(self.acc), int(self.acc1))
            self.operador = '-'
            self.acc = aaa
            self.acc1 = ''
            self.frame_display(self.acc)
        else:
            self.status = True
            self.operador = '-'

    def operation_mux(self):

        if self.status:
            aaa = Operation.multiplica(int(self.acc), int(self.acc1))
            self.operador = 'X'
            self.acc = aaa
            self.acc1 = ''
            self.frame_display(self.acc)
        else:
            self.status = True
            self.operador = 'X'

    def operation_div(self):

        if self.status:
            aaa = Operation.multiplica(int(self.acc), int(self.acc1))
            self.operador = '/'
            self.acc = aaa
            self.acc1 = ''
            self.frame_display(self.acc)
        else:
            self.status = True
            self.operador = '/'

    def operation_clear(self):
        self.acc = ''
        self.acc1 = ''
        self.result = ''
        self.status = False
        self.operador = ''

    def operation_equal(self):
        print(self.operador)
        if self.operador == '+':
            self.result = Operation.soma(int(self.acc), int(self.acc1))
            self.frame_display(self.result)

        elif self.operador == '-':
            self.result = Operation.subtracao(int(self.acc), int(self.acc1))
            self.frame_display(self.result)

        elif self.operador == 'X':
            self.result = Operation.multiplica(int(self.acc), int(self.acc1))
            self.frame_display(self.result)

        else:
            self.result = Operation.divisao(int(self.acc), int(self.acc1))
            self.frame_display(self.result)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
