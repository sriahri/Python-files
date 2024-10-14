import tkinter
# import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class InternshipForm:

    def __init__(self):
        self.main_window = tkinter.Tk()
        #################
        self.main_window.title("Internship Form")
        self.main_window.geometry("400x400")
        self.main_window.configure(bg="lightblue")
        ##################
        self.full_name = StringVar()
        self.id = StringVar()
        self.phone_number = StringVar()
        self.gpa = StringVar()
        self.dept = StringVar()
        self.file_name = StringVar()
        #################first label and entry
        self.full_name_label = Label(self.main_window, text="Full Name", bg="lightblue").grid(row=1, column=0, padx=20,
                                                                                              pady=10)
        self.full_name_entry = Entry(self.main_window, textvariable=self.full_name).grid(row=1, column=1, padx=20,
                                                                                         pady=10)

        #################secound label and entry
        self.id_label = Label(self.main_window, text="ID", bg="lightblue").grid(row=2, column=0, padx=20, pady=10)
        self.id_entry = Entry(self.main_window, textvariable=self.id).grid(row=2, column=1, padx=20, pady=10)

        #################third label and entry
        self.phone_number_label = Label(self.main_window, text="Phone #", bg="lightblue").grid(row=3, column=0, padx=20,
                                                                                               pady=10)
        self.phone_number_entry = Entry(self.main_window, textvariable=self.phone_number).grid(row=3, column=1, padx=20,
                                                                                               pady=10)

        ###############fourth label and entry
        self.gpa_label = Label(self.main_window, text="GPA", bg="lightblue").grid(row=4, column=0, padx=20, pady=10)
        self.gpa_entry = Entry(self.main_window, textvariable=self.gpa).grid(row=4, column=1, padx=20, pady=10)

        ###############RaidioButtons
        self.dept_label = Label(self.main_window, text="Dep", bg="lightblue").grid(row=5, column=0, padx=20, pady=10)
        self.dept_radio = Radiobutton(self.main_window, text="IS", variable=self.dept, value="IS", bg="lightblue").grid(
            row=5, column=1, padx=10, pady=10)
        self.dept_radio = Radiobutton(self.main_window, text="CS", variable=self.dept, value="CS", bg="lightblue").grid(
            row=5, column=2, padx=10, pady=10)
        self.dept_radio = Radiobutton(self.main_window, text="SE", variable=self.dept, value="SE", bg="lightblue").grid(
            row=5, column=3, padx=10, pady=10)

        ###############file to be saved lable and entry
        self.filename_label = Label(self.main_window, text="File to be saved", bg="lightblue").grid(row=6, column=0,
                                                                                                    padx=20, pady=10)
        self.filename_entry = Entry(self.main_window, textvariable=self.file_name).grid(row=6, column=1, padx=20,
                                                                                        pady=10)

        #############open, submit button
        self.open_button = Button(self.main_window, text="Open", bg="grey", command=self.open_file).grid(row=6,
                                                                                                         column=2,
                                                                                                         padx=20,
                                                                                                         pady=10)
        # command=self.open_file)>>>>>>>>should crat method
        self.submit_button = Button(self.main_window, text="Submit", bg="grey", command=self.submit_info).grid(row=7,
                                                                                                               column=1,
                                                                                                               padx=20,
                                                                                                               pady=10)
        # command=self.submit_info)>>>>>>>>should crat method

        ############close button optional
        self.close_button = Button(self.main_window, text="Close", bg="grey", command=self.main_window.destroy).grid(
            row=7, column=2, padx=20, pady=10)
        ################ DONE
        tkinter.mainloop()
        #####################functions to check

    def submit_info(self):

        if self.file_name == "":
            messagebox.showerror("Error", "Please select a file")

        else:
            with open(self.file_name.get(), "a") as file:

                if self.full_name.get() == "":
                    messagebox.showinfo("Error", "Please enter your full name")
                    return
                elif type(self.full_name.get()) != str:
                    messagebox.showerror("Error", "Please enter name charachters only")
                    return
                else:
                    file.write("Name is: " + self.full_name.get() + "\n")

                if self.id.get() == "":
                    messagebox.showinfo("Error", "Please enter your ID")
                    return
                elif len(self.id.get()) == 10:
                    file.write("ID : " + self.id.get() + "\n")
                else:
                    messagebox.showerror("Error", "ID must be 10 digits only")
                    return

                if self.phone_number.get() == "":
                    messagebox.showinfo("Error", "Please enter your phone number")
                    return
                if len(self.phone_number.get()) == 10:
                    file.write("Phone Number is " + self.phone_number.get() + "\n")
                else:
                    messagebox.showerror("Error", "Phone number must be 10 digits and should start with 05")
                    return

                if self.gpa.get() == "":
                    messagebox.showinfo("Error", "Please enter your GPA")
                    return
                elif 0 <= float(self.gpa.get()) <= 5:
                    file.write("GPA is" + self.gpa.get() + "\n")
                else:
                    messagebox.showerror("Error", "GPA must be in 0 to 5 Range")
                    return

                if self.dept.get() == "":
                    messagebox.showinfo("Error", "Please select your department")
                    return
                else:
                    file.write("Department is " + self.dept.get() + "\n")

                    messagebox.showinfo("Success", "Information submitted successfully")
                    # self.clear_fields()

    def open_file(self):
        self.file_name1 = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("Text files", "*.txt"), ("all files", "*.*")))


x = InternshipForm()
