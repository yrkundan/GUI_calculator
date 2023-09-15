import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    print(calculation, "POS:", len(calculation))


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        print(calculation)
    except:
        clear_field()
        print(calculation, "Except")
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

def remove_last_item():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def calculate_percentage():
    global calculation
    try:
        calculation = str(eval(calculation) / 100)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

btn_1 =tk.Button(root, text="1", command=lambda: add_to_calculation("1"), width =5, font=("Arial", 14))
btn_1.grid(row=4, column=1)

btn_2 =tk.Button(root, text="2", command=lambda: add_to_calculation(2), width =5, font=("Arial", 14))
btn_2.grid(row=4, column=2)

btn_3 =tk.Button(root, text="3", command=lambda: add_to_calculation("3"), width =5, font=("Arial", 14))
btn_3.grid(row=4, column=3)

btn_4 =tk.Button(root, text="4", command=lambda: add_to_calculation(4), width =5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 =tk.Button(root, text="5", command=lambda: add_to_calculation(5), width =5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 =tk.Button(root, text="6", command=lambda: add_to_calculation(6), width =5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 =tk.Button(root, text="7", command=lambda: add_to_calculation(7), width =5, font=("Arial", 14))
btn_7.grid(row=2, column=1)

btn_8 =tk.Button(root, text="8", command=lambda: add_to_calculation(8), width =5, font=("Arial", 14))
btn_8.grid(row=2, column=2)

btn_9 =tk.Button(root, text="9", command=lambda: add_to_calculation(9), width =5, font=("Arial", 14))
btn_9.grid(row=2, column=3)

btn_plus =tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width =5, font=("Arial", 14))
btn_plus.grid(row=4, column=4)

btn_sub =tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width =5, font=("Arial", 14))
btn_sub.grid(row=3, column=4)

btn_mul =tk.Button(root, text="X", command=lambda: add_to_calculation("*"), width =5, font=("Arial", 14))
btn_mul.grid(row=2, column=4)

btn_0 =tk.Button(root, text="0", command=lambda: add_to_calculation("0"), width =5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_00 =tk.Button(root, text="00", command=lambda: add_to_calculation("00"), width =5, font=("Arial", 14))
btn_00.grid(row=5, column=1)

btn_dot =tk.Button(root, text=".", command=lambda: evaluate_calculation, width =5, font=("Arial", 14))
btn_dot.grid(row=5, column=3)

btn_clear =tk.Button(root, text="C", command=clear_field, width =5, font=("Arial", 14))
btn_clear.grid(row=1, column=1)

btn_percentage =tk.Button(root, text="%", command=lambda: calculate_percentage(), width =5, font=("Arial", 14))
btn_percentage.grid(row=1, column=2)

btn_equal =tk.Button(root, text="=", command= evaluate_calculation, width =5, font=("Arial", 14),bg="orange")

btn_equal.grid(row=5, column=4)

btn_divition =tk.Button(root, text="/", command=lambda:add_to_calculation("/"), width =5, font=("Arial", 14))
btn_divition.grid(row=1, column=4)

btn_cut =tk.Button(root, text="⬅️", command=lambda: remove_last_item(), width =5, font=("Arial", 14))
btn_cut.grid(row=1, column=3)

root.mainloop()