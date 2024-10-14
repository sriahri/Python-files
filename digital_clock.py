from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Digital Clock")
window.geometry("200x120")
window.configure(bg="black")
window.resizable(False, False)

clock = Label(window, bg="black", fg="white", font=("Times", 30, "bold"), relief="flat")
clock.place(x=20, y=20)


def update_time():
    current_time = strftime("%H: %M: %S")
    clock.configure(text=current_time)
    clock.after(80, update_time)


update_time()
window.mainloop()
