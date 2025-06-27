import tkinter as tk

def convert():
        inches = float(entry_inch.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    

root = tk.Tk()
root.title("Inch to CM Converter")
root.geometry("300x200")

label_inch = tk.Label(root, text="Enter inches:")
label_inch.pack(pady=10)

entry_inch = tk.Entry(root)
entry_inch.pack()

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="Result will appear here")
label_result.pack(pady=10)

root.mainloop()