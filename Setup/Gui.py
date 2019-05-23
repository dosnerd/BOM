from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

G_APP = None


def wire_click(event):
    if event.widget.state:
        event.widget.config(bg="red")
        event.widget.state = False
    else:
        event.widget.config(bg="green")
        event.widget.state = True


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.start_time = {}
        self.duration = {}
        self.disable_codes = None
        self.wires = {}
        self.matrix = {}
        self.init_window()

    def init_window(self):
        # allowing the widget to take the full space of the root window
        self.master.title("Avans Bom Setup")
        self.master.geometry("1000x800")
        self.master.configure(background='white')

        self.pack(fill=BOTH, expand=True)

        self.build_start_time()
        self.build_duration()
        self.build_disable_codes()
        self.build_display()
        self.build_main_board()
        self.build_button()

    def build_start_time(self):
        start_time_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        start_time_frame.pack(fill=X)

        start_label = Label(start_time_frame, text="Countdown begint vanaf (UTF-0)")
        start_label.pack(side=LEFT)

        self.start_time[0] = Spinbox(start_time_frame, from_=0, to=23, width=3, value=12)
        self.start_time[0].pack(side=LEFT)

        self.start_time[1] = Spinbox(start_time_frame, from_=0, to=59, width=3)
        self.start_time[1].pack(side=LEFT)

        self.start_time[2] = Spinbox(start_time_frame, from_=0, to=59, width=3)
        self.start_time[2].pack(side=LEFT)

    def build_duration(self):
        duration_time_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        duration_time_frame.pack(fill=X)

        duration_label = Label(duration_time_frame, text="Countdown lengte (HH:MM::SS)")
        duration_label.pack(side=LEFT)

        self.duration[0] = Spinbox(duration_time_frame, from_=0, to=23, width=3, value=2)
        self.duration[0].pack(side=LEFT)

        self.duration[1] = Spinbox(duration_time_frame, from_=0, to=59, width=3, value=30)
        self.duration[1].pack(side=LEFT)

        self.duration[2] = Spinbox(duration_time_frame, from_=0, to=59, width=3)
        self.duration[2].pack(side=LEFT)

    def build_disable_codes(self):
        disable_codes_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        disable_codes_frame.pack(fill=X)

        disable_codes_label = Label(disable_codes_frame, text="Aantal codes om bom te ontmantelen")
        disable_codes_label.pack(side=LEFT)

        self.disable_codes = Spinbox(disable_codes_frame, from_=0, to=23, width=3, value=5)
        self.disable_codes.pack(side=LEFT)

    def build_display(self):
        display_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        display_frame.pack(fill=X)

        display_image = ImageTk.PhotoImage(Image.open("./display.jpeg")
                                           .resize((800, 315), Image.ANTIALIAS)
                                           .crop((90, 45, 710, 285)))

        img_label = Label(display_frame, borderwidth=0, image=display_image)
        img_label.image = display_image  # keep a reference!
        img_label.pack(side=LEFT)

        canvas = Canvas(display_frame, bg='red')
        canvas.place(x=155, rely=0.69, width=160, relheight=0.045, anchor=NW)
        canvas.state = False
        canvas.bind("<Button-1>", wire_click)
        self.wires[0] = canvas

        canvas = Canvas(display_frame, bg='red')
        canvas.place(x=155, rely=0.765, width=160, relheight=0.045, anchor=NW)
        canvas.state = False
        canvas.bind("<Button-1>", wire_click)
        self.wires[1] = canvas

        canvas = Canvas(display_frame, bg='red')
        canvas.place(x=155, rely=0.84, width=160, relheight=0.045, anchor=NW)
        canvas.state = False
        canvas.bind("<Button-1>", wire_click)
        self.wires[2] = canvas

        canvas = Canvas(display_frame, bg='red')
        canvas.place(x=155, rely=0.915, width=160, relheight=0.045, anchor=NW)
        canvas.state = False
        canvas.bind("<Button-1>", wire_click)
        self.wires[3] = canvas
        
        self.build_display_help(display_frame)

    def build_display_help(self, parent):
        display_help_frame = Frame(parent, bg='white')
        display_help_frame.pack(fill=Y, side=RIGHT)
		
        red_label = Label(display_help_frame, text="Rood => doorknippen geeft straftijd", fg='red', bg='white')
        red_label .pack()
		
        green_label = Label(display_help_frame, text="Groen => doorknippen geeft bonustijd", fg='green', bg='white')
        green_label.pack()
		
    def build_main_board(self):
        main_board_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        main_board_frame.pack(fill=X)

        display_image = ImageTk.PhotoImage(Image.open("./main.jpeg")
                                           .resize((800, 556), Image.ANTIALIAS)
                                           .crop((65, 60, 720, 485)))

        img_label = Label(main_board_frame, borderwidth=0, image=display_image)
        img_label.image = display_image  # keep a reference!
        img_label.pack(side=LEFT)

        self.build_table(main_board_frame)
        label = Label(main_board_frame, text="1")
        label.place(x=350, y=30)

        label = Label(main_board_frame, text="2")
        label.place(x=360, y=40)
		
        label = Label(main_board_frame, text="3")
        label.place(x=370, y=30)
                
        label = Label(main_board_frame, text="4")
        label.place(x=380, y=40)
        
        label = Label(main_board_frame, text="5")
        label.place(x=425, y=30)

        label = Label(main_board_frame, text="6")
        label.place(x=435, y=40)
        
        label = Label(main_board_frame, text="7")
        label.place(x=445, y=30)
        
        label = Label(main_board_frame, text="8")
        label.place(x=455, y=40)


        label = Label(main_board_frame, text="a")
        label.place(x=350, y=310)

        label = Label(main_board_frame, text="h")
        label.place(x=460, y=320)

    def build_table(self, parent):
        matrix_frame = Frame(parent, relief=RAISED, borderwidth=1)
        matrix_frame.pack(fill=Y, side=RIGHT)

        self.create_matrix_row(parent, "a")
        self.create_matrix_row(parent, "b")
        self.create_matrix_row(parent, "c")
        self.create_matrix_row(parent, "d")
        self.create_matrix_row(parent, "e")
        self.create_matrix_row(parent, "f")
        self.create_matrix_row(parent, "g")
        self.create_matrix_row(parent, "h")

    def create_matrix_row(self, parent, row):
        frame = Frame(parent, relief=RAISED, borderwidth=1)
        frame.pack(fill=X)

        lbl_a = Label(frame, text=row)
        lbl_a.pack(side=LEFT)

        self.matrix[ord(row) - ord('a')] = Spinbox(frame, from_=0, to=8, width=5, value=ord(row) - ord('a') + 1)
        self.matrix[ord(row) - ord('a')].pack(side=RIGHT)

    def build_button(self):
        button_frame = Frame(self, relief=RAISED, borderwidth=1, bg="white")
        button_frame.pack(fill=X)

        button = Button(button_frame, text="Save config", command=self.generate)
        button.pack()

    def generate(self):
        file = ""

        file += self.write_line(1, self.duration[0].get())
        file += self.write_line(2, self.duration[1].get())
        file += self.write_line(3, self.duration[2].get())

        file += self.write_line(4, self.start_time[0].get())
        file += self.write_line(5, self.start_time[1].get())
        file += self.write_line(6, self.start_time[2].get())

        file += self.write_line(7, self.disable_codes.get())

        mask = 0
        for i in self.wires:
            if not self.wires[i].state:
                mask |= 1 << i
        file += self.write_line(8, mask)

        if not self.check_matrix_valid():
            return

        for i in self.matrix:
            file += self.write_line(i + 9, self.matrix[i].get())
            self.matrix[i].config(bg='white')

        filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=[("BOM files", "*.bom")])
        if len(filename) == 0:
            return

        f = open(filename, "w")
        f.write(file)
        f.close()

    def check_matrix_valid(self):
        check = {}
        valid = True

        for i in self.matrix:
            try:
                value = int(self.matrix[i].get())
                if value > 8 or (value != 0 and value in check):
                    if value < 9:
                        self.matrix[check[value]].config(bg='red')

                    self.matrix[i].config(bg='red')
                    valid = False
                else:
                    self.matrix[i].config(bg='green')
                    check[value] = i
            except ValueError:
                valid = False
                self.matrix[i].config(bg='red')

        return valid

    def write_line(self, output, value):
        return "SET OUTPUT_" + str(output) + " " + str(value) + "\r\n"


def show():
    global G_APP

    root = Tk()
    G_APP = Window(root)
    root.mainloop()
