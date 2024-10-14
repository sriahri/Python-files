import tkinter
import tkinter.messagebox
import pickle


class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Build Your Own Baseball Roster')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.look = tkinter.Radiobutton(self.top_frame, text='Look up Player on roster',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Player to Roster',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change position of current player',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete player off roster',
                                          variable=self.radio_var, value=4)

        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangeGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Not available')


class LookGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'rb')
            self.players = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Search for player')

        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        self.search_label = tkinter.Label(self.top_frame, text='Enter player name to search: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.players.get(str(name).lower(), 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):
        try:
            input_file = open('roster_file', 'rb')
            self.players = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.add = tkinter.Toplevel(master)
        self.add.title('Add a player')

        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)

        self.add_label = tkinter.Label(self.top_frame, text='Enter player name to add')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)
        self.position_label = tkinter.Label(self.top_frame, text='Enter the players position')
        self.position_entry = tkinter.Entry(self.top_frame, width=15)

        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.position_label.pack(side='left')
        self.position_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.add_button = tkinter.Button(self.bottom_frame, text='Add player', command=self.add_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add_person(self):
        name = str(self.add_entry.get()).lower()
        position = self.position_entry.get()
        if name in self.players:
            result = name + ' already exists'
        else:
            result = name + ' ' + position + ' will be added'
            self.players[name] = position
            output_file = open('roster_file', 'wb')
            pickle.dump(self.players, output_file)
            pickle.dump("\n", output_file)
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangeGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'rb')
            self.players = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.change = tkinter.Toplevel(master)
        self.change.title('Change players position')

        self.top_frame = tkinter.Frame(self.change)
        self.middle_frame1 = tkinter.Frame(self.change)
        self.middle_frame2 = tkinter.Frame(self.change)
        self.bottom_frame = tkinter.Frame(self.change)

        self.name_label = tkinter.Label(self.top_frame, text='Enter the name of the player: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.position_label = tkinter.Label(self.middle_frame1, text='Enter new position: ')
        self.position_entry = tkinter.Entry(self.middle_frame1, width=20)

        self.position_label.pack(side="left")
        self.position_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame2, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame2, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.change_button = tkinter.Button(self.bottom_frame, text='Change Position', command=self.change_data)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame1.pack()
        self.middle_frame2.pack()
        self.bottom_frame.pack()

    def change_data(self):
        name = self.name_entry.get()
        new_position = self.position_entry.get()
        result = self.players.get(name, 'Not Found')
        if result != 'Not Found':
            self.players[name] = new_position
            self.value.set(name + " has had their position changed.")
            self.save_data()
        else:
            self.value.set(result)

    def back(self):
        self.change.destroy()

    def save_data(self):
        output_file = open("roster_file", "wb")
        pickle.dump(self.players, output_file)
        output_file.close()


class DeleteGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'rb')
            self.players = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.delete = tkinter.Toplevel(master)
        self.delete.title('Delete')

        self.top_frame = tkinter.Frame(self.delete)
        self.middle_frame = tkinter.Frame(self.delete)
        self.bottom_frame = tkinter.Frame(self.delete)

        self.name_label = tkinter.Label(self.top_frame, text='Enter the name of the player: ')
        self.name_entry = tkinter.Entry(self.top_frame, width=15)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        self.info.pack(side='left')
        self.result_label.pack(side='left')

        self.delete_button = tkinter.Button(self.bottom_frame, text='Change Position', command=self.delete_data)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete_data(self):
        name = self.name_entry.get()
        result = self.players.get(name, 'Not Found')
        if result != 'Not Found':
            del self.players[name]
            self.value.set(name + " has been deleted from the roster.")
            self.save_data()
        else:
            self.value.set(result)

    def back(self):
        self.delete.destroy()

    def save_data(self):
        output_file = open("roster_file", "wb")
        pickle.dump(self.players, output_file)
        output_file.close()


def main():
    root = tkinter.Tk()
    _ = CrudGUI(root)
    root.mainloop()


main()
