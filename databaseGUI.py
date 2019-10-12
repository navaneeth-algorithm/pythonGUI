import tkinter
class Dog:
    def __init__(self,window):
        dogButton = tkinter.Button(window,text="DOG")
        dogButton.bind("<Button-1>",self.callDog)
        dogButton.grid()

    def callDog(self,event):
        callLabel = tkinter.Label(window,text="BOW BOW BOW").grid()
        

def sayhi():
    labelHi = tkinter.Label(window,text="Login LEFT").grid()
def sayregister(event):
    labelHi = tkinter.Label(window,text="Register RIGHT").grid()

def function():
    pass

window = tkinter.Tk()
window.title("Database Management")

root_menu = tkinter.Menu(window)
window.config(menu=root_menu)

#Creating FileMenu
file_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File",command=function)
file_menu.add_command(label="Open File",command=function)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=window.quit)

#Creating Editing File
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Edit File",command=function)
edit_menu.add_command(label="Edit Database",command=function)

labelWelcome = tkinter.Label(window,text="WELCOME TO GUI").grid(row=0)
labeluserName = tkinter.Label(window,text="Name").grid(row=1)
userInput = tkinter.Entry(window).grid(row=1,column=1)
labeluserPassword = tkinter.Label(window,text="Enter Password").grid(row=2,column=0)
userPass = tkinter.Entry(window).grid(row=2,column=1)
loginCheck = tkinter.Checkbutton(window,text="Keep me Loggind").grid(row=3,column=0)
login = tkinter.Button(window,text="LOGIN",fg="black",bg="white", command=sayhi).grid(row=3,column=1,columnspan=5)

register = tkinter.Button(window,text="REGISTER")
register.bind('<Button-3>',sayregister)
register.grid(row=3,column=2)


dog1 = Dog(window)
window.mainloop()