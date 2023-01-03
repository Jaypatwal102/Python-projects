from tkinter import *
class calculator:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("400x600")
        self.window.title("CALCUTOR")
        self.display_frame=self.create_display_frame()
        self.button_frame=self.create_button_frame()
        self.total_expression=""
        self.current_expression=""
        self.digit={1:(1,1),2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3),0:(4,2)}
        self.create_digit_button=self.create_digit_button()
        self.operator={'/':"\u00f7",'*':"\u00D7","+":"+","-":"-"}
        self.create_operator_button()
        for i in range(1,5):
            self.button_frame.rowconfigure(i,weight=1)
            self.button_frame.columnconfigure(i,weight=1)
        self.create_dot_button()
        self.create_equal_button()
        self.create_clear_button()
        self.create_square_button()
        self.create_squareroot_button()
        self.bind_keys()
        self.total_label,self.label=self.create_display_label()
    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()
    def update_operators(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()
    def clear_button(self):
        self.current_expression=''
        self.total_expression=''
        self.update_label()
        self.update_total_label()

    def create_display_label(self):
        total_label=Label(self.display_frame,text=self.total_expression,font="smallfontsize",bg="white",fg="black",anchor=E)
        total_label.pack(expand=True,fill="both")
        label = Label(self.display_frame, text=self.current_expression, font="largefontsize", bg="white",
                            fg="black", anchor=E)
        label.pack(expand=True, fill="both")
        return total_label,label
    def create_dot_button(self):
        button=Button(self.button_frame,text=".",bg="white",fg="black",borderwidth=0,font="Arial")
        button.grid(row=4,column=1)

    def create_clear_button(self):
        button = Button(self.button_frame, text="C", bg="white", fg="black", borderwidth=0, font="Arial",command=self.clear_button)
        button.grid(row=0, column=1,columnspan=3)
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evalute())
        for key in self.digit:
            self.window.bind(str(key), lambda event,digit=key: self.add_to_expression(digit))
        for key in self.operator:
            self.window.bind(str(key), lambda event,operator=key: self.update_operators(operator))
    def evalute(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="ERROR"
        self.update_label()
    def square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_label()
    def squareroot(self):
        self.current_expression=str(eval(f"{self.current_expression}**0.5"))
        self.update_label()
    def create_equal_button(self):
        button = Button(self.button_frame, text="=", bg="lightblue", fg="black", borderwidth=0, font="Arial",command=self.evalute)
        button.grid(row=4, column=3,columnspan=2,sticky=NSEW)

    def create_square_button(self):
        button = Button(self.button_frame, text="x\u00b2", bg="white", fg="black", borderwidth=0, font="Arial",
                        command=self.square)
        button.grid(row=0, column=1)

    def create_squareroot_button(self):
        button = Button(self.button_frame, text="\u221ax", bg="white", fg="black", borderwidth=0, font="Arial",
                        command=self.squareroot)
        button.grid(row=0, column=3)

    def create_operator_button(self):
        i=0
        for digit,grid in self.operator.items():
            button=Button(self.button_frame,text=grid,bg="white",fg="black",borderwidth=0,font="Arial",command=lambda x=digit: self.update_operators(x))
            button.grid(row=i,column=4)
            i+=1

    def create_display_frame(self):
        frame=Frame(self.window,height=100,bg="gray")
        frame.pack(expand=True,fill="both")
        return frame
    def create_button_frame(self):
        frame_b=Frame(self.window)
        frame_b.pack(expand=True,fill="both")
        return frame_b


    def create_digit_button(self):
        for digit,grid in self.digit.items():
            button=Button(self.button_frame,text=str(digit),bg="white",fg="black",borderwidth=0,font="Arial",command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid[0],column=grid[1])



    def update_total_label(self):
        expression=self.total_expression
        for digit,symbol in self.operator.items():
            expression=expression.replace(digit,f'{symbol}')
        self.total_label.config(text=expression)
    def update_label(self):
        self.label.config(text=self.current_expression[:11])
    def run(self):
        self.window.mainloop()
if __name__=="__main__":
    calc=calculator()
    calc.run()