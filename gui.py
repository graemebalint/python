from tkinter import *
from password_generator import generatePassword

class GUI:

    def __init__(self):
        #create root window
        self.root = Tk()
        self.root.title("Password Manager")
        self.root.minsize(width=300,height=100)
        self.root.configure(padx=20,pady=20)

        #create frames
        self.logo_frame = Frame(self.root)
        self.logo_frame.grid(row=0,rowspan=2,column=0,columnspan=2)
        # self.logo_frame.configure()
        self.input_frame = Frame(self.root)
        self.input_frame.grid(row=2,column=0)
        self.input_frame.configure()

        #create logo
        self.canvas = Canvas(self.logo_frame,width=200,height=200)
        self.canvas.configure()
        self.logo = PhotoImage(file="logo.png")
        self.canvas.create_image(100,100,image=self.logo)
        self.canvas.grid(row=0,column=0,columnspan=2)

        #site name
        self.site_label = Label(self.input_frame,text="Site:")
        self.site_label.grid(row=0,column=0)

        self.site_entry = Entry(self.input_frame,width=21)
        self.site_entry.grid(row=0,column=1)

        #username
        self.username_label = Label(self.input_frame,text="Username:")
        self.username_label.grid(row=1,column=0)

        self.username_entry = Entry(self.input_frame,width=21)
        self.username_entry.grid(row=1,column=1)
        self.username_entry.insert(0,"graeme.m.balint@gmail.com")

        #password
        self.password_label = Label(self.input_frame,text="Password:")
        self.password_label.grid(row=2,column=0)

        self.password_entry = Entry(self.input_frame,width=21)
        self.password_entry.grid(row=2,column=1)

        #generate password button
        self.generate_pw = Button(self.input_frame,text="Generate password")
        self.generate_pw.bind("<Button-1>", self.new_random_password)
        self.generate_pw.grid(row=3,column=1)

        #submit button
        self.submit = Button(self.input_frame,text="Submit")
        self.submit.bind("<Button-1>", self.save_credentials)
        self.submit.grid(row=4,column=1)

        #gui loop
        self.root.mainloop()

    def new_random_password(self,event):
        pw = generatePassword()
        self.password_entry.delete(0,END)
        self.password_entry.insert(0,pw.return_password())

    def save_credentials(self,event):
        site = self.site_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        with open("/Users/graemebalint/Desktop/passwords.txt", "a") as file:
            file.write(f"Site: {site}\n")
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write("\n\n")
            self.site_entry.delete(0,END)
            self.password_entry.delete(0,END)