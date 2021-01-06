from tkinter import *
import os

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'

def register_user():
  print("working")
   
  username_info = username.get() #returns the value for the given key, if present otherwise it will return None
  password_info = password.get()

  #storing the redistration data into a file
  with open(creds, 'w') as f:   # Creates a document using the variable we made at the top.
    f.write(username_info)      # username_info is the variable we were storing the input to.
    f.write('\n')               # Splits the line so both variables are on different lines.
    f.write(password_info)      # Same as username_info just with password_info var
    f.close()                   # Closes the file

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

  
def register():
  global screen1 # make these variable avaliable to all other modules
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("350x300")

  #Show the tkinter window at the center
  windowWidth = screen1.winfo_reqwidth()
  windowHeight = screen1.winfo_reqheight()
 
  positionRight = int(screen1.winfo_screenwidth()/2.5 - windowWidth/2)
  positionDown = int(screen1.winfo_screenheight()/2.5 - windowHeight/2)

  screen1.geometry("+{}+{}".format(positionRight, positionDown)) 

  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()  #convert to string
  password = StringVar()  #^^
 
  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def DelUser():
    os.remove(creds) # Removes the file
    screen.destroy() # Destroys the login window

def main_screen():

  from PIL import ImageTk, Image
  import os

  global screen

  screen = Tk()

  img = ImageTk.PhotoImage(Image.open("logo.jpg"))
  panel = Label(screen, image = img)
  panel.place(rely=1.0, relx=1.0, x=-7, y=-7, anchor=SE) # Place the logo at right bottom corner of the window
  
  screen.geometry("350x300")
  screen.title("Registration")

  #Show the tkinter window at the center
  windowWidth = screen.winfo_reqwidth()
  windowHeight = screen.winfo_reqheight()
 
  positionRight = int(screen.winfo_screenwidth()/2.5 - windowWidth/2)
  positionDown = int(screen.winfo_screenheight()/2.5 - windowHeight/2)

  screen.geometry("+{}+{}".format(positionRight, positionDown))

  #Widgets inside it
  Label(text = "Smart Login Protection", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  
  Label(text = "").pack()

  
  # This makes the deluser button. blah go to the deluser def.
  delete_user = Button( text='Delete User', height = "2", width = "30", fg='red', command= DelUser).pack()

  Label(text = "").pack()
  Label(text = "MADE BY ARYAN RAVAL \n PUBLISHED IN 2020", bg = "grey", width = "30", height = "2", font = ("Calibri", 10)).place(rely=1.0, relx=1.0, x=-157, y=-50, anchor=E)
  
  screen.mainloop()
 
main_screen()
