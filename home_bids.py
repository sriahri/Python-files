from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Final Question Example")
        self._name = StringVar()
        self._name.set("Enter the name here")
        self._age = IntVar()
        self._age.set("Enter age here")
        self._displayLabelText = StringVar()
        self._displayLabelText.set("\n\n\n\n")
        self._createWidgets()

    def _createWidgets(self):
        textEntry = Entry(self, takefocus=1, textvariable=self._name, width=40)
        textEntry.grid(row=0, sticky=EW)

        ageEntry = Entry(self, takefocus=1, textvariable=self._age, width=20)
        ageEntry.grid(row=1, sticky=W)

        displayLabel = Label(self, textvariable=self._displayLabelText, justify=LEFT)
        displayLabel.grid(row=2, sticky=NSEW)

        doneButton = Button(self, text='DONE', command=self.myEvent)
        doneButton.grid(row=3, sticky=S)

    def myEvent(self):
        print("Button Pressed")
        self._displayLabelText.set("\nName: " + self._name.get() +
                                   "\nAge: " + str(self._age.get()) + "\n\n")


def main():
    Application().mainloop()


main()
