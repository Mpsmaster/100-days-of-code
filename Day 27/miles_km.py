import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# empty_label = tk.Label(text="")
# empty_label.grid(column=0, row=0)
# empty_label.config(padx=50, pady=20)

input = tk.Entry(width=10)
input.grid(column=1, row=0)


miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)
# miles_label.config(padx=20, pady=20)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)
# equal_label.config(padx=20, pady=0)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)
# result_label.config(padx=20, pady=5)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)
# km_label.config(padx=20, pady=0)

def calculate():
    miles = float(input.get())
    km = miles * 1.60934
    result_label.config(text=km)
calculate_button = tk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)










window.mainloop()