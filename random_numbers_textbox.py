import random
import tkinter as tk

frame = tk.Tk()
frame.title("Random numbers")
frame.geometry('400x200')


def printInput():
    lower_limit = text_box_lower.get()
    upper_limit = text_box_upper.get()
    count = text_box_count.get()
    result = []
    for i in range(int(count)):
        result.append(str(random.randint(int(lower_limit), int(upper_limit))))
    result = ' '.join(result)
    lbl.config(text="The numbers are: " + result)


# TextBox Creation
text_box_lower = tk.Entry(frame,
                          width=15)
text_box_lower.insert(0, "Lower limit")

text_box_upper = tk.Entry(frame,
                          width=15)
text_box_upper.insert(0, "Upper limit")

text_box_count = tk.Entry(frame,
                          width=15)
text_box_count.insert(0, "Total Count")

text_box_lower.pack()
text_box_upper.pack()
text_box_count.pack()

# Button Creation
Generate = tk.Button(frame,
                     text="Generate",
                     command=printInput)
Generate.pack()

# Label Creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()
