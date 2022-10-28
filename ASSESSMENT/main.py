#Importing all the required Modules 
import tkinter as tk
from tkinter import NW, Canvas, PhotoImage, filedialog
from tkinter.messagebox import showinfo
from matplotlib.figure import Figure
import pymongo 
from pymongo import MongoClient 
import urllib.parse
from urllib.parse import quote_plus

#Importing ALl classes from other files
from Import_Modules import *
from Graph_Analysis import Analysis
from DecisionTree import Tree
from tkinter_treepage import Tkinter
import tkinter as ttk


#Creating class App with tkinter as tk
class App(tk.Tk): 
    def __init__(self):
        #Instantiating the super class 
        super().__init__()
        
        #Tree()
        # configuring the root  window
        self.title('"Login form"')
        self.geometry('440x440')
        self.configure(bg='#333333')
        self.frame = tk.Frame(self,bg='#333333')
        self.frame.pack(padx = 55, pady= 45,expand=True,fill="both")
        
        
        
        # Creating widgets --> Label, Entry, Button
        self.login_Label =  tk.Label(self.frame, text="Login", bg='#333333', fg="#FFFFFF", font=("Arial", 30))
        self.username_Label = tk.Label(self.frame, text="Username ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_Entry = tk.Entry(self.frame, font=("Arial", 14))
        self.username_Entry.insert('end', "SaideepikaKandiganti")
        self.password_Entry = tk.Entry(self.frame, show="*", font=("Arial", 14))
        self.password_Entry.insert('end', "Deepika@123")
        self.password_Label = tk.Label(self.frame, text="Password ", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.login_Button = tk.Button(self.frame, text="Login", bg="#333333", fg="#FFFFFF", font=("Arial", 16), command=self.LoginValidation)

        # Placing widgets on the screen, as per the rows and columns 
        self.login_Label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        self.username_Label.grid(row=1, column=0)
        self.username_Entry.grid(row=1, column=1, pady=20)
        self.password_Label.grid(row=2, column=0)
        self.password_Entry.grid(row=2, column=1, pady=20)
        self.login_Button.grid(row=3, column=0, columnspan=2, pady=30)
        
        self.frame.pack() # Packing the whole frame 
        
    #Function to validate the login with username and password
    #where this LoginValidation method is called by Login Button as command 
    def LoginValidation(self):
        
        #Assiging the username and password to cross check with the user entered details 
        self.username = "SaideepikaKandiganti"
        self.password = "Deepika@123"
        
        if(self.username_Entry.get()== self.username and self.password_Entry.get()== self.password):
           
            #messagebox.showinfo("Login is success!" , message ="Please proceed and click on graph buttons")
            
            Tkinter() #Calling tkinter class from tkinter_treepage
            
        else: #else it will display as error
            messagebox.showerror(title="Error", message="Invalid login.")
        
app = App() #Caliinng the class App and assigning to app variable
app.mainloop() # To close the root window, assigned it to app varibale

    