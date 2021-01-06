from tkinter import *
import os

creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'   
failure_max = 3

def delete3():
    screen4.destroy()


def password_not_recognised():

    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Access Denied")
    screen4.geometry("220x100")
    Label(screen4, text = "Wrong username or password \n Try Again!").pack()
    Label(screen4, text = "").pack()
    Button(screen4, text = "OK", command =delete3).pack()

    #Show the tkinter window at the center
    windowWidth = screen4.winfo_reqwidth()
    windowHeight = screen4.winfo_reqheight()
 
    positionRight = int(screen4.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(screen4.winfo_screenheight()/2.4 - windowHeight/2)

    screen4.geometry("+{}+{}".format(positionRight, positionDown))

def enter(event):
    login_verify()
  
def login_verify(failures=[]):

    with open(creds) as f:
        data = f.readlines()        # This takes the entire document we put the info into and puts it into the data variable
        username = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        password = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
    
    if username_entry1.get() == username and password_entry1.get() == password: # Checks to see if you entered the correct data.
        screen.destroy()
        return

    failures.append(1)

    username_entry1.delete(0, END) # if username or password is wrong, it delete the old entry and blank for new entry
    password_entry1.delete(0, END)
    
    if sum(failures) >= failure_max:
        screen.destroy()
        
#Captures a image of unautorized person

        try:
            from Capture_Image import camera_capture
        except:
            pass
        
#Send email

        try:
            from Email import send
        except:
            pass
        
#Shutdown computer if unauthorize person detect

        os.system('start shutdown /r')
    
        raise SystemExit('Unauthorized login attempt')

    else:
        password_not_recognised()

        
def main_screen():

    from PIL import ImageTk, Image
    import os

    global screen
    
    screen = Tk()

    # Logo setup
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    panel = Label(screen, image = img)
    panel.place(x = 430, y = 350)

    screen.geometry('1396x1280')
    screen.overrideredirect(1)
    screen.title("Notes 1.0")

    Label(text = "Smart Login Protection", bg = "grey", fg = "White", width = "300", height = "2", font = ("Calibri", 18)).pack()
    Label(text = "").pack()
    Label(text = "Please Login", font = ("Calibri", 15)).pack()
    Label(text = "").pack()

# Login Checkup

    global username_entry1
    global password_entry1
  
    Label(screen, text = "Username * ", font = ("Calibri", 13)).pack()
    username_entry1 = Entry(screen, borderwidth=3)
    username_entry1.pack()

    Label(screen, text = "").pack()

    Label(screen, text = "Password * ", font = ("Calibri", 13)).pack()
    password_entry1 = Entry(screen, borderwidth=3, show = "*")
    password_entry1.pack()

    Label(screen, text = "").pack()
    Button(screen, text = "Login", borderwidth=2,bg = "Blue", fg = "White", width = 14, height = 1, font = ("Calibri", 13), command = login_verify).pack()

    screen.bind('<Return>', enter)  #bind ENTER button 
    username_entry1.focus_set()     #Set cursor to username by default
    
    screen.mainloop()

main_screen()

