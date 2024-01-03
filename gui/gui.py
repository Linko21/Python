import tkinter as tk


def button_action():
    submitted_value = input_string_value.get()
    label_for_submitted_value = tk.Label(root, text=submitted_value, bg="yellow")
    label_for_submitted_value.pack()
    print("submitted: " + submitted_value)


root = tk.Tk()

input_string_value = tk.StringVar()

text_box = tk.Entry(root, textvariable=input_string_value)
text_box.insert(0, "Test.xlsx")
text_box.pack()

button = tk.Button(root, text="Aktion durchführen", command=button_action)
button.pack()

root.mainloop()
