from tkinter import *

try:

    first = Tk()

    second = Tk()

    total = 0

    items = []

    second.withdraw()

    first_frame = Frame(first)

    second_frame = Frame(first)

    third_frame = Frame(first)

    Shope_name = Label(first_frame, text="Welcome to Cam's Coffee Shop")

    Shope_name.pack()

    CheckVar1 = IntVar()

    CheckVar2 = IntVar()

    CheckVar3 = IntVar()

    CheckVar4 = IntVar()

    CheckVar5 = IntVar()

    CheckVar6 = IntVar()

    CheckVar7 = IntVar()

    C1 = Checkbutton(second_frame, text="Arabica Coffee ($4)", onvalue=1, offvalue=0, variable=CheckVar1).grid(sticky=W,
                                                                                                               column=0,
                                                                                                               row=0)

    C2 = Checkbutton(second_frame, text="Expresso Coffee($5)", onvalue=1, offvalue=0, variable=CheckVar2).grid(sticky=W,
                                                                                                               column=0,
                                                                                                               row=1)

    C3 = Checkbutton(second_frame, text="Americano Coffee($7)", onvalue=1, offvalue=0, variable=CheckVar3).grid(
        sticky=W, column=0, row=2)

    C4 = Checkbutton(second_frame, text="Bagel ($2)", onvalue=1, offvalue=0, variable=CheckVar4).grid(sticky=W,
                                                                                                      column=0, row=3)

    C5 = Checkbutton(second_frame, text="Donut ($3)", onvalue=1, offvalue=0, variable=CheckVar5).grid(sticky=W,
                                                                                                      column=0, row=4)

    C6 = Checkbutton(second_frame, text="Sugar ($0.25)", onvalue=1, offvalue=0, variable=CheckVar6).grid(sticky=W,
                                                                                                         column=0,
                                                                                                         row=5)

    C7 = Checkbutton(second_frame, text="Cream ($0.25)", onvalue=1, offvalue=0, variable=CheckVar7).grid(sticky=W,
                                                                                                         column=0,
                                                                                                         row=6)


    def Next():

        global total

        global items

        global CheckVar1

        global CheckVar2

        global CheckVar3

        global CheckVar4

        global CheckVar5

        global CheckVar6

        global CheckVar7

        C1 = Checkbutton(second_frame, text="Arabica Coffee ($4)", onvalue=1, offvalue=0, variable=CheckVar1).grid(
            sticky=W, column=0, row=0)

        C2 = Checkbutton(second_frame, text="Expresso Coffee($5)", onvalue=1, offvalue=0, variable=CheckVar2).grid(
            sticky=W, column=0, row=1)

        C3 = Checkbutton(second_frame, text="Americano Coffee($7)", onvalue=1, offvalue=0, variable=CheckVar3).grid(
            sticky=W, column=0, row=2)

        C4 = Checkbutton(second_frame, text="Bagel ($2)", onvalue=1, offvalue=0, variable=CheckVar4).grid(sticky=W,
                                                                                                          column=0,
                                                                                                          row=3)

        C5 = Checkbutton(second_frame, text="Donut ($3)", onvalue=1, offvalue=0, variable=CheckVar5).grid(sticky=W,
                                                                                                          column=0,
                                                                                                          row=4)

        C6 = Checkbutton(second_frame, text="Sugar ($0.25)", onvalue=1, offvalue=0, variable=CheckVar6).grid(sticky=W,
                                                                                                             column=0,
                                                                                                             row=5)

        C7 = Checkbutton(second_frame, text="Cream ($0.25)", onvalue=1, offvalue=0, variable=CheckVar7).grid(sticky=W,
                                                                                                             column=0,
                                                                                                             row=6)


    def Next():

        global total

        global items

        global CheckVar1

        global CheckVar2

        global CheckVar3

        global CheckVar4

        global CheckVar5

        global CheckVar6

        global CheckVar7

        if (CheckVar1.get() == 1):
            total += 4

            items.append("Arabica Coffee ($4)")

        if CheckVar2.get() == 1:
            total += 5

            items.append("Expresso Coffee($5)")

        if (CheckVar3.get() == 1):
            total += 7

            items.append("Americano Coffee($7)")

        if (CheckVar4.get() == 1):
            total += 2

            items.append("Bagel ($2)")

        if (CheckVar5.get() == 1):
            total += 3

            items.append("Donut ($3)")

        if (CheckVar6.get() == 1):
            total += 0.25

            items.append("Sugar ($0.25)")

        if (CheckVar7.get() == 1):

            total += 0.25

            items.append("Cream ($0.25)")

            print(total)

            first.withdraw()

            second.deiconify()

            Total_price.config(text="Total Price = $" + str(total))

            temp = ""

            for i in items:
                temp += i + "\n"

                Display_items.config(text=temp)

                B = Button(third_frame, text="Next", command=Next)

                B.pack()

                second_first_frame = Frame(second)

                second_second_frame = Frame(second)

                second_third_frame = Frame(second)

                second_forth_frame = Frame(second)

                second_fifth_frame = Frame(second)

                Show_items = Label(second_first_frame, text="Here are the items you chose...")

                Show_items.pack()

                Display_items = Label(second_third_frame, text="No Items bought!")

                Display_items.pack()

                Total_price = Label(second_third_frame, text="Total Price = " + str(total))

                Total_price.pack()

                Click_Done = Label(second_forth_frame, text="")

                Click_Done.pack()


    def Done():

        global total

        global items

        external_file = open("Bill.txt", "w")

        for i in items:
            external_file.write(i + "\n")

            external_file.write("Total = $" + str(total))

            items = []

            Total_price.config(text="Total Price = $")

            first.deiconify()

            second.withdraw()

            total = 0

            Done_button = Button(second_fifth_frame, text="Done", command=Done)

            Done_button.pack()

            second_first_frame.pack()

            second_second_frame.pack()

            second_third_frame.pack()

            second_forth_frame.pack()

            second_fifth_frame.pack()

            first_frame.pack()

            second_frame.pack()

            third_frame.pack()

            first.mainloop()

except:

    print("Error occour: ")
