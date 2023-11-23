import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import db
'''
loginwindow = tk.Tk()
mainWindow = tk.Tk()

loginwindow.title('login')
loginwindow.iconbitmap()

width,height=300,200
display_height = loginwindow.winfo_screenheight()
display_width = loginwindow.winfo_screenwidth()
loginwindow.geometry(f'{width}x{height}+{int(display_width/2-width/2)}+{int(display_height/2-height/2)}') # open position center
loginwindow.resizable(False,False)

usrName= tk.StringVar(value="userName")
passwd= tk.StringVar(value="password")

lbl_usrName = ttk.Label(loginwindow, text="userName")
lbl_usrName.pack()

entry_usrName = ttk.Entry(loginwindow, textvariable=usrName)
entry_usrName.pack()

lbl_passwd= ttk.Label(loginwindow, text="password")
lbl_passwd.pack()

entry_passwd = ttk.Entry(loginwindow, textvariable=passwd)
entry_passwd.pack()

def click_btn_login(dbname,usrName,passwd):
    db.auth_login(dbname,usrName,passwd)

def click_btn_addUser(usrName,passwd):
    pass
   
btn_login= ttk.Button(loginwindow,text='login',command=click_btn_login(db.database_name,usrName,passwd))
btn_login.pack()

btn_addUser= ttk.Button(loginwindow,text='addUser',command=click_btn_addUser)
btn_addUser.pack()

loginwindow.mainloop()
'''


class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        self.signup_pw= tk.StringVar(value="")
        self.signup_username= tk.StringVar(value="")
        self.signupData={}

        self.login_pw= tk.StringVar(value="")
        self.login_username= tk.StringVar(value="")
        self.loginData={}

        #adding users own data-table using own name as table name
        self.addfunc_site=tk.StringVar(value="")
        self.addfunc_username=tk.StringVar(value="")
        self.addfunc_passwd=tk.StringVar(value="")

        self.auth=False


        
    
    
        width,height=300 ,300
        display_height = master.winfo_screenheight()
        display_width = master.winfo_screenwidth()
        master.geometry(f'{width}x{height}+{int(display_width/2-width/2)}+{int(display_height/2-height/2)}') # open position center
        master.resizable(True,True)
        
        #defineing the Grid
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=3)
        master.columnconfigure(2, weight=1)
         
        master.rowconfigure(0, weight=3)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=2)
         
 
         # Load the PNG image
        icon_path = 'icons/icon-password-book.png'
        icon_img = Image.open(icon_path)
        icon_img = ImageTk.PhotoImage(icon_img)

        # Set the icon for the main window
        master.iconphoto(True, icon_img)

        # Load the PNG image
        image_path = 'icons/icon-password-manager.png'  
        image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(master, image=self.tk_image).grid(row=0, column=1,  sticky="nsew")
      
        label = ttk.Label(master, text="PASSWORD MANAGER",font=("Helvetica", 18)).grid(row=1, column=1,  )
        
        # Create a button in the main window
        
        self.button = ttk.Button(master, text="login", command=self.loginWindow).grid(row=2, column=1 ,sticky="w"  ) 
        

        self.button = ttk.Button(master, text="sign up", command=self.signupWindow).grid(row=2, column=1 , sticky="e" )
        

    def signupWindow(self):
        #defineing the Grid
        """
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        self.master.columnconfigure(2, weight=1)
         
        self.master.rowconfigure(0, weight=3)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=2)
"""
        # Create a new window
        signup_Window = tk.Toplevel(self.master)
        signup_Window.title("signup Window")

        width,height=300 ,300
        display_height = signup_Window.winfo_screenheight()
        display_width = signup_Window.winfo_screenwidth()
        signup_Window.geometry(f'{width}x{height}+{int(display_width/2-width/2)}+{int(display_height/2-height/2)}') # open position center
        signup_Window.resizable(False,False)

        label = ttk.Label(signup_Window, text="Sign up",font=("Helvetica", 14)).grid(row=0, column=0,  ) 

       
        entry = ttk.Entry(signup_Window, textvariable=self.signup_username).grid(row=1, column=2, sticky="w"  )
        label = ttk.Label(signup_Window, text="User Name").grid(row=1, column=0, sticky="e"  )

    
        entry = ttk.Entry(signup_Window, textvariable=self.signup_pw ,show='*').grid(row=2, column=2,sticky="e"   )
        label = ttk.Label(signup_Window, text="Password").grid(row=2, column=0, sticky="w"  )

        
        
        signup_button = ttk.Button(signup_Window, text="sign up", command=self.signup).grid(row=3, column=1,  ) 
        
         
        close_button = ttk.Button(signup_Window, text="Close", command=signup_Window.destroy).grid(row=3, column=2,  ) 
         

    def loginWindow(self):
        # Create a new window
        login_Window = tk.Toplevel(self.master)
        login_Window.title("login Window")

        width,height=300 ,300
        display_height = login_Window.winfo_screenheight()
        display_width = login_Window.winfo_screenwidth()
        login_Window.geometry(f'{width}x{height}+{int(display_width/2-width/2)}+{int(display_height/2-height/2)}') # open position center
        login_Window.resizable(False,False)

        label = ttk.Label(login_Window, text="Log in",font=("Helvetica", 14)).grid(row=0, column=0,  ) 
       
        entry = ttk.Entry(login_Window, textvariable=self.login_username).grid(row=1, column=2, sticky="w"  )
        label = ttk.Label(login_Window, text="User Name").grid(row=1, column=0, sticky="e"  )
    
        entry = ttk.Entry(login_Window, textvariable=self.login_pw ,show='*').grid(row=2, column=2,sticky="e"   )
        label = ttk.Label(login_Window, text="Password").grid(row=2, column=0, sticky="w"  )

        login_button = ttk.Button(login_Window, text="login", command=self.login).grid(row=3, column=1,  ) 
        close_button = ttk.Button(login_Window, text="Close", command=login_Window.destroy).grid(row=3, column=2,  ) 

    def add(self):
        addData(self.login_username.get(),self.addfunc_site.get(),self.addfunc_username.get(),self.addfunc_passwd.get())

    def show(self):
        data=getData(self.login_username.get())
        if data:
            # Add data to the Treeview
            for row in data:
                self.tree.insert("", "end", values=row)

        
    
    def dataAccess(self,):
        dataAccess_Window = tk.Toplevel(self.master)
        dataAccess_Window.title("dataAccess_Window")

        width,height=550 ,400
        display_height = dataAccess_Window.winfo_screenheight()
        display_width = dataAccess_Window.winfo_screenwidth()
        dataAccess_Window.geometry(f'{width}x{height}+{int(display_width/2-width/2)}+{int(display_height/2-height/2)}') # open position center
        dataAccess_Window.resizable(True,True)

        self.tree = ttk.Treeview(dataAccess_Window)
        self.tree["columns"] = ('id' ,'username','password',)
        self.tree.heading("id", text="ID")
        self.tree.heading("username", text="USERNAME")
        self.tree.heading("password", text="PASSWORD")
        
        self.tree["show"] = "headings"

        

        
        
        label = ttk.Label(dataAccess_Window, text="site").grid(row=0, column=0,  )
        entry = ttk.Entry(dataAccess_Window, textvariable=self.addfunc_site).grid(row=1, column=0,   )

        
        label = ttk.Label(dataAccess_Window, text="User Name").grid(row=2, column=0,  )
        entry = ttk.Entry(dataAccess_Window, textvariable=self.addfunc_username).grid(row=3, column=0,  )

        
        label = ttk.Label(dataAccess_Window, text="password").grid(row=4, column=0,   )
        entry = ttk.Entry(dataAccess_Window, textvariable=self.addfunc_passwd).grid(row=5, column=0,  )

        self.button = ttk.Button(dataAccess_Window, text="add", command=self.add).grid(row=8, column=0 , )
        self.button = ttk.Button(dataAccess_Window, text="show", command=self.show).grid(row=50, column=0 ,   )
       

       
        self.tree.grid(row=20, column=0)      

    def signup(self):
        self.signupData={'username':self.signup_username.get(),'pw':self.signup_pw.get()}
        add_users(self.signupData,self.signup_username.get())
        messagebox.showinfo('done','user added')

    
    def login(self):
        self.loginData={'username':self.login_username.get(),'pw':self. login_pw.get()}
        if loginTopwManager(self.login_username.get(),self.login_pw.get()):
            self.dataAccess()
    
        else:
            messagebox.showerror("error","incorrect password")
        
     

    

def add_users(signupdata,usrname):
    db1 = db.SQLiteDB()
    db1.connect()
    db1.create_table('users', ['id INTEGER PRIMARY KEY AUTOINCREMENT' , 'username TEXT', 'pw TEXT'])
    
    db1.create_table(f"{usrname}",['id INTEGER PRIMARY KEY AUTOINCREMENT' , 'site TEXT','username TEXT', 'passwd TEXT'])
 
    db1.insert_data('users',signupdata)
    db1.close_connection()
       
def loginTopwManager(username,passwd):
    auth=False 
    db2 = db.SQLiteDB()
    db2.connect()
    pw=db2.checkpw('users',username)
    if passwd==pw[0]:
        auth=True
    return auth 

def addData(table_name,site,username,password):
    db3=db.SQLiteDB()
    db3.connect()
    db3.addData(table_name,site,username,password)


def getData(table_name):
    db4=db.SQLiteDB()
    db4.connect()
    data=db4.getData(table_name)
    return data      
        

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the PasswordManagerApp class
app = PasswordManagerApp(root)

# Run the Tkinter event loop
root.mainloop()
   