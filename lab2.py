
from tkinter import *
import tkinter.messagebox as tmsg
import re
import json
from PIL import Image, ImageTk
root = Tk()
root.title("WELCOME TO IIT KGP PAGE")
root.geometry("800x450")
root.config(relief=SUNKEN)

UG_dic = {}
pg_dic = {}
teacher_dic = {}

def resize_image(event):
    # Resize the image to match the window size
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_image)
    
    # Update the image on the label
    image_label.config(image=photo)
    image_label.image = photo

def save_data():
    with open("ug_dic.json", "w") as file:
        json.dump(UG_dic, file, indent=2)
    with open("pg_dic.json", "w") as file:
        json.dump(pg_dic, file, indent=2)
    with open("tea_dic.json", "w") as file:
        json.dump(teacher_dic, file, indent=2)
    tmsg.showinfo("Saved", "Data has been saved successfully")
    print("Data has been saved successfully")
    return


def load_data():
    try:
        with open("ug_dic.json", "r") as file:
            global UG_dic
            UG_dic = json.load(file)
        with open("pg_dic.json", "r") as file:
            global pg_dic
            pg_dic = json.load(file)
        with open("tea_dic.json", "r") as file:
            global teacher_dic
            teacher_dic = json.load(file)
        tmsg.showinfo("Loaded", "Data has been loaded successfully")
        print("Data has been loaded successfully")
    except FileNotFoundError:
        tmsg.showinfo("File Not Found", "No saved data found. Please register or login to create data.")
    except json.JSONDecodeError:
        tmsg.showinfo("Error", "Error decoding JSON data. File may be corrupted.")
    except Exception as e:
        tmsg.showinfo("Error", f"An error occurred while loading data: {str(e)}")


load_data()


# Rest of your code ...


class Person:
    def __init__(self, usermail):
        self.usermail = usermail


class student(Person):
    def __init__(self, usermail):
        super().__init__(usermail)


class UG_Student(student):
    def __init__(self, usermail, password):
        super().__init__(usermail)
        self._password = password
        d2 = {usermail: self._password}
        global UG_dic
        UG_dic.update(d2)
        # print(UG_dic.keys())
        print(list(UG_dic.keys()))


class pg_Student(student):
    def __init__(self, usermail, password):
        super().__init__(usermail)
        self._password = password
        d2 = {usermail: self._password}
        global pg_dic
        pg_dic.update(d2)
        # print(UG_dic.keys())
        print(list(pg_dic.keys()))


class teacher(Person):
    def __init__(self, usermail, password):
        super().__init__(usermail)
        self._password = password
        d2 = {usermail: self._password}
        global teacher_dic
        teacher_dic.update(d2)
        # print(teacher_dic.keys())
        print(list(teacher_dic.keys()))


def lt():
    attempts_left = 3

    def submit():
        nonlocal attempts_left
        print(" registering as a teacher")
        if (u.get()) in teacher_dic:
            tmsg.showinfo("error", "this mail_id already exists try something else")
        elif is_gmail(u.get()) and is_valid_password(v.get()):
            ug_class = teacher(u.get(), v.get())
            tmsg.showinfo("Thank you", "You have successfully created your profile")
        else:
            attempts_left -= 1
            if u.get() in teacher_dic.keys():
                tmsg.showinfo("Error", f"mail_id already exist ,try with different id {attempts_left} attempts left.")
            else:
                tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")

    root_teacher = Tk()
    root_teacher.geometry("800x400")
    root_teacher.minsize(100, 100)
    root_teacher.title(" new teachers registration")
    write = Label(root_teacher, text="Email")
    write.grid(row=0)
    wri = Label(root_teacher, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_teacher, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_teacher, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_teacher, text="Submit", command=submit)
    b.grid(row=2, column=4)
    root_teacher.mainloop()
    tmsg.showinfo("Thank you", " registering as a teacher")


def is_gmail(email):
    pattern = re.compile(r'.+@gmail\.com$')
    return bool(pattern.search(email))


def is_valid_password(password):
    if not 8 <= len(password) <= 12:
        return False

    if not any(char.isupper() for char in password) or \
            not any(char.isdigit() for char in password) or \
            not any(char.islower() for char in password):
        return False

    if not any(char in "!@#$%&*" for char in password):
        return False

    if ' ' in password:
        return False

    return True


def ug():
    attempts_left = 3

    def submit():
        nonlocal attempts_left
        print(" registering as a UG student")
        if (u.get()) in UG_dic:
            tmsg.showinfo("error", "this mail_id already exists try something else")
        elif is_gmail(u.get()) and is_valid_password(v.get()):
            ug_class = UG_Student(u.get(), v.get())
            tmsg.showinfo("Thank you", "You have successfully created your profile")
        else:
            attempts_left -= 1
            if u.get() in UG_dic.keys():
                tmsg.showinfo("Error", f"mail_id already exist ,try with different id {attempts_left} attempts left.")
            else:
                tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")

    root_ug = Tk()
    root_ug.geometry("800x400")
    root_ug.minsize(100, 100)
    root_ug.title("UG REGISTRATION")
    write = Label(root_ug, text="Email")
    write.grid(row=0)
    wri = Label(root_ug, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_ug, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_ug, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_ug, text="Submit", command=submit)
    b.grid(row=2, column=4)
    root_ug.mainloop()


def pg():
    attempts_left = 3

    def submit():
        nonlocal attempts_left
        print(" registering as a PG student")
        if (u.get()) in pg_dic:
            tmsg.showinfo("error", "this mail_id already exists try something else")
        elif is_gmail(u.get()) and is_valid_password(v.get()):
            ug_class = pg_Student(u.get(), v.get())
            tmsg.showinfo("Thank you", "You have successfully created your profile")
        else:
            attempts_left -= 1
            if u.get() in pg_dic.keys():
                tmsg.showinfo("Error", f"mail_id already exist ,try with different id {attempts_left} attempts left.")
            else:
                tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")

    root_pg = Tk()
    root_pg.geometry("800x400")
    root_pg.minsize(100, 100)
    root_pg.title("PG REGISTRATION")
    write = Label(root_pg, text="Email")
    write.grid(row=0)
    wri = Label(root_pg, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_pg, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_pg, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_pg, text="Submit", command=submit)
    b.grid(row=2, column=4)
    root_pg.mainloop()

    print(" registering as a PG student")


# function for changing mailid
def change_Email():
    attempts_left = 3

    def check():
        which_dic = None
        id = u.get()
        nonlocal attempts_left
        if id in UG_dic:
            which_dic = "ug"
            user_dic = UG_dic
        elif id in pg_dic:
            which_dic = "pg"
            user_dic = pg_dic
        else:
            which_dic = "tea"
            user_dic = teacher_dic
        if u.get() in user_dic.keys():
            user_id = u.get()
        else:
            attempts_left -= 1
            tmsg.showinfo("error", f"User ID not found, try again {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
                return

        new_Email = p.get()

        if new_Email in user_dic.keys():
            tmsg.showinfo("error", "Email already exists. Please choose a different one.")
        elif not is_gmail(new_Email):
            attempts_left -= 1
            tmsg.showinfo("error", f"User ID not found, try again {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
                return

        else:
            if which_dic == "ug":
                v = UG_dic[id]
                UG_dic.pop(id)
                ug_class = UG_Student(new_Email, v)
            elif which_dic == "pg":
                o = pg_dic[id]
                pg_dic.pop(id)
                pg_class = pg_Student(new_Email, o)

            elif which_dic == "tea":
                q = pg_dic[id]
                teacher.pop(id)
                pg_class = teacher_Student(new_Email, q)
            tmsg.showinfo("update", f"Email has been updated to {new_Email}")

    print("Changing Email")
    root_change = Tk()
    root_change.geometry("800x400")
    root_change.title("EDIT PROFILE")
    root_change.minsize(100, 100)
    write = Label(root_change, text="User Mail id")
    write.grid(row=0)
    wri = Label(root_change, text="New Mail id")
    wri.grid(row=1)

    uservalue = StringVar()
    new_Email_value = StringVar()

    u = Entry(root_change, textvariable=uservalue)
    u.grid(row=0, column=5)
    p = Entry(root_change, textvariable=new_Email_value)
    p.grid(row=1, column=5)

    b = Button(root_change, text="Confirm", command=check)
    b.grid(row=3, column=9)

    root_change.mainloop()


# function for changing password
def change_password():
    attempts_left = 3

    def check():
        which_dic = None
        nonlocal attempts_left
        if (u.get() in UG_dic):
            which_dic = "ug"
            user_dic = UG_dic
        elif (u.get() in pg_dic):
            which_dic = "pg"
            user_dic = pg_dic
        elif (u.get() in teacher_dic):
            which_dic = "tea"
            user_dic = teacher_dic
        else:
            attempts_left -= 1
            tmsg.showinfo("error", f"Some error occurred, try again {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
        user_id = u.get()

        if (u.get(), v.get()) in user_dic.items():
            if is_valid_password(p.get()) and p.get() == c.get():
                tmsg.showinfo("update", "Password has been updated")
                if which_dic == "tea":
                    teacher_dic[user_id] = p.get()
                elif which_dic == "ug":
                    UG_dic[user_id] = p.get()
                elif which_dic == "pg":
                    pg_dic[user_id] = p.get()
                tmsg.showinfo("private", f"Your new password is {p.get()}, don't share it with anyone")
        elif u.get() in user_dic.keys():
            if not u.get() in user_dic.values():
                attempts_left -= 1
                tmsg.showinfo("error", f"Incorrect password, try again {attempts_left} attempts left.")
                if attempts_left == 0:
                    b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                    tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
        elif (u.get(), v.get()) in user_dic.items():
            if is_valid_password(p.get()):
                if not p.get() == c.get():
                    attempts_left -= 1
                    tmsg.showinfo("error", f"Password not matched, try again {attempts_left} attempts left.")
                    if attempts_left == 0:
                        b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                        tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
            else:
                if not is_valid_password(p.get()):
                    attempts_left -= 1
                    tmsg.showinfo("error", f"Invalid password format, try again {attempts_left} attempts left.")
                    if attempts_left == 0:
                        b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                        tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
        elif not u.get() in user_dic.keys():
            attempts_left -= 1
            tmsg.showinfo("error", f"User ID not found, try again {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")
        else:
            attempts_left -= 1
            tmsg.showinfo("error", f"Some error occurred, try again {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                tmsg.showinfo("Error", "Maximum attempts reached. Please contact support.")

    print("Changing password")
    root_change = Tk()
    root_change.geometry("800x400")
    root_change.title("EDIT PROFILE")
    root_change.minsize(100, 100)
    write = Label(root_change, text="Email")
    write.grid(row=0)
    wri = Label(root_change, text="Current Password")
    wri.grid(row=1)
    w = Label(root_change, text="New Password")
    w.grid(row=2)
    cpy = Label(root_change, text="Confirm New Password")
    cpy.grid(row=3)

    uservalue = StringVar()
    passwordvalue = StringVar()
    newpassword = StringVar()
    confirm_ = StringVar()
    u = Entry(root_change, textvariable=uservalue)
    u.grid(row=0, column=5)
    v = Entry(root_change, textvariable=passwordvalue)
    v.grid(row=1, column=5)
    p = Entry(root_change, textvariable=newpassword)
    p.grid(row=2, column=5)
    c = Entry(root_change, textvariable=confirm_)
    c.grid(row=3, column=5)
    b = Button(root_change, text="Confirm", command=check)
    b.grid(row=5, column=9)

    root_change.mainloop()


def none():
    tmsg.showinfo("sorry", "sorry but u should either be a teacher or a student to register in this institute")


def error():
    tmsg.showinfo("sorry", "sorry but u should either be a ug or a pg student to register in this institute")


def error1():
    tmsg.showinfo("sorry", "sorry but u should either be a ug or a pg student to login in this institute")


def login_as_teacher():
    attempts_left = 3

    def sign_in():
        nonlocal attempts_left
        if (u.get(), v.get()) in teacher_dic.items():
            tmsg.showinfo("verified", f"You have successfully signed in as {u.get()}")
            root_sign = Tk()
            root_sign.geometry("800x800")
            root_sign.title(" IIT KGP PAGE")
            w = Label(root_sign, text="WELCOME TO IIT KGP", font="Helvitika 20 bold", padx=15, pady=9)
            w.grid(row=8)
            o = Label(root_sign, text=f"THANK YOU FOR VISITING {u.get()}", font="Helvitika 20 bold", padx=15, pady=9)
            o.grid(row=10)
            logout_button = Button(root_sign, text="Log Out", command=logout)
            logout_button.grid(row=12, column=5)
            root_sign.mainloop()

        else:
            attempts_left -= 1
            tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                if ((u.get() in teacher_dic.keys()) or (v.get() in teacher_dic.values())):
                    teacher_dic.pop(u.get())
                tmsg.showinfo("Error", "Maximum attempts reached.account if present has been deactivated!.")

    def logout():
        tmsg.showinfo("Logout", "You have successfully logged out.")
        # Close the login window
        logout_button.config(state=DISABLED)
        root_sign.destroy()

    root_log_t = Tk()
    root_log_t.geometry("800x400")
    root_log_t.minsize(100, 100)
    root_log_t.title("log in page")
    write = Label(root_log_t, text="Email")
    write.grid(row=0)
    wri = Label(root_log_t, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_log_t, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_log_t, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_log_t, text="Sign In", command=sign_in)
    b.grid(row=2, column=4)
    root_log_t.mainloop()


# login as a ug student
def login_as_ug_student():
    attempts_left = 3

    def sign_in():
        nonlocal attempts_left
        if (u.get(), v.get()) in UG_dic.items():
            tmsg.showinfo("verified", f"You have successfully signed in as {u.get()}")
            root_si = Tk()
            root_si.geometry("800x800")
            root_si.title(" IIT KGP PAGE")
            w = Label(root_si, text="WELCOME TO IIT KGP", font="Helvitika 20 bold", padx=15, pady=9)
            w.grid(row=8)
            o = Label(root_si, text=f"THANK YOU FOR VISITING {u.get()}", font="Helvitika 20 bold", padx=15, pady=9)
            o.grid(row=10)
            logout_button = Button(root_si, text="Log Out", command=logout)
            logout_button.grid(row=12, column=5)
            root_si.mainloop()
        else:
            attempts_left -= 1
            tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                if ((u.get() in UG_dic.keys()) or (v.get() in UG_dic.values())):
                    UG_dic.pop(u.get())
                tmsg.showinfo("Error", "Maximum attempts reached.account if present has been deactivated!.")

    def logout():
        tmsg.showinfo("Logout", "You have successfully logged out.")
        # Close the login window
        logout_button.config(state=DISABLED)
        root_si.destroy()

    root_log_ug = Tk()
    root_log_ug.geometry("800x400")
    root_log_ug.minsize(100, 100)
    root_log_ug.title("log in page")
    write = Label(root_log_ug, text="Email")
    write.grid(row=0)
    wri = Label(root_log_ug, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_log_ug, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_log_ug, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_log_ug, text="Sign In", command=sign_in)
    b.grid(row=2, column=4)
    root_log_ug.mainloop()


def list_(user_dic):
    mail_list = list(user_dic.keys())

    # Create a new window for displaying the mail list
    mail_list_window = Tk()
    mail_list_window.title("Mail List")

    # Create a Listbox widget
    listbox = Listbox(mail_list_window, selectmode=SINGLE, width=40, height=10)
    listbox.pack(padx=10, pady=10)

    # Add mail IDs to the Listbox
    for mail_id in mail_list:
        listbox.insert(END, mail_id)

        # Create a Scrollbar and link it to the Listbox
    scrollbar = Scrollbar(mail_list_window, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    mail_list_window.mainloop()


def list_ug():
    list_(UG_dic)


def list_pg():
    list_(pg_dic)


def list_teacher():
    list_(teacher_dic)


# login as pg studet=nt function
def login_as_pg_student():
    attempts_left = 3

    def sign_in():
        nonlocal attempts_left
        if (u.get(), v.get()) in pg_dic.items():
            tmsg.showinfo("verified", f"You have successfully signed in as {u.get()}")
            root_s = Tk()
            root_s.geometry("800x800")
            root_s.title(" IIT KGP PAGE")
            w = Label(root_s, text="WELCOME TO IIT KGP", font="Helvitika 20 bold", padx=15, pady=9)
            w.grid(row=8)
            o = Label(root_s, text=f"THANK YOU FOR VISITING {u.get()}", font="Helvitika 20 bold", padx=15, pady=9)
            o.grid(row=10)
            logout_button = Button(root_s, text="Log Out", command=logout)
            logout_button.grid(row=12, column=5)
            root_s.mainloop()
        else:
            attempts_left -= 1
            tmsg.showinfo("Error", f"Invalid Gmail or password. {attempts_left} attempts left.")
            if attempts_left == 0:
                b.config(state=DISABLED)  # Disable the submit button after 3 failed attempts
                if ((u.get() in pg_dic.keys()) or (v.get() in pg_dic.values())):
                    pg_dic.pop(u.get())
                tmsg.showinfo("Error", "Maximum attempts reached.account if present has been deactivated!.")

    def logout():
        tmsg.showinfo("Logout", "You have successfully logged out.")
        logout_button(state=DISABLED)
        # Close the login window
        root_s.destroy()

    root_log_pg = Tk()
    root_log_pg.geometry("800x400")
    root_log_pg.minsize(100, 100)
    write = Label(root_log_pg, text="Email")
    write.grid(row=0)
    wri = Label(root_log_pg, text="Password")
    wri.grid(row=1)
    uservalue = StringVar()
    passwordvalue = StringVar()
    u = Entry(root_log_pg, textvariable=uservalue)
    u.grid(row=0, column=1)
    v = Entry(root_log_pg, textvariable=passwordvalue)
    v.grid(row=1, column=1)
    b = Button(root_log_pg, text="Sign In", command=sign_in)
    b.grid(row=2, column=4)
    root_log_pg.mainloop()


# deregistration function
def deregistration():
    def request():
        user_id = u.get()
        if user_id in UG_dic.keys():
            UG_dic.pop(user_id)
            tmsg.showinfo("Deactivated", "Your account has been deactivated")
        elif user_id in pg_dic.keys():
            pg_dic.pop(user_id)
            tmsg.showinfo("Deactivated", "Your account has been deactivated")
        elif user_id in teacher_dic.keys():
            teacher_dic.pop(user_id)
            tmsg.showinfo("Deactivated", "Your account has been deactivated")
        else:
            tmsg.showinfo("Error", "Can't find user id")

    root_dc = Tk()
    root_dc.geometry("800x400")
    root_dc.minsize(100, 100)
    root_dc.title("DEREGISTRATION SITE")

    write = Label(root_dc, text="Email", font="Helvitika 19 bold", padx=15, pady=9)
    write.grid(row=0)

    uservalue = StringVar()
    u = Entry(root_dc, textvariable=uservalue, font="Helvitika 19 bold")
    u.grid(row=0, column=1, padx=18, pady=15)

    b = Button(root_dc, text="Send Request", command=request)
    b.grid(row=5, column=3, padx=19)
    root_dc.mainloop()


menu_font = ("Helvetica", 12)

login = Menu(root, font=menu_font)
m1 = Menu(login, tearoff=0, font=menu_font)
m1.add_command(label="Teacher", command=lt)

m_student = Menu(m1, tearoff=0, font=menu_font)
m_student.add_command(label="UG student", command=ug)
m_student.add_command(label="PG student", command=pg)
m_student.add_command(label="none", command=error)
m1.add_cascade(label="Student", menu=m_student)
m1.add_cascade(label="none", command=none)
root.config(menu=login)
login.add_cascade(label="User Registration", menu=m1)
# the login menu
m2 = Menu(login, tearoff=0, font=menu_font)
m2.add_command(label="Login as a Teacher", command=login_as_teacher)
m3 = Menu(m2, tearoff=0, font=menu_font)
m3.add_command(label="UG student", command=login_as_ug_student)
m3.add_command(label="PG student", command=login_as_pg_student)
m3.add_command(label="none", command=error1)
m2.add_cascade(label="Login as a Student", menu=m3)
root.config(menu=login)
login.add_cascade(label="Login", menu=m2)
update = Menu(login, tearoff=0, font=menu_font)
update.add_command(label="Change Password", command=change_password)
update.add_command(label="Update Email", command=change_Email)

root.config(menu=login)
login.add_cascade(label="Edit Profile", menu=update, font=menu_font)

dc = Menu(login, tearoff=0, font=menu_font)
dc.add_command(label="Request for Deregistration", command=deregistration)
root.config(menu=login)
login.add_cascade(label="Deregistration", menu=dc)
l = Menu(login, tearoff=0, font=menu_font)
l.add_command(label="show ug list", command=list_ug)
l.add_command(label="show pg list", command=list_pg)
l.add_command(label="show teacher list", command=list_teacher)
root.config(menu=login)
login.add_cascade(label="show list", menu=l, font=menu_font)
'''s=Menu(login,tearoff=0, font=menu_font)
root.config(menu=login)
login.add_cascade(label="save ", menu=s, font=menu_font)'''
save_menu = Menu(login, tearoff=0, font=menu_font)
save_menu.add_command(label="Save Data", command=save_data)
root.config(menu=login)
l.add_cascade(label="Save", menu=save_menu, font=menu_font)

# Menu option to load data
load_menu = Menu(login, tearoff=0, font=menu_font)
load_menu.add_command(label="Load Data", command=load_data)
root.config(menu=login)
l.add_cascade(label="Load", menu=load_menu, font=menu_font)

original_image = Image.open("origi.png")

# Create a Label widget and place it in the window
image_label = Label(root)
image_label.pack(fill="both", expand=True)

# Bind the window resize event to the resize_image function
root.bind("<Configure>", resize_image)

root.mainloop()