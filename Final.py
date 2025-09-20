import tkinter as tk
from tkinter import ttk




root = tk.Tk()
root.title("Калькулятор")
root.geometry("200x230")
root.iconbitmap(default="calculator icon.ico")


style = ttk.Style()
style.theme_use('clam')

style.configure("TButton", font=("Lato-Black", 20), padding=1)
style.configure("TLabel", font=("Lato-Black", 30), padding=10)

style.map("TButton", foreground=[("active", "orange")], background=[("active", "white")])
style.map("TButton", foreground=[("pressed", "white")], background=[("pressed", "orange")])
style.configure("TButton", foreground="black", background="white", borderwidth=2, relief="groove")
style.configure("TButton", highlightthickness=2, highlightbackground="orange")

expression = ""

result = tk.StringVar()
expression_field = ttk.Label(root, textvariable=result, width=8, font=("Lato-Black", 30), background="white", relief="groove", borderwidth=2, )

def update_font_size():
    font_size = int(min(root.winfo_height(), root.winfo_width())/8)
    expression_field.config(font=("Lato-Black", font_size))
    root.after(100, update_font_size)

update_font_size()

style.map("TButton", bordercolor=[("active", "orange")])
style.map("reset.TButton", bordercolor=[("active", "red")])
style.configure("TButton", borderwidth=2, relief="groove")
style.map("TButton", highlightthickness=[("active", 2), ("pressed", 0)])

style.map("reset.TButton", foreground=[("active", "red")], background=[("active", "white")], highlightbackground=[("active", "red")])
style.map("reset.TButton", foreground=[("pressed", "white")], background=[("pressed", "red")])
style.configure("reset.TButton", highlightthickness=2, borderwidth=2, relief="groove", highlightbackground="red")

for i in range (4):
    root.grid_columnconfigure(i, weight=1, minsize=1)

for i in range(6):
    root.grid_rowconfigure(i, weight=1, minsize=1)



expression_field.grid(columnspan=4, row=0, pady=(0,0))

def press_num(num):
    global expression
    if len(expression) < 8:
        expression += str(num)
        result.set(expression)
        

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.set("error")
        expression = ""
        

def reset():
    global expression
    total = ""
    result.set(total)
    expression = total

Button7 = ttk.Button(root, text="7", command=lambda: press_num(7), takefocus=False,)
Button7.grid(row=2, column=0, sticky="nsew")

Button8 = ttk.Button(root, text="8", command=lambda: press_num(8), takefocus=False)
Button8.grid(row=2, column=1, sticky="nsew")

Button9 = ttk.Button(root, text="9", command=lambda: press_num(9), takefocus=False)
Button9.grid(row=2, column=2, sticky="nsew")

dele = ttk.Button(root, text="/", command=lambda: press_num("/"), takefocus=False)
dele.grid(row=2, column=3, sticky="nsew")

Button4 = ttk.Button(root, text="4", command=lambda: press_num(4), takefocus=False)
Button4.grid(row=3, column=0, sticky="nsew")

Button5 = ttk.Button(root, text="5", command=lambda: press_num(5), takefocus=False)
Button5.grid(row=3, column=1, sticky="nsew")

Button6 = ttk.Button(root, text="6", command=lambda: press_num(6), takefocus=False)
Button6.grid(row=3, column=2, sticky="nsew")

umn = ttk.Button(root, text="*", command=lambda: press_num("*"), takefocus=False)
umn.grid(row=3, column=3, sticky="nsew")

Button1 = ttk.Button(root, text="1", command=lambda: press_num(1), takefocus=False)
Button1.grid(row=4, column=0, sticky="nsew")

Button2 = ttk.Button(root, text="2", command=lambda: press_num(2), takefocus=False)
Button2.grid(row=4, column=1, sticky="nsew")

Button3 = ttk.Button(root, text="3", command=lambda: press_num(3), takefocus=False)
Button3.grid(row=4, column=2, sticky="nsew")

minus = ttk.Button(root, text="-", command=lambda: press_num("-"), takefocus=False)
minus.grid(row=4, column=3, sticky="nsew")

Button0 = ttk.Button(root, text="0", command=lambda: press_num(0), takefocus=False)
Button0.grid(row=5, column=0, sticky="nsew")


reset = ttk.Button(root, text="C", command=reset, takefocus=False, style="reset.TButton")
reset.grid(row=5, column=1, sticky="nsew")

equal = ttk.Button(root, text="=", command=equalpress, takefocus=False)
equal.grid(row=5, column=2, sticky="nsew")

plus = ttk.Button(root, text="+", command=lambda: press_num("+"), takefocus=False)
plus.grid(row=5, column=3, sticky="nsew")


root.mainloop()