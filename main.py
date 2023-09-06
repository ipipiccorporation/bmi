import tkinter as tk

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        if height > 3 or height < 1.2:
            raise ValueError("！")
        if weight > 300 or weight < 30:
            raise ValueError("！")
        bmi = weight / (height ** 2)
        result_label.config(text="BMI: {:.2f}".format(bmi))
    except ValueError as e:
        result_label.config(text=str("你输入的参数有误，请重新输入"), fg="red")

root = tk.Tk()
root.title("BMI计算器")

height_label = tk.Label(root, text="身高（米）：")
height_label.grid(row=0, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1)

weight_label = tk.Label(root, text="体重（千克）：")
weight_label.grid(row=1, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="计算", command=calculate_bmi)
calculate_button.grid(row=2, column=0)

result_label = tk.Label(root)
result_label.grid(row=2, column=1)

root.mainloop()
