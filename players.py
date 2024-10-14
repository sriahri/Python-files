import tkinter
import tkinter.messagebox


class Main:
    def __init__(self, master):
        self.master = master
        self.master.title('Build Your Own Baseball Roster')
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.look = tkinter.Radiobutton(self.top_frame, text='Look up Player on roster',
                                        variable=self.radio_var, value=1, font="Arial 13", fg="blue")
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Player to Roster',
                                       variable=self.radio_var, value=2, font="Arial 13", fg="blue")
        self.change = tkinter.Radiobutton(self.top_frame, text='Change position of current player',
                                          variable=self.radio_var, value=3, font="Arial 13", fg="blue")
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete player off roster',
                                          variable=self.radio_var, value=4, font="Arial 13", fg="blue")
        self.look.pack(anchor='w', padx=100)
        self.add.pack(anchor='w', padx=100)
        self.change.pack(anchor='w', padx=100)
        self.delete.pack(anchor='w', padx=100)
        self.ok_button = tkinter.Button(self.bottom_frame, text='ENTER', fg="blue", font="Arial 13 bold",
                                        command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', fg="blue", font="Arial 13 bold",
                                          command=self.master.destroy)
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookupPlayerGUI(self.master)
        elif self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        elif self.radio_var.get() == 3:
            _ = ChangePlayerGUI(self.master)
        elif self.radio_var.get() == 4:
            _ = DeletePlayerGUI(self.master)
        else:
            tkinter.messagebox.showinfo('Not available')


class LookupPlayerGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'r')
            input_file.readlines(self.players)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.look = tkinter.Toplevel(master)
        self.look.title('Search for player')
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)
        self.search_label = tkinter.Label(self.top_frame, text='Enter player name to search the current roster: ',
                                          font="Arial 13", fg="blue")
        self.search_entry = tkinter.Entry(self.top_frame, width=20)
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Position: ', font="Arial 13", fg="blue")
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)
        self.info.pack(side='left')
        self.result_label.pack(side='left')
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', fg="blue", font="Arial 13 bold",
                                            command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', fg="blue", font="Arial 13 bold",
                                          command=self.back)
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def case_search(self, name):
        found = False
        for player in self.players:
            if name.lower() == player.lower():
                found = True
        return found

    def search(self):
        name = self.search_entry.get()
        if self.case_search(name):
            result = 'sill working on this part'
        else:
            result = 'Not Found'
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master):
        try:
            input_file = open('roster_file', 'r')
            lines = input_file.readlines()
            self.players = {}
            for i in lines:
                name, position = i.split(':')
                self.players[name] = position
            input_file.close()
        except (FileNotFoundError, IOError):
            self.players = {}

        self.add = tkinter.Toplevel(master)
        self.add.title('Add a player')
        self.top_frame = tkinter.Frame(self.add)
        self.middle_frame = tkinter.Frame(self.add)
        self.bottom_frame = tkinter.Frame(self.add)
        self.add_label = tkinter.Label(self.top_frame, text='Enter the players name to add')
        self.add_entry = tkinter.Entry(self.top_frame, width=25)
        self.position_label = tkinter.Label(self.top_frame, text='Enter their position')
        self.position_entry = tkinter.Entry(self.top_frame, width=15)
        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')
        self.position_label.pack(side='left')
        self.position_entry.pack(side='left')
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)
        self.info.pack(side='left')
        self.result_label.pack(side='left')
        self.add_button = tkinter.Button(self.bottom_frame, text='Add a player', command=self.add_person)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def case_search(self, name):
        found = False
        for player in self.players:
            if name.lower() == player.lower():
                found = True
        return found

    def add_person(self):
        name = self.add_entry.get()
        position = self.position_entry.get()
        found = self.case_search(name)
        if found:
            result = name + ' already exists'
        else:
            result = name + ' : ' + position + ' has been added to the roster'
            self.players[name] = position
            output_file = open('roster_file', 'w')
            for name, position in self.players.items():
                output_file.write(name + ':' + position + '\n')
            output_file.close()
        self.value.set(result)

    def back(self):
        self.add.destroy()


class ChangePlayerGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'r')
            input_file.read(self.players)
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
        self.info = tkinter.Label(self.middle_frame2, text='')
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

    def case_search(self, name):
        found = False
        for player in self.players:
            if name.lower() == player.lower():
                found = True
        return found

    def change_data(self):
        name = self.name_entry.get()
        new_position = self.position_entry.get()
        if self.case_search(name):
            self.players[name] = new_position
            self.value.set(name + " has had their position changed.")
            self.save_data()
        else:
            self.value.set('Not Found')

    def back(self):
        self.change.destroy()

    def save_data(self):
        output_file = open("roster_file", "w")
        output_file.write(self.players)
        output_file.close()


class DeletePlayerGUI:
    def __init__(self, master):
        try:
            input_file = open("roster_file", 'r')
            input_file.read(self.players)
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
        self.info = tkinter.Label(self.middle_frame, text='')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)
        self.info.pack(side='left')
        self.result_label.pack(side='left')
        self.delete_button = tkinter.Button(self.bottom_frame, text='Delete Player', command=self.delete_data)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)
        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def case_search(self, name):
        for player in self.players:
            if name.lower() == player.lower():
                return True, player
        return False, 0

    def delete_data(self):
        name = self.name_entry.get()
        found, name = self.case_search(name)
        if found:
            del self.players[name]
            self.value.set(name + " has been deleted from the roster.")
            self.save_data()
        else:
            self.value.set('Not Found')

    def back(self):
        self.delete.destroy()

    def save_data(self):
        output_file = open("roster_file", "w")
        output_file.write(self.players)
        output_file.close()


def main():
    root = tkinter.Tk()
    _ = Main(root)
    root.mainloop()


main()
