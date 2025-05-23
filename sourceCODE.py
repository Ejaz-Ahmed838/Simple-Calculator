import tkinter as tk
class CustomerError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class Calculator:
    button_style = {
        'width': 3,'height': 1,'borderwidth': 5,'highlightthickness': 6,
        'relief':"raised",'font':("Arial", 20),'fg': 'black','bg': '#F5E9D9',
        'activebackground': '#C0C0C0','activeforeground': '#FFFFFF' 
    }
    operator_style = {
    'width': 3,'height': 1,'borderwidth': 3,'highlightthickness': 0,
    'relief': "raised",'font': ("Arial", 20, "bold"),'fg': '#FFFFFF',
    'bg': '#8D6E63','activebackground': '#C0C0C0','activeforeground': '#000000'  
    }

    def __init__(self, window):

        self.window = window
        self.number = ''
        self.new_number = ''
        self.operator = ''

        self.entry_feild = tk.Entry(window, font=("Arial", 20),width=20)
        self.entry_feild.grid(row=0, column=0,sticky="ew", columnspan=4,padx=0,pady=0)
        self.create_button(Calculator.button_style,Calculator.operator_style)

    def create_button(self, style,oper_style):
        for i, value in enumerate(range(1, 10)):
            row = 4 - i // 3
            col = i % 3
            btn = tk.Button(self.window, text=str(value),
                            command=lambda val=value: self.on_click(val),
                            **style)
            btn.grid(row=row, column=col,padx=0,pady=0)

        
        btn = tk.Button(self.window,text='+',**oper_style,command=self.add)
        btn.grid(row=1,column=3,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='C',**oper_style,command=self.clear)
        btn.grid(row=1,column=0,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='⌫',**oper_style,command=self.backspace)
        btn.grid(row=1,column=1,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='=',**oper_style,command=self.equal_to)
        btn.grid(row=1,column=2,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='-',**oper_style,command=self.subtraction)
        btn.grid(row=2,column=3,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='x',**oper_style,command=self.multiplication)
        btn.grid(row=3,column=3,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window,text='/',**oper_style,command=self.division)
        btn.grid(row=4,column=3,sticky="nsew", padx=0, pady=0)
        btn = tk.Button(self.window, text='0',command=lambda : self.on_click(0),**style)
        btn.grid(row=5, column=1,padx=0,pady=0)
        btn = tk.Button(self.window, text='.',command=lambda : self.on_click('.'),**style)
        btn.grid(row=5, column=0,padx=0,pady=0)


    def on_click(self, num):
        if num == '.' and '.' in self.number:
            return 
        self.number += str(num)
        self.entry_feild.delete(0,tk.END)
        self.entry_feild.insert(0,self.new_number + self.operator + self.number)

    def equal_to(self):
            try:
                result = ''
                exp = self.entry_feild.get()
                if any(char in exp for char in "+x/-"):

                    if self.new_number.replace('.','').isdigit() and self.number.replace('.','').isdigit():
                        if self.operator in '+-/x':
                            match(self.operator):
                                case '+':
                                    result = float(self.new_number)+float(self.number)
                                case '-':
                                    result = float(self.new_number)-float(self.number)
                                case 'x':
                                    result = float(self.new_number)*float(self.number)
                                case '/':
                                    if float(self.number == 0):
                                        raise CustomerError("Division by 0")
                                    result = float(self.new_number)/float(self.number)
                                case '_':
                                    pass
                        else:
                            raise CustomerError("operator Error")

                    else:
                        raise CustomerError("Error")
                else:
                    pass
            except CustomerError  as e:
                self.entry_feild.delete(0,tk.END)
                self.entry_feild.insert(0,e)
            else:
                self.entry_feild.delete(0,tk.END)
                self.entry_feild.insert(0,str(result))
            finally:
                self.new_number = ''
                self.number = ''
                self.operator = ''

    def clear(self):
        self.new_number = ''
        self.number = ''
        self.operator = ''
        self.entry_feild.delete(0,tk.END)
    
    def add(self):
        try:
            exp = self.entry_feild.get().lower()
            if len(exp)!=0:
                if exp[-1] not in '+-/x':
                    self.new_number = self.number
                    self.number = ''
                    self.entry_feild.insert(tk.END,'+')
                else:
                    exp = list(exp)
                    exp[-1] = '+'
                    exp = ''.join(exp)
                    self.entry_feild.delete(0,tk.END)
                    self.entry_feild.insert(0,exp)     
            else:
                raise CustomerError('')
        except CustomerError as e:
            self.entry_feild.delete(0,tk.END)
            self.new_number = ''
            self.number = ''
            self.operator = ''
        else:
            self.operator = '+'         
        

    def backspace(self):
        try:
        
            if len(self.number)!=0:
                self.number = list(self.number)
                self.number = self.number[:-1]
                self.number = ''.join(self.number)
            else:
                pass
        except :
            self.entry_feild.delete(0,tk.END)
            self.entry_feild.insert(0,'Error')
            self.number = ''
        else:
            exp = self.entry_feild.get()
            exp = exp[:-1]
            self.entry_feild.delete(0,tk.END)
            self.entry_feild.insert(0,exp)
    
    def subtraction(self):
        try:
            exp = self.entry_feild.get().lower()
            if len(exp)!=0:
                if exp[-1] not in '+-/x':
                    self.new_number = self.number
                    self.number = ''
                    self.entry_feild.insert(tk.END,'-')
                else:
                    exp = list(exp)
                    exp[-1] = '-'
                    exp = ''.join(exp)
                    self.entry_feild.delete(0,tk.END)
                    self.entry_feild.insert(0,exp)     
            else:
                raise CustomerError('')
        except CustomerError as e:
            self.entry_feild.delete(0,tk.END)
            self.new_number = ''
            self.number = ''
            self.operator = ''
        else:
            self.operator = '-' 


    def division(self):
        try:
            exp = self.entry_feild.get().lower()
            if len(exp)!=0:
                if exp[-1] not in '+-/x':
                    self.new_number = self.number
                    self.number = ''
                    self.entry_feild.insert(tk.END,'/')
                else:
                    exp = list(exp)
                    exp[-1] = '/'
                    exp = ''.join(exp)
                    self.entry_feild.delete(0,tk.END)
                    self.entry_feild.insert(0,exp)     
            else:
                raise CustomerError('')
        except CustomerError as e:
            self.entry_feild.delete(0,tk.END)
            self.new_number = ''
            self.number = ''
            self.operator = ''
        else:
            self.operator = '/' 


    def multiplication(self):
        try:
            exp = self.entry_feild.get().lower()
            if len(exp)!=0:
                if exp[-1] not in '+-/x':
                    self.new_number = self.number
                    self.number = ''
                    self.entry_feild.insert(tk.END,'x')
                else:
                    exp = list(exp)
                    exp[-1] = 'x'
                    exp = ''.join(exp)
                    self.entry_feild.delete(0,tk.END)
                    self.entry_feild.insert(0,exp)     
            else:
                raise CustomerError('')
        except CustomerError as e:
            self.entry_feild.delete(0,tk.END)
            self.new_number = ''
            self.number = ''
            self.operator = ''
        else:
            self.operator = 'x' 

if __name__ == "__main__":
    root = tk.Tk()
    root.title("caculator")
    cal = Calculator(root)
    root.mainloop()