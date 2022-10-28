
#Importing all the required Modules 
import tkinter as tk
from tkinter import NW, Canvas, PhotoImage, filedialog
from tkinter.messagebox import showinfo
from matplotlib.figure import Figure
import pymongo 
from pymongo import MongoClient 
import urllib.parse
from urllib.parse import quote_plus

from Import_Modules import *
from Graph_Analysis import Analysis
from DecisionTree import Tree

from tkinter import * 
from matplotlib.figure import Figure
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import tkinter as tk
from tkinter import NW, Canvas, PhotoImage, filedialog
from PIL import Image, ImageTk

#Class Tkinter for  visualization
class Tkinter(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        # configure the root  window
        self.title("Analysis")
        #self.geometry('740x940')
        self.configure(bg='#333333')
        self.frame = tk.Frame(self,bg='#333333')
        #self.frame.pack(padx = 55, pady= 45,expand=True,fill="both")
        
        #Creating widgets --> Label,and Button for decision Tree and plotting visualization
        self.WelcomeLabel = tk.Label(self.frame, text = "Please proceed and click on graph buttons", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.decisionButton = tk.Button(self.frame, text = "Click for Decision Tree",bg="#333333", fg="#FFFFFF", font=("Arial", 16), command = self.get_decisionTree)
        
        
        self.graphButton = tk.Button(self.frame, text = "Click for data analysis",bg="#333333", fg="#FFFFFF", font=("Arial", 16),command = self.get_graph)
        
        
      
        # Placing widgets on the screen, as per the rows and columns 
        self.WelcomeLabel.grid(row=0, column=0, columnspan=5, sticky="news", pady=40)
        self.decisionButton.grid(row = 1, column = 2, padx =20, pady= 20)
        self.graphButton.grid(row = 2, column = 2, padx =20, pady= 20)
        
        
        self.frame.pack(padx =20, pady= 20,expand=True,fill="both")
        
        
       
    #Function to get the decision tree visualization
    def get_decisionTree(self):
        
        
        if (self.decisionButton['state'] == NORMAL):
            self.decisionButton['state'] = DISABLED
        else:
            self.decisionButton['state'] = NORMAL
        
        #To open a new window for decision tree after clicking the Decision Tree Button
        new_window  = Toplevel(self)
        new_window.geometry('740x540')
        new_window.title("Decision Tree")
        
        self.treeLabel = tk.Label(new_window, text = "Decision Tree", font=15)
        self.treeLabel.pack(padx= 5, pady=5)
        #after executing the decision tree code it will save the image and display as an output
        img= ImageTk.PhotoImage(file = 'Final_DecisionTree.png')
        self.label = tk.Label(new_window,image=img)
        self.label.image = img
        self.label.pack(padx=3, pady=2)
        
       
    #Function to get the graph visualization
    def get_graph(self):
        
        if (self.graphButton['state'] == NORMAL):
            self.graphButton['state'] = DISABLED
            
        else:
            self.graphButton['state'] = NORMAL
        
        
        #To open a new window for decision tree after clicking the Decision Tree Button
        new_window  = Toplevel(self)
        new_window.geometry('740x340')
        new_window.title("Graph Analysis")
        
        self.graphLabel = tk.Label(new_window, text = "Liver Patient Analysis", font=15)
        self.graphLabel.pack(padx= 5, pady=5)
        
        #after executing the plot analysis code it will save the image and display as an output
        self.graphImg = ImageTk.PhotoImage(file = 'GraphImage.png')
        self.label= tk.Label(new_window, image= self.graphImg)
        self.label.image =  self.graphImg
        self.label.pack(padx=15, pady=15)
        
        
#main 
if __name__ == "__main__":
    tkinter = Tkinter()
    tkinter.mainloop()
    
    